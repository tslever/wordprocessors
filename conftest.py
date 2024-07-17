'''
Module conftest.py makes function pytest_runtest_makereport available.
'''

import subprocess

def pytest_runtest_makereport(item, call):
    '''
    Runs a command if a test fails and is not marked as expected to fail

    Keyword arguments:
        item
        call

    Return values:
        none

    Side effects:
        Runs a command if a test fails and is not marked as expected to fail

    Exceptions raised:
        none

    Restrictions of when this is called:
        This function is called automatically by pytest.
    '''

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
    '''
    Prints data from Standard Output and Standard Error
    when data is read from a pytest log and written to Standard Output

    Keyword arguments:
        none

    Return values
        none

    Side effects:
        Prints data from Standard Output and Standard Error
        when data is read from a pytest log and written to Standard Output

    Exceptions raised:
        none

    Restrictions on when this method can be called:
        This function is called automatically by function pytest_runtest_makereport.
    '''

    command = "cat pytest.log"
    result = subprocess.run(
        command, shell = True, capture_output = True, text = True, check = False
    )
    print(f"Command output: {result.stdout}")
    print(f"Command errors: {result.stderr}")
