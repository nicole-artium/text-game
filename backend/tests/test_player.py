from models import Player, Item


def test_player_with_items(db_session):
    player = Player(name="PlayerWithItems")
    db_session.add(player)
    db_session.commit()
    db_session.refresh(player)

    item1 = Item(name="Sword", description="A sharp blade", player_id=player.id)
    item2 = Item(name="Shield", description="Protective gear", player_id=player.id)

    db_session.add(item1)
    db_session.add(item2)
    db_session.commit()
    db_session.refresh(player)

    assert len(player.inventory) == 2
    assert player.inventory[0].name == "Sword"
    assert player.inventory[1].name == "Shield"
