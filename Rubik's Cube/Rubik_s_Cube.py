from enum import Enum
import sys
from sty import fg, bg, ef, rs, Style, RgbBg


bg.orange = Style(RgbBg(255, 150, 50))

import os, sys
if sys.platform == "win32":
    os.system('color')

class Color(Enum):
    RED = bg.red
    GREEN = bg.green
    BLUE = bg.blue
    WHITE = bg.white
    ORANGE = bg.orange
    YELLOW = bg.yellow

colors = ["Red", "Green", "Blue", "White", "Orange", "Yellow"]
COLOR_MAP = { "Red" : bg.red,
             "Green" : bg.green,
             "Blue" : bg.blue,
             "White" : bg.white,
             "Orange" : bg.orange,
             "Yellow" : bg.yellow
            }
class PieceColor(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    ORANGE = 4
    YELLOW = 5

class Side(Enum):
    FRONT = "Front"
    LEFT = "Left"
    RIGHT = "Right"
    BACK = "Back"
    TOP = "Top"
    BOTTOM = "Bottom"

class FaceNum(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    ORANGE = 4
    YELLOW = 5

class RubixCube:

    def __init__(self):
        self.front_face = Face(Color.ORANGE, FaceNum.ORANGE, Side.FRONT)
        self.top_face = Face(Color.WHITE, FaceNum.WHITE, Side.TOP)
        self.bottom_face = Face(Color.YELLOW, FaceNum.YELLOW, Side.BOTTOM)
        self.back_face = Face(Color.RED, FaceNum.RED, Side.BACK)
        self.left_face = Face(Color.BLUE, FaceNum.BLUE, Side.LEFT)
        self.right_face = Face(Color.GREEN, FaceNum.GREEN, Side.RIGHT)
        self.cube = self.init_solved_cube()

    def init_solved_cube(self):
        rubix_cube = [None]*6
        rubix_cube[FaceNum.RED.value] = self.back_face
        rubix_cube[FaceNum.GREEN.value] = self.right_face
        rubix_cube[FaceNum.BLUE.value] = self.left_face
        rubix_cube[FaceNum.WHITE.value] = self.top_face
        rubix_cube[FaceNum.ORANGE.value] = self.front_face
        rubix_cube[FaceNum.YELLOW.value] = self.bottom_face
        return rubix_cube

    def turn_side(self, side, clockwise):
        '''
        Turns a face of the cube clockwise or counter-clockwise.

        :param Side side: The face that you want to turn
        :param boolean clockwise: Whether the turn is clockwise or counter-clockwise
        :return: None
        '''
        if side == Side.FRONT:
            self.turn_front_side(clockwise)
        elif side == Side.BACK:
            self.turn_back_side(clockwise)
        elif side == Side.BOTTOM:
            self.turn_bottom_side(clockwise)
        elif side == Side.TOP:
            self.turn_top_side(clockwise)
        elif side == Side.LEFT:
            self.turn_left_side(clockwise)
        elif side == Side.RIGHT:
            self.turn_right_side(clockwise)
        else:
            print("Invalid side \"" + side + "\" given. To turn Front side, use Side.FRONT.")

    def turn_front_side(self, clockwise):
        pass

    def turn_back_side(self, clockwise):
        if clockwise:
            top_face = self.top_face.face_color
            right_face = self.right_face
            #self.set_piece_color(top_face, )
    def turn_left_side(self, clockwise):
        pass
    def turn_right_side(self, clockwise):
        pass
    def turn_top_side(self, clockwise):
        pass
    def turn_bottom_side(self, clockwise):
        pass



    def __str__(self):
        return   str(self.back_face) + "\n" \
               + str(self.top_face) + "\n" \
               + self.left_front_right_tostring() + "\n" \
               + str(self.bottom_face)

    def left_front_right_tostring(self):
        str = ""
        for k in range(self.left_face.num_rows):
            for i in range(3):
                #formatted output
                if i > 0:
                    str+= " "
                for j in range(self.left_face.num_columns):
                    #printing left face
                    if i == 0: str+= COLOR_MAP[self.left_face.array[k][j]] + "  " + bg.rs + " "
                    #printing front face
                    if i == 1: str+= COLOR_MAP[self.front_face.array[k][j]] + "  " + bg.rs + " "
                    if i == 2:
                        str+= COLOR_MAP[self.right_face.array[k][j]] + "  " + bg.rs + " "
                        # last element in row
                        if j == 2:
                            str+= "\n\n"
               
        return str  

   
    def set_piece_color(self, face, i, j, color):
        '''
        Set the color of a piece on the cube.

        :param FaceNum face: The face that you are targeting
        :param int i: The row on that face
        :param int j: The column on that face
        :param str color: The color you want to set this piece to
        :return: None
        '''
        self.cube[face.value].array[i][j] = color

class Face:
    def __init__(self, output_color, face_color, side):
        #Type sty
        self.output_color = output_color

        #Type FaceNum
        self.face_color = face_color

        #Type Side
        self.side = side
        self.num_rows = 3
        self.num_columns = 3
        self.array = [[colors[self.face_color.value] for k in range(3)] for j in range(3)]

    def __str__(self):
        final_str = ""
        # formatting output-- need extra spaces before printing each line if one of these sides
        for i in range(self.num_rows):
            if self.side.value == "Back" or self.side.value == "Bottom" or self.side.value == "Top":
                final_str += " "*10
            for j in range(self.num_columns):
                final_str += COLOR_MAP[self.array[i][j]] + "  " + bg.rs + " "
            final_str += "\n\n"

        return final_str

class Piece:
    def __init__(self):
        self.center = None


rubix = RubixCube()
rubix.set_piece_color(FaceNum.ORANGE, 1, 1, "Red")
print(rubix)
rubix.turn_front_side(True)
#rubix.turn_side(Side.FRONT, True)
#rubix.turn_side(Side.FRONT, True)
#print(rubix.cube[FaceNum.ORANGE.value])
#print(rubix.cube[FaceNum.WHITE.value].array)
#print(str(rubix.cube[FaceNum.GREEN.value][0][0]) + "Should be: "+ str(FaceNum.GREEN.value))
