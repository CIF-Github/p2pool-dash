import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '2f0c6b4d'.decode('hex')
P2P_PORT = 43199
ADDRESS_VERSION = 28
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 43198
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'dashaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('cif_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('cif_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'DASH'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'DashCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/DashCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dashcore'), 'dash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
