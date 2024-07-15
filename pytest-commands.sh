#!/bin/bash

cat <<EOE 
# run tests only for smoke marker
pytest -m 'smoke'

# run tests for smoke and integration
pytest -m 'smoke and integration'

# run tests for smoke and not integration
pytest -m 'smoke and not integration'

# run tests for either smoke or integration
pytest -m 'smoke or integration'

# run tests not for smoke
pytest -m 'not smoke'

# run tests not for smoke, only for one file
pytest -m 'not smoke' [filename]

# list fixtures for all or selected modules::functions
pytest --fixtures
pytest --fixtures DemoPytest
pytest --fixtures DemoPytest/test_fixtures_1.py
pytest --fixtures DemoPytest/test_fixtures_1.py::test1_order_history_title

# collects test and show parameters
pytest --collect-only [filename]

# stops tests after {maxfail} failures
pytest --maxfail=1 [filename]
EOE