import pinocchio as se3
import tsid
import numpy as np

print ""
print "Test RobotWrapper"
print ""


import os
filename = str(os.path.dirname(os.path.abspath(__file__)))
mesh_dir = filename + '/../models/romeo'
urdf_model_path = mesh_dir + '/urdf/romeo.urdf'
vector = se3.StdVec_StdString()
vector.extend(item for item in mesh_dir)

robot = tsid.RobotWrapper(urdf_model_path, vector, se3.JointModelFreeFlyer(), False)
# model = robot.model()
model, collision_model, visual_model = se3.buildModelsFromUrdf(urdf_model_path, mesh_dir, se3.JointModelFreeFlyer())
lb = model.lowerPositionLimit
lb[0:3] = -10.0*np.matrix(np.ones(3)).transpose()
lb[3:7] = -1.0*np.matrix(np.ones(4)).transpose()

ub = model.upperPositionLimit
ub[0:3] = 10.0*np.matrix(np.ones(3)).transpose()
ub[3:7] = 1.0*np.matrix(np.ones(4)).transpose()

q = se3.randomConfiguration(model, lb, ub)
print q.transpose()
# robot.data()
data = model.createData()
v = np.matrix(np.ones(robot.nv)).transpose()
robot.computeAllTerms(data, q, v)
print robot.com(data)

print "All test is done"
