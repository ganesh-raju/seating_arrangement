import pdb

class Seating:
    def __init__(self):
        self.aeroplane_seats = [[5,4], [4,5], [4,3], [3,4], [5,7], [4,1]]
        self.filled = 0
        self.number = 30
        self.row = 0
        self.tempFilled = -1

    def construct(self):
        seats = []
        for i in self.aeroplane_seats:
            rows = i[1]
            cols = i[0]
            mat = []
            for i in range(rows):
                mat.append([-1]*cols)
            seats.append(mat)
        #pdb.set_trace()
        return seats

    def printSeats(self, seats):
        blksize = len(str(self.number))
        rows = [x[1] for x in self.aeroplane_seats]
        cols = [x[0] for x in self.aeroplane_seats]
        maximum = max(rows)
        top = True
        for i in range(maximum):
            rowlist = []
            rowlistl = []
            for j in range(len(seats)):
                row = ' '
                rowl = ' '
                if len(seats[j]) <= i:
                    for k in range(cols[j]):
                        row += ' '*blksize
                        rowl += ' '*blksize
                        row += ' '
                        rowl += ' '
                else:
                    row = '|'
                    rowl = '+'
                    for k in seats[j][i]:
                        if k == -1:
                            row += ' '*blksize
                            rowl += '-'*blksize
                            row += '|'
                            rowl += '+'
                        else:
                            row += str(k)+(' '*(blksize - len(str(k))))
                            rowl += '-'*blksize
                            row += '|'
                            rowl += '+'
                
                rowlist.append(row)
                rowlistl.append(rowl)
            if top:
                print('    '.join(rowlistl))
                top = False
            print('    '.join(rowlist))
            print('    '.join(rowlistl))

                    
    def aisle_seats(self):
        self.filled = 0
        row = 0
        length = len(self.aeroplane_seats)
        self.tempFilled = -1
        while self.filled < self.number and self.filled != self.tempFilled:
            tempFilled = self.filled
            for i in range(len(self.aeroplane_seats)):
                if self.aeroplane_seats[i][1] > row:
                    if i == 0 and self.aeroplane_seats[i][0] > 1:
                        self.filled += 1
                        aisleCol = self.aeroplane_seats[i][0] - 1
                        seats[i][row][aisleCol] = self.filled
                        if self.filled >= self.number:
                            break
                    elif i == length - 1 and self.aeroplane_seats[i][0] > 1:
                        self.filled += 1
                        aisleCol = 0
                        seats[i][row][aisleCol] = self.filled
                        if self.filled >= self.number:
                            break
                    else:
                        self.filled += 1
                        aisleCol = 0
                        seats[i][row][aisleCol] = self.filled
                        if self.filled >= self.number:
                            break
                        if self.aeroplane_seats[i][0] > 1:
                            self.filled += 1
                            aisleCol = self.aeroplane_seats[i][0] - 1
                            seats[i][row][aisleCol] = self.filled
                            if self.filled >= self.number:
                                break
            row += 1


    def window_seats(self):
        row = 0
        self.filled = 0
        self.number = 0
        self.tempFilled = 0
        while self.filled < self.number and self.filled != self.tempFilled:
            self.tempFilled = self.filled
            if aeroplane_seats[0][1] > row:
                self.filled += 1
                window = 0
                seats[0][row][window] = self.filled
                if filled >= number:
                    break
            if self.aeroplane_seats[length-1][1] > row:
                self.filled += 1
                window = self.aeroplane_seats[length-1][0] - 1
                seats[length-1][row][window] = self.filled
                if self.filled >= self.number:
                    break
            row += 1

    def middle_seats(self):
        row = 0
        self.tempFilled = 0
        self.filled = 0
        while self.filled < self.number and self.filled != self.tempFilled:
            self.tempFilled = self.filled
            for i in range(length):
                if self.aeroplane_seats[i][1] > row:
                    if self.aeroplane_seats[i][0] > 2:
                        for col in range(1, self.aeroplane_seats[i][0] - 1):
                            self.filled += 1
                            seats[i][row][col] = self.filled
                            if self.filled >= self.number:
                                break
            row += 1


seating = Seating()

seats = seating.construct()
seating.aisle_seats()
seating.window_seats()
seating.middle_seats()
seating.printSeats(seats)