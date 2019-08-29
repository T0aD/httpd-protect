import tools

def down(params):
    for port in params.protected_port:
        tools.run("iptables -D INPUT -p tcp --dport %d -j %s" % (port, params.chain_name))
    tools.run("iptables -F %s" % params.chain_name)
    tools.run("iptables -X %s" % params.chain_name)


def up(params):
    rv = tools.run("iptables -L %s -n" % params.chain_name)
    if rv == 3:
        raise Exception("Permission denied: you need to be root")

    #if rv != 0:
    if True:
        tools.run("iptables -N %s" % params.chain_name)
        tools.run("iptables -A %s -j REJECT" % params.chain_name)

        if len(params.allow):
            for addr in params.allow:
                tools.run("iptables -I %s --source %s -j ACCEPT" % (params.chain_name, addr))

        for port in params.protected_port:
            tools.run("iptables -I INPUT -p tcp --dport %d -j %s" % (port, params.chain_name))

    # check:
    #tools.run("iptables -L INPUT -n -v")
    #tools.run("iptables -L %s -n -v" % params.chain_name)


def is_whitelist(params, remote_ip):
    rv = tools.run_and_return("iptables -L %s -n" % (params.chain_name))
    rrv = rv.split("\n")
    for l in rrv:
        if remote_ip in l:
            #print 'remote_ip found in!'
            return True
    return False

def whitelist(params, remote_ip):
    if not is_whitelist(params, remote_ip):
        #print 'whitelisting', remote_ip
        tools.run("iptables -I %s --source %s -j ACCEPT" % (params.chain_name, remote_ip))
        return True
    return False
    #else:
    #    print 'already in white list'

    #tools.run("iptables -L %s -n -v" % params.chain_name)
