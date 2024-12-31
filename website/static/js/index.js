function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


document.getElementById("note").addEventListener("input", function () {
    const textarea = this;
    const value = textarea.value;

    // Check if the text contains Persian or Arabic characters
    const isRTL = /[\u0600-\u06FF\u0750-\u077F]/.test(value);

    // Set the direction dynamically
    textarea.setAttribute("dir", isRTL ? "rtl" : "ltr");
});



// Edit a note
function editNote(noteId) {
  const noteContent = document.getElementById(`note-content-${noteId}`);
  const currentContent = noteContent.textContent;

  // Create a textarea for editing
  noteContent.innerHTML = `
    <textarea id="edit-note-${noteId}" class="form-control mb-2">${currentContent}</textarea>
    <button class="btn btn-success btn-sm" onClick="saveNote(${noteId})">Save</button>
    <button class="btn btn-secondary btn-sm" onClick="cancelEdit(${noteId}, '${currentContent}')">Cancel</button>
  `;
}

// Save an updated note
async function saveNote(noteId) {
  const updatedContent = document.getElementById(`edit-note-${noteId}`).value;

  if (updatedContent.length < 1) {
    alert("Note content is too short!");
    return;
  }

  const response = await fetch('/update-note', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ noteId, content: updatedContent }),
  });

  const result = await response.json();
  if (response.ok) {
    document.getElementById(`note-content-${noteId}`).textContent = updatedContent;
  } else {
    alert(result.error || "Failed to update the note.");
  }
}

// Cancel editing a note
function cancelEdit(noteId, originalContent) {
  const noteContent = document.getElementById(`note-content-${noteId}`);
  noteContent.textContent = originalContent;
}

// Delete a note
async function deleteNote(noteId) {
  const response = await fetch('/delete-note', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ noteId }),
  });

  if (response.ok) {
    document.getElementById(`note-${noteId}`).remove();
  }
}
