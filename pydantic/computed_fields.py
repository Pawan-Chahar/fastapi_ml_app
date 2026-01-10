from pydantic import BaseModel, EmailStr,computed_field
from typing import Any, List ,Dict, Optional

class Patient(BaseModel):


    name: str
    email: EmailStr
    age: int 
    weight: float
    height: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi 
    








def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    # print(patient.linkedin_url)
    print('BMI' , patient.bmi)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print('Update into Database')


patient_info = {'name': 'mohan shyam', 'email' : 'abc@hdfc.com' , 'age': '65', 'weight': 89.17 ,'height': 1.61,'contact_details': {'email' : 'abc@gmail.com','emergency':'5678936' ,'phone': '2353462'}}

patient1 = Patient(**patient_info)  # validation -> type coercion 

update_patient_data(patient1)