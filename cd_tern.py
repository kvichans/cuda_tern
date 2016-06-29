''' Plugin for CudaText editor
Authors:
    Andrey Kvichansky    (kvichans on github.com)
Version:
    '0.1.0 2016-06-29'
ToDo: (see end of file)
'''

import  re, os, json
import  cudatext            as app
from    cudatext        import ed
import  cudax_lib           as apx
from    .cd_plug_lib    import *

# I18N
_       = get_translation(__file__)

pass;                           LOG     = (-1==-1)  # Do or dont logging.

class Command:
    def __init__(self):
        pass;                   LOG and log('ok',())
    
    def on_complete(self, ed_self):
        pass;                   app.msg_status(_('No release yet'))
    def on_goto_def(self, ed_self):
        pass;                   app.msg_status(_('No release yet'))
    def on_func_hint(self, ed_self):
        pass;                   app.msg_status(_('No release yet'))
   #class Command

'''
ToDo
[ ][kv-kv][29jun16] Start
[ ][kv-kv][29jun16] 
'''
