"""
test_error_bars:
================

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs.graph_objs import *
from ...plotly_exceptions import (PlotlyDictKeyError, PlotlyDictValueError,
                           PlotlyDataTypeError, PlotlyListEntryError)


def test_instantiate_error_x():
    ErrorX()
    ErrorX(array=[1, 2, 3],
           arrayminus=[2, 1, 2],
           color='red',
           copy_ystyle=False,
           opacity=.4,
           symmetric=False,
           thickness=2,
           traceref=0,  # TODO, what's this do again?
           type='percent',
           value=1,
           valueminus=4,
           visible=True,
           width=5)


def test_instantiate_error_y():
    ErrorY()
    ErrorY(array=[1, 2, 3],
           arrayminus=[2, 1, 2],
           color='red',
           opacity=.4,
           symmetric=False,
           thickness=2,
           traceref=0,  # TODO, what's this do again?
           type='percent',
           value=1,
           valueminus=4,
           visible=True,
           width=5)


@raises(PlotlyDictKeyError)
def test_key_error():
    ErrorX(value=0.1, typ='percent', color='red')