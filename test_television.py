import pytest
from python.television import Television

@pytest.fixture
def tv():
    return Television()

def test_initial_state(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power(tv):
    tv.power()
    assert str(tv).startswith("Power = True")

def test_channel_up(tv):
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_wrap(tv):
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down(tv):
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)

def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

def test_volume_down(tv):
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)

def test_volume_limits(tv):
    tv.power()
    tv.volume_down()
    assert "Volume = 0" in str(tv)

def test_mute(tv):
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 0" in str(tv)
    tv.mute()
    assert "Volume = 1" in str(tv)
