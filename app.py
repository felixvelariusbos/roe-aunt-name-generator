from flask import Flask
from flask import render_template, request
import aunt_namer

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():

    if request.method == 'POST':
        result = 'posted!'
        first_letter = request.form['letter']
        
        if first_letter == '':
            first_letter = None
            
        result = aunt_namer.main(first_letter)
        #result = "here was your letter! %s" % first_letter   
    else:
        result = '-'
    
    return render_template('home.html', result = result)
    
if __name__ == "__main__":
    app.run(debug=True)