from selenium.webdriver.support.wait import WebDriverWait 


from pages.hero_home_page import HeroHomePage
from pages.hero_checkbox_page import HeroCheckPage

from time import sleep

def test_interactions(_browser):
    
    URL_hero = "https://the-internet.herokuapp.com/"
    URL_demo = "https://demoqa.com/"
    wait = WebDriverWait(_browser, 10)

    _browser.maximize_window()
    _browser.get(URL_hero)
    
    # Initializations
    hero_home_page = HeroHomePage(_browser)
    hero_check_page = HeroCheckPage(_browser)

    hero_home_page.open_checkboxes()
    hero_check_page.click_check_1(wait)

    sleep(300)