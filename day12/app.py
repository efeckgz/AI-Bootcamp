from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('salary_lr.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    experience = float(request.form.get('experience'))
    test_score = float(request.form.get('testScore'))
    interview_score = float(request.form.get('interviewScore'))

    prediction = model.predict([[experience, test_score, interview_score]])
    prediction = f'Prediction: ${float(str(prediction)[2: -2]):.2f}'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)