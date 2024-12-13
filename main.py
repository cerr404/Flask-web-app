from website import create_app

app = create_app()

if __name__ == "__main__": # Ensures the app runs when executed directly (not imported)
    app.run(debug=True)