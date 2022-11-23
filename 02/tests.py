from faker import Faker
from json_parser import parse_json, keyword_handler
import json
import random
import unittest.mock


class JsonParserTests(unittest.TestCase):

    def setUp(self) -> None:
        faker = Faker()
        json_dict = {}
        self.required_fields = []
        self.keywords = []
        self.result = []

        for i in range(10):
            random_key = faker.word()
            random_value = faker.name()
            json_dict[random_key] = random_value

            if random.randint(0, 1):
                self.required_fields.append(random_key)
                word = random_value.split()[random.randint(0, 1)]

                self.keywords.append(word)
                self.result.append(word)

        self.json_object = json.dumps(json_dict)
        # print(self.json_object)
        # print(self.result)
        # print(self.keywords)
        # print(self.required_fields)

    def test_json_parser(self):
        result = parse_json(str(self.json_object), self.required_fields, self.keywords, None)
        self.assertEqual(result, self.result)

        result = parse_json(str(self.json_object), self.required_fields, self.keywords)
        self.assertEqual(result, self.result)



    @unittest.mock.patch("json_parser.keyword_handler")
    def test_json_parser_callback(self, keyword_handler_mock):
        keyword_handler_mock.return_value = "Value"
        result = parse_json(str(self.json_object), self.required_fields,
                            self.keywords, keyword_handler_mock)
        # print(result)
        self.assertTrue(keyword_handler_mock.called)
        self.assertEqual(keyword_handler_mock.call_count, len(self.result))


if __name__ == '__main__':
    unittest.main()
