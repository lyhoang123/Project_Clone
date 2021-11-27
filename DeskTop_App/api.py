from flask import Flask,request,jsonify
from sqlalchemy import create_engine
from datetime import datetime,timedelta
from database import get_number_of_violation,get_one_student,get_student,get_number_of_violation,get_violator_list,get_last_time_violation
app = Flask(__name__)


@app.route('/check-violation',methods=['GET'])
def return_information_violator():
    id_student = request.args.get("id")

    print(get_violator_list())
    NumberViolation = get_number_of_violation(str(id_student))
    if int(NumberViolation) == 0:
        data_return = {     
            "Violation":False,
            "data":""}
        return jsonify(data_return)
    else:
        LastTime = str(get_last_time_violation(id_student,int(NumberViolation)))
    information_list = get_one_student(str(id_student))
    data = {
        "IdStudent":information_list[0],
        "NameStudent":information_list[1],
        "Class":information_list[2],
        "PhoneNumber":information_list[3],
        "NumberViolation":NumberViolation,
        "LastTime-Violation":LastTime
    }
    data_return = {
        "Violation":True,
        "data":data
    }
    return jsonify(data_return)

if __name__ == '__main__':
    app.run(debug=True,port=9999)