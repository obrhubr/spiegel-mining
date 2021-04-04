import logging
import datetime
import os

import wrangler.main as wm
import miner.main as mm
import vizier.imagegen.main as vm

logging.info('Mining the data: ')
mm.main()
logging.info('Wrangling the data: ')
wm.main()
logging.info('Visualizing the data: ')
vm.main()