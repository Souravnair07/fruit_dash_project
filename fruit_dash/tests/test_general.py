from fruit_dash.mechanics import make_in_range

def test_speed_cap():
    # speed should never go above 99
    assert make_in_range(150, 5, 99) == 99

def test_speed_floor():
    # speed should never go below 5
    assert make_in_range(1, 5, 99) == 5