import os
import commands
from test_windowssupport import *
(perp_state,prep_reason) = environment_tester()
location = os.path.dirname(os.path.realpath(__file__))
exec_order = 'cd' + location +  '\crawler_scrapy & scrapy crawl test'
# output1 = os.popen(exec_order)
# print output1.read()
(status, output) = commands.getstatusoutput(exec_order)
print status, output

