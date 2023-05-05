# selenium_pom_design
Learning project about how to combine different tools and designs to improve maintenance and avoid duplicated code in large projects.

This project was based on "SDET- QA Automation Techie" video series on youtube Link: https://www.youtube.com/playlist?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf

Frontend: https://demo.nopcommerce.com/
Backend: https://admin-demo.nopcommerce.com/login
    - Admin email: admin@yourstore.com
    - Admin password: admin

### Prerequisites
- [Python 3.10.11](https://www.example.com)
- [Selenium 4.8.3]
- [Pytest]
- [ChromeWebDriver] (https://chromedriver.chromium.org/downloads - Same version as your Chrome)
- [Pytest-html]
- [Python-dotenv==1.0.0]
- Configure PATH_DRIVER variable to your local "chromedriver.exe" in .env file. (PATH_DRIVER="your/chromedriver.exe/route")
- [Pytest-xdist]
- [Openpyxl]
- [Allure-pytest]

### Commands: 
pytest -s -v  -n=2 --html=reports\\report.html testCases\\test_login.py

### Tests
-   test_homePageTitle
-   test_login
-   test_addNewCustomer
-   test_searchCustomerByEmail
-   test_searchCustomerByName
