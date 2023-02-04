# IWU Project Call Search Engine
> Instruction for future developers

## Prerequisites
- Python 3.9+
- Pip 21+
- Setuptools 56+

Use below command(s) to determine if your environment meets the prerequisites
```bash
python -V                       # Python version
python -m pip -V                # Pip version
python -m pip show setuptools   # Setuptools version
```

## Environment
From terminal navigate to project-root, create and activate the virtual environment
```bash
iwu-callse> python -m venv .venv
iwu-callse> .venv\Scripts\activate  # Windows
# Or,
iwu-callse$ source .venv/bin/activate # UNIX-like
```

## Develop
Install the current project in development mode along with all dependencies.
```bash
(.venv) iwu-callse> pip install -e .[test,build]
```
Running the project
```bash
(.venv) iwu-callse> iwu-callse
```

## Distribute
TBA