from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Any, List ,Dict, Optional, Annotated

class Patient(BaseModel):


    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com' ,'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value


    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

    ''' field operator are worked on two mode 
    1. before mode
    2. after mode (default value)
    '''
    @field_validator('age' , mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
        










def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    # print(patient.linkedin_url)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print('Update into Database')


patient_info = {'name': 'mohan shyam', 'email' : 'abc@hdfc.com' , 'age': '30', 'weight': 89.17 ,'contact_details': {'email' : 'abc@gmail.com','phone': '2353462'}}

patient1 = Patient(**patient_info)  # validation -> type coercion 

update_patient_data(patient1)