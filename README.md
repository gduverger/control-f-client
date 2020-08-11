# Control-F Python client

```bash
pipenv install ctrlf-python
```

## Usage

```python
>>> import ctrlf as find
>>> find.food('This morning, I ate an apple with some peanut butter.', token='…').json()
{'matches': ['peanut butter', 'apple'], 'result': 'This morning, I ate an apple with some peanut butter.'}
```

## Dependencies

	requests (2.23.0)
