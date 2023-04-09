from flask import *
two=Flask(__name__)

@two.route('/CSS')
def Amar():
    return render_template('css.html')

if __name__=="__main__":
    two.run(debug=True)
