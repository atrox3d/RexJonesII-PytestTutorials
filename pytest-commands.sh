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
pytest -m 'not smoke' <filename>

EOE