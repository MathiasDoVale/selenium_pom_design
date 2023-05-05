import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    # Add customer Page
    lnkSide_bar_menu_id = "nopSideBarPusher"
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']" #El problema se me esta dando aca porque detecta dos barras iguales.
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
        

    def clickSideBarMenu(self):
        self.driver.find_element(By.ID, self.lnkSide_bar_menu_id).click()

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        if role not in( 'Administrators',
                        'Forum Moderators',
                        'Guests',
                        'Vendors'):
            raise ValueError("Role is not available")
        else:
            self.driver.maximize_window()
            unselectable_divs = self.driver.find_elements(By.XPATH, '//div[@class="k-widget k-multiselect k-multiselect-clearable"]')
            i=0
            for div in unselectable_divs:
                i+=1
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", div)
                if i == 2:
                    div.click()
            time.sleep(2)
            if(role=='Administrators'):
                option = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[1]")
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", option)
                option.click()
            elif(role=='Forum Moderators'):
                option = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[2]")
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", option)
                option.click()
            elif(role=='Registered'):
                option = self.driver.find_element(By.XPATH, "//html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[3]")
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", option)
                option.click()
            elif(role=='Guests'):
                #Business Rule. If a customer is Guest, can not be Registrered
                delete_span = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]")
                delete_span.click()

                option = self.driver.find_element(By.XPATH, "//html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[3]")
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", option)
                option.click()
            elif(role=='Vendors'):
                option = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[5]")
                self.driver.execute_script("arguments[0].removeAttribute('unselectable')", option)
                option.click()

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()