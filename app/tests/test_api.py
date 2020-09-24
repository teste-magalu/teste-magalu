import json

def test_post_message(client):
    """Test post message"""
    # Act
    data = {
      "recipient": "test@gmail.com",
      "message": "Mensagem teste.",
      "date_time": "2020-10-20 22:00:00"
    }
    response = client.post('/api/v1/message', json=data, headers={"Content-Type": "application/json"})
    data = response.json
    # Assert
    assert response.status_code == 201
    assert data["recipient"] == "test@gmail.com"
    assert data["message"] == "Mensagem teste."
    assert data["date_time"] == "2020-10-20 22:00:00"
    assert data["id"] == 1
    assert data["status"] == False
    
def test_get_messages(client):
    """Test get messages"""
    # Act
    response = client.get('/api/v1/message')
    data = response.json
    # Assert
    assert response.status_code == 200
    assert len(data) == 1
    print(type(data))
    print(data)
    assert "test@gmail.com" in [item["recipient"] for item in data['messages']]
    assert "Mensagem teste." in [item["message"] for item in data['messages']]
    assert "2020-10-20 22:00" in [item["date_time"] for item in data['messages']]
    assert 1 in [item["id"] for item in data['messages']]
    assert False in [item["status"] for item in data['messages']]

def test_get_message(client):
    """Test get message"""
    # Act
    response = client.get('/api/v1/message/1')
    data = response.json
    # Assert
    assert response.status_code == 200
    assert data["recipient"] == "test@gmail.com"
    assert data["message"] == "Mensagem teste."
    assert data["date_time"] == "2020-10-20 22:00"
    assert data["id"] == 1
    assert data["status"] == False

def test_put_message(client):
    """Test put message"""
    # Act
    data = {
      "recipient": "test@gmail.com",
      "message": "Mensagem teste.",
      "date_time": "2020-10-20 22:00:00",
      "status": True
    }
    response = client.put('/api/v1/message/1', json=data, headers={"Content-Type": "application/json"})
    data = response.json
    # Assert
    assert response.status_code == 200
    assert data["recipient"] == "test@gmail.com"
    assert data["message"] == "Mensagem teste."
    assert data["date_time"] == "2020-10-20 22:00:00"
    assert data["id"] == 1
    assert data["status"] == True

def test_delete_message(client):
    """Test delete message"""
    # Act
    response = client.delete('/api/v1/message/1')
    # Assert
    assert response.status_code == 200
