# Advent2023
Advent of Code 2023 solutions.

# Compatibility
This project uses Python 3.10+

# Usage
Run a script by executing it and passing the appropriate input file

```
python/day01.py input/day01.txt
```

# Development
- Setup a virtual environment: `python3 -m venv .venv`
- Activate the venv: `. .venv/bin/activate`
- Install the requirements from requirements.txt: `pip install -r requirements.txt`
- Symbolic link githooks/pre-commit to .git/pre-commit: `a=$(pwd); cd .git/hooks/; ln -s ../../.githooks/pre-commit; cd $a`