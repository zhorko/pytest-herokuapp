from selenium.webdriver.support.wait import WebDriverWait 

from pages.hero_home_page import HeroHomePage
from pages.hero_checkbox_page import HeroCheckPage


def test_interactions(_browser):
    
    URL_hero = "https://the-internet.herokuapp.com/"
    wait = WebDriverWait(_browser, 10)

    _browser.maximize_window()
    _browser.get(URL_hero)
    
    # Initializations
    hero_home_page = HeroHomePage(_browser)
    hero_check_page = HeroCheckPage(_browser)

    hero_home_page.open_checkboxes()

    assert hero_check_page.click_check_1(wait) is True
    assert hero_check_page.click_check_2(wait) is True