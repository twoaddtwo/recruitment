import unittest
from DockerStation import patientdata
import random


class Patient(unittest.TestCase):
    random_num = random.randint(18800000000, 18899999999)
    phone = str(random_num)

    def test_create_mypatient(self):
        result = patientdata.create_patient(self.phone)
        print(result)
        self.assertEqual("患者新增成功", result['message'])
        print(self.phone)

