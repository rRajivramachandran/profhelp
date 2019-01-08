from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='/home/rajiv/Desktop/selenium/geckodriver')

def make100():
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/label/select/option[4]').click()  

def isfinallist():
    next_button=browser.find_element_by_id('dataTables1_next')
    return (next_button.get_attribute('class')=='paginate_button next disabled')
browser.get('https://www.facilities.aicte-india.org/dashboard/pages/faculties.php')
browser.find_element_by_xpath('/html/body/nav/div[2]/form/div/select[1]/option[7]').click()
browser.find_element_by_xpath('/html/body/nav/div[2]/form/section/button').click()
make100()
while not isfinallist():
    table=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/table/tbody')
    for i in table.find_elements_by_xpath('.//tr'):
        s=i.get_attribute('innerHTML')
    #print s
        cnt=0
        s_nam=False
        s_nam_e=False
        s_dept= False
        s_dept_e= False
        for i in range(len(s)):
        #print s[i]
            if s[i]=='>':
                cnt+=1
            if cnt==3 and not s_nam:
                start_nam=i+1
                s_nam=True
            elif cnt==4 and not s_nam_e:
                name=s[start_nam:i-4]
                s_nam_e=True
            elif cnt==11 and not s_dept:
                start_dep=i+1
                s_dept=True
            elif cnt==12 and not s_dept_e:
                dept=s[start_dep:i-4]
                s_dept_e=True
        print name,dept
    next_button=browser.find_element_by_id('dataTables1_next')
    next_button.click()
