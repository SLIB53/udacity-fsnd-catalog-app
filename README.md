# Catalog App

Web application for storing categories and items.

## Contribution

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
