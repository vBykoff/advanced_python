#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <stdlib.h>
#include <stdio.h>
#include <numpy/arrayobject.h>
#include <Python.h>

double determinantOfMatrix(double **mat, long size);
void getCofactor(double **mat, double **temp, long p, long q, long n);
PyObject* cutils_multiply_matrix(PyObject* self, PyObject* args);
PyMODINIT_FUNC PyInit_cutils(void);