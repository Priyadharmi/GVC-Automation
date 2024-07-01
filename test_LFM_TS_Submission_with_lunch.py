import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from TS_details import TS_details


def test_lfm_ts_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gvcqa.adcuratio.net/login")

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("charles.boyle@adcuratio.com")
    driver.find_element(By.ID, "password").send_keys("Adcuratio@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    #TS_details()
    projectbtn = driver.find_element(By.XPATH,"(//span[@class='ant-select-selection-search'])[1]")
    projectbtn.click()
    time.sleep(5)
    projectselectionbtn = driver.find_element(By.XPATH, "//div[@title='ProjectGvcQATest2']")
    projectselectionbtn.click()
    startDateandtime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[1]")))
    startDateandtime.send_keys('2024-06-26 05:01 AM')
    startDateandtime.send_keys(Keys.ENTER)
    time.sleep(10)
    enddateandtime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Date Time'])[2]")))
    enddateandtime.send_keys('2024-06-26 09:00 AM')
    enddateandtime.send_keys(Keys.ENTER)
    time.sleep(5)
    Lunchtogglebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")))
    Lunchtogglebtn.click()
    time.sleep(10)
    Lunchstarttime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Time'])[1]")))
    Lunchstarttime.send_keys('07:30 AM')
    Lunchstarttime.send_keys(Keys.ENTER)
    time.sleep(10)
    # Lunchendtime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Time'])[2]")))
    # Lunchendtime.clear()
    # time.sleep(10)
    # Lunchendtime.send_keys('2024-06-26 08:00 AM')
    # Lunchendtime.send_keys(Keys.ENTER)
    phasecodeselbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")))
    time.sleep(5)
    phasecodeselbtn.click()
    time.sleep(5)
    phasebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@title='GENERAL CONDITIONS']")))
    phasebtn.click()
    time.sleep(10)
    laborcodeselbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='ant-select-selection-search'])[3]")))
    laborcodeselbtn.click()
    time.sleep(5)
    laborcodebtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@title='PROJECT MANAGER']")))
    laborcodebtn.click()
    time.sleep(5)
    hrsbtn = driver.find_element(By.XPATH, "//input[@placeholder='00:00']")
    hrsbtn.send_keys('03:29')
    hrsbtn.send_keys(Keys.ENTER)
    time.sleep(5)
    legalquestionbtn1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[1]")))
    legalquestionbtn1.click()
    time.sleep(2)
    legalquestionbtn2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[2]")))
    legalquestionbtn2.click()
    time.sleep(2)
    legalquestionbtn3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-radio'])[3]")))
    legalquestionbtn3.click()
    time.sleep(2)
    checkboxbtn = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkboxbtn.click()
    time.sleep(2)
    submitbtn = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submitbtn.click()
    confirmationbtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Yes']")))
    confirmationbtn.click()
    time.sleep(15)
    Okaybtn = driver.find_element(By.XPATH, "//span[text()='Okay']")
    if Okaybtn is not None:
        Okaybtn.click()
        print("TS submitted successfully")
    driver.quit()