import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5000)
