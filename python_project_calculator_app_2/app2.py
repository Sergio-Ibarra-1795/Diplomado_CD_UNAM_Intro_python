from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__, template_folder='templates')


# importing function for calculations
from basic_calculator_function import basic_calculator

# Define calculator
@app.route('/index')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port= 5001)