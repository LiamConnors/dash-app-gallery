"""
Script that saves screenshots of multi-page app pages.
Requires that the app is running on a separate process on localhost:8050

Save images in the utils_make_images/assets directory


"""

import os
from selenium import webdriver
import time

from utils.file_names import get_example_app_names


def snapshot(driver):

    example_apps = get_example_app_names()

    for page in example_apps:
        driver.get(f"http://localhost:8050/{page}")
        time.sleep(5)
        driver.save_screenshot(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "assets", f"{page}.png"
            )
        )


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.set_window_size(850, 850)
    try:
        snapshot(driver)
    finally:
        driver.quit()
