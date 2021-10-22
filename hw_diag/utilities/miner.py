from hm_pyhelper.miner_json_rpc import MinerClient


client = MinerClient()


def fetch_miner_data(diagnostics):
    try:
        peerbook = client.get_peer_book()[0]
        height = client.get_height()
    except Exception as err:
        raise Exception("Unable to fetch keys from miner container"
                        "via JSON RPC API. Exception: %s" % str(err))

    diagnostics['MC'] = peerbook.get('connection_count') > 1
    diagnostics['MD'] = peerbook.get('listen_addr_count') > 0
    diagnostics['MH'] = height.get('height')
    diagnostics['MN'] = peerbook.get('nat')
    diagnostics['MR'] = diagnostics['MN'] == 'symmetric'
    return diagnostics
