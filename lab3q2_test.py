import lab3q2
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'-20 -18 -16 -14 -12 -10 -8 -6 -4 -2') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab3q2.py") as tf:
    head = [next(tf) for _ in range(10)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'Starting') != -1
    assert captured_stdout.strip().find(f'Done') != -1