from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__) # creating the blueprint for our views object

@views.route('/', methods= ['GET', 'POST'])
@login_required # makes sure to show this route only if we've loged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Your note is too short')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has added :D', category='success')




    return render_template("home.html", user=current_user)




@views.route('/update-note', methods=['POST'])
@login_required
def update_note():
    data = json.loads(request.data)
    note_id = data.get('noteId')
    new_content = data.get('content')

    if not new_content or len(new_content) < 1:
        return jsonify({"error": "Note content is too short."}), 400

    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        note.data = new_content
        db.session.commit()
        return jsonify({"message": "Note updated successfully."}), 200
    else:
        return jsonify({"error": "Note not found or unauthorized."}), 404




@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})  


