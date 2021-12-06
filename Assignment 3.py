import csv

class Physician:
    __slots__ = ['id', 'name', 'speciality']
    def __init__(self, id, name, speciality):
        self.id = id
        self.name = name
        self.speciality = speciality

    def get_id(self):
        return self.id 

    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_specialty(self):
        return self.specialty

    def set_specialty(self, specialty):
        self.specialty = specialty

    def _str_(self):
        return " A " + self.specialty + " Physician.\n"

    def _repr_(self):
        return "\n Physician:\n  id = " + str(self.id) \
            + "\n  name = " + str(self.name) \
            + "\n  specialty = " + \
            str(self.specialty)

class Patient:
    _slots_ = ['emr_id', 'name', 'gender', 'phone_number']
    def _init_(self, emr_id, name, gender, phone_number):
        self.emr_id = emr_id
        self.name = name
        self.gender = gender
        self.phone_number = phone_number

    def get_emr_id(self):
        return self.emr_id

    def set_emr_id(self, emr_id):
        self.emr_id = emr_id

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
    
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def _repr_(self):
        return "\n Patient:\n  emirates id = " + str(self.emr_id) \
            + "\n  name = " + str(self.name) \
            + "\n  gender = " + str(self.gender) \
            + "\n   phone number = " + \
            str(self.phone_number)

class Encounters:
    _slots_ = ['physician', 'patient', 'date', 'disease', 'medication']
    def _init_(self, physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication
    
    def _repr_(self):
        return "\n Encounters:\n  physician = " + str(self.physician) \
            + "\n  patient = " + str(self.patient) \
            + "\n  date = " + str(self.date) \
            + "\n  disease = " + str(self.disease) \
            + "\n  medication = " + \
            str(self.medication)


def csv_read():

    with open('patients.csv','r') as file:
        csv_reader = csv.reader(file)
        for read in csv_reader:
            print(read)

    with open('physicians.csv', 'r') as file1:
        csv_reader1 = csv.reader(file1)
        for read_1 in csv_reader1:
            print(read_1)

def csv_write(write1, write2, write3, write4, write5):
    with open('encounter.csv','w') as file2:
        data = str(write1) + '\n' + str(write2) + '\n' + str(write3) + '\n' + str(write4) + '\n' + str(write5)
        file2.write(data)


def main():

    physician1 = Physician('21AC265', 'Sara', 'Surgery')
    physician2 = Physician('21AC265', 'Tom', 'Pediatrics')
    physician3 = Physician('21AC265', 'Karl', 'Dermatology')

    patient1 = Patient('56582e1d-3064-448f-b360-14c307b6d', 'Alicia', 'Female', 505842884)
    patient2 = Patient('d307505b-a617-4c7d-b367-c764fcd80', 'Junaid', 'Male', 5074832994)
    patient3 = Patient('3fc89529-ecc6-4b0d-8b60-a4549d6ab', 'Mahir', 'Male', 5074854995)
    patient4 = Patient('aea1205b-6b25-44a7-95a2-1cc283c59', 'Nakul', 'Male', 503748944)
    patient5 = Patient('9a82eb81-c977-4301-bfc8-49941375d', 'Usman', 'Male', 509405776)
    patient6 = Patient('a99d5426-eadb-493a-9386-ee9629f65', 'Farha', 'Female', 529038440)
    patient7 = Patient('29573b3a-337c-4238-b9bd-83b75f0fa', 'Osama', 'Male', 529576884)
    patient8 = Patient('c5dfcce1-03d7-420d-ae5d-4c7fc81b6', 'Ismail', 'Male', 506374332)
    patient9 = Patient('af528b48-ffaf-4164-a6c1-dfab7ef4d', 'Samir', 'Male', 520586775)
    patient10 = Patient('6dd77a04-7352-4edf-adbf-69d4c405a', 'Masri', 'Male', 507364665)

    encounter1 = Encounter(physician1, patient7, 16-12-2021, 'Influenza', 'Panadol')
    encounter2 = Encounter(physician3, patient4, 22-12-2021, 'Anthrax', 'Paracetamol')
    encounter3 = Encounter(physician1, patient2, 13-12-2021, 'Pneumonia', 'Adol')
    encounter4 = Encounter(physician2, patient9, 29-12-2021, 'Bronchitis', 'Ibuprofen')
    encounter5 = Encounter(physician3, patient6, 5-12-2021, 'Covid', 'Asperen')

    print(physician1)
    print(physician2)
    print(physician3)

    print(patient1)
    print(patient2)
    print(patient3)
    print(patient4)
    print(patient5)
    print(patient6)
    print(patient7)
    print(patient8)
    print(patient9)
    print(patient10)

    print(encounter1)
    print(encounter2)
    print(encounter3)
    print(encounter4)
    print(encounter5)

    csv_read()
    csv_write(encounter1, encounter2, encounter3, encounter4, encounter5)

main()