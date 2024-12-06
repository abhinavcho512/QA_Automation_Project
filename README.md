# QA_Automation_Project

This repository contains the QA Automation Project for automating the process of adding and deleting packages in the KloudShip application. The project uses Selenium with Python for automation testing. Additionally, Postman is used for API testing, and SQL queries are used for database verification.

The project is structured into three main sections:
	1.	Automation Testing with Selenium: Automating the addition and deletion of packages in the application.
	2.	API Testing with Postman: Creating and running tests to verify API responses.
	3.	SQL Queries: Running queries for database validation.

Table of Contents

	•	Technologies Used
	•	Setup Instructions
	•	Running the Automation Tests
	•	Running Postman Tests
	•	Running SQL Queries
	•	Project Structure
	•	Contributing
	•	License

Technologies Used

	•	Selenium (Python): For automating the browser to add and delete packages.
	•	Postman: For testing REST API endpoints.
	•	MySQL / PostgreSQL: For validating database actions.
	•	Python: The main programming language for the automation scripts.

Setup Instructions

1. Install Python and Selenium

Ensure Python is installed on your system. If not, download it from python.org.

Once Python is installed, install Selenium using pip:

pip install selenium

2. Download ChromeDriver

	•	Download ChromeDriver to interact with Google Chrome in the automation tests. Visit ChromeDriver Download to download the version compatible with your installed Chrome browser.
	•	Place chromedriver.exe in the same directory as your Python script.

3. Set Up Postman

	•	Download and install Postman from Postman’s website.
	•	Import the Postman collection provided in this repository to run the API tests.

4. Database Setup (Optional)

	•	Make sure you have access to a MySQL or PostgreSQL database.
	•	Use the SQL Queries from this repository to interact with the database for validation.

Running the Automation Tests

1. Run Selenium Test Script

To run the Selenium automation tests, follow these steps:
	1.	Ensure Python and Selenium are installed.
	2.	Navigate to the folder containing automation_script.py and run the script:

python automation_script.py

The script will:
	•	Log in to the KloudShip application.
	•	Add a new package.
	•	Delete the package.
	•	Log out.

2. Headless Mode for Selenium

You can run the tests in headless mode (without opening a browser window) by configuring ChromeDriver options in automation_script.py:

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

3. Error Handling

Check the terminal output for any errors. The logs will indicate if something goes wrong during the test execution (e.g., login failure, element not found).

Running Postman Tests

1. Import the Postman Collection

	•	Import the Impledge_QA_Exercise.postman_collection.json collection into Postman.
	•	Rename the collection to Impledge_QA_YourFullName.

2. Run API Tests

	•	Open Postman and select the imported collection.
	•	Click on the Send button to run the test requests.
	•	The results will appear in the Test Results section.

3. Test Cases Included

	•	Fix Failing Test Cases: Verifies the response status and content type.
	•	Get Shipment Details: Fetches shipment details by shipment ID.
	•	Verify Rates: Checks the retail rate and ensures it is greater than the list rate.

Running SQL Queries

1. Execute SQL Queries

The provided SQL queries are for validating actions in the database. These include:
	•	Updating records in the Admissions table.
	•	Running SELECT queries to retrieve data about Doctors and Patients.

To run the SQL queries:
	1.	Connect to your MySQL or PostgreSQL database.
	2.	Execute the UPDATE queries first to modify the database.
	3.	Then, execute the SELECT queries to fetch and validate data.

Example to run in MySQL or PostgreSQL:

UPDATE Admissions
SET attending_doctor_id = 29
WHERE attending_doctor_id = 3;

SELECT * FROM Doctors;

Project Structure

QA_Automation_Project/
│
├── automation_script.py       # Python Selenium automation script
├── postman_tests/             # Postman collection for API tests
│   ├── Impledge_QA_YourFullName.postman_collection.json
├── sql_queries.sql           # SQL queries for database validation
├── README.md                 # Project documentation

Contributing

If you want to contribute to this project, follow these steps:
	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature-name).
	3.	Make your changes and commit them (git commit -am 'Add new feature').
	4.	Push to your forked repository (git push origin feature-name).
	5.	Create a pull request to the main repository.

License

This project is licensed under the MIT License - see the LICENSE file for details.
