# Catalog App

Web application for storing categories and items.

## Run

To run the application, `Python 3` and the requirements listed in [`requirements.txt`](/requirements.txt) must be installed.

```sh
pip install -r requirements.txt
```

For additional information on installation, see the [Development Environment](#development-environment) section.

To start the server, first set up the database by running:

```sh
python -c "from start_database import setup; setup()"
```

Then run `start.py`.

```sh
python start.py
```

## Development Environment

### Dependencies

- Python 3
  - pip
  - bottle


#### Ubuntu (16.04+) / Windows Subsystem for Linux

Firstly, install system dependencies:

```sh
sudo apt install python3 python3-pip
```

Then, set up the python virtual environment (venv):

```sh
python3 -m venv . && source bin/activate
```

Lastly, install additional dependencies:

```sh
pip install -r requirements.txt
```

#### Windows 10

_Note: The following instructions are expected to run on PowerShell._

Firstly, install Python 3 with pip from [python.org](https://www.python.org/).

Then, set up the python virtual environment (venv):

```PowerShell
python -m venv .
.\Scripts\Activate.ps1
```

Lastly, install additional dependencies:

```PowerShell
pip install -r requirements.txt
```

### IDE (Recommendation)

This project is developed with Visual Studio Code, with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) enabled. Additionally, the Python package `pep8` is used for linting.

`.vscode/settings.json`:

```json
{
    "python.pythonPath": <insert full path to venv python binary>,
    "python.linting.pylintEnabled": false, // disable default linter
    "python.linting.pep8Enabled": true,
    "files.encoding": "utf8",
    "files.eol": "\n",
    "files.trimTrailingWhitespace": true,
    "files.trimFinalNewlines": true,
    "files.insertFinalNewline": true,
}
```
