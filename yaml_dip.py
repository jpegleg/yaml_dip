import yaml
import hashlib
import requests
import threading
import binascii
from datetime import datetime

def find(d, tag):
    """ Recurse a YAML structure for tagging. """
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, tag):
                yield i

def timestamper():
    """ Make a timestamp. """
    timestamp = datetime.now()
    return (timestamp)

class ProcessSalsa():
    """ Send data to a salsa_falcon service to encrypt it. """
    def encrypt():
        """ Encrypt datasegment with remote salsa20 as defined in YAML."""
        try:
            stream = open('struct.yml', 'r')
            data = yaml.safe_load(stream)
            timestamp = str(timestamper())
            print(timestamp, '-> Loaded struct.yml for salsa20...')
        except Exception as err:
            print(timestamp, ' ERROR - ', err)
            
        for salsafalcon in find(data, 'salsafalconE'):
            timestamp = str(timestamper())
            print(timestamp, '<- Sending to salsa falcon.')

            for datasegment in find(data, 'datasegment'):
                for datasend in datasegment:
                    timestamp = str(timestamper())
                    stoken = 'honkhonktoken'
                    headers = {'X-API-TOKEN': stoken}
                    payload = datasend
                    try:
                        callurl = str(salsafalcon)
                        timestamp = str(timestamper())
                        uricontext = callurl[2:-2].encode('utf-8')
                        urihash = hashlib.sha256(uricontext).hexdigest()
                        r = requests.post(callurl[2:-2], data=payload, headers=headers)
                        resp = binascii.hexlify(r.content)
                        timestamp = str(timestamper())
                        print(timestamp, urihash[0:12], '-> Recv output: ', resp)
                    except Exception as err:
                        timestamp = str(timestamper())
                        errstr = str(err)
                        print(timestamp, 'ERROR - ', errstr)


class DecryptSalsa():
    """ Send data to a salsa_falcon service to decrypt it. """
    def decrypt():
        """ Decrypt eseg with remote salsa falcon as defined in YAML."""
        try:
            stream = open('struct.yml', 'r')
            data = yaml.safe_load(stream)
        except Exception as err:
            timestamp = str(timestamper())
            print(timestamp, 'ERROR - ', err)
        for salsafalcon in find(data, 'salsafalconD'):
            timestamp = str(timestamper())
            print(timestamp, '<- Sending to salsa falcon.')

            for eseg in find(data, 'eseg'):
                for datasend in eseg:
                    timestamp = str(timestamper())
                    stoken = 'honkhonktoken'
                    headers = {'X-API-TOKEN': stoken}
                    try:
                        callurl = str(salsafalcon)
                        payload = binascii.unhexlify(datasend)
                        uricontext = callurl[2:-2].encode('utf-8')
                        urihash = hashlib.sha256(uricontext).hexdigest()
                        r = requests.post(callurl[2:-2], data=bytes(payload), headers=headers)
                        resp = r.content
                        timestamp = str(timestamper())
                        print(timestamp, urihash[0:12], '-> Recv output: ', resp)
                    except Exception as err:
                        timestamp = str(timestamper())
                        errstr = str(err)
                        print(timestamp, 'ERROR - ', errstr)


if __name__ == '__main__':
    KRAKEN = threading.Thread(target=ProcessSalsa.encrypt)
    SPEAR = threading.Thread(target=DecryptSalsa.decrypt)
    KRAKEN.start()
    SPEAR.start()
    KRAKEN.join()
    SPEAR.join()
