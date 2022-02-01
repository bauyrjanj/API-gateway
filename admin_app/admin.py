from flask import Flask

app = Flask(__name__)

@app.route("/")
def jobs():
    return "Admin app running"

@app.route("/health")
def health_check():
    return "Ok"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5056)

