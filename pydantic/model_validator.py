from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator
from typing import Any, List ,Dict, Optional, Annotated

class Patient(BaseModel):


    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]



    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age> 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency number')
        return model







def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    # print(patient.linkedin_url)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details['email'])
    print('Update into Database')


patient_info = {'name': 'mohan shyam', 'email' : 'abc@hdfc.com' , 'age': '65', 'weight': 89.17 ,'contact_details': {'email' : 'abc@gmail.com','emergency':'5678936' ,'phone': '2353462'}}

patient1 = Patient(**patient_info)  # validation -> type coercion 

update_patient_data(patient1)