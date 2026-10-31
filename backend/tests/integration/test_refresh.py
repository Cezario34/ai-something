import pytest


@pytest.mark.asyncio
async def test_refresh_token(client):
    await client.post("/users/", json={
        "username": "refreshuser",
        "email": "refresh@example.com",
        "password": "password123",
        "role": "guest",
    })

    login = await client.post("/auth/login", data={
        "username": "refreshuser",
        "password": "password123",
    })
    assert login.status_code == 200
    refresh_token = login.json()["refresh_token"]

    # Обновляем токен
    response = await client.post("/auth/refresh", json={
        "refresh_token": refresh_token
    })
    assert response.status_code == 200
    new_data = response.json()
    assert "access_token" in new_data
    assert "refresh_token" in new_data