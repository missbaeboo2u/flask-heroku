from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello ชลัมพู วัฒนศัพท์ เลขที่21 ชั้น ม.4/7"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/baebeebi')
def hi():
    return "สวัสดีค่ะ"    

if __name__ == "__main__":
    app.run(debug=False)
