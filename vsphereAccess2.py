#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2011 Carnimaniac 

"""
vSphere Python
"""

import ssl

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim

def main():
    # activation protocole SSL
    sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslContext.verify_mode = ssl.CERT_NONE

    try:
        # connection a la VM
        service_instance = connect.SmartConnect(host="10.102",
                                                user="root",
                                                pwd="",
                                                port=int("443"),
                                                sslContext=sslContext)
        
        # recup la liste des objet VM
        content = service_instance.RetrieveContent()
        objview = content.viewManager.CreateContainerView(content.rootFolder,[vim.VirtualMachine],True)
        
        # cherche le nom de toutes les VM
        esxi_hosts = objview.view
        objview.Destroy()

        for esxi_host in esxi_hosts:
            print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.name))
            #print("{}\t{}\t\n".format("ESXi Name:     ", esxi_host.config.hardware))
            #print("{}\t{}\t\n".format("ESXi Name:     ", esxi_host.config.hardware.memoryMB))
            #print("{}\t{}\t\n".format("ESXi Name:     ", esxi_host.config.uuid))
            #print("{}\t{}\t\n".format("ESXi Guest:     ", esxi_host.config.guestFullName))
            #print("{}\t{}\t\n".format("ESXi State:     ", esxi_host.runtime))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.guest.ipAddress))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.config.hardware.numCPU))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.config.guestId))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.storage))
            #print("{}\t{}\t\n".format("ESXi status:     ", esxi_host.overallStatus))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.customValue))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.capability))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.layout.logFile ))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.layoutEx))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.environmentBrowser))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.resourcePool))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.parentVApp))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.resourceConfig))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.summary.runtime))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.datastore))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.network))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.snapshot))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.rootSnapshot))
            #print("{}\t{}\t\n".format("ESXi IP:     ", esxi_host.guestHeartbeatStatus))

    
    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

    return 0

# Start program
if __name__ == "__main__":
    main()
