from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():

    #printing to help check what requests are going through
    '''
    print "\n\n\n\n"
    print "***DIAG: THIS FLASK OBJ***"
    print app
    print "***DIAG: REQUEST OBJ"
    print request
    print "***DIAG: REQUEST HEADERS***"
    print "headers"
    print request.headers
    print "***DIAG: REQUEST ARGS***"
    print "args"
    print request.args 
    print "***DIAG: REQUEST FORM"
    print "form"
    print request.form
    '''
    return render_template("login.html")


@app.route("/welcome")
def welcome():
    name = request.args['name']
    username = request.args['username']
    password = request.args['password']
    method = request.method

    return render_template("welcome.html", name=name, username=username, password=password, method=method)



if __name__ == "__main__":
    app.debug = True
    app.run()
