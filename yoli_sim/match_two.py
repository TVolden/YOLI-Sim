from yoli_sim import YoliTileGame, YoliTile

class MatchTwo (YoliTileGame):
    def __init__(self, tiles = 4):
        self._tiles = [{"image": f"{x:02}.png", "group": int((x)/2+0.5)} for x in range(1, tiles+1)]

    def tile_at(self, index:int) -> YoliTile:
        return YoliTile(f"{index}", self._tiles[index].get("image"))

    def count_tiles(self) -> int:
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
                    indication[i] = YoliTileGame.ACCEPTED
                elif group != tile.get("group"):
                    indication[i] = YoliTileGame.REJECTED
                else:
                    indication[i] = YoliTileGame.ACCEPTED
                    terminal = True # Win
        
        return tuple(indication), terminal