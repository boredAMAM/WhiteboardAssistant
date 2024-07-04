from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

@app.route('/')
def display_homepage():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def save_drawing():
    drawing_data = request.json
    return jsonify({'status': 'success', 'message': 'Drawing saved successfully.'})

@app.route('/erase', methods=['POST'])
def erase_drawing_part():
    erased_data = request.json
    return jsonify({'status': 'success', 'message': 'Selected drawing part erased successfully.'})

@app.route('/notes', methods=['GET', 'POST', 'DELETE'])
def notes_management():
    if request.method == 'GET':
        notes = [{'id': 1, 'content': 'Sample note'}]
        return jsonify(notes)
    
    elif request.method == 'POST':
        new_note_data = request.json
        return jsonify({'status': 'success', 'message': 'Note added successfully.'})
    
    elif request.method == 'DELETE':
        deleted_note_id = request.json.get('id')
        return jsonify({'status': 'success', 'message': 'Note deleted successfully.'})

if __name__ == '__main__':
    app.run(debug=True)