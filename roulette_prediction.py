from flask import Flask, render_template, request

app = Flask(__name__)

history = []
prediction = []

@app.route('/')
def home():
    return render_template('index.html', history=history, prediction=prediction)

@app.route('/record_result', methods=['POST'])
def record_result():
    result = request.form['result']
    history.append(result)
    if len(history) >= 5:
        analyze_history()
    return render_template('index.html', history=history, prediction=prediction)

def analyze_history():
    global prediction
    prediction = []
    for i in range(1, 5):
        predicted_number = int(history[-1]) + i
        if predicted_number > 36:
            predicted_number -= 36
        prediction.append(predicted_number)

if __name__ == '__main__':
    app.run(debug=True)