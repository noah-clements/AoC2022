from abc import ABC
import logging

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

class Rock(ABC):
    RWALL_X=8
    LWALL_X=0
    MIN_Y=0

    _cavern = {}
    
    def __init__(self, current_y):
        self._bottom_y = current_y + 4
        self._rock_positions = []

    def fall(self):
        room_to_fall = True
        top_y = self._bottom_y - 4
        replacement_positions = []
        for position in self._rock_positions:
            x, y = position
            # Need to test for two below. Can only move one, but want to stop 1 above.
            test_pos = (x, y - 1) 
            if (test_pos in self._cavern 
                or not room_to_fall
                or not y-1 > Rock.MIN_Y):
                # self._cavern[position] = 'r'
                room_to_fall = False
                top_y = max(top_y, y)
            else:
                replacement_positions.append(test_pos)
                top_y = max(top_y, y-1)
        if room_to_fall:
            self._rock_positions = replacement_positions
        else:
            # Have to do this after the tests above and after top_y calc.
            for position in self._rock_positions:
                self._cavern[position] = 'r'
        # logging.debug(f'Fell. {type(self)}. {self._rock_positions}')
        # logging.debug(f'Still falling? {room_to_fall}')
        # if not room_to_fall:
        #     logging.debug(self._cavern)
        #     logging.debug(f'Top _y: {top_y}')
        return room_to_fall, top_y            

    def move_left(self):
        more_room = True
        replacement_positions = []
        for position in self._rock_positions:
            x, y = position
            test_pos = (x-1, y)
            if not x-1 > Rock.LWALL_X or test_pos in self._cavern:
                more_room = False
                break
            else:
                replacement_positions.append(test_pos)
        if more_room:
            self._rock_positions = replacement_positions
        # logging.debug(f'Moved Left(?) {type(self)}. {self._rock_positions}')


    def move_right(self):
        more_room = True
        replacement_positions = []
        for position in self._rock_positions:
            x, y = position
            test_pos = (x+1, y)
            if not x+1 < Rock.RWALL_X or test_pos in self._cavern:
                more_room = False
                break
            else:
                replacement_positions.append(test_pos)
        if more_room:
            self._rock_positions = replacement_positions
        # logging.debug(f'Moved Right(?) {type(self)}. {self._rock_positions}')

    @classmethod
    def reset_cavern(cls):
        cls._cavern = {}
        


class HorizontalRock(Rock):
    '''####'''
    def __init__(self, current_y):
        super().__init__(current_y)
        self._rock_positions = [(i, self._bottom_y) for i in range(3,7)]
        

class CrossRock(Rock):
    ''' .#.
        ###
        .#.'''
    def __init__(self, current_y):
        super().__init__(current_y)
        self._rock_positions = [(4, self._bottom_y), 
                                (3, self._bottom_y + 1),
                                (4, self._bottom_y + 1),
                                (5, self._bottom_y + 1),
                                (4, self._bottom_y + 2)]
        

class CornerRock(Rock):
    ''' ..#
        ..#
        ###'''
    def __init__(self, current_y):
        super().__init__(current_y)
        self._rock_positions = [(3, self._bottom_y), 
                                (4, self._bottom_y),
                                (5, self._bottom_y),
                                (5, self._bottom_y +1),
                                (5, self._bottom_y + 2)]
        

class VerticalRock(Rock):
    ''' #
        #
        # 
        # '''
    def __init__(self, current_y):
        super().__init__(current_y)
        self._rock_positions = [(3,i) for i in range (self._bottom_y, self._bottom_y+4)]
        

class BoxRock(Rock):
    ''' ##
        ##'''
    def __init__(self, current_y):
        super().__init__(current_y)
        self._rock_positions = [(3, self._bottom_y), (4, self._bottom_y),
                                (3, self._bottom_y+1), (4, self._bottom_y+1)]
        

class RockFactory():
    HORIZONTAL = 0
    CROSS = 1
    CORNER = 2
    VERTICAL = 3
    BOX = 4
    
    def __init__(self, next_rock=0):
        self._next_rock = next_rock

    def get_next_rock(self, current_y):
        # this_rock = None
        match self._next_rock:
            case self.HORIZONTAL:
                this_rock = HorizontalRock(current_y)
            case self.CROSS:
                this_rock = CrossRock(current_y)
            case self.CORNER:
                this_rock = CornerRock(current_y)
            case self.VERTICAL:
                this_rock = VerticalRock(current_y)
            case self.BOX:
                this_rock = BoxRock(current_y)
        # logging.debug(f'Creating next rock: {type(this_rock)} number: {self._next_rock}')            
        self._next_rock = ((self._next_rock + 1) % 5)
        return this_rock
