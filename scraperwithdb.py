from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path='/home/rajiv/Desktop/selenium/geckodriver') #download the driver and add the path name
def make100(browser):
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/label/select/option[4]').click()  

def isfinallist(browser):
    next_button=browser.find_element_by_id('dataTables1_next')
    return (next_button.get_attribute('class')=='paginate_button next disabled')
def stategetter(x,browser):
    browser.find_element_by_xpath(x).click() # name of the state
    state=browser.find_element_by_xpath(x).text
#/html/body/nav/div[2]/form/div/select[1]/option[3]
    browser.find_element_by_xpath('/html/body/nav/div[2]/form/section/button').click()
    make100(browser)
    while not isfinallist(browser):
        table=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/table/tbody')
        for i in table.find_elements_by_xpath('.//tr'):
            s=i.get_attribute('innerHTML')
    #print s
            cnt=0
            s_nam=False
            s_nam_e=False
            s_dept= False
            s_dept_e= False
            s_inst=False
            s_inst_e=False
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
                elif cnt==16 and not s_inst:
                    start_ins_nam=i+1
                    s_inst=True
                elif cnt==17 and not s_inst_e:
                    inst_name=s[start_ins_nam:i-3]
                    s_inst_e=True
            dumptodb((name,inst_name,dept,state))
        next_button=browser.find_element_by_id('dataTables1_next')
        next_button.click()
def scrape_local():
    browser = webdriver.Firefox(executable_path='/home/rajiv/Desktop/selenium/geckodriver')
    browser.get('https://www.facilities.aicte-india.org/dashboard/pages/faculties.php')
    statestringbase='/html/body/nav/div[2]/form/div/select[1]/option['
    cleardb('local_institutes')
    for i in range(1,39):
        print statestringbase+str(i)+']'
        stategetter(statestringbase+str(i)+']',browser)
def connect():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12273432",
    passwd="d91U1fGfc7",
    db="sql12273432"
    ) 
    return mydb
def dumptodb(val):
    mydb=connect()
    cursor=mydb.cursor()
    sql="INSERT INTO local_institutes VALUES(%s,%s,%s,%s)"
    '''val=[
        ('xyz','abc','def'),
        ('ghhj','ddj','dd'),
        ('sh','sks','sh')
    ]'''
    cursor.execute(sql,val)
    mydb.commit()
def cleardb(tab_name):
    db=connect()
    sql="Delete from "+x+" "
    cursor=db.cursor()
    cursor.executesql(sql)
    db.commit()
if __name__=='__main__':
	scrape_local()