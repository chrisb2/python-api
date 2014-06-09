"""
test_data:
==========

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs.graph_objs import *
from ...plotly_exceptions import (PlotlyDictKeyError, PlotlyDictValueError,
                           PlotlyDataTypeError, PlotlyListEntryError)


def setup():
    import warnings
    warnings.filterwarnings('ignore')


def test_trivial():
    assert Data() == list()


def test_weird_instantiation():  # Python allows this...
    assert Data({}) == list({})


def test_default_scatter():
    assert Data([{}]) == list([{'type': 'scatter'}])


def test_dict_instantiation():
    Data([{'type': 'scatter'}])


@raises(PlotlyDictKeyError)
def test_dict_instantiation_key_error():
    print Data([{'not-a-key': 'anything'}])


@raises(PlotlyDictValueError)
def test_dict_instantiation_key_error():
    print Data([{'marker': 'not-a-dict'}])


@raises(PlotlyDataTypeError)
def test_dict_instantiation_type_error():
    Data([{'type': 'invalid_type'}])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_0():
    Data([Data()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_1():
    Data([Figure()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_2():
    Data([Annotations()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_3():
    Data([Layout()])


def test_validate():
    data = Data()
    data.validate()
    data += [{'type': 'scatter'}]
    data.validate()
    data += [{},{},{}]
    data.validate()


@raises(PlotlyDictKeyError)
def test_validate_error():
    data = Data()
    data.append({'not-a-key': 'anything'})
    data.validate()

