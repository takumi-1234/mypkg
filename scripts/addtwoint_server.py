#!/usr/bin/env python3

import rospy
#from ros_practice_msgs.srv import AddTwoInt, AddTwoIntResponse
from mypkg.srv import AddTwoInt, AddTwoIntResponse

class Server():

    def __init__(self):
        self.add_srv = rospy.Service("/addtwoint", AddTwoInt, self.callback)

    def callback(self, req):

        rospy.loginfo(f"Reserved x = {req.x} y = {req.y}")

        res = AddTwoIntResponse()
        res.z = req.x + req.y

        rospy.loginfo(f"Sending Z = {res.z}")

        return res

if __name__ == "__main__":
    
    rospy.init_node("addtwoint_server_node")

    server = Server()

    rospy.spin()




