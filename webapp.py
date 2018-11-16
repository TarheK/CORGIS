from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')
@app.route("/responseh")
def render_responseh():
    millimeters = float(request.args['millimeters'])
    response=millimeters * (1/10)
    return render_template('response.html', response = response)
if __name__=="__main__":
    app.run(debug=False, port=54321)
