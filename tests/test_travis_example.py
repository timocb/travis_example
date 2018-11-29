from travis_example import __version__, example

def test_version():
    assert __version__ == '0.1.0'


def test_x():
    assert example.x(1, 1) == 2
