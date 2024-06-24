import pytest
import subprocess

def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        print(f"Test {item.name} failed.")
        run_command()

def run_command():
    command = "cat pytest.log"
    result = subprocess.run(command, shell = True, capture_output = True, text = True)
    print(f"Command output: {result.stdout}")
    print(f"Command errors: {result.stderr}")
