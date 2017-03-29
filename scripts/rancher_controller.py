#!/usr/bin/env python
import os
import rospy
import gdapi
import actionlib
from rancher_ctrl.msg import *

class RancherCtrl(object):
    def __init__(self, name):
        self._access_key = os.environ['RANCHER_ACCESS_KEY']
        self._secret_key = os.environ['RANCHER_SECRET_KEY']
        self._url = os.environ['RANCHER_URL']
        self._client = gdapi.Client(url=self._url, access_key=self._access_key, secret_key=self._secret_key)
        self.act_serv = actionlib.SimpleActionServer(name + '/control', RancherCtrlAction, self.act_serv_execute, False)
        self.act_serv.start()

    def act_serv_execute(self, action):
        self.obj_list = eval('self._client.list_' + action.scope + '(sort="name")')
        count = 0
        for obj in self.obj_list:
            if obj.name in action.nodes:
                try:
                    self._client.action(obj, action.command)
                    count += 1
                except Exception as e:
                    self.act_serv.set_aborted(RancherCtrlResult(message=e.message))
                    return
            if count == len(action.nodes):
                self.act_serv.set_succeeded(RancherCtrlResult())
                return
        self.act_serv.set_aborted(RancherCtrlResult(message='Not all actions could be executed'))

if __name__ == '__main__':
    name = 'rancher_controller'
    rospy.init_node(name)
    node = RancherCtrl(name)
    rospy.spin()
