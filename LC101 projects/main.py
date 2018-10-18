

from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True




    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    form="""
<!DOCTYPE html>
<html>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:</label>
                <input  type="text" name="rot" value="0"/>
            
        <textarea> name="text">{0}</textarea>
        <input type ="submit"/>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

app.run()