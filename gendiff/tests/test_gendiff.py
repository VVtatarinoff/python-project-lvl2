# import json

import argparse

import gendiff.gendiff as g


def test_prepare_argparse_object():
    parser = g.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
