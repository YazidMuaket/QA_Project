import sys
from time import sleep
import pytest
import timedelta
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from datetime import date , timedelta

@pytest.fixture
def driver():
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = uc.Chrome(options=options)
    driver.get('https://www.booking.com/index.html')
    sleep(3)
    yield driver
    driver.quit()

#TC2 - Login with Valid Email Address but entering incorrect OTP Code

def test_1(driver):

    signInButton = driver.find_element(By.XPATH, '//span[text()="Sign in"]')
    signInButton.click()
    sleep(1)

    email = driver.find_element(By.ID, 'username')
    email.send_keys('tu.pp.24.9.8@gmail.com')
    continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
    continueButton.click()
    sleep(3)
    for i in range (6):
        codeName= '//input[@name="code_'
        codeName = codeName+str(i)+'"]'
        otpInput = driver.find_element(By.XPATH, codeName)
        otpInput.send_keys(i)
        sleep(1)
    verifyButton = driver.find_element(By.XPATH, '//span[text()="Verify email"]')
    verifyButton.click()
    sleep(1)
    errorMessage = driver.find_element(By.XPATH, '//span[@class="error-block"]').text
    assert (errorMessage) == "This code is expired. Request a new code and try again.", "Test failed"

    sleep(3)

#TC3 - Registering Invalid Email Address without (@)

# def test_2(driver):
#
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys('test.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(3)
#     errorMessage = driver.find_element(By.ID, 'username-note').text
#     assert (errorMessage) == "Make sure the email address you entered is correct.", "Test failed"

#TC_4 - Registering with empty value for the email

# def test_3(driver):
#
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(3)
#     errorMessage = driver.find_element(By.ID, 'username-note').text
#     assert (errorMessage) == "Registering with empty value for the email", "Test failed"


#TC7 - Registering with these special characters ( ! +  @ # $ % ^ & * ( ) ) for the email address

# def test_4(driver):
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys('testi#ng123@gmail.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)
#     errorMessage = driver.find_element(By.XPATH, '//h1[text()="Verify your email address"]').text
#     assert (errorMessage) == "Verify your email address", "Test failed"

#TC8 - Registering Invalid Email Address starting with ( _ or - )

# def test_5(driver):
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys('_test@gmail.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)

#TC12 - Registering with email containing spaces

# def test_6(driver):

#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys('testi ng123@gmail.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)
#     errorMessage = driver.find_element(By.XPATH, '//h1[text()="Verify your email address"]').text
#     assert (errorMessage) == "Verify your email address", "Test failed"


#Testing if the stay is booked in Paris

# def test_7(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('Paris')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     today = str(date.today())
#     datexPath= '//span[@data-date="'
#     datexPath = datexPath+today+'"]'
#     selectedDate = driver.find_element(By.XPATH,datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     address = driver.find_element(By.XPATH, '//span[@data-testid="address"]').text
#     assert ('Paris' in address),'Test Failed'


#Testing if one night is booked in Cairo

# def test_8(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('Cairo')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     today = str(date.today())
#     datexPath= '//span[@data-date="'
#     datexPath = datexPath+today+'"]'
#     selectedDate = driver.find_element(By.XPATH,datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     address = driver.find_element(By.XPATH, '//span[@data-testid="address"]').text
#     night = driver.find_element(By.XPATH, '//div[@data-testid="price-for-x-nights"]').text.split(' ')[0]
#     assert ('Cairo' in address),'Test Failed'
#     assert ('1' in night),'Test Failed'

#TC13 - Filtering search results by price range mish kamel

# def test_8(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('Paris')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     today = str(date.today())
#     datexPath= '//span[@data-date="'
#     datexPath = datexPath+today+'"]'
#     selectedDate = driver.find_element(By.XPATH,datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(30)


#-----------------------------
#TC14 - Registering with temporary email domains

# def test_9(driver):
#
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys('worngemail@test.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)
#     errorMessage = driver.find_element(By.XPATH, '//h1[text()="Verify your email address"]').text
#     assert (errorMessage) == "Verify your email address", "Test failed"


# TC15 - Registering with emoji in email field

# def test_10(driver):
#
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID,'username')
#     email.send_keys("emailcontainingemoji♥@gmail.com")
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)
#     errorMessage = driver.find_element(By.XPATH, '//h1[text()="Verify your email address"]').text
#     assert (errorMessage) == "Verify your email address", "Test failed"
#


# TC15 - Registering with email containing non-ASCII characters


# def test_11(driver):
#     registerButton = driver.find_element(By.XPATH, '//span[text()="Register"]')
#     registerButton.click()
#     sleep(1)
#     email = driver.find_element(By.ID, 'username')
#     email.send_keys("éuser@email.com")
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(30)
#     errorMessage = driver.find_element(By.XPATH, '//h1[text()="Verify your email address"]').text
#     assert (errorMessage) == "Verify your email address", "Test failed"


#TC18 Searching for hotels with valid criteria

# def test_12(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('London')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     today = str(date.today())
#     datexPath= '//span[@data-date="'
#     datexPath = datexPath+today+'"]'
#     selectedDate = driver.find_element(By.XPATH,datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     address = driver.find_element(By.XPATH, '//span[@data-testid="address"]').text
#     night = driver.find_element(By.XPATH, '//div[@data-testid="price-for-x-nights"]').text.split(' ')[0]
#     adults= driver.find_element(By.XPATH, '//div[@data-testid="price-for-x-nights"]').text.split(', ')[1][0]
#     assert ('London' in address),'Test Failed'
#     assert ('1' in night),'Test Failed'
#     assert ('2' in adults),'Test Failed'



# # TC19 Searching for hotels with invalid dates (check-out before check-in)
#
# def test_13(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('London')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     checkIn = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     checkIn.click()
#     checkIn.click()
#
#     tomorrow = str(date.today() + timedelta(1))
#     print(tomorrow)
#
#     today = str(date.today())
#     print(today)
#
#     CheckinxPath = '//span[@data-date="'
#     CheckinxPath = CheckinxPath+tomorrow+'"]'
#
#     CheckoutxPath = '//span[@data-date="'
#     CheckoutxPath = CheckoutxPath + today + '"]'
#
#
#
#     selectedDate1 = driver.find_element(By.XPATH,CheckinxPath)
#     selectedDate1.click()
#     sleep(5)
#     selectedDate2 = driver.find_element(By.XPATH, CheckoutxPath)
#     selectedDate2.click()
#     sleep(5)
#
#
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#
#     searchedDate = driver.find_element(By.XPATH, '//span[@data-testid="date-display-field-start"]').text.split(" ")[2]
#     # print(searchedDate)
#     # print(date.today().day)
#     # assert searchedDate == today
#     bdo takmel
#     print("mahmoud el top")





