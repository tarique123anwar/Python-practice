# from flask import Flask, render_template, request
# from p3 import EmployeeManagementSystem  # Replace with the actual filename of your Python script

# app = Flask(__name__)
# emp_system = EmployeeManagementSystem()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add_employee', methods=['POST'])
# def add_employee():
#     if request.method == 'POST':
#         try:
#             name = request.form['name']
#             position = request.form['position']
#             salary = float(request.form['salary'])
#             emp_joining_date = request.form['joining_date']
#             emp_dob = request.form['dob']
#             emp_mobile = request.form['mobile']

#             emp_system.add_employee(name, position, salary, emp_joining_date, emp_dob, emp_mobile)
#         except ValueError:
#             print("Invalid input. Please enter a valid salary.")
        
#     return render_template('index.html')  # Redirect to the main page

# # Add similar routes for other functionalities (display, show, delete)

# if __name__ == "__main__":
#     app.run(debug=True)



            ###///////////////////////


from flask import Flask ,render_template 
from flask_wtf import FlaskForm

app = Flask(__name__)

@app.route('/')
def de():
    return "hi"
# render_template('ht.html')
if __name__=='__main__':
    app.run(debug=True)