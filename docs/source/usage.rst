Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumachex.get_random_ingredients()`` function:

.. autofunction:: lumachex.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumachex.get_random_ingredients`
will raise an exception.

.. autoexception:: lumachex.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

.. _anotherlabel:

Another Section
---------------

Another section with stuff and some text to _`text to link to` just previous.
And check out this link to `text to link to`_ above also.
And check another way this link to :ref:`text for link to text in this file <text to link to>` above also.

And use the FOO module for other things ...

.. autofunctin:: foo.some_foo_function
