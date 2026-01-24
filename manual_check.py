import sys
import os

def main():
    print("--- MANUAL TEST START ---")
    print(f"Path: {sys.path}")

    try:
        import flask
        print(f"Flask imported: {flask.__version__} from {flask.__file__}")
    except ImportError:
        print("CRITICAL: Flask not found in manual test!")
        sys.exit(1)

    try:
        print("Importing salary_app.app...")
        from salary_app.app import app
        print("salary_app.app imported successfully.")
        
        app.config['TESTING'] = True
        client = app.test_client()
        
        print("Testing GET / ...")
        rv = client.get('/')
        print(f"Status: {rv.status_code}")
        if rv.status_code == 200:
            print("GET / PASSED")
        else:
            print("GET / FAILED")

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    print("--- MANUAL TEST END ---")

if __name__ == "__main__":
    main()
