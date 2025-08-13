import pytest

def register_user(email, password, existing=False):
    if not existing and email == "valid@example.com" and password == "StrongPass123!":
        return {"status": "success", "confirmation_email_sent": True}
    elif existing:
        return {"status": "fail", "error": "Email already in use"}
    else:
        return {"status": "fail"}

def login_user(email, password):
    if email == "valid@example.com" and password == "correctpassword":
        return {"status": "fail", "error": "Server timeout"}
    elif email == "valid@example.com" and password == "wrongpassword":
        return {"status": "fail", "error": "Incorrect password"}
    else:
        return {"status": "fail", "error": "Invalid credentials"}

def book_appointment(date):
    if date == "future-date":
        return {"status": "fail", "error": "No confirmation email received"}
    elif date == "past-date":
        return {"status": "fail", "error": "Invalid date selected"}
    else:
        return {"status": "success", "confirmation": True}

def search_services(query):
    if query == "valid-service":
        return {"status": "fail", "results": ["wrong-service"]}
    else:
        return {"status": "success", "results": ["service1", "service2"]}

def process_payment(card_number, valid=True):
    if valid:
        return {"status": "success", "confirmation_page": True}
    else:
        return {"status": "fail", "error": "Invalid card details"}

def logout_user(session_id):
    if session_id == "123abc":
        return {"status": "success", "redirect_url": "/login"}
    else:
        return {"status": "fail"}

# Mock Tests

def test_babi_01_registration_valid():
    resp = register_user("valid@example.com", "StrongPass123!")
    assert resp["status"] == "success"
    assert resp.get("confirmation_email_sent") is True

def test_babi_02_registration_existing_email():
    resp = register_user("valid@example.com", "StrongPass123!", existing=True)
    assert resp["status"] == "fail"
    assert resp.get("error") == "Email already in use"

def test_babi_03_login_valid_credentials():
    resp = login_user("valid@example.com", "correctpassword")
    assert resp["status"] == "success"  # This will fail (server timeout)

def test_babi_04_login_incorrect_password():
    resp = login_user("valid@example.com", "wrongpassword")
    assert resp["status"] == "fail"
    assert resp.get("error") == "Incorrect password"

def test_babi_05_book_appointment_success():
    resp = book_appointment("future-date")
    assert resp["status"] == "success"  # This will fail (no confirmation email)

def test_babi_06_booking_with_past_date():
    resp = book_appointment("past-date")
    assert resp["status"] == "fail"
    assert resp.get("error") == "Invalid date selected"

def test_babi_07_service_search_functionality():
    resp = search_services("valid-service")
    assert resp["status"] == "success"  # This will fail (incorrect results)
    assert all("valid-service" in s for s in resp["results"])

def test_babi_08_payment_processing_successful():
    resp = process_payment("4111111111111111", valid=True)
    assert resp["status"] == "success"
    assert resp.get("confirmation_page") is True

def test_babi_09_payment_with_invalid_card():
    resp = process_payment("0000000000000000", valid=False)
    assert resp["status"] == "fail"
    assert resp.get("error") == "Invalid card details"

def test_babi_10_logout_functionality():
    resp = logout_user("123abc")
    assert resp["status"] == "success"
    assert resp.get("redirect_url") == "/login"
