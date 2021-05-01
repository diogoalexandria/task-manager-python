import sys
sys.path.append(".")
from fastapi.testclient import TestClient
from fastapi import status
from task_manager.manager import app, TAREFAS

def test_when_list_tasks_should_return_status_code_200():
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.status_code == status.HTTP_200_OK

def test_when_list_tasks_should_return_json_format():
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.headers["Content-Type"] == "application/json"

def test_when_list_tasks_should_return_list_type():
    client = TestClient(app)
    response = client.get("tasks")    
    assert isinstance(response.json(), list)

def test_when_list_tasks_the_tasks_should_have_id():
    client = TestClient(app)
    response = client.get("/tasks")    
    assert "id" in response.json().pop()    

def test_when_list_tasks_the_tasks_should_have_title():
    client = TestClient(app)
    response = client.get("/tasks")    
    assert "title" in response.json().pop()    

def test_when_list_tasks_the_tasks_should_have_description():
    client = TestClient(app)
    response = client.get("/tasks")    
    assert "description" in response.json().pop()    

def test_when_list_tasks_the_tasks_should_have_status():
    client = TestClient(app)
    response = client.get("/tasks")    
    assert "status" in response.json().pop()
    