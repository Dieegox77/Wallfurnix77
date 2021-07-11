import threading
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from g_python.hdirection import Direction
from g_python.hmessage import HMessage, HPacket

from wallfurnigui import  Ui_WallFurniUI

HEADER_ON_PLACE_WALL_ITEM = 'MoveWallItem'
id_original = None
string_original = None
string_last = None

class WallFurni:
    def __init__(self, extension):
        self.__extension = extension
        self.furni_id = 0
        self.z = 0
        self.x = 0
        self.depth = 0
        self.y = 0
        self.orientation = "l"
        self.__verbose = True
        self.__block = True
        self.__lock = threading.Lock()
        self.__guiLoopThread = None

        extension.intercept(Direction.TO_SERVER, self.__on_place_wall_item, HEADER_ON_PLACE_WALL_ITEM)

        self.__app = None
        self.__window = None
        self.__ui = None

        self.__initialize_gui()

    def __initialize_gui(self):
        self.__app = QApplication(sys.argv)
        self.__window = QtWidgets.QMainWindow()
        self.__window.setWindowTitle("WallFurni by kSlide")
        self.__ui = Ui_WallFurniUI(self)
        self.__ui.setupUi(self.__window)
        self.__window.show()
        sys.exit(self.__app.exec_())

    def __on_place_wall_item(self, message: HMessage):
        global id_original
        global string_original

        (self.furni_id, string) = message.packet.read("is")
        id_original = self.furni_id
        string_original = string
        string = string.replace(":w=", "").replace("l=", "").split(" ")
        string = ",".join(string).split(",")
        self.z, self.x, self.depth, self.y, self.orientation = string

        self.log(
            f'<PlaceWallitem> [{self.furni_id}] - Z: {self.z} - X: {self.x} - D: {self.depth} - Y: {self.y} - '
            f'orientation: {self.orientation}')

        self.__ui.emitRefresh()
        message.is_blocked = self.__block

        #self.y = int(self.y) -115
        #self.__place_wall_item(self.furni_id, self.z, self.x, self.depth, self.y, self.orientation)

    def __place_wall_item(self, furni, z, x, depth, y, orientation):
        global string_last
        string_last = ':w='+str(z)+','+str(x)+' l='+str(depth)+','+str(y)+' '+str(orientation)
        self.__extension.send_to_server(HPacket(HEADER_ON_PLACE_WALL_ITEM, furni, ':w='+str(z)+','+str(x)+' l='+str(depth)+','+str(y)+' '+str(orientation)))

    def __refresh_wall_item_position(self):
        self.__place_wall_item(self.furni_id, self.z, self.x, self.depth, self.y, self.orientation)
        self.__ui.emitRefresh()

    def set_furni(self, furni: str):
        self.furni_id = furni
        self.__refresh_wall_item_position()
        return self

    def set_z(self, z: int):
        self.z = z
        self.__refresh_wall_item_position()
        return self

    def set_x(self, x: int):
        self.x = x
        self.__refresh_wall_item_position()
        return self

    def set_depth(self, depth: int):
        if(depth <= 32):
            self.depth = depth
        else:
            self.depth = 32
        self.__refresh_wall_item_position()
        return self

    def set_y(self, y: int):
        self.y = y
        self.__refresh_wall_item_position()
        return self

    def set_orientation(self, orientation: str):
        self.orientation = orientation
        self.__refresh_wall_item_position()
        return self

    def reset(self):
        global string_original
        string = string_original.replace(":w=", "").replace("l=", "").split(" ")
        string = ",".join(string).split(",")
        self.z, self.x, self.depth, self.y, self.orientation = string
        self.__refresh_wall_item_position()

    def move_to_last(self):
        global string_last
        string = string_last.replace(":w=", "").replace("l=", "").split(" ")
        string = ",".join(string).split(",")
        self.z, self.x, self.depth, self.y, self.orientation = string
        self.__refresh_wall_item_position()

    def front(self):
        self.x = int(self.x) + 1
        self.z = int(self.z) + 1
        self.y = int(self.y) - 32
        self.__refresh_wall_item_position()

    def back(self):
        self.x = int(self.x) - 1
        self.z = int(self.z) - 1
        self.y = int(self.y) + 32
        self.__refresh_wall_item_position()


    def log(self, message):
        if self.__verbose:
            print(f'({time.strftime("%d %b %Y %H:%M:%S", time.gmtime())}) <WallFurni> {message}')
