import os
import subprocess
from test_windowssupport import *
(perp_state,prep_reason) = environment_tester()
location = os.path.dirname(os.path.realpath(__file__))
exec_order = 'cd ' + location +  '\crawler_scrapy & scrapy crawl test'
# exec_order = 'cd ' + location +  '\crawler_scrapy & dir'
print exec_order
result = subprocess.call(exec_order,shell=True)
print result

