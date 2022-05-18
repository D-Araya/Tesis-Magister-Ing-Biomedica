################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
import datetime
import csv
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np



class SampleListener(Leap.Listener):
    # finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    # bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def __init__(self):
        Leap.Listener.__init__(self)
        self.data = []
        self.lifetime = []
        #self.fingerTipIndex = []
        self.fingerTipMiddle = []
        self.lengths = []
        #self.key = []
        #self.fps = []
        #self.Tool = []


    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        #controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        #controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        #controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):

        #list_ = [self.data, self.time, self.key, self.fps]

        out_filename = datetime.datetime.now().strftime("signal/%Y%m_%d-%H%M_%S.csv")
        name = open(out_filename, "wb")
        CSV = csv.writer(name)#,  delimiter=',')#, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
        #CSV.writerows(self.fingerTipIndex)
        CSV.writerows(self.fingerTipMiddle)
        #CSV.writerows(self.Tool)

        #for row in zip(self.data, self.key):
            #CSV.writerow(row)
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        #timestamp = frame.timestamp #* .000001 \second
        fps = frame.current_frames_per_second
        #ident = frame.id
        #print "fps: %d, Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            #frame.current_frames_per_second, frame.id, timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        """
        for tools in frame.tools:
            tx = tools.tip_position[0]
            ty = tools.tip_position[1]
            tz = tools.tip_position[2]
            ToolTip = Leap.Vector(tx, ty, tz).to_float_array()
            self.Tool.append(ToolTip)
            print ToolTip, len(frame.tools)
            time.sleep(0.02)
        """
        # Get hands
        for hand in frame.hands:
            #if hand.isRight:

            #handType = "Left hand" if hand.is_left else "Right hand"

            #print "  %s, id %d, position: %s" % (
                #handType, hand.id, hand.palm_position)

            # Get the hand's normal vector and direction
            #normal = hand.palm_normal
            #direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            #print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                #direction.pitch * Leap.RAD_TO_DEG,
                #normal.roll * Leap.RAD_TO_DEG,
                #direction.yaw * Leap.RAD_TO_DEG)

            # Get arm bone
            #arm = hand.arm
            #print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                #arm.direction,
                #arm.wrist_position,
                #arm.elbow_position)

            # Get fingers
            ###### TRACKING  ########### PULGAR
            #x1 = hand.fingers[0].tip_position[0]
            #y1 = hand.fingers[0].tip_position[1]
            #z1 = hand.fingers[0].tip_position[2]
            #Thumb = Leap.Vector(x1, y1, z1).to_float_array()

            """
            ###### TRACKING  ########### INDICE
            x2 = hand.fingers[1].tip_position[0]
            y2 = hand.fingers[1].tip_position[1]
            z2 = hand.fingers[1].tip_position[2]
            vx2 = hand.fingers[1].tip_velocity[0]
            vy2 = hand.fingers[1].tip_velocity[1]
            vz2 = hand.fingers[1].tip_velocity[2]

            Indice = Leap.Vector(x2, y2, z2)   # DATOS ACTUALES
            Index = Indice.to_float_array()
            self.fingerTipIndex.append(Index)
            velocity_Index = Leap.Vector(vx2, vy2, vz2).to_float_array()


            ###### FPS  ######
            #time.sleep(0.02)  # 12.5 miliseg -0.0125 seg/ 10 miliseg -0.01 seg = 80/100 Hz

            ####### GET DATA   #############

            times = hand.fingers[1].time_visible
            tiempo = np.asarray(times)  # INICIA TIEMPO EN CUALQUIER SEGUNDO
            self.lifetime.append(tiempo)

            # TIEMPO REAL
            tiempoTotal = self.lifetime[-1] - self.lifetime[0]

            # SD DE LA VELOCIDAD INSTANTANEA   #### INDICE
            self.data.append(velocity_Index)
            speedVariability = np.std([self.data], ddof=1)
            #print velocity_Index, len(self.data)

            # LONGITUD TOTAL DE LA TRAYECTORIA  ####### DISTANCIA EUCLDEANA ENTRE PUNTOS ADYACENTES EN mm
            tipX = self.fingerTipIndex[-2][0]
            tipY = self.fingerTipIndex[-2][1]
            tipZ = self.fingerTipIndex[-2][2]
            #print tipX, tipY
            #print Index[0], Index[1]
            # http://stackoverflow.com/questions/20773612/python-compute-the-length-of-a-path-for-a-moving-object
            pts = [[tipX, tipY], [Index[0], Index[1]]]
            self.lengths.append(np.sqrt(np.sum(np.diff(pts, axis=0) ** 2, axis=1)))  # Length between points
            total_length = np.sum(self.lengths)
            #averageSpeed = total_length/tiempoTotal  # altamente correlacionado con el tiempo de movimiento
            #print tiempoTotal, total_length, speedVariability


            #earlierFrame = controller.frame(59) # 60 frames earlier than
            #earlierHand = earlierFrame.hand(hand.id)  # look up the hand by its ID
            #print earlierFrame, earlierHand
            #if earlierHand.is_valid:               # then we found the same hand
                #displacement = hand.fingers[1].tip_position - earlierHand.fingers[1].tip_position
                #print displacement
                #dt = frame.timestamp - earlierFrame.timestamp  # microseconds
                #dt = dt * .000001  # seconds
                #velocity = displacement*(1/dt)   # mm  per  second
                #print "velocity x2: %d, velocity y2 : %d, velocity z3 : %d, second : %d" % (
                    #velocity[0], velocity[1], velocity[2], dt)
                #print Index, velocity_Index
            """

            ##### MEDIO
            x3 = hand.fingers[2].tip_position[0]
            y3 = hand.fingers[2].tip_position[1]
            z3 = hand.fingers[2].tip_position[2]
            vx3 = hand.fingers[2].tip_velocity[0]
            vy3 = hand.fingers[2].tip_velocity[1]
            vz3 = hand.fingers[2].tip_velocity[2]

            Medio = Leap.Vector(x3, y3, z3)
            Middle = Medio.to_float_array()
            self.fingerTipMiddle.append(Middle)
            velocity_Middle = Leap.Vector(vx3, vy3, vz3).to_float_array()
            print Middle, fps

            ###### FPS  ######
            #time.sleep(0.02)  # 12.5 miliseg -0.0125 seg/ 10 miliseg -0.01 seg = 80/100 Hz

            ####### GET DATA   #############

            times = hand.fingers[2].time_visible
            tiempo = np.asarray(times)  # INICIA TIEMPO EN CUALQUIER SEGUNDO
            self.lifetime.append(tiempo)

            # TIEMPO REAL
            tiempoTotal = self.lifetime[-1] - self.lifetime[0]

            # SD DE LA VELOCIDAD INSTANTANEA
            self.data.append(velocity_Middle)
            speedVariability = np.std([self.data], ddof=1)
            # print velocity_Index, len(self.data)

            # LONGITUD TOTAL DE LA TRAYECTORIA  ####### DISTANCIA EUCLDEANA ENTRE PUNTOS ADYACENTES EN mm
            tipX = self.fingerTipMiddle[-2][0]
            tipY = self.fingerTipMiddle[-2][1]
            tipZ = self.fingerTipMiddle[-2][2]
            # print tipX, tipY
            # print Index[0], Index[1]
            # http://stackoverflow.com/questions/20773612/python-compute-the-length-of-a-path-for-a-moving-object
            pts = [[tipX, tipY], [Middle[0], Middle[1]]]
            self.lengths.append(np.sqrt(np.sum(np.diff(pts, axis=0) ** 2, axis=1)))  # Length between points
            total_length = np.sum(self.lengths)
            # averageSpeed = total_length/tiempoTotal  # altamente correlacionado con el tiempo de movimiento
            # print tiempoTotal, total_length, speedVariability

            ##########################################################################33

            #x4 = hand.fingers[3].tip_position[0]
            #y4 = hand.fingers[3].tip_position[1]
            #z4 = hand.fingers[3].tip_position[2]
            #Ring = Leap.Vector(x4, y4, z4).to_float_array()

            #x5 = hand.fingers[4].tip_position[0]
            #y5 = hand.fingers[4].tip_position[1]
            #z5 = hand.fingers[4].tip_position[2]
            #Pinky = Leap.Vector(x5, y5, z5).to_float_array()
            #print Thumb, Index, Middle, Ring, Pinky


            #for finger in hand.fingers:
                #print "    %s finger, tip_position: %s" % (
                      #, length: %fmm, width: %fmm" % (
                    #self.finger_names[finger.type],
                    #finger.tip_position.to_float_array())
                    #finger.id,
                    #finger.length,
                    #finger.width)

                # Get bones
                #for b in range(0, 4):
                    #bone = finger.bone(b)
                    #print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                        #self.bone_names[bone.type],
                        #bone.prev_joint,
                        #bone.next_joint,
                        #bone.direction)

        # Get tools
        #for tool in frame.tools:

            #print "  Tool id: %d, position: %s, direction: %s" % (
                #tool.id, tool.tip_position, tool.direction)

        # Get gestures
        for gesture in frame.gestures():

            #if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                #circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                #if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    #clockwiseness = "clockwise"
                #else:
                    #clockwiseness = "counterclockwise"

                # Calculate the angle swept since the last frame
                #swept_angle = 0
                #if circle.state != Leap.Gesture.STATE_START:
                    #previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    #swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                #print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        #gesture.id, self.state_names[gesture.state],
                        #circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            #if gesture.type == Leap.Gesture.TYPE_SWIPE:
                #swipe = SwipeGesture(gesture)
                #print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                        #gesture.id, self.state_names[gesture.state],
                        #swipe.position, swipe.direction, swipe.speed)

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                    gesture.id, self.state_names[gesture.state], keytap.position, keytap.direction)
                key_tap = Leap.Vector(keytap.position[0], keytap.position[1], keytap.position[2]).to_float_array()

                ####### ARREGLAR #####
                #else keytap = Leap.Vector(0,0,0)
                ############
            #if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                #screentap = ScreenTapGesture(gesture)
                #print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        #gesture.id, self.state_names[gesture.state],
                        #screentap.position, screentap.direction)

                #self.key.append(key_tap)
            #self.time.append(lifetime)
        #self.fps.append(frame.current_frames_per_second)


        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

    def state_string(self, state):
        #if state == Leap.Gesture.STATE_START:
            #return "STATE_START"

        #if state == Leap.Gesture.STATE_UPDATE:
            #return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        #if state == Leap.Gesture.STATE_INVALID:
            #return "STATE_INVALID"


def main():


    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
