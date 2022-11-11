from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import math

class Clock(QWidget):
    def __init__(self, parent_container):
        super().__init__()
        
        self.container = parent_container
        
        self.hour = datetime.now().hour
        self.minute = datetime.now().second

        self.set_clock_radius(400)

    def set_clock_radius(self, new_radius=200):
        self.clock_radius = new_radius

    def update_time(self):
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.update()

    def draw_clock(self, painter):
        canvas_horizontal_mid = int(self.container.size().width() / 2)
        canvas_vertical_mid = int(self.container.size().height() / 2)

        painter.drawEllipse(int(canvas_horizontal_mid - self.clock_radius), int(canvas_vertical_mid - self.clock_radius), int(self.clock_radius * 2), int(self.clock_radius * 2))

        font = QtGui.QFont()
        font.setPointSize(20)
        painter.setFont(font)
        for i in range(12):
            hour_angle = ((-2*math.pi*i) + (6 * math.pi)) / 12

            start_x = canvas_horizontal_mid
            start_y = canvas_vertical_mid
            
            hour_stop_x = start_x + int((0.9 * self.clock_radius) * math.cos(hour_angle))
            hour_stop_y = start_y - int((0.9 * self.clock_radius) * math.sin(hour_angle))
            
            painter.drawText(hour_stop_x, hour_stop_y, str(i))
    
    def update_hourhand(self, painter, start_x, start_y, ellipse_radius):
        hour_angle = ((-2*math.pi*self.hour) + (6 * math.pi)) / 12
        hour_stop_x = start_x + int((0.6 * ellipse_radius) * math.cos(hour_angle))
        hour_stop_y = start_y - int((0.6 * ellipse_radius) * math.sin(hour_angle))
        painter.drawLine(start_x, start_y, hour_stop_x, hour_stop_y)

    def update_minutehand(self, painter, start_x, start_y, ellipse_radius):
        minute_angle = ((-2*math.pi*self.minute) + (30 * math.pi)) / 60
        minute_stop_x = start_x + int((0.8 * ellipse_radius) * math.cos(minute_angle))
        minute_stop_y = start_y - int((0.8 * ellipse_radius) * math.sin(minute_angle))
        painter.drawLine(start_x, start_y, minute_stop_x, minute_stop_y)

    def paintEvent(self, event):
        # print("In paint event")
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor("white"))
        pen.setWidth(2)
        painter = QPainter(self)
        painter.setPen(pen)

        self.draw_clock(painter)

        ellipse_diameter = 400
        ellipse_radius = int(ellipse_diameter / 2)

        canvas_horizontal_mid = int(self.container.size().width() / 2)
        canvas_vertical_mid = int(self.container.size().height() / 2)

        painter.drawEllipse(int(canvas_horizontal_mid - self.clock_radius), int(canvas_vertical_mid - self.clock_radius), int(self.clock_radius * 2), int(self.clock_radius * 2))
        # painter.drawEllipse(int(canvas_horizontal_mid - (ellipse_diameter / 2)), int(canvas_vertical_mid - (ellipse_diameter / 2)), ellipse_diameter, ellipse_diameter)

        start_x = canvas_horizontal_mid
        start_y = canvas_vertical_mid

        # painter.drawPoint(canvas_horizontal_mid, canvas_vertical_mid)
        self.update_hourhand(painter, start_x, start_y, self.clock_radius)
        self.update_minutehand(painter, start_x, start_y, self.clock_radius)
