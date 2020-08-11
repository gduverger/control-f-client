# Control-F Python client

```bash
pipenv install control-f
```

## Usage

```python
>>> import control_f as find
>>> find.food('This morning, I ate an apple with some peanut butter.', token='…').json()
{'matches': ['peanut butter', 'apple'], 'result': 'This morning, I ate an apple with some peanut butter.'}
```

## Dependencies

	requests (2.23.0)

## Development

Packaging

```console
# Generating distribution archives
$ python setup.py sdist bdist_wheel

# Uploading the distribution archives
$ twine upload --skip-existing dist/*
```
