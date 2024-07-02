from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    drawing_data = request.json
    return jsonify({'status': 'success', 'message': 'Drawing saved.'})

@app.route('/erase', methods=['POST'])
def erase():
    erase_data = request.json
    return jsonify({'status': 'success', 'message': 'Part of the board erased.'})

@app.route('/notes', methods=['GET', 'POST', 'DELETE'])
def manage_notes():
    if request.method == 'GET':
        notes = [{'id': 1, 'content': 'Sample note'}]
        return jsonify(notes)
    
    elif request.method == 'POST':
        note_data = request.json
        return jsonify({'status': 'success', 'message': 'Note saved.'})
    
    elif request.method == 'DELETE':
        note_id = request.json.get('id')
        return jsonify({'astatus': 'success', 'message': 'Note deleted.'})

if __name__ == '__main__':
    app.run(debug=True)