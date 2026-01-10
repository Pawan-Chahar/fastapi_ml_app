from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List ,Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Mohan','Vinay'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None ,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

# def insert_patient_data(patient: Patient):

#     print(patient.name)
#     print(patient.age)
#     print(patient.weight)
#     print(patient.allergies)
#     print('Inserted into Database')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print('Update into Database')


patient_info = {'name': 'mohan shyam', 'email' : 'abc@gmail.com' ,'linkedin_url':'http://linkdin.com/14576', 'age': 30, 'weight': 89.17 ,'contact_details': {'email' : 'abc@gmail.com','phone': '2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)




