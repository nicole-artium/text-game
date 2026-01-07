def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Text RPG API"}


def test_create_player(client):
    response = client.post(
        "/api/game/player",
        json={"name": "TestHero"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestHero"
    assert "id" in data


def test_create_duplicate_player(client):
    client.post("/api/game/player", json={"name": "Hero"})
    response = client.post("/api/game/player", json={"name": "Hero"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Player already exists"


def test_get_player(client):
    create_response = client.post(
        "/api/game/player",
        json={"name": "GetTestHero"}
    )
    player_id = create_response.json()["id"]

    response = client.get(f"/api/game/player/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == player_id
    assert data["name"] == "GetTestHero"


def test_get_nonexistent_player(client):
    response = client.get("/api/game/player/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Player not found"
