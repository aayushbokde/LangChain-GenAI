from pydantic import BaseModel, EmailStr, Field
import json
from typing import Optional


class Student(BaseModel):
    name: str = 'Aayush' #default value
    age: Optional[int] = None #optional field
    email: EmailStr #inbuilt to validate Emails
    cgpa: float = Field(gt=0, lt=10, default=5, description='decimal value representing cgpa of the student')


new_student = {'age':21, 'email':'abs@gmail.com', 'cgpa':9}

student = Student(**new_student)

# print(Student.name)
student_dict = dict(student) #explicitely converting the pydantic object to dictionary
# print(student_dict['age']) 


student_json = student.model_dump_json()
# json.loads(student_json)
print({json.loads(student_json)['age']})