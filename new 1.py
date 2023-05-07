from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Desired capabilities of the mobile device and application under test
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "RMX1825",
    "appPackage": "com.example.android.testapp",
    "appActivity": "MainActivity"
}

# URL of the Appium server
appium_url = "http://localhost:4723/wd/hub"

# Initialize the driver with the desired capabilities and URL
driver = webdriver.Remote(appium_url, desired_caps)

# Wait for the login screen to appear and enter the login credentials
wait = WebDriverWait(driver, 10)
#username and Password input
username = input('Enter UserName ')
Password = input("Enter Password")
username_input = wait.until(EC.visibility_of_element_located((By.ID, "username_input")))
password_input = wait.until(EC.visibility_of_element_located((By.ID, "password_input")))
username_input.send_keys(username)
password_input.send_keys(Password)
driver.find_element_by_id("login_button").click()

# Navigate to the main screen and verify the presence of a button
main_screen_button = wait.until(EC.visibility_of_element_located((By.ID, "main_screen_button")))
assert main_screen_button.is_displayed()

# Test Logging Workouts
def test_logging_workouts():
    # Log a new workout
    driver.find_element_by_id('Quickstart').click()
    driver.find_element_by_id('START').click()
   # Locate the pause button element
	pause_button = driver.find_element_by_id("pause_button")
	action = TouchAction(driver)
	action.tap(pause_button).perform()
	# Wait for the popup
	popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "popup_id")))
	# Check if the message is "Are you sure you want to discard run?"
	if popup.text == "Are you sure you want to discard run?":
    # Click on OK button
    ok_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ok_button_id")))
    ok_button.click()

    # Verify the workout log displays accurate data
    workout_logs = driver.find_elements_by_id('Activity')
    menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_button_id")))

	# Tap on the menu button to display the dropdown options
	action = TouchAction(driver)
	action.tap(menu_button).perform()

	# Wait for the dropdown options to appear and select the desired option
	Recent_Activity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Recent Activity")))
	Recent_Activity.click()
	# Adding new workout in Acitivity menu
	add_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "com.NRC.app:id/add_button")))
	add_button.click()
	# Click on the back button
	back_btn = driver.find_element(By.ID, "android:id/button1") # assuming ID of back button is 'android:id/button1'
	back_btn.click()


    # Edit and update a previous workout log
    workout_logs[0].click()
    driver.find_element_by_id('edit_button').click()
    driver.find_element_by_id('Recent_Activity')
	edit_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "com.NRC.app:id/add_button")))
	edit_button.click()
    driver.find_element_by_id("com.NRC.app:id/add_button").send_keys('15 KM Run')
    driver.find_element_by_id('save_button').click()
	back_btn = driver.find_element(By.ID, "android:id/button1") # assuming ID of back button is 'android:id/button1'
	back_btn.click() 


    # Verify the updated workout log displays accurate data
    assert workout_logs[0].find_element_by_id('com.NRC.app:id/add_button').text == '15 KM Run'

    # Delete a workout log
    driver.find_element_by_id('delete_button').click()
    workout_logs = driver.find_elements_by_id('workout_log')
    assert len(workout_logs) == 0
	# Click on the back button
	back_btn = driver.find_element(By.ID, "android:id/button1") # assuming ID of back button is 'android:id/button1'
	back_btn.click()

# Test Tracking Progress
def test_tracking_progress():
    # Set a fitness goal
	# Tap on the menu button to display the dropdown options
	action = TouchAction(driver)
	action.tap(menu_button).perform()
    driver.find_element_by_id('Create a Challenge').click()
	# Name your Challenge
    edit_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "com.NRC.app:id/add_button")))
	edit_button.click()
    driver.find_element_by_id('"com.NRC.app:id/add_button"').send Keys ("5 KM run in 30 mins" )
	Date_driver = TouchAction(driver)
	action.tap(Date).perform()
	# clicking on dates in calendar
	# find the calendar button element and click it
	calendar_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='calendar']")))
	calendar_button.click()

	# wait for the calendar to load
	time.sleep(3)

	# find the date picker elements
	picker_columns = driver.find_elements_by_xpath("//XCUIElementTypePickerWheel")

	# select the first date
	picker_columns[0].send_keys("May")
	picker_columns[1].send_keys("10")
	picker_columns[2].send_keys("2023")

	# select the second date
	picker_columns[3].send_keys("May")
	picker_columns[4].send_keys("15")
	picker_columns[5].send_keys("2023")
	# click the Done button to confirm the selection
	done_button = driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']")
	done_button.click()

	# wait for the selection to be confirmed
	time.sleep(2)

    # Verify the goal is displayed
    # Tap on the menu button to display the dropdown options
	action = TouchAction(driver)
	action.tap(menu_button).perform()
	# Find and click on Challenges
	challenges_button = driver.find_element_by_id("challenges_button_id")
	challenges_button.click()
	scrollable_element = driver.find_element_by_id("scrollable_element_id")

# Perform a swipe down action on the element
	action = TouchAction(driver)
	action.press(scrollable_element, x=0, y=0).move_to(scrollable_element, x=0, y=-200).release().perform()
# Track progress towards the goal
# Find the class element
class_element = driver.find_element_by_class_name("class_name")

# Check if the class element contains a following element
   try:
    element = driver.find_element_by_id('5 KM run in 30 mins')
except NoSuchElementException:
    raise NoSuchElementException('Element not found')

    driver.find_element_by_id('5 KM run in 30 mins').click()
    driver.find_element_by_id('progress_input').send_keys('28 minutes')
    driver.find_element_by_id('save_button').click()
	# Wait for the colon button to be visible
	wait = WebDriverWait(driver, 10)
	colon_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text=':']")))
	# Tap on the colon button using TouchAction
	action = TouchAction(driver)
	action.tap(colon_button).perform()
	# Wait for Edit Challenge option to be visible and click on it
	edit_challenge_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "edit_challenge_option_id")))
	edit_challenge_option.click()
	# Update distance to 4 km
	distance_input = challenge_editor.find_element_by_id('create_challenge_distance')
	distance_input.clear()
	distance_input.send_keys('4')

# Save changes
	save_button = driver.find_element_by_id('create_challenge_save_button')
	save_button.click()

    # Verify the progress is displayed
    # Check if the class element contains a following element
   try:
    element = driver.find_element_by_id('4 KM run in 30 mins')
except NoSuchElementException:
    raise NoSuchElementException('Element not found')

# Test Connecting with Friends
def test_connecting_with_friends():
    # Connect with a friend
    driver.find_element_by_id('connect_button').click()
    driver.find_element_by_id('friend_input').send_keys('John Doe')
    driver.find_element_by_id('send_request_button').click()

    # Verify the friend request is sent
    friend_requests = driver.find_elements_by_id('friend_request')
    assert friend_requests[0].find_element_by_id('friend_name').text == 'John Doe'

    # Accept a friend request
    friend_requests[0].find_element_by_id('accept_button').click()

    