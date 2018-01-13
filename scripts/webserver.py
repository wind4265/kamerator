#!/usr/bin/env python
import rospy, os
import SimpleHTTPServer

def kill():
	os.system("kill -KILL " + str(os.getpid()))

os.chdir(os.path.dirname(__file__) + "/../contents")
rospy.init_node("webserber")
rospy.on_shutdown(kill)
SimpleHTTPServer.test()
