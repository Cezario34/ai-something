import pytest


@pytest.mark.asyncio
async def test_clear_conversation_history(client):
    # Создаём админа и персонажа
    await client.post("/users/", json={
        "username": "adminclear",
        "email": "adminclear@example.com",
        "password": "password123",
        "role": "admin",
    })
    admin_login = await client.post("/auth/login", data={
        "username": "adminclear",
        "password": "password123",
    })
    admin_token = admin_login.json()["access_token"]

    char = await client.post(
        "/characters/",
        json={"name": "ClearBot", "personality": "Test"},
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    character_id = char.json()["id"]

    # Обычный пользователь
    await client.post("/users/", json={
        "username": "clearuser",
        "email": "clear@example.com",
        "password": "password123",
        "role": "guest",
    })
    login = await client.post("/auth/login", data={
        "username": "clearuser",
        "password": "password123",
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Отправляем сообщение
    await client.post(
        "/chat/",
        json={"message": "Hello", "character_id": character_id},
        headers=headers,
    )

    # Получаем диалог
    convs = await client.get("/conversations/", headers=headers)
    conversation_id = convs.json()[0]["id"]

    # Проверяем, что сообщения есть
    messages = await client.get(f"/conversations/{conversation_id}/messages", headers=headers)
    assert len(messages.json()) > 0

    # Очищаем историю
    response = await client.delete(
        f"/conversations/{conversation_id}/messages",
        headers=headers,
    )
    assert response.status_code == 200

    # Проверяем, что сообщений нет
    messages = await client.get(f"/conversations/{conversation_id}/messages", headers=headers)
    assert len(messages.json()) == 0