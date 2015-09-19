Development mode
************************************

Install dependencies:

.. code-block:: bash

    conda create -n myqueue python=3 pip setuptools nose

Install `myqueue` in development mode:

.. code-block:: bash

    pip install -e .

Run the test:

.. code-block:: bash

    nosetests

Uninstall `myqueue`:

.. code-block:: bash

    pip uninstall myqueue

