#!/usr/bin/env python
# William Lam
# www.virtuallyghetto.com

"""
vSphere Python SDK program for listing all ESXi datastores and their
associated devices
"""

import ssl

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
import pprint

def PrintVmInfo(vm, depth=1):
   """
   Print information for a particular virtual machine or recurse into a folder
   or vApp with depth protection
   """
   maxdepth = 10

   # if this is a group it will have children. if it does, recurse into them
   # and then return
   if hasattr(vm, 'childEntity'):
      if depth > maxdepth:
         return
      vmList = vm.childEntity
      for c in vmList:
         PrintVmInfo(c, depth+1)
      return

   # if this is a vApp, it likely contains child VMs
   # (vApps can nest vApps, but it is hardly a common usecase, so ignore that)
   if isinstance(vm, vim.VirtualApp):
      vmList = vm.vm
      for c in vmList:
         PrintVmInfo(c, depth + 1)
      return

   summary = vm.summary
   print("Name       : ", summary.config.name)
   print("Path       : ", summary.config.vmPathName)
   print("Guest      : ", summary.config.guestFullName)
   annotation = summary.config.annotation
   if annotation != None and annotation != "":
      print("Annotation : ", annotation)
   print("State      : ", summary.runtime.powerState)
   if summary.guest != None:
      ip = summary.guest.ipAddress
      if ip != None and ip != "":
         print("IP         : ", ip)
   if summary.runtime.question != None:
      print("Question  : ", summary.runtime.question.text)
   print("")
   
   
def main():
    """
   Simple command-line program for listing all ESXi datastores and their
   associated devices
   """

    sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslContext.verify_mode = ssl.CERT_NONE

    try:
        
        service_instance = connect.SmartConnect(host="10.102",
                                                user="root",
                                                pwd="",
                                                port=int("443"),
                                                sslContext=sslContext)

        content = service_instance.RetrieveContent()
        #objview = content.viewManager.CreateContainerView(content.rootFolder,[vim.Datacenter],True)
        objview = content.viewManager.CreateContainerView(content.rootFolder,[vim.VirtualMachine],True)
        
        # Search for all ESXi hosts
        esxi_hosts = objview.view
        objview.Destroy()

        for esxi_host in esxi_hosts:
            print("{}\t{}\t\n".format("ESXi Name:     ", esxi_host.config.name))
            #print("{}\t{}\t\n".format("ESXi Path:     ", esxi_host.config.vmPathName))
            print("{}\t{}\t\n".format("ESXi Guest:     ", esxi_host.config.guestFullName))
            #print("{}\t{}\t\n".format("ESXi Host:     ", esxi_host.config.annotation))
            print("{}\t{}\t\n".format("ESXi power:     ", esxi_host.runtime.powerState))
            print("{}\t{}\t\n".format("ESXi Host:     ", esxi_host.guest.ipAddress))

            #pprint.pprint(esxi_host)
            
        for child in content.rootFolder.childEntity:
          if hasattr(child, 'vmFolder'):
             datacenter = child
             vmFolder = datacenter.vmFolder
             vmList = vmFolder.childEntity
             for vm in vmList:
                PrintVmInfo(vm)
        


    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

    return 0

# Start program
if __name__ == "__main__":
    main()
