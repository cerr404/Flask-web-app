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