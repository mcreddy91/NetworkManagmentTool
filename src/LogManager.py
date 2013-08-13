#!/usr/bin/env python

import logging
import logging.handlers


LOG_FILENAME = "data/network.mylog"

class Log:
    def __init__(self,_msg,_log_type=0):
        FORMAT = "%(levelname)s: %(asctime)-15s %(message)s"
        logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG, format = FORMAT)

        if _log_type == 0: #info
            logging.info(_msg)
        elif _log_type == 1: # warning
            logging.warning(_msg)

    def mylog(self,msg,log_type):
        if log_type:
            print "Log"
            #self.logger.info(self.msg)

