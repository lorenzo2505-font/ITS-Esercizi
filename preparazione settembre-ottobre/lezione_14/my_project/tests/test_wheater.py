from my_project.wheater import check_weather

# passed
def test_check_weather():

    assert check_weather(21.00) == "hot", "temperatures greater than 20 degree must be considered as hot"