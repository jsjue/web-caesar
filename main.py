from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                font-size: 32px;
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "post">
        <div>
            <label for "rot">Rotate by:</label>
            <input type= "text" name = "rot" value = "0">
            <p class="error"></p>
        </div>
        <h1><textarea type ="text" name = "text">{0}</textarea></h1>
    
        <br>
        <input type = "Submit">
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods = ["POST"])


def encrypt():
    rotation = request.form["rot"]
    rotation = int(rotation)
    text = (request.form["text"])
    encrypt = rotate_string(text, rotation)
    '''encrypt = "<h1>" + encrypt + "</h1>" '''
    
    return form.format(encrypt) 

app.run()