from .tile_master import TileMaster

class MatchTwo (TileMaster):
    tiles = []

    def __init__(self, tiles = 4):
        self.tiles = [None] + [{"image": f"tiles\\{x+1:02}.png", "group": int((x+1)/2+0.5)} for x in range(tiles)]
    
    def evaluate(self, positions: tuple()) -> tuple():
        # Initialize output
        size = len(positions)
        indication = [0] * size
        terminal = False

        group = None
        for i in range(size):
            pos = positions[i]
            tile = self.tiles[pos]
            if tile is not None:
                if group is None:
                    group = tile.get("group")
                    indication[i] = 1 # Accept
                elif group != tile.get("group"):
                    indication[i] = 2 # Rejected
                else:
                    indication[i] = 1 # Accept
                    terminal = True # Win
        
        return tuple(indication), terminal