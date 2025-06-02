import sys
from time import sleep
import pytest
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

# def test_1(driver):
#
#     signInButton = driver.find_element(By.XPATH, '//span[text()="Sign in"]')
#     signInButton.click()
#     sleep(1)
#
#     email = driver.find_element(By.ID, 'username')
#     email.send_keys('tu.pp.24.9.8@gmail.com')
#     continueButton = driver.find_element(By.XPATH, '//span[text()="Continue with email"]')
#     continueButton.click()
#     sleep(3)
#     for i in range (6):
#         codeName= '//input[@name="code_'
#         codeName = codeName+str(i)+'"]'
#         otpInput = driver.find_element(By.XPATH, codeName)
#         otpInput.send_keys(i)
#         sleep(1)
#     verifyButton = driver.find_element(By.XPATH, '//span[text()="Verify email"]')
#     verifyButton.click()
#     sleep(1)
#     errorMessage = driver.find_element(By.XPATH, '//span[@class="error-block"]').text
#     assert (errorMessage) == "This code is expired. Request a new code and try again.", "Test failed"
#
#     sleep(30)

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

#TC13 - Filtering search results by price range

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
#     dev = driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')
#     Minprice = dev.find_element(By.XPATH, './/span[@role="status"]').text.split(' ')[1]
#     Minprice = int(Minprice)
#     Maxprice = dev.find_element(By.XPATH, './/span[@role="status"]').text.split(' ')[-1]
#     Maxprice = Maxprice.replace(',','')
#     Maxprice = Maxprice.replace('+', '')
#     Maxprice= int(Maxprice)
#     actualprice = driver.find_element(By.XPATH, '//span[@data-testid="price-and-discounted-price"]').text.split(' ')[1]
#     actualprice = actualprice.replace(',','')
#     actualprice = int(actualprice)
#     assert ((actualprice <= Maxprice) and (actualprice >= Minprice)), 'Test failed'



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



# TC19 Searching for hotels with invalid dates (check-out before check-in (Today and Tomorrow))

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
#     tomorrow = str(date.today() + timedelta(1))
#     today = str(date.today())
#     todayShortFormat = date.today().strftime('%a, %b %d')
#     CheckinxPath = '//span[@data-date="'
#     CheckinxPath = CheckinxPath+tomorrow+'"]'
#     CheckoutxPath = '//span[@data-date="'
#     CheckoutxPath = CheckoutxPath + today + '"]'
#     selectedDate1 = driver.find_element(By.XPATH,CheckinxPath)
#     selectedDate1.click()
#     sleep(5)
#     selectedDate2 = driver.find_element(By.XPATH, CheckoutxPath)
#     selectedDate2.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     searchedDate = driver.find_element(By.XPATH, '//span[@data-testid="date-display-field-start"]').text
#     assert (searchedDate == todayShortFormat), 'Test Failed'

# TC_20 - Sorting hotels by customer ratings

# def test_14(driver):
#
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
#     sortButton = driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
#     sortButton.click()
#     sleep(1)
#     highToLowButton = driver.find_element(By.XPATH, '//span[text()="Property rating (high to low)"]')
#     highToLowButton.click()
#     sleep(5)
#     stars = driver.find_element(By.XPATH, '//div[@aria-label="5 out of 5"]')
#     starsValue = stars.get_attribute('aria-label')
#     assert(starsValue == "5 out of 5"), 'Test Failed'


# TC_26 - Searching for hotels with maximum date range

# def test_15(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('London')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     checkIn = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     checkIn.click()
#     checkIn.click()
#     nextYear = str(date.today() + timedelta(365))
#     today = str(date.today())
#     CheckinxPath = '//span[@data-date="'
#     CheckinxPath = CheckinxPath+today+'"]'
#     CheckoutxPath = '//span[@data-date="'
#     CheckoutxPath = CheckoutxPath + nextYear + '"]'
#     selectedDate1 = driver.find_element(By.XPATH,CheckinxPath)
#     selectedDate1.click()
#     sleep(5)
#     for i in range(11):
#         nextMonthButton = driver.find_element(By.XPATH, '//button[@aria-label="Next month"]')
#         nextMonthButton.click()
#         sleep(1)
#     sleep(5)
#     selectedDate2 = driver.find_element(By.XPATH, CheckoutxPath)
#     selectedDate2.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     errorMessage = driver.find_element(By.XPATH, '//div[text()="Sorry, reservations for more than 90 nights aren\'t possible."]').text
#     assert (errorMessage == "Sorry, reservations for more than 90 nights aren't possible."), 'Test failed'

#TC_27 - Verifying map functionality on search results page

# def test_16(driver):
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
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(5)
#     mapButton = driver.find_element(By.XPATH, '//div[@data-testid="map-entry-point"]')
#     mapButton.click()
#     sleep(10)
#     MapBox = driver.find_element(By.XPATH,'//input[@name="field"]')
#     MapBoxtext = MapBox.get_attribute("placeholder")
#     assert ('See distance from' in MapBoxtext),'Test Failed'


# TC_28 - Checking for pet-friendly accommodation filter

# def test_17(driver):
#
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
#     sleep(2)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(2)
#     petFriendlyCheckbox = driver.find_element(By.XPATH, '//div[text()="Pet friendly"]')
#     petFriendlyCheckbox.click()
#     sleep(2)
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(10)
#     petsText = driver.find_element(By.XPATH, '//div[text()="Pets are allowed on request. Charges may apply."]').text
#     assert (petsText == "Pets are allowed on request. Charges may apply."), 'Test failed'


# TC_29 - Verifying the “Free Cancellation” filter

# def test_18(driver):

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
#     sleep(10)
#     freeCancellationCheckbox = driver.find_element(By.XPATH, '//div[text()="Free cancellation"]')
#     freeCancellationCheckbox.click()
#     sleep(5)
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(20)
#     freeCancellationText = driver.find_element(By.XPATH, '//strong[@class="bui-text--variant-strong_2"]').text
#     assert (freeCancellationText == "Free cancellation"), 'Test failed'

#TC_34 - Verify the ability to book without registration

# def test_19(driver):
#
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
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     availabilityButton = driver.find_element(By.XPATH, '//div[@data-testid="title"]')
#     availabilityButton.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     firstReserveButton = driver.find_element(By.XPATH, '//span[@class="bui-button__text"]')
#     firstReserveButton.click()
#     sleep(2)
#     secondReserveButton = driver.find_element(By.XPATH, '//span[@class="bui-button__text js-reservation-button__text"]')
#     secondReserveButton.click()
#     sleep(2)
#     detailsHeader = driver.find_element(By.XPATH, '//h2[text()="Enter your details"]').text
#     assert(detailsHeader == "Enter your details"), 'Test failed'
#     sleep(5)


#TC_35 - Checking social media sharing functionality

#def test_20(driver):
#
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
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(10)
#     ShareB = driver.find_element(By.XPATH, '//button[@data-testid="property-share-button"]')
#     ShareB.click()
#     sleep(5)
#     FacebookB = driver.find_element(By.XPATH, '//button[@data-channel="facebook"]')
#     FacebookB.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[2])
#     sleep(5)
#     Facebooklogo = driver.find_element(By.XPATH,'//a[@href="https://www.facebook.com/"]')
#     Ftitle = Facebooklogo.get_attribute("title")
#     assert(Ftitle == "Go to Facebook home"), 'Test Failed'
#     sleep(5)

#TC_36 - Ensure content updates properly when switching languages

# def test_21(driver):
#     beforeSwitchText = driver.find_element(By.XPATH, '//span[@data-testid="herobanner-title1"]').text
#     switchlanguage = driver.find_element(By.XPATH, '//button[@data-testid="header-language-picker-trigger"]')
#     switchlanguage.click()
#     sleep(5)
#     arabiclanguage = driver.find_element(By.XPATH, '//button[@lang="ar"]')
#     arabiclanguage.click()
#     sleep(5)
#     afterSwitchText = driver.find_element(By.XPATH, '//span[@data-testid="herobanner-title1"]').text
#     assert(beforeSwitchText != afterSwitchText), 'Test Failed'
#     sleep(5)

#TC_41 - Ensure multi-city trips can be booked

# def test_22(driver):
#     flightsButton = driver.find_element(By.ID, 'flights')
#     flightsButton.click()
#     multichoose = driver.find_element(By.XPATH, '//div[@role="combobox"]')
#     multichoose.click()
#     multiC = driver.find_element(By.ID, 'multicity')
#     multiC.click()
#     firstSearchDir = driver.find_element(By.XPATH,'//input[@aria-label="Flight 1 destination"]' )
#     firstSearchDir.send_keys('London')
#     sleep(2)
#     firstdir = driver.find_element(By.XPATH, '//li[@role="option"]')
#     firstdir.click()
#     firstdate =  driver.find_elements(By.XPATH,'//div[@aria-label="Departure date"]')[0]
#     firstdate.click()
#     sleep(5)
#     today = date.today().strftime('%B %d, %Y')
#
#     datexPath = '//div[@aria-label="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#
#     seconddate = driver.find_elements(By.XPATH,'//div[@aria-label="Departure date"]')[1]
#     seconddate.click()
#     sleep(5)
#     nextDate = (date.today() + timedelta(2)).strftime('%B %#d, %Y')
#     print(nextDate)
#     datexPath = '//div[@aria-label="'
#     datexPath = datexPath + nextDate + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#
#
#     thirdSearchDir = driver.find_element(By.XPATH,'//input[@aria-label="Flight 3 origin"]' )
#     thirdSearchDir.send_keys('TLV')
#     sleep(2)
#     firstdir = driver.find_element(By.XPATH, '//li[@role="option"]')
#     firstdir.click()
#
#
#     secondSearchDir = driver.find_element(By.XPATH,'//input[@aria-label="Flight 3 destination"]' )
#     secondSearchDir.send_keys('Dubai')
#     sleep(5)
#     seconddir = driver.find_element(By.XPATH, '//li[@role="option"]')
#     seconddir.click()
#
#
#     thirddate = driver.find_elements(By.XPATH,'//div[@aria-label="Departure date"]')[2]
#     thirddate.click()
#     sleep(5)
#     nextDate2 = (date.today() + timedelta(10)).strftime('%B %#d, %Y')
#     print(nextDate2)
#     datexPath = '//div[@aria-label="'
#     datexPath = datexPath + nextDate2 + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#
#     searchB = driver.find_element(By.XPATH,'//button[@aria-label="Search"]')
#     searchB.click()
#     sleep(5)


#TC_TC_43 - Ensure users can filter hotels based on proximity to popular landmarks
#
# def test_23(driver):
#
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
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)
#     landmarksSection = driver.find_element(By.XPATH, '//div[@data-filters-group="popular_nearby_landmarks"]')
#     firstLandmarkName = landmarksSection.find_element(By.XPATH,'.//div[@data-testid="filters-group-label-content"]').text
#     firstLandmarkCheckBox = landmarksSection.find_element(By.XPATH,'.//input[@type="checkbox"]')
#     firstLandmarkCheckBox.click()
#     sleep(10)
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(5)
#     hotelDescription = driver.find_element(By.XPATH, '//div[@class = "hp-description"]').text
#     assert(firstLandmarkName in hotelDescription), 'Test Failed'


#TC_44 - Try to book without a credit card filter

# def test_24(driver):
#
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
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(10)
#     noCardFilter = driver.find_element(By.XPATH, '//div[text()="Book without credit card"]')
#     noCardFilter.click()
#     sleep(10)
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     priceDataFirstHotel=firstHotel.find_element(By.XPATH, './/strong[text()="No prepayment needed"]').text
#     assert (priceDataFirstHotel == "No prepayment needed"), 'Test Failed'


#TC_45 - Ensure beachfront hotels can be filtered

# def test_25(driver):
#
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('Maldives')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     today = str(date.today())
#     datexPath = '//span[@data-date="'
#     datexPath = datexPath + today + '"]'
#     selectedDate = driver.find_element(By.XPATH, datexPath)
#     selectedDate.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(10)
#     beachSection = driver.find_element(By.XPATH, '//div[@data-filters-group="ht_beach"]')
#     beachCheckbox= beachSection.find_element(By.XPATH, './/input')
#     beachCheckbox.click()
#     sleep(10)
#     firstHotel = driver.find_element(By.XPATH, '//div[@data-testid="property-card"]')
#     firstHotel.click()
#     sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(5)
#     PropertySpecs = driver.find_element(By.XPATH, '//div[@data-testid="PropertyBadges-wrapper"]').text
#     assert ("Beachfront" in PropertySpecs), 'Test Failed'

#TC_46 - Verify search results display options for flexible travel dates

# def test_26(driver):
#     searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
#     searchBox.send_keys('Paris')
#     sleep(2)
#     searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
#     searchResult.click()
#     sleep(2)
#     datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
#     datePicker.click()
#     datePicker.click()
#     sleep(5)
#     flexibleButton = driver.find_element(By.ID, 'flexible-searchboxdatepicker-tab-trigger')
#     flexibleButton.click()
#     sleep(5)
#     weekEndCheckbox = driver.find_element(By.XPATH, '//div[@data-testid="flexible-dates-day"]')
#     weekEndCheckbox.click()
#     monthSelection = driver.find_element(By.XPATH, '//label[@data-testid="flexible-dates-month"]')
#     monthSelection.click()
#     sleep(5)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(5)

#TC_48 - Ensure hyperlink “Terms & conditions” lead to the desired destination

# def test_27(driver):
#     registerButton = driver.find_element(By.XPATH,'//span[text()="Register"]')
#     registerButton.click()
#     sleep(3)
#     termsAndConditonsLink = driver.find_element(By.XPATH, '//span[text()="Terms & Conditions"]')
#     termsAndConditonsLink.click()
#     driver.switch_to.window(driver.window_handles[1])
#     headerText = driver.find_element(By.XPATH, '//h1').text
#     assert (headerText == "Customer terms of service"), 'Test Failed'


#TC_49 - Ensure hyperlink “Privacy statement” lead to the desired destination

# def test_28(driver):
#     registerButton = driver.find_element(By.XPATH,'//span[text()="Register"]')
#     registerButton.click()
#     sleep(3)
#     PrivacyStatementLink = driver.find_element(By.XPATH, '//span[text()="Privacy Statement"]')
#     PrivacyStatementLink.click()
#     driver.switch_to.window(driver.window_handles[1])
#     headerText = driver.find_element(By.ID, 'privacy-statement').text
#     assert ("Privacy & Cookie Statement" in headerText), 'Test Failed'


#TC - Testing to see button "save to next trip" works

# def test_29(driver):
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
#     sleep(2)
#     searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
#     searchButton.click()
#     sleep(2)
#     hotelName = driver.find_element(By.XPATH,'//div[@data-testid="title"]').text
#     saveFavouriteButton = driver.find_element(By.XPATH, '//button[@data-testid="wishlist-button"]')
#     saveFavouriteButton.click()
#     sleep(2)
#     myNextTripButton = driver.find_element(By.XPATH, '//span[text()="My next trip"]')
#     myNextTripButton.click()
#     sleep(2)
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(10)
#     savedHotelName = driver.find_element(By.XPATH, '//h3').text
#     sleep(2)
#     assert (hotelName == savedHotelName), 'Test failed'


# TC - removing a hotel from favourite list

def test_30(driver):
    searchBox = driver.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
    searchBox.send_keys('London')
    sleep(2)
    searchResult = driver.find_element(By.XPATH, '//div[@data-testid="autocomplete-result"]')
    searchResult.click()
    sleep(2)
    datePicker = driver.find_element(By.XPATH, '//button[@data-testid="searchbox-dates-container"]')
    datePicker.click()
    datePicker.click()
    today = str(date.today())
    datexPath = '//span[@data-date="'
    datexPath = datexPath + today + '"]'
    selectedDate = driver.find_element(By.XPATH, datexPath)
    selectedDate.click()
    sleep(2)
    searchButton = driver.find_element(By.XPATH, '//span[text()="Search"]')
    searchButton.click()
    sleep(2)
    saveFavouriteButton = driver.find_element(By.XPATH, '//button[@data-testid="wishlist-button"]')
    saveFavouriteButton.click()
    sleep(2)
    myNextTripButton = driver.find_element(By.XPATH, '//span[text()="My next trip"]')
    myNextTripButton.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    sleep(10)
    unsaveFavouriteButton = driver.find_element(By.XPATH, '//button[@data-testid="wishlist-button"]')
    unsaveFavouriteButton.click()
    sleep(3)
    afterDeletionText = driver.find_element(By.XPATH, '//h3').text
    assert (afterDeletionText == 'Here are 3 simple steps to get you started:'), 'Test failed'




