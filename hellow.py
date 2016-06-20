from flask import Flask
#import prime_number
app = Flask(__name__)


@app.source('/<int:n>',methods=(['GET']))
def prime(n):
    return n**2
