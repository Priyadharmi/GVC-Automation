from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import driver

def test_Payroll():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://cvcqa.adcuratio.net/login")
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("kfunes@concretevalue.com")
    driver.find_element(By.ID, "password").send_keys("Payroll@123")
    time.sleep(10)
    submitbtn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submitbtn.click()
    time.sleep(15)
    #daily audit report
    reporttypebtn = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn.click()
    dailyauditrpt = driver.find_element(By.XPATH, "//option[text()='Daily Audit Report']")
    dailyauditrpt.click()
    time.sleep(10)
    selectdaybtn = driver.find_element(By.XPATH,"//input[@placeholder='Select Day']")
    selectdaybtn.click()
    time.sleep(10)
    datebtn = driver.find_element(By.XPATH,"(//div[@tabindex='0'])[2]")
    datebtn.click()
    time.sleep(10)
    selectcompdrop = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop.click()
    time.sleep(10)
    selectcompname = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname).perform()
    time.sleep(10)
    selectcompname.click()
    time.sleep(10)
    proceedbtn = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn.click()
    time.sleep(60)
    searchbtn = driver.find_element(By.XPATH, "//input[@placeholder = 'Search name/emp no.']")
    searchbtn.send_keys("Charles Boyle")
    time.sleep(10)

    #rejected TS report
    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reporttypebtn1 = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn1.click()
    rejectedrpt = driver.find_element(By.XPATH, "//option[@value='report-type-1-a' and text()='Rejected Time Sheet Report']")
    rejectedrpt.click()
    time.sleep(5)
    selectdaybtn1 = driver.find_element(By.XPATH, "//input[@placeholder='Select Day']")
    selectdaybtn1.click()
    time.sleep(10)
    datebtn1 = driver.find_element(By.XPATH, "(//div[@tabindex='0'])[2]")
    datebtn1.click()
    time.sleep(10)
    selectcompdrop1 = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop1.click()
    time.sleep(10)
    selectcompname1 = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname1).perform()
    time.sleep(15)
    selectcompname1.click()
    proceedbtn1 = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn1.click()
    time.sleep(60)
    print("Successfully logged into rejected TS Report")

    # Rest Period Report
    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reporttypebtn2 = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn2.click()
    restperiodrpt = driver.find_element(By.XPATH, "//option[text()='Rest Period Report']")
    restperiodrpt.click()
    time.sleep(5)
    selectdaybtn2 = driver.find_element(By.XPATH, "//input[@placeholder='Select Day']")
    selectdaybtn2.click()
    time.sleep(10)
    datebtn2 = driver.find_element(By.XPATH, "//div[text()='25']")
    datebtn2.click()
    time.sleep(10)
    selectcompdrop2 = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop2.click()
    time.sleep(10)
    selectcompname2 = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname2).perform()
    time.sleep(25)
    selectcompname2.click()
    proceedbtn2 = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn2.click()
    time.sleep(60)
    print("Successfully logged into Rest Period TS Report")

    #Weekly Approved Report
    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reportradiobtn2 = driver.find_element(By.XPATH, "//input[@value='report-type-2']")
    reportradiobtn2.click()
    reporttypebtn3 = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn3.click()
    weeklyapprovedrpt = driver.find_element(By.XPATH, "//option[text()='Weekly Approved Time Sheet Report']")
    weeklyapprovedrpt.click()
    time.sleep(10)
    selectweekbtn = driver.find_element(By.XPATH, "//input[@placeholder='Select Week']")
    selectweekbtn.click()
    time.sleep(10)
    weekbtn = driver.find_element(By.XPATH, "(//div[@class='react-datepicker__week'])[4]")
    weekbtn.click()
    time.sleep(10)
    selectcompdrop3 = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop3.click()
    time.sleep(10)
    selectcompname3 = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname3).perform()
    time.sleep(15)
    selectcompname3.click()
    time.sleep(10)
    proceedbtn3 = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn3.click()
    time.sleep(120)
    searchbtn = driver.find_element(By.XPATH, "//input[@placeholder = 'Search name/emp no.']")
    searchbtn.send_keys("Charles Boyle")
    print("Successfully logged into weekly approved Report")

    #Weekly Un-approved Report
    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reportradiobtn2 = driver.find_element(By.XPATH, "//input[@value='report-type-2']")
    reportradiobtn2.click()
    reporttypebtn = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn.click()
    weeklyunapprovedrpt = driver.find_element(By.XPATH, "//option[text()='Weekly Unapproved Time Sheet Report']")
    weeklyunapprovedrpt.click()
    time.sleep(10)
    selectweekbtn4 = driver.find_element(By.XPATH, "//input[@placeholder='Select Week']")
    selectweekbtn4.click()
    time.sleep(10)
    weekbtn1 = driver.find_element(By.XPATH, "(//div[@class='react-datepicker__week'])[4]")
    weekbtn1.click()
    time.sleep(10)
    selectcompdrop4 = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop4.click()
    time.sleep(10)
    selectcompname4 = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname4).perform()
    time.sleep(20)
    selectcompname4.click()
    time.sleep(10)
    proceedbtn4 = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn4.click()
    time.sleep(120)
    searchbtn4 = driver.find_element(By.XPATH, "//input[@placeholder = 'Search name/emp no.']")
    searchbtn4.send_keys("Charles Boyle")
    time.sleep(10)
    print("Successfully logged into weekly Un-approved Report")

#Timesheet Report

    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reportradiobtn3 = driver.find_element(By.XPATH, "//input[@value='report-type-3']")
    reportradiobtn3.click()
    reporttypebtn5 = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn5.click()
    timesheetrpt = driver.find_element(By.XPATH, "//option[text()='Time Sheet Report']")
    timesheetrpt.click()
    time.sleep(5)
    selectdayorweekbtn6 = driver.find_element(By.XPATH, "//input[@placeholder='Select Day/Week']")
    selectdayorweekbtn6.click()
    time.sleep(10)
    datebtn1 = driver.find_element(By.XPATH, "//div[text()='25']")
    datebtn1.click()
    time.sleep(10)
    datebtn2 = driver.find_element(By.XPATH, "//div[text()='26']")
    datebtn2.click()
    time.sleep(10)
    selectcompdrop6 = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop6.click()
    time.sleep(10)
    selectcompname6 = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname6).perform()
    time.sleep(15)
    selectcompname6.click()
    proceedbtn6 = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn6.click()
    time.sleep(60)
    searchbtn6 = driver.find_element(By.XPATH, "//input[@placeholder = 'Search name/emp no.']")
    searchbtn6.send_keys("Charles Boyle")
    time.sleep(10)
    print("Successfully logged into Timesheet Report")

#overnight TS Report
    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reportradiobtn3 = driver.find_element(By.XPATH, "//input[@value='report-type-3']")
    reportradiobtn3.click()
    reporttypebtn6 = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn6.click()
    overnightrpt = driver.find_element(By.XPATH, "//option[text()='Over Night Timesheet Report']")
    overnightrpt.click()
    time.sleep(5)
    selectdayorweekbtn6 = driver.find_element(By.XPATH, "//input[@placeholder='Select Day/Week']")
    selectdayorweekbtn6.click()
    time.sleep(10)
    datebtn1 = driver.find_element(By.XPATH, "//div[text()='25']")
    datebtn1.click()
    time.sleep(10)
    datebtn2 = driver.find_element(By.XPATH, "//div[text()='26']")
    datebtn2.click()
    time.sleep(10)
    proceedbtn = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn.click()
    time.sleep(60)
    searchbtn = driver.find_element(By.XPATH, "//input[@placeholder = 'Search name/emp no.']")
    searchbtn.send_keys("charles boyle")
    time.sleep(10)
    print("Successfully logged into Overnight Timesheet Report")

#Missing Approval Timesheet Report

    backbtn = driver.find_element(By.XPATH, "//span[@aria-label='left-circle']")
    backbtn.click()
    reportradiobtn3 = driver.find_element(By.XPATH, "//input[@value='report-type-3']")
    reportradiobtn3.click()
    reporttypebtn = driver.find_element(By.XPATH, "//select[@class='reportTypeSelectore_selector__ej--y']")
    reporttypebtn.click()
    Missingapprovalrpt = driver.find_element(By.XPATH, "//option[text()='Missing Approval Time Sheet Report']")
    Missingapprovalrpt.click()
    time.sleep(5)
    selectdayorweekbtn = driver.find_element(By.XPATH, "//input[@placeholder='Select Day/Week']")
    selectdayorweekbtn.click()
    time.sleep(10)
    datebtn1 = driver.find_element(By.XPATH, "//div[text()='25']")
    datebtn1.click()
    time.sleep(10)
    datebtn2 = driver.find_element(By.XPATH, "//div[text()='26']")
    datebtn2.click()
    time.sleep(10)
    time.sleep(10)
    selectcompdrop = driver.find_element(By.XPATH, "//span[contains(text(),'011-Concrete Corp Of Nevada')]")
    selectcompdrop.click()
    time.sleep(10)
    selectcompname = driver.find_element(By.XPATH, "//div[contains(text(),'041-GVC LLC')]")
    action_obj = ActionChains(driver)
    action_obj.move_to_element(selectcompname).perform()
    time.sleep(15)
    selectcompname.click()
    proceedbtn = driver.find_element(By.XPATH, "//span[text()=' Proceed']")
    proceedbtn.click()
    time.sleep(60)
    print("Successfully logged into Missing Approval Timesheet Report")

    driver.quit()