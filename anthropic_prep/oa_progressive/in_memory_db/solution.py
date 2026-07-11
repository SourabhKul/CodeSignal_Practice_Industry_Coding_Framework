class InMemoryDB:
    """Candidate workspace. Add later-level methods only after unlocking them."""

    def __init__(self):
      self.database = {} # {key : field : {value: expires_at:}  
      self.backups = {}

    def set(self, key, field, value):
        if key not in self.database.keys():
            self.database[key] = {}
        self.database[key][field] = value
        return None

    def get(self, key, field):
        if key not in self.database.keys():
            return None
        if field not in self.database[key].keys():
            return None
        return self.database[key][field]

    def delete(self, key, field):
        if key not in self.database.keys():
            return False
        if field not in self.database[key].keys():
            return False
        del self.database[key][field]
        return True 
    
    def scan(self, key):
        if key not in self.database.keys():
            return []
        scan = []
        for field in self.database[key].keys():
            scan.append(f"{field}({self.database[key][field]})")
        return sorted(scan)

    def scan_by_prefix(self, key, prefix):
        if key not in self.database.keys():
            return []
        scan = []
        for field in self.database[key].keys():
            if field.startswith(prefix):
                scan.append(f"{field}({self.database[key][field]})")
        return sorted(scan)
    
    def set_at(self, key, field, value, timestamp):
        if key not in self.database.keys():
            self.database[key] = {}
        self.database[key][field] = {'value' : value, 'expires_at' : None}
        return None        

    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        if key not in self.database.keys():
            self.database[key] = {}
        self.database[key][field] = {'value' : value, 'expires_at' : timestamp + ttl}
        return None 

    def get_at(self, key, field, timestamp):
        if key not in self.database.keys():
            return None
        if field not in self.database[key].keys():
            return None
        if self.database[key][field]['expires_at'] is None:
            return self.database[key][field]['value']
        if  self.database[key][field]['expires_at'] > timestamp:
            return self.database[key][field]['value']
        else: return None

    def delete_at(self, key, field, timestamp):
        if key not in self.database.keys():
            return False
        if field not in self.database[key].keys():
            return False
        if self.database[key][field]['expires_at'] is None:
            del self.database[key][field]
            return True
        elif self.database[key][field]['expires_at'] < timestamp: 
            del self.database[key][field]
            return True 
        else: return False

    def scan_at(self, key, timestamp):
        if key not in self.database.keys():
            return []
        scan = []
        for field in self.database[key].keys():
            if self.database[key][field]['expires_at'] is None:
                scan.append(f"{field}({self.database[key][field]['value']})")
            elif self.database[key][field]['expires_at'] > timestamp:
                scan.append(f"{field}({self.database[key][field]['value']})")
        return sorted(scan)

    def scan_by_prefix_at(self, key, prefix, timestamp):
        if key not in self.database.keys():
            return []
        scan = []
        for field in self.database[key].keys():
            if field.startswith(prefix):
                if self.database[key][field]['expires_at'] is None:
                    scan.append(f"{field}({self.database[key][field]['value']})")
                elif self.database[key][field]['expires_at'] > timestamp:
                    scan.append(f"{field}({self.database[key][field]['value']})")
        return sorted(scan)
    
    def backup(self, timestamp):
        backup = {}
        num_live_keys = 0
        for key in self.database.keys():
            backup[key] = {}
            for field in self.database[key].keys():
                if self.database[key][field]['expires_at'] is None:
                    backup[key][field] = { 
                        'value': self.database[key][field]['value'], 
                        'expires_at': None, 
                    }
                elif self.database[key][field]['expires_at'] > timestamp:
                    backup[key][field] = {
                        'value': self.database[key][field]['value'],
                        'expires_at': self.database[key][field]['expires_at'],
                    }
            if backup[key]:
                num_live_keys += 1
        self.backups[timestamp] = backup
        return num_live_keys
    
    def restore(self, timestamp, restore_to):
        timestamp_before_restore = max([timestamp for timestamp in (list(self.backups.keys())) if timestamp <= restore_to])
        if not timestamp_before_restore:
            return None
        restore = {}
        for key in self.backups[timestamp_before_restore].keys():
            restore[key] = {}
            for field in self.backups[timestamp_before_restore][key].keys():
                if self.backups[timestamp_before_restore][key][field]['expires_at'] is None:
                    restore[key][field] = {
                        'value': self.backups[timestamp_before_restore][key][field]['value'],
                        'expires_at': None
                    }
                elif self.backups[timestamp_before_restore][key][field]['expires_at'] > timestamp_before_restore:
                    restore[key][field] = {
                        'value': self.backups[timestamp_before_restore][key][field]['value'],
                        'expires_at': self.backups[timestamp_before_restore][key][field]['expires_at'] - timestamp_before_restore + timestamp
                    }
        self.database = restore
        return None                    
         