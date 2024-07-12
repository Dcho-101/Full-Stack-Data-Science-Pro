# first we need to import the flask

from flask import Flask,render_template,request
app = Flask('__name__')

## we need to render the html page in which the data will be input


@app.route('/dibyendu_calculator')
def cal_page() :
    return render_template('calculator.html') ## it return the html page
## this is an python function so this need to call through an api (app.route) 

## when someone press calculate, the form will be submitted. in other word when someone call action, the form will sumitted. that means when we call the action on route

@app.route("/math", methods = ['POST']) ## it retrurns the result
def calculator():
    ## we have to get data first for evaluation
    ops = request.form['operation'] # request is comming from the operation

    first_number = request.form['num1'] # id of first number is num1
    second_number = request.form['num2']

    first_num = int(first_number)
    second_num = int(second_number)

    ## all the data from html file is available now

    if(ops == 'add') :
        r = first_num + second_num
        return f"addition of {first_num} and {second_num} is {r}"
    if(ops == 'subtract') :
        r = first_num - second_num
        return f"subtraction of {first_num} and {second_num} is {r}"
    if(ops == 'multiply') :
        r = first_num * second_num
        return f"multiplication of {first_num} and {second_num} is {r}"
    if(ops == 'divide'):
        r = first_num / second_num
        return f"division of {first_num} and {second_num} is {r}"

## now we have to call the main function

if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 5000)
        