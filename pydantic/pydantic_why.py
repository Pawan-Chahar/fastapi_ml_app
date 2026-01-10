
def insert_patient_data(name: str,age: int):

    if type(name) == str and type(age) == int:
        if age<0:
            raise ValueError('Age cant be negative')
        else:
            print(name)
            print(age)
            print('Inserted into Database')
    else:
        raise TypeError('Incorrect data type')
    

def update_patient_data(name:str , age: int):
    if type(name) == str and type(age) == int:
        if age<0:
            raise ValueError('Age cant be negative')
            print(name)
            print(age)
            print('Inserted into Database')
    else:
        raise TypeError('Incorrect data type') 

insert_patient_data('mohan','30')
