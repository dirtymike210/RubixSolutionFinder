class Cube:
    corners = None  # A corner is a triple of color values interpreted as the color visible along the x-, y-, and z-axes, respectively
    edges = None  # An edge is a pair of color values interpreted with order of precedence: x-, y-, z- axes
    # The index of a corner or edge in its respective array determines its position on the cube. Its orientation in that position is determined by the order of its colors.
    # X axis: White and Yellow
    # Y axis: Blue and Green
    # Z axis: Red and Orange

    def __init__(self):
        # Set corners and edges in "completed" positions and orientations
        self.corners = [
            ("w", "b", "r"),  # 0
            ("w", "b", "o"),  # 1
            ("w", "g", "r"),  # 2
            ("w", "g", "o"),  # 3
            ("y", "b", "r"),  # 4
            ("y", "b", "o"),  # 5
            ("y", "g", "r"),  # 6
            ("y", "g", "o"),  # 7
        ]
        self.edges = [
            ("w", "b"),  # 0
            ("w", "g"),  # 1
            ("w", "r"),  # 2
            ("w", "o"),  # 3
            ("y", "b"),  # 4
            ("y", "g"),  # 5
            ("y", "r"),  # 6
            ("y", "o"),  # 7
            ("b", "r"),  # 8
            ("b", "o"),  # 9
            ("g", "r"),  # 10
            ("g", "o"),  # 11
        ]

    def show_state(self):
        white = (
            self.corners[0][0]
            + " "
            + self.edges[0][0]
            + " "
            + self.corners[1][0]
            + "\n"
            + self.edges[2][0]
            + " w "
            + self.edges[3][0]
            + "\n"
            + self.corners[2][0]
            + " "
            + self.edges[1][0]
            + " "
            + self.corners[3][0]
            + "\n"
        )

        blue = (
            self.corners[4][1]
            + " "
            + self.edges[4][1]
            + " "
            + self.corners[5][1]
            + "\n"
            + self.edges[8][0]
            + " b "
            + self.edges[9][0]
            + "\n"
            + self.corners[0][1]
            + " "
            + self.edges[0][1]
            + " "
            + self.corners[1][1]
            + "\n"
        )

        red = (
            self.corners[4][2]
            + " "
            + self.edges[8][1]
            + " "
            + self.corners[0][2]
            + "\n"
            + self.edges[6][1]
            + " r "
            + self.edges[2][1]
            + "\n"
            + self.corners[6][2]
            + " "
            + self.edges[10][1]
            + " "
            + self.corners[2][2]
            + "\n"
        )
        yellow = (
            self.corners[5][0]
            + " "
            + self.edges[4][0]
            + " "
            + self.corners[4][0]
            + "\n"
            + self.edges[7][0]
            + " y "
            + self.edges[6][0]
            + "\n"
            + self.corners[7][0]
            + " "
            + self.edges[5][0]
            + " "
            + self.corners[6][0]
            + "\n"
        )

        green = (
            self.corners[2][1]
            + " "
            + self.edges[1][1]
            + " "
            + self.corners[3][1]
            + "\n"
            + self.edges[10][0]
            + " g "
            + self.edges[11][0]
            + "\n"
            + self.corners[6][1]
            + " "
            + self.edges[5][1]
            + " "
            + self.corners[7][1]
            + "\n"
        )

        orange = (
            self.corners[1][2]
            + " "
            + self.edges[9][1]
            + " "
            + self.corners[5][2]
            + "\n"
            + self.edges[3][1]
            + " o "
            + self.edges[7][1]
            + "\n"
            + self.corners[3][2]
            + " "
            + self.edges[11][1]
            + " "
            + self.corners[7][2]
            + "\n"
        )
        print(
            white
            + "\n"
            + blue
            + "\n"
            + red
            + "\n"
            + yellow
            + "\n"
            + green
            + "\n"
            + orange
        )

    def move(self, action):
        face = int(action / 2)  # Which face to rotate
        dir = action % 2  # Which direction to rotate the face
        if face == 0:  # White
            if dir == 0:  # CW
                self.corners = [
                    (self.corners[2][0], self.corners[2][2], self.corners[2][1]),
                    (self.corners[0][0], self.corners[0][2], self.corners[0][1]),
                    (self.corners[3][0], self.corners[3][2], self.corners[3][1]),
                    (self.corners[1][0], self.corners[1][2], self.corners[1][1]),
                ] + self.corners[4:]
                self.edges = [
                    self.edges[2],
                    self.edges[3],
                    self.edges[1],
                    self.edges[0],
                ] + self.edges[4:]
            else:  # CCW
                self.corners = [
                    (self.corners[1][0], self.corners[1][2], self.corners[1][1]),
                    (self.corners[3][0], self.corners[3][2], self.corners[3][1]),
                    (self.corners[0][0], self.corners[0][2], self.corners[0][1]),
                    (self.corners[2][0], self.corners[2][2], self.corners[2][1]),
                ] + self.corners[4:]
                self.edges = [
                    self.edges[3],
                    self.edges[2],
                    self.edges[0],
                    self.edges[1],
                ] + self.edges[4:]
        elif face == 1:  # Blue
            if dir == 0:
                self.corners = (
                    [
                        (self.corners[1][2], self.corners[1][1], self.corners[1][0]),
                        (self.corners[5][2], self.corners[5][1], self.corners[5][0]),
                    ]
                    + self.corners[2:4]
                    + [
                        (self.corners[0][2], self.corners[0][1], self.corners[0][0]),
                        (self.corners[4][2], self.corners[4][1], self.corners[4][0]),
                    ]
                    + self.corners[6:]
                )
                self.edges = (
                    [(self.edges[9][1], self.edges[9][0])]
                    + self.edges[1:4]
                    + [(self.edges[8][1], self.edges[8][0])]
                    + self.edges[5:8]
                    + [
                        (self.edges[0][1], self.edges[0][0]),
                        (self.edges[4][1], self.edges[4][0]),
                    ]
                    + self.edges[10:]
                )
            else:
                self.corners = (
                    [
                        (self.corners[4][2], self.corners[4][1], self.corners[4][0]),
                        (self.corners[0][2], self.corners[0][1], self.corners[0][0]),
                    ]
                    + self.corners[2:4]
                    + [
                        (self.corners[5][2], self.corners[5][1], self.corners[5][0]),
                        (self.corners[1][2], self.corners[1][1], self.corners[1][0]),
                    ]
                    + self.corners[6:]
                )
                self.edges = (
                    [(self.edges[8][1], self.edges[8][0])]
                    + self.edges[1:4]
                    + [(self.edges[9][1], self.edges[9][0])]
                    + self.edges[5:8]
                    + [
                        (self.edges[4][1], self.edges[4][0]),
                        (self.edges[0][1], self.edges[0][0]),
                    ]
                    + self.edges[10:]
                )
        elif face == 2:  # Red
            if dir == 0:
                self.corners = [
                    (self.corners[4][1], self.corners[4][0], self.corners[4][2]),
                    self.corners[1],
                    (self.corners[0][1], self.corners[0][0], self.corners[0][2]),
                    self.corners[3],
                    (self.corners[6][1], self.corners[6][0], self.corners[6][2]),
                    self.corners[5],
                    (self.corners[2][1], self.corners[2][0], self.corners[2][2]),
                    self.corners[7],
                ]
                self.edges = (
                    self.edges[0:2]
                    + [self.edges[8]]
                    + self.edges[3:6]
                    + [
                        self.edges[10],
                        self.edges[7],
                        self.edges[6],
                        self.edges[9],
                        self.edges[2],
                        self.edges[11],
                    ]
                )
            else:
                self.corners = [
                    (self.corners[2][1], self.corners[2][0], self.corners[2][2]),
                    self.corners[1],
                    (self.corners[6][1], self.corners[6][0], self.corners[6][2]),
                    self.corners[3],
                    (self.corners[0][1], self.corners[0][0], self.corners[0][2]),
                    self.corners[5],
                    (self.corners[4][1], self.corners[4][0], self.corners[4][2]),
                    self.corners[7],
                ]
                self.edges = (
                    self.edges[0:2]
                    + [self.edges[10]]
                    + self.edges[3:6]
                    + [
                        self.edges[8],
                        self.edges[7],
                        self.edges[2],
                        self.edges[9],
                        self.edges[6],
                        self.edges[11],
                    ]
                )
        elif face == 3:  # Yellow
            if dir == 0:
                self.corners = self.corners[0:4] + [
                    (self.corners[5][0], self.corners[5][2], self.corners[5][1]),
                    (self.corners[7][0], self.corners[7][2], self.corners[7][1]),
                    (self.corners[4][0], self.corners[4][2], self.corners[4][1]),
                    (self.corners[6][0], self.corners[6][2], self.corners[6][1]),
                ]
                self.edges = (
                    self.edges[0:4]
                    + [self.edges[7], self.edges[6], self.edges[4], self.edges[5]]
                    + self.edges[8:]
                )
            else:
                self.corners = self.corners[0:4] + [
                    (self.corners[6][0], self.corners[6][2], self.corners[6][1]),
                    (self.corners[4][0], self.corners[4][2], self.corners[4][1]),
                    (self.corners[7][0], self.corners[7][2], self.corners[7][1]),
                    (self.corners[5][0], self.corners[5][2], self.corners[5][1]),
                ]
                self.edges = (
                    self.edges[0:4]
                    + [self.edges[6], self.edges[7], self.edges[5], self.edges[4]]
                    + self.edges[8:]
                )
        elif face == 4:  # Green
            if dir == 0:
                self.corners = (
                    self.corners[0:2]
                    + [
                        (self.corners[6][2], self.corners[6][1], self.corners[6][0]),
                        (self.corners[2][2], self.corners[2][1], self.corners[2][0]),
                    ]
                    + self.corners[4:6]
                    + [
                        (self.corners[7][2], self.corners[7][1], self.corners[7][0]),
                        (self.corners[3][2], self.corners[3][1], self.corners[3][0]),
                    ]
                )
                self.edges = (
                    [self.edges[0], (self.edges[10][1], self.edges[10][0])]
                    + self.edges[2:5]
                    + [(self.edges[11][1], self.edges[11][0])]
                    + self.edges[6:10]
                    + [
                        (self.edges[5][1], self.edges[5][0]),
                        (self.edges[1][1], self.edges[1][0]),
                    ]
                )
            else:
                self.corners = (
                    self.corners[0:2]
                    + [
                        (self.corners[3][2], self.corners[3][1], self.corners[3][0]),
                        (self.corners[7][2], self.corners[7][1], self.corners[7][0]),
                    ]
                    + self.corners[4:6]
                    + [
                        (self.corners[2][2], self.corners[2][1], self.corners[2][0]),
                        (self.corners[6][2], self.corners[6][1], self.corners[6][0]),
                    ]
                )
                self.edges = (
                    [self.edges[0], (self.edges[11][1], self.edges[11][0])]
                    + self.edges[2:5]
                    + [(self.edges[10][1], self.edges[10][0])]
                    + self.edges[6:10]
                    + [
                        (self.edges[1][1], self.edges[1][0]),
                        (self.edges[5][1], self.edges[5][0]),
                    ]
                )
        else:  # Orange
            if dir == 0:
                self.corners = [
                    self.corners[0],
                    (self.corners[3][1], self.corners[3][0], self.corners[3][2]),
                    self.corners[2],
                    (self.corners[7][1], self.corners[7][0], self.corners[7][2]),
                    self.corners[4],
                    (self.corners[1][1], self.corners[1][0], self.corners[1][2]),
                    self.corners[6],
                    (self.corners[5][1], self.corners[5][0], self.corners[5][2]),
                ]
                self.edges = self.edges[0:3] + [(self.edges[11])] + self.edges[4:7] + [self.edges[9], self.edges[8], self.edges[3], self.edges[10], self.edges[7]]
            else:
                self.corners = [
                    self.corners[0],
                    (self.corners[5][1], self.corners[5][0], self.corners[5][2]),
                    self.corners[2],
                    (self.corners[1][1], self.corners[1][0], self.corners[1][2]),
                    self.corners[4],
                    (self.corners[7][1], self.corners[7][0], self.corners[7][2]),
                    self.corners[6],
                    (self.corners[3][1], self.corners[3][0], self.corners[3][2]),
                ]
                self.edges = self.edges[0:3] + [(self.edges[9])] + self.edges[4:7] + [self.edges[11], self.edges[8], self.edges[7], self.edges[10], self.edges[3]]

    def getStateIndex(self):
        pass


cube = Cube()
cube.move(10)
cube.move(11)
cube.show_state()
