from application import app,manager
from flask_script import Server
import urls

manager.add_command("runserver",Server(host="localhost",port=5000,use_debugger=True,use_reloader=True))



def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()