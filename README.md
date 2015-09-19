# myqueue

A queue implemented with 2 stacks, for demo purpose

## Development mode

Install dependencies:

    conda create -n myqueue python=3 pip setuptools nose

Install `myqueue` in development mode:

    pip install -e .

Run the test:

    nosetests

Uninstall `myqueue`:

    pip uninstall myqueue

## Writting documentation

Install `sphinx`:

    conda install sphinx sphinx_rtd_theme

Build the doc:

    cd doc
    make html

View the doc:

    firefox _build/html/index.html
