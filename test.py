import yaml_complexity_index as yci


def test_measure_max_nestedness_works_on_dicts():
    i = {
        "foo": "bar",
        "biz": "baz",
    }
    assert yci.measure_max_nestedness(i) == 2


def test_measure_max_nestedness_works_on_nested_dicts():
    i = {
        "foo": {
            "bar": "baz",
        }
    }
    assert yci.measure_max_nestedness(i) == 3
