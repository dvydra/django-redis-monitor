from redis_monitor import get_instance
from util import is_sampling_request
import time

class MonitoredCursorWrapper(object):
    def __init__(self, cursor, db):
        self.cursor = cursor
        self.db = db
    
    def execute(self, sql, params=()):
        if is_sampling_request():
            start = time.time()
            self.rm = get_instance('sqlops')
            try:
                return self.cursor.execute(sql, params)
            finally:
                stop = time.time()
                duration_in_microseconds = int(1000000 * (stop - start))
                try:
                    self.rm.record_hit_with_weight(duration_in_microseconds)
                except Exception, e:
                    pass #logging.warn('RedisMonitor error: %s' % str(e))
        else:
            return self.cursor.execute(sql, params)
    
    def executemany(self, sql, param_list):
        if is_sampling_request():
            start = time.time()
            self.rm = get_instance('sqlops')
            try:
                return self.cursor.executemany(sql, param_list)
            finally:
                stop = time.time()
                duration_in_microseconds = int(1000000 * (stop - start))
                try:
                    self.rm.record_hits_with_total_weight(
                        len(param_list), duration_in_microseconds
                    )
                except Exception, e:
                    pass #logging.warn('RedisMonitor error: %s' % str(e))
        else:
            return self.cursor.executemany(sql, param_list)
    
    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return getattr(self.cursor, attr)
    
    def __iter__(self):
        return iter(self.cursor)
