import json
import re
import argparse
from tqdm import tqdm

path = '13.txt'


class ReadFile:
    path: str

    def __init__(self, p: str) -> None:
        self.path = p

    def read_file(self) -> list:
        result: list = []
        data_file = json.load(open(self.path, encoding='windows-1251'))
        for i in data_file:
            result.append(ValidatorCondition(i.copy()))
        return result


class WriteFile:
    path: str

    def __init__(self, name: str) -> None:
        self.path = name

    def write_file(self, res) -> None:
        tmp = []
        for i in tqdm(range(len(res.result)), desc="File was wrote!", ncols=100):
            if not (False in res.validation(i).values()):
                tmp.append(res.result[i].dictionary.copy())
        json.dump(tmp, open(self.path, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)


class Validator:
    result: list

    def __init__(self, arr) -> None:
        self.result = arr

    def validation(self, ind) -> dict:
        tmp = {"email": self.result[ind].check_email(),
               "weight": self.result[ind].check_weight(),
               "inn": self.result[ind].check_inn(),
               "passport_number": self.result[ind].check_pass(),
               "university": self.result[ind].check_uni(),
               "age": self.result[ind].check_age(),
               "academic_degree": self.result[ind].check_degree(),
               "worldview": self.result[ind].check_view(),
               "address": self.result[ind].check_address()}
        return tmp.copy()

    def count_valid(self) -> int:
        count_valid = 0
        for i in range(len(self.result)):
            if not (False in self.validation(i).values()):
                count_valid += 1
        return count_valid

    def count_invalid(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if False in self.validation(i).values():
                count += 1
        return count

    def count_invalid_email(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_email():
                count += 1
        return count

    def count_invalid_weight(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_weight():
                count += 1
        return count

    def count_invalid_inn(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_inn():
                count += 1
        return count

    def count_invalid_pass(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_pass():
                count += 1
        return count

    def count_invalid_uni(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_uni():
                count += 1
        return count

    def count_invalid_age(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_age():
                count += 1
        return count

    def count_invalid_degree(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_degree():
                count += 1
        return count

    def count_invalid_view(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_view():
                count += 1
        return count

    def count_invalid_address(self) -> int:
        count = 0
        for i in range(len(self.result)):
            if not self.result[i].check_address():
                count += 1
        return count


class ValidatorCondition:
    dictionary: dict

    def __init__(self, d: dict) -> None:
        self.dictionary = d.copy()

    def check_email(self) -> bool:
        pattern = r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.dictionary["email"]):
            return True
        return False

    def check_weight(self) -> bool:
        if type(self.dictionary["weight"]) == int and 40 < self.dictionary["weight"] < 100:
            return True
        return False

    def check_inn(self) -> bool:
        pattern = "^[0-9]{12}"
        if re.match(pattern, self.dictionary["inn"]):
            return True
        return False

    def check_pass(self) -> bool:
        if type(self.dictionary["passport_number"]) == int and 99999 < self.dictionary["passport_number"] < 1000000:
            return True
        return False

    def check_uni(self) -> bool:
        pattern = "^.+(?:[Уу]ниверситет)|([Уу]ниверситет)|^.+([Аа]кадеми[ия])|^.+(институт)|МГУ|^.+(политех)|^.+(" \
                  "МГТУ)|САУ|МФТИ|СПбГУ"
        if re.match(pattern, self.dictionary["university"]):
            return True
        return False

    def check_age(self) -> bool:
        if type(self.dictionary["age"]) == int and 18 < self.dictionary["age"] < 100:
            return True
        return False

    def check_degree(self) -> bool:
        pattern = "Бакалавр|Кандидат наук|Специалист|Магистр|Доктор наук"
        if re.match(pattern, self.dictionary["academic_degree"]):
            return True
        return False

    def check_view(self) -> bool:
        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern, self.dictionary["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        pattern = r'[а-яА-Я.\s\d-]+\s+[0-9]+$'
        if re.match(pattern, self.dictionary["address"]):
            return True
        return False


parser = argparse.ArgumentParser("Input & output parser")
parser.add_argument("-input", type=str, default=path, help="Input path")
parser.add_argument("-output", type=str, default="Output.txt", help="Output path")
pars = parser.parse_args()
read = ReadFile(pars.input)
array = Validator(read.read_file())
write = WriteFile(pars.output)
write.write_file(array)
print("Amount of valid: ", array.count_valid())
print("Amount of invalid: ", array.count_invalid())
print("Amount of invalid email: ", array.count_invalid_email())
print("Amount of invalid weight: ", array.count_invalid_weight())
print("Amount of invalid inn: ", array.count_invalid_inn())
print("Amount of invalid passport number: ", array.count_invalid_pass())
print("Amount of invalid university: ", array.count_invalid_uni())
print("Amount of invalid age: ", array.count_invalid_age())
print("Amount of invalid academic degree: ", array.count_invalid_degree())
print("Amount of invalid worldview: ", array.count_invalid_view())
print("Amount of invalid address: ", array.count_invalid_address())
