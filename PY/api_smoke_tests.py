import requests
import base64

base_url = "https://restful-booker.herokuapp.com"
created_booking_id = None

def test_health_check():
    url = f"{base_url}/ping"
    response = requests.get(url)

    if response.status_code == 201 and response.text == "Created":
        print("Health Check test: PASSED")
    else:
        print("Health Check test: FAILED")

def test_create_booking():
    global created_booking_id

    url = f"{base_url}/booking"
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-06-01",
            "checkout": "2023-06-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=data)

    if response.status_code == 200 and "bookingid" in response.json():
        created_booking_id = response.json()["bookingid"]
        print(f"Create Booking test: PASSED. Created Booking ID: {created_booking_id}")
    else:
        print("Create Booking test: FAILED")

def test_get_booking():
    url = f"{base_url}/booking/{created_booking_id}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Get Booking test: PASSED")
    else:
        print("Get Booking test: FAILED")

def test_update_booking():
    global auth_token

    # Get an authentication token
    auth_url = f"{base_url}/auth"
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = requests.post(auth_url, json=auth_data)
    
    if auth_response.status_code == 200 and "token" in auth_response.json():
        auth_token = auth_response.json()["token"]
        headers = {"Authorization": f"Basic YWRtaW46cGFzc3dvcmQxMjM="}
        url = f"{base_url}/booking/{created_booking_id}"
        data = {
            "firstname": "Jane",
            "lastname": "Smith",
            "totalprice": 150,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2023-07-01",
                "checkout": "2023-07-10"
            },
            "additionalneeds": "Lunch"
        }
        response = requests.put(url, json=data, headers=headers)

        if response.status_code == 200:
            print("Update Booking test: PASSED")
        else:
            print("Update Booking test: FAILED")
            print(f"Error message: {response.text}")
    else:
        print("Update Booking test: FAILED. Failed to obtain authentication token.")


def test_delete_booking():
    global auth_token

    # Get a Basic Authentication token
    username = "admin"
    password = "password123"
    auth_token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    # print(auth_token)
    headers = {"Authorization": f"Basic {auth_token}"}

    url = f"{base_url}/booking/{created_booking_id}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 201 and response.text == "Created":
        print("Delete Booking test: PASSED")
    else:
        print("Delete Booking test: FAILED")
        print(f"Error message: {response.text}")

if __name__ == "__main__":
    test_health_check()
    test_create_booking()
    if created_booking_id:
        test_get_booking()
        test_update_booking()
        test_delete_booking()
    else:
        print("Skipping dependent tests due to failure in Create Booking test")
