import configparser
from pyral import Rally

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('testRail.cfg')

# Set up a connection to TestRail using the configuration settings
testrail_server = config.get('API', 'url')
testrail_user = config.get('API', 'email')
testrail_password = config.get('API', 'password')
project_id = config.get('TESTRUN', 'project_id')

# Initialize the TestRail connection
rally = Rally(testrail_server, testrail_user, testrail_password)


def update_testrail_result(testrail_id, verdict, comments):
    test_case = rally.get('TestCase', query=f'(FormattedID = "{testrail_id}")', project=project_id)
    if test_case:
        test_case = test_case[0]
        result = {
            'Verdict': verdict,
            'Comments': comments,
        }
        rally.create('TestCaseResult', data=result, project=project_id, TestCase=test_case)
    else:
        print(f"TestRail ID {testrail_id} not found in TestRail")
