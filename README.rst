GDELT in Python with ``gdeltPyR`` 
======================

``gdeltPyR`` is a Python-based framework to retrieve `[Global Database of Events, Language, and Tone (GDELT) 1.0 and 2.0 data <http://gdeltproject.org/data.html>`_ for analysis in Python Pandas or R dataframes (R dataframe output feature coming soon). A user can enter a single date, date range (two strings), or several individual dates and return a `tidy data set ready for scientific or data-driven exploration <http://vita.had.co.nz/papers/tidy-data.pdf>`_.


`gdeltPyR` retrieves `[Global Database of Events, Language, and Tone (GDELT) 1.0 and 2.0 data <http://gdeltproject.org/data.html>`_  via `[parallel HTTP GET requests <http://docs.python-requests.org/en/v0.10.6/user/advanced/#asynchronous-requests>`_ and is an alternative to `accessing GDELT data via Google BigQuery  <http://gdeltproject.org/data.html#googlebigquery>`_. Therefore, the more CPUs or cores you have, the less time it takes to pull more data.  Moreover, the more RAM you have, the more data you can pull.  And finally, for RAM-limited workflows, create a pipeline that pulls data, writes to disc, and flushes.  The only limitation with data pulls ``gdeltPyR`` is you hardware.

The GDELT Project is the largest, most comprehensive, and highest resolution open database of human society ever created. It monitors print, broadcast, and web news media in over 100 languages from across every country in the world to keep continually updated on breaking developments anywhere on the planet. Its historical archives stretch back to January 1, 1979 and accesses the world’s breaking events and reaction in near-realtime as both the GDELT Event and Global Knowledge Graph update every 15 minutes.  Visit the `GDELT website to learn more about the project <(http://gdeltproject.org/#intro)>`_.


Installation
--------------

Latest release installs from PyPi::

    pip install gdelt

Latest dev version of ``gdeltPyR`` can be installed from GitHub.com::

    pip install git+https://github.com/linwoodc3/gdeltPyR
    
    


.. image:: https://twistedsifter.files.wordpress.com/2015/06/people-tweeting-about-sunrises-over-a-24-hour-period.gif?w=700&h=453
:alt: GDELT can help you visualize the world's news!!!  Analyze GDELT data with gdeltPyR!!
    
Basic Usage
--------------  

.. code-block:: python

    #############################
    # Import gdeltPyR; instantiate
    #############################
    
    import gdelt
    
    gd = gdelt.gdelt(version=2)
    
    results = gd.Search(['2016 10 19','2016 10 22'],table='events',coverage=True)
    
Output Type
--------------

At the moment, ``gdeltPyR`` outputs pandas dataframes with the headers for which ever table/version your set as your input parameters.  Performance and speed of query return depends on your computer.  The more cores you have, the quicker your queries return.  As an example, the query above takes ~36 seconds on a 4  core, MacOS Sierra 10.12 with 16GB of RAM laptop.  It returns 900,000 rows of data with 61 columns (events database table).

    
    

