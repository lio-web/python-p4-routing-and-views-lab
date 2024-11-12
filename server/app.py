# #!/usr/bin/env python3

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#         return '<h1>Python Operations with Flask Routing and Views</h1>'
    
# @app.route('/print/<string:parameter>')
# def print_string(parameter):
#     print(parameter) 
#     return parameter  

# @app.route('/count/<int:parameter>')
# def count(parameter):
#     result = ''
#     for i in range(parameter):
#         result += f'{i}\n' 
#     return result


# @app.route('/math/<float:num1>/<string:operation>/<float:num2>')
# def math(num1, operation, num2):
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == 'div':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             return 'Error: Division by zero', 400
#     elif operation == '%':
#         result = num1 % num2
#     else:
#         return 'Error: Unsupported operation', 400

#     return str(result)  # Return plain text result

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'
  

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operations(num1, operation, num2):
    # Match the operations expected by the test cases
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)  # Return the result as plain text

if __name__ == '__main__':
    app.run(port=5555, debug=True)

