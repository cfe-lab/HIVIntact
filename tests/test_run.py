
import os
import sys
import filecmp
from unittest.mock import patch
import bin.proviral as run

def test_basic_run(tmp_path, request):
    working_dir = os.path.join(tmp_path, "wd")
    pwd = request.fspath.dirname
    input = os.path.join(pwd, "data-small.fasta")

    testargs = ["proviral", "intact", "--subtype", "B", "--working-folder", working_dir, input]

    with patch.object(sys, 'argv', testargs):
        try: run.cli()
        except SystemExit as e: assert e.code == 0

    expected_dir = os.path.join(pwd, "expected-results-small")
    assert os.path.exists(os.path.join(working_dir, "errors.json"))
