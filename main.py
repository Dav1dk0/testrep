from flask import *

app = Flask(__name__)

#asd
@app.route('/')
def index():
    return render_template_string('1234')
#df

if __name__ == "__main__":
    app.run(debug=True)
