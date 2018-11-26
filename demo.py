from __future__ import absolute_import

from six.moves import range

from automation import CommandSequence, TaskManager

import urls		#Import the urls.py file we created for the project. urls.py creates list element of URLS from alexa top 1m sites.

# The list of sites that we wish to crawl
NUM_BROWSERS = 1
sites = urls.getURL()

# Loads the manager preference and 3 copies of the default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)

# Update browser configuration (use this for per-browser settings)
for i in range(NUM_BROWSERS):
    # Record HTTP Requests and Responses
    browser_params[i]['http_instrument'] = True
    # Enable flash for all three browsers
    browser_params[i]['disable_flash'] = False
browser_params[0]['headless'] = True  # Launch only browser 0 headless
browser_params[0]['cookie_instrument'] = True	#Used to turn on JS cookie grabbing. 

# Update TaskManager configuration (use this for crawl-wide settings)
manager_params['data_directory'] = '~/Desktop/'
manager_params['log_directory'] = '~/Desktop/'

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params)

# Visits the sites with all browsers simultaneously
for site in sites:
    command_sequence = CommandSequence.CommandSequence(site)

    # Start by visiting the page
    command_sequence.get(sleep=0, timeout=60)

    # dump_profile_cookies/dump_flash_cookies closes the current tab.
    command_sequence.dump_profile_cookies(120)
    command_sequence.dump_profile	#Used to dump JS cookies to SQLiteDB. Still need to get browser extensions enabled. 

    # index='**' synchronizes visits between the three browsers
    manager.execute_command_sequence(command_sequence, index='**')

# Shuts down the browsers and waits for the data to finish logging
manager.close()
