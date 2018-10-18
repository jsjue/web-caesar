from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                <h1>font: 16px sans-serif;</h1>
                border-radius: 10px;
            }}
            textarea{{
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
        <textarea type ="text" name = "text">{0}</textarea>
    
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
    rotation = int(request.form["rot"])
    word = (request.form["text"])
    encrypto = rotate_string(word, rotation)
    return form.format(encrypto) 

app.run()