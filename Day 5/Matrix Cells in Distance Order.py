class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = []
        for i in range(R):
            for j in range(C):
                cells.append((i,j))
        # print(cells)
        dist_dict = {}
        for cell in cells:
            d = abs(r0-cell[0]) + abs(c0 - cell[1])
            if cell not in dist_dict:
                dist_dict[cell] = d
        # print(dist_dict)
        sort_dict = sorted(dist_dict.items() ,key= lambda x:x[1])
        # print(sort_dict)
        rlst = []
        for el in sort_dict:
            # print(el)
            rlst.append([el[0][0],el[0][1]])
          
        return rlst
