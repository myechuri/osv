from osv.modules.filemap import FileMap
from osv.modules import api
import os, os.path

usr_files = FileMap()

provides = ['java']

non_isolated_jvm = True

api.require('fonts')
api.require('ca-certificates')
api.require('libz')
api.require('josvsym')
api.require('httpserver-jolokia-plugin')
api.require('httpserver-jvm-plugin')

jdkdir = os.path.basename(os.path.expandvars('${jdkbase}'))

usr_files.add('${jdkbase}').to('/usr/lib/jvm/java') \
    .include('lib/**') \
    .include('jre/**') \
    .exclude('jre/lib/security/cacerts') \
    .exclude('jre/lib/audio/**')

usr_files.link('/usr/lib/jvm/' + jdkdir).to('java')
usr_files.link('/usr/lib/jvm/jre').to('java/jre')
usr_files.link('/usr/lib/jvm/java/jre/lib/security/cacerts').to('/etc/pki/java/cacerts')
