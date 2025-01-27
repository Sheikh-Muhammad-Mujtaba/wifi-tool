import subprocess
import sys

def check_and_run(program):
    required_modules = ["colorama", "tabulate"]
    missing_modules = []

    # Check for missing modules
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    # If missing modules, run install.py
    if missing_modules:
        print("Missing required modules: ", ", ".join(missing_modules))
        print("Running install.py to install missing modules...")
        try:
            subprocess.run([sys.executable, "install.py"], check=True)
        except subprocess.CalledProcessError as e:
            print("Failed to install required modules. Exiting...")
            sys.exit(1)

    # Run the main program
    print("All requirements satisfied. Running the program...")
    program()

# Example usage with your main program
if __name__ == "__main__":
    from wifi_tool import main 
    check_and_run(main)
