
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
class DemoFindElementById:
    def __init__(self,range,keys):
        self.range=range
        self.keys=keys
    def locate_by_id_demo(self):
        self.driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get("https://www.google.co.in")
        self.driver.maximize_window()
    def give_keys(self):
        self.driver.find_element(By.XPATH,"//input[@title='Search']").send_keys(self.keys)
        self.driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
        self.driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]').click()
    
    def print_title_url_import_csv(self):
        with open('scraping3.csv','w',encoding='utf8',newline='') as f:
            self.writer=csv.writer(f)
            
            header=['titles','url']
            self.writer.writerow(header)
            for i in range(self.range):
                print('scraping page',i+1)
                self.titles=self.driver.find_elements(By.CLASS_NAME,'mCBkyc')
                self.url=self.driver.find_elements(By.CLASS_NAME,'WlydOe')
                for j,k in zip(self.titles,self.url):
                    print('titles',j.text,'url',k.get_attribute('href'))
                    self.writer.writerow([j.text,k.get_attribute('href')])
                next_button=self.driver.find_element(By.XPATH,"//span[normalize-space()='Next']")
                next_button.click()
                time.sleep(1)
           
id=DemoFindElementById(12,"Virat Kohli")
id.locate_by_id_demo()
id.give_keys()
id.print_title_url_import_csv()


