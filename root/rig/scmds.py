#!/usr/bin/python
# -*- coding:utf-8 -*-
# Autor: PengCheng 
# E-mail: southAngel@126.com 
# Time: 2018-09-19 17:11 
from maya import cmds
import pymel.core as pm
from SouAng.smod import ssys
from ..functionsCollection import postion


def orientChildrenJoints():
    joints = cmds.listRelatives(ad=1, type='joint')
    cmds.makeIdentity(joints, jo=1)

def grpZeroTheObj():
    sel = cmds.ls(sl=1)
    if sel:
        for each in sel:
            parent_list = cmds.listRelatives(each, p=1)
            if parent_list:
                nowPos = cmds.getAttr('%s.t'%each)[0]
                nowRot = cmds.getAttr('%s.r'%each)[0]
                newGrp = cmds.group(em=1, p=parent_list[0])
                cmds.xform(newGrp, r=1, t=nowPos, ro=nowRot)
                cmds.parent(each, newGrp)

def buttonF3():
    print('F3')

def jjjIkFkSet(text):
    sel = cmds.ls(sl=1)
    if len(sel) < 4:
        return 0
    ikfk_c = sel[0]
    ikfkAttr = text
    origin_j = [None for i in xrange(3)]
    ik_j = [None for i in xrange(3)]
    fk_j = [None for i in xrange(3)]
    print('F1', text)

def buttonlF2(text):
    print('F2', text)

def buttonlF3(text):
    print('F3', text)


class JointSegment(object):

    def __init__(self):
        super(JointSegment, self).__init__()

    def joinParent(self):
        sel = cmds.ls(sl=1)
        if sel:
            self.addSegmentPos(sel[0])

    def joinParentEx(self, seg_num=2):
        sel = cmds.ls(sl=1)
        if sel:
            seg_num = int(seg_num)
            count_num = seg_num + 1
            for i in xrange(seg_num):
                self.addSegmentPos(sel[0], 1.0/count_num)
                print(1.0 / count_num)
                count_num += -1

    def addSegmentPos(self, obj, loc=0.5):
        parent = cmds.listRelatives(obj, p=1, f=1)
        if parent:
            rad = cmds.joint(obj, q=1, rad=1)[0]
            nowPos = cmds.getAttr('%s.t'%obj)[0]
            newJoint = cmds.joint(parent[0], r=1, rad=rad, p=(nowPos[0]*loc, nowPos[1]*loc, nowPos[2]*loc))
            cmds.parent(obj, newJoint)


BUTTON_LIST = (
        ('Zero Postion', postion.zeroTR, ''),
        ('Center And Freeze', postion.resetToCenterFreeze),
        ('World Center And Freeze', postion.resetToZero),
        ('Move World Center', postion.moveWorldZero),
        ('Add Middle Joint', JointSegment().joinParent),
        ('Orient All Joint', orientChildrenJoints),
        ('Zero Parent Group', grpZeroTheObj),
        )
BUTTONLINE_LIST = (
        ('Add Mult Joint', JointSegment().joinParentEx, '2'),
        ('IKFK Set', jjjIkFkSet, 'IKFK'),
        ('F2', buttonlF2, 'd2'),
        ('F3', buttonlF3, 'd3'),
        )
