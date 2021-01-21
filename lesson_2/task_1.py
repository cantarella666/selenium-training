import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://ru.wikipedia.org/")
    driver.find_element_by_name("search").send_keys("Корги")
    driver.find_element_by_name("go").click()
    WebDriverWait(driver, 10).until(EC.title_is("Вельш-корги — Википедия"))

