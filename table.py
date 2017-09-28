import random
from flask import Flask, render_template
from utils import anotherThing

app=Flask(__name__)
@app.route('/occupations')
def occupations():
    return render_template('base.html',header1="Job Class",header2="Percentage",dict=anotherThing.function(),randomJob=anotherThing.randomJob())
    
if __name__=="__main__":
    app.debug = True
    app.run()