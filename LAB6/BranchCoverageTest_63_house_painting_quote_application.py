import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_unknown_paint():
    with pytest.raises(ValueError, match="unknown paint"):
        painting_quote("plastic", 500, 2, False)


def test_invalid_area():
    with pytest.raises(ValueError, match="invalid job"):
        painting_quote("emulsion", 0, 2, False)


def test_invalid_coats():
    with pytest.raises(ValueError, match="invalid job"):
        painting_quote("emulsion", 500, 0, False)


def test_exterior_distemper():
    with pytest.raises(ValueError, match="distemper is for interiors only"):
        painting_quote("distemper", 500, 2, True)


def test_interior_distemper():
    assert painting_quote("distemper", 500, 2, False) == 12000


def test_large_area_discount():
    assert painting_quote("emulsion", 2500, 2, False) == 90000


def test_large_area_boundary():
    assert painting_quote("emulsion", 2000, 2, False) == 80000


def test_minimum_quote():
    assert painting_quote("emulsion", 100, 1, False) == 5000


def test_below_minimum_quote():
    assert painting_quote("distemper", 100, 1, False) == 5000


def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_litres():
    assert paint_litres(200, 1, "rough") == 4


def test_unknown_surface():
    with pytest.raises(ValueError, match="unknown surface"):
        paint_litres(200, 1, "uneven")


def test_smooth_exact_coverage():
    assert paint_litres(100, 1, "smooth") == 1


def test_invalid_painters():
    with pytest.raises(ValueError, match="need at least one painter"):
        crew_days(1000, 0, False)


def test_crew_days_with_remainder():
    assert crew_days(1000, 2, False) == 2


def test_crew_days_exact_division():
    assert crew_days(800, 2, False) == 1


def test_wallpaper_removal():
    assert crew_days(800, 2, True) == 3


def test_wallpaper_removal_with_remainder():
    assert crew_days(1000, 2, True) == 4

