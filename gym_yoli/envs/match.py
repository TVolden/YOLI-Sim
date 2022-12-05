from .tile_master import TileMaster

class MatchTwo (TileMaster):
    def __init__(self, tiles = 4):
        self._tiles = [{"image": f"tiles\\{x+1:02}.png", "group": int((x+1)/2+0.5)} for x in range(tiles)]

    def tile_at(self, index:int) -> dict():
        return self._tiles[index]

    def tile_count(self) -> int:
        return len(self._tiles)

    def evaluate(self, board: tuple()) -> tuple():
        # Initialize output
        size = len(board)
        indication = [0] * size
        terminal = False

        group = None
        for i in range(size):
            index = board[i]
            if index is None:
                continue # No tile at this position
            
            tile = self._tiles[index]
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