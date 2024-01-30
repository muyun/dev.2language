# Import flask and datetime module for showing date and time
from app import app
import datetime
 
x = datetime.datetime.now()
 

#app = Flask(__name__)
 
 
# Route for seeing a data
@app.route('/')
def index():
    return "<h1>Hello React+Flask!</h1>"
 
     
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)