import pytest
from selenium import webdriver


# This is to run test cases on different browsers-

def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="Chrome", help="Specify the browser: Chrome or Firefox or "
                                                                         "Edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "Edge":
        driver = webdriver.Edge
    else:
        raise ValueError("Unsupported Browser")
    return driver


##########################################################
#Hook for adding new fields in the html report-
from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]['Project Nmae'] = 'Ecommerce project,Test'
    config.stash[metadata_key]['Test module name'] = 'Admin login test'
    config.stash[metadata_key]['Tester Name'] = 'AbhijeetQA'


#HOOK for delete/modify env info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
