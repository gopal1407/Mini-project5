from app import create_app  # This assumes you have a 'create_app' function in your 'app/__init__.py'

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
