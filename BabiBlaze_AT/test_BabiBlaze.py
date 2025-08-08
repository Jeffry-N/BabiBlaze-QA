def test_user_registration_valid():
    response = register_user(email="valid@example.com", password="StrongPass123!")
    assert response["status"] == "success"
    assert "confirmation_email_sent" in response and response["confirmation_email_sent"] == True

def test_login_incorrect_password():
    response = login_user(email="valid@example.com", password="wrongpassword")
    assert response["status"] == "fail"
    assert response["error"] == "Incorrect password"

def test_logout_functionality():
    response = logout_user(session_id="123abc")
    assert response["status"] == "success"
    assert response["redirect_url"] == "/login"

# mock functions definitions to simulate tests
def register_user(email, password):
    if email == "valid@example.com" and password == "StrongPass123!":
        return {"status": "success", "confirmation_email_sent": True}
    else:
        return {"status": "fail"}

def login_user(email, password):
    if email == "valid@example.com" and password == "correctpassword":
        return {"status": "success"}
    else:
        return {"status": "fail", "error": "Incorrect password"}

def logout_user(session_id):
    if session_id == "123abc":
        return {"status": "success", "redirect_url": "/login"}
    else:
        return {"status": "fail"}