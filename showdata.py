from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import os
from get_latest_chromedriver import update_driver


# options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

prefs = {
    'download.default_directory': str(os.getcwd()) + '\showdata', 
    'profile.default_content_setting_values.automatic_downloads': 1
}

options.add_experimental_option('prefs', prefs)

# disable webdriver-mode
options.add_argument("--disable-blink-features=AutomationControlled")




def main():

    exception_count = 0

    try:
        def get_showdata():
            # initiate webdriver
            driver = webdriver.Chrome(
                'chromeDriver/chromedriver.exe',
                options=options
            )

            driver.get('https://showdata.gks.ru/finder/descriptors')

            url_list = []

            WebDriverWait(driver, 200).until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, ".rosstat2-dmarts_last_data_update")))
            driver.find_element_by_css_selector('.rosstat2-dmarts_last_data_update').click()

            new_data_list = driver.find_elements_by_css_selector('.slick-multiline')

            for data_item in new_data_list:
                url = data_item.find_element_by_css_selector('a').get_attribute('href')
                url_list.append(url)

        
            for url in url_list:
                driver.get(url)
                print(url)

                WebDriverWait(driver, 2000).until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, ".report-btn.btn.btn-primary")))
                driver.find_element_by_css_selector('.report-btn.btn.btn-primary').click()

                time.sleep(3)
                WebDriverWait(driver, 2000).until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, ".report-export")))
                driver.find_element_by_css_selector('.report-export').click()
                time.sleep(2)
            

        get_showdata()


    except Exception as e:

        if (exception_count > 1):
            return print(e)

        update_driver()
        get_showdata()
        
        exception_count += 1
        print(e)

    
   

def get_current_date():
    now = datetime.now()
    return now.strftime('%d-%m-%y %H-%M')




def write_json(data):
    with open(f'rosstat/{get_current_date()}.json', 'w', encoding='utf-8') as f:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(str(json_data))


if __name__ == '__main__':
    main()

