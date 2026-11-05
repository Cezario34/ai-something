from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_serves_editor():
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    page = response.text
    assert "Автописатель" in page
    assert 'id="fragment"' in page
    assert 'id="char-count"' in page
    assert "Проверить текст" in page
    assert 'src="/static/app.js"' in page


def test_static_script_counts_on_the_client():
    response = client.get("/static/app.js")

    assert response.status_code == 200
    script = response.text
    assert "fragment.value.length" in script
    assert "/api/check" in script


def test_check_is_a_stub_and_ignores_text():
    response = client.post("/api/check", json={"text": "секретный фрагмент"})

    assert response.status_code == 200
    body = response.json()
    assert body == {
        "status": "not_implemented",
        "message": "Проверка текста пока не реализована.",
    }
    assert "секретный" not in response.text
