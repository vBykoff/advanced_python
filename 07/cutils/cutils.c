#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_DIMENTIONS 2

PyObject *cutils_multiply_matrix(PyObject *self, PyObject *args);

PyObject *cutils_multiply_matrix(PyObject *self, PyObject *args) {
  PyArrayObject **alpha, **betta;
  long alpha_cols, alpha_rows, betta_cols, betta_rows;

  PyArg_ParseTuple(args, "OllOll", &alpha, &alpha_rows, &alpha_cols, &betta,
                   &betta_rows, &betta_cols);
  if (PyErr_Occurred()) {
    printf("ERROR: Failed to parse argument");
    return NULL;
  }
  if (alpha_cols != betta_rows) {
    printf("ERROR: invalid arguments");
    return NULL;
  }

  double **alpha_data;
  npy_intp alpha_dims[] = {[0] = alpha_rows, [1] = alpha_cols};
  PyArray_AsCArray((PyObject **)&alpha, &alpha_data, alpha_dims,
                   NUMBER_OF_DIMENTIONS, PyArray_DescrFromType(NPY_DOUBLE));

  double **betta_data;
  npy_intp betta_dims[] = {[0] = betta_rows, [1] = betta_cols};
  PyArray_AsCArray((PyObject **)&betta, &betta_data, betta_dims,
                   NUMBER_OF_DIMENTIONS, PyArray_DescrFromType(NPY_DOUBLE));

  double *result_data =
      (double *)malloc(sizeof(double) * alpha_rows * betta_cols);

  for (int i = 0; i < alpha_rows; ++i) {
    for (int j = 0; j < betta_cols; ++j) {
      result_data[i * betta_cols + j] = 0;
      for (int k = 0; k < alpha_cols; ++k) {
        result_data[i * betta_cols + j] = result_data[betta_cols * i + j] +
                                          alpha_data[i][k] * betta_data[k][j];
      }
    }
  }

  npy_intp result_dims[] = {[0] = alpha_rows, [1] = betta_cols};
  PyObject *result = PyArray_SimpleNewFromData(
      NUMBER_OF_DIMENTIONS, result_dims, NPY_DOUBLE, result_data);
  PyObject *res = Py_BuildValue("O", result);
  return res;
}

static PyMethodDef methods[] = {{"multiply_matrix", cutils_multiply_matrix,
                                 METH_VARARGS,
                                 "return multiplication of 2 numpy matrix"},
                                {NULL, NULL, 0, NULL}};

static struct PyModuleDef cutils_module = {PyModuleDef_HEAD_INIT, "cutils",
                                           NULL, -1, methods};

PyMODINIT_FUNC PyInit_cutils(void) {
  PyObject *module = PyModule_Create(&cutils_module);
  import_array();
  return module;
}