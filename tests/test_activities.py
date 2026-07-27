def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_name = "Chess Club"
    expected_participant = "michael@mergington.edu"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    activities = response.json()
    assert expected_activity_name in activities
    assert activities[expected_activity_name]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert expected_participant in activities[expected_activity_name]["participants"]


def test_get_activities_includes_participant_lists(client):
    # Arrange
    expected_activity_name = "Drama Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    activities = response.json()
    participants = activities[expected_activity_name]["participants"]
    assert participants == ["isabella@mergington.edu", "lucas@mergington.edu"]