from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("123 Main St, Springfield, IL 62704") == "Springfield"
    assert extract_city("456 Elm St, Metropolis, NY 10001") == "Metropolis"
    assert extract_city("789 Oak St, Gotham, NJ 07001") == "Gotham"

def test_extract_state():
    assert extract_state("123 Main St, Springfield, IL 62704") == "IL"
    assert extract_state("456 Elm St, Metropolis, NY 10001") == "NY"
    assert extract_state("789 Oak St, Gotham, NJ 07001") == "NJ"

def test_extract_zipcode():
    assert extract_zipcode("123 Main St, Springfield, IL 62704") == "62704"
    assert extract_zipcode("456 Elm St, Metropolis, NY 10001") == "10001"
    assert extract_zipcode("789 Oak St, Gotham, NJ 07001") == "07001"

pytest.main( ["-v", "--tb=line",  "-rN",  __file__] )       