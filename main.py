from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

students = {}
students_data = {"id": 0, "name": "", "age": 0, "sex": "", "height":0}

@app.get('/')
def home():
    return {"Messages": "Welcome to my Homepage"}

# To Create a Student resource
@app.post('/students')
def createStudent(name: str, age: int, sex: str, height: float):
    id_ = len(students) + 1
    new_student = {
        'id': id_,
        'name': name,
        'age': age,
        'sex': sex,
        'height': height
    }
    students[id_] = new_student
    return {'message': 'Student created successfully', 'data': new_student}

# To Retrieve all Student resource
@app.get('/students')
def get_students():
    students_arr = []
    for stu in students:
        students_arr.append(students[stu])
    return {
        'message': 'students fetched was successful',
        'data': students_arr
    }

# To Retrieve a Student resource
@app.get('/students/{id}')
def get_one_student(id: int):
    try:
        student = students[id]
        if student:
            return {
                'message': 'Student fetched successfully',
                'data': student
            }
    except KeyError:
        return {
            'message': 'Student not found'
        }

# To Update a Student resource
@app.put('/students/{id}')
def update_student(id: int, name: str, height: float):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}
    
    student['name'] = name
    student['height'] = height
    return {
        'message': 'Student updated sucessfully',
        'data': student
    }

# Delete a Student resource
@app.delete('/students/{id}')
def delete_student(id: int):
    try:
        student = students[id]
        del students[id]
    except KeyError:
        return{
            'message': 'Student does not exist'
        }
    return {
        'message': 'Student deleted sucessfully'
    }

