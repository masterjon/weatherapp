# WeatherApp

Python implementation of a weather app using the Openweathermap.org API.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT
## Setup

```docker-compose -f local.yml build```

```docker-compose -f local.yml up -d```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```docker-compose -f local.yml run --rm django coverage run -m pytest```

```docker-compose -f local.yml run --rm django coverage html```

```docker-compose -f local.yml run --rm django open htmlcov/index.html```

#### Running tests with pytest

```docker-compose -f local.yml run --rm django pytest```
