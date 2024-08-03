import pytest
import subprocess

def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        # Check if the test has failed
        if call.excinfo is not None:
            # Check if the test is marked as xfail
            xfail_marker = item.get_closest_marker('xfail')
            if xfail_marker is None:
                # If the test is not marked as xfail, run the command
                print(f"Test {item.name} failed and is not marked as xfail.")
                run_command()

def run_command():
    command = "cat pytest.log"
    result = subprocess.run(command, shell = True, capture_output = True, text = True)
    print(f"Command output: {result.stdout}")
    print(f"Command errors: {result.stderr}")
