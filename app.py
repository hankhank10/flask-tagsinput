from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/submit', methods=['POST'])
def submit_names():

    cities_string = request.form.get("tag-input-field")

    cities_list = cities_string.split(",")

    print (cities_list)
    return render_template('output.html', cities_list=cities_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)