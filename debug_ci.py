import sys
import os

print("=== DEBUG INFO ===")
print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")
print(f"CWD: {os.getcwd()}")
print(f"SYS.PATH: {sys.path}")

print("\n--- CHECKING FLASK ---")
try:
    import flask
    print(f"SUCCESS: Flask imported from {flask.__file__}")
    print(f"Flask Version: {flask.__version__}")
except ImportError as e:
    print(f"FAILURE: Could not import flask. Error: {e}")
except Exception as e:
    print(f"FAILURE: Error importing flask: {e}")

print("\n--- CHECKING APP IMPORT ---")
try:
    # Mimic what pytest does / what test_app.py does
    import app.app
    print(f"SUCCESS: Imported app.app from {app.app.__file__}")
except ImportError as e:
    print(f"FAILURE: Could not import app.app. Error: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"FAILURE: Error importing app.app: {e}")
    import traceback
    traceback.print_exc()

print("=== END DEBUG INFO ===")

