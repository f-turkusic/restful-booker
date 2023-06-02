# Documentation for the API restful-booker testing -  how to run the automated tests.

**To run automated tests for both POSTMAN and Python on your machine on local machine, you can follow these steps:**
POSTMAN:
Install the Postman application on your machine if you haven't already.
Open Postman and import the collection file (restful-booker.herokuapp.postman_collection.json) and environment file (restful-booker.herokuapp_env.postman_environment.json) into Postman.
Ensure that the necessary test scripts and assertions are defined within the collection's requests or in the associated test scripts.
To run the tests manually, select the collection or individual requests, and click on the "Send" button to send the requests and evaluate the test results.
Python:
Make sure you have Python installed on your machine.
Open a terminal or command prompt and navigate to the directory containing the api_smoke_tests.py file.
Run the script by executing the command "python api_smoke_tests.py". This will execute the defined tests in the script and display the test results in the console.

**To run automated tests for both POSTMAN and Python using GitHub Actions - Workflows, you can follow these steps:**
To manually trigger the workflow, go to the "Actions" tab in your repository on GitHub, select workflow, and click on the "Run workflow" button.

Also, the workflows will be started automatically on every push to the main branch.
