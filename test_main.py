def test_summarize():
    response = client.post("/summarize", json={
        "text": "This is a long email about project updates and deadlines."
    })

    assert response.status_code == 200
    assert "summary" in response.json()