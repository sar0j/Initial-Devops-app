from flask import Flask

app =  Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps World 🚀 UPDATE 1.0 minikube"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    