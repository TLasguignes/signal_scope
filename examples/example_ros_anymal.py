'''
A working example for signals from Anymal

Plots x,y,z in position and the yaw angle
'''


import numpy

import sys
sys.argv = ['test']
import tf


def getYawDegrees(msg):
    '''yaw degrees'''
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    return msg.header.stamp, euler[2]*180.0/numpy.pi

def getPositionNorm(msg):
    '''position magnitude'''
    x = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
    return msg.header.stamp, numpy.linalg.norm(x)

def getVelocity(msg):
    '''velocity in m/sec'''
    vel = [msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z]
    return msg.header.stamp, numpy.linalg.norm(vel)

addPlot(timeWindow=20, yLimits=[-10, 10])
addSignal('/state_estimator/anymal_state', msg.header.stamp, msg.pose.pose.position.x)
addSignal('/state_estimator/anymal_state', msg.header.stamp, msg.pose.pose.position.y)
addSignal('/state_estimator/anymal_state', msg.header.stamp, msg.pose.pose.position.z)
addSignalFunction('/state_estimator/anymal_state', getPositionNorm)

addPlot(timeWindow=20, yLimits=[-180, 180])
addSignalFunction('/state_estimator/anymal_state', getYawDegrees)


addPlot(timeWindow=20, yLimits=[-2, 2])
addSignalFunction('/state_estimator/anymal_state', getVelocity)



