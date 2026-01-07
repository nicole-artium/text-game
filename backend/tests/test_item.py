from models import Player, Item


def test_create_item(db_session):
    player = Player(name="ItemOwner")
    db_session.add(player)
    db_session.commit()

    item = Item(name="Sword", description="A sharp blade", player_id=player.id)
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    assert item.id is not None
    assert item.name == "Sword"
    assert item.description == "A sharp blade"
    assert item.player_id == player.id


def test_item_owner_relationship(db_session):
    player = Player(name="ItemOwner")
    db_session.add(player)
    db_session.commit()

    item = Item(name="Potion", description="Health restore", player_id=player.id)
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    assert item.owner.name == "ItemOwner"
    assert item.owner.id == player.id


def test_multiple_items_same_name(db_session):
    player = Player(name="Collector")
    db_session.add(player)
    db_session.commit()

    item1 = Item(name="Coin", description="Gold coin", player_id=player.id)
    item2 = Item(name="Coin", description="Silver coin", player_id=player.id)

    db_session.add(item1)
    db_session.add(item2)
    db_session.commit()

    items = db_session.query(Item).filter(Item.player_id == player.id).all()
    assert len(items) == 2
    assert all(item.name == "Coin" for item in items)
