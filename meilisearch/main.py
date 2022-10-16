# import meilisearch
# import json

# # open pull request fixing the missing api_key in the docs and the print too
# client = meilisearch.Client('http://localhost:7700', api_key='MASTER_KEY')

# json_file = open('/home/yassine/learning/clean_architecture/meilisearch/movies.json')
# movies = json.load(json_file)

# result = client.index('movies').add_documents(movies)
# # print(result)

# # result = client.index('movies').search('botman')
# # print(result)

# print(client.get_keys())


"""
introduction to meilisearch
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import unittest

class CarType(Enum):
    """
    types of cars
    """
    SUV: str = "SUV"
    BERLINE: str = "BERLINE"
    COMPACT: str = "COMPACT"

@dataclass
class Car:
    """
    class representing a car
    """
    color: str
    type_: CarType
    @classmethod
    def get_blue_car(cls, type_: CarType) -> Car:
        """
        return a new blue car
        """
        return Car(color="blue", type_=type_)


class TestCar(unittest.TestCase):
    """
    tests for Car class
    """
    def test_get_blue_car(self: TestCar):
        """
        testing get new blue car
        """
        self.assertEqual(Car.get_blue_car(type_=CarType.SUV).color, "blue")

if __name__ == "__main__":
    unittest.main()
