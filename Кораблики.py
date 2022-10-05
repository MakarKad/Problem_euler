from random import randint, shuffle


class Ship:

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._cells = [1] * length

    def get_cells_coords(self):
        self_coords = [list(self.get_start_coords())]
        for i in range(0, self._length - 1):
            new_coord = self_coords[-1][:]
            if self._tp == 1:
                new_coord[0] += 1
            else:
                new_coord[1] += 1
            self_coords.append(new_coord)
        return self_coords

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def is_collide(self, ship):
        if self._x is None or ship._x is None:
            return True
        ship_coords = ship.get_cells_coords()
        self_coords = self.get_cells_coords()

        for i in self_coords:
            for j in ship_coords:
                if abs(i[0] - j[0]) <= 1 and abs(i[1] - j[1]) <= 1:
                    return True

        return False

    def is_out_pole(self, size):
        self_coords = self.get_cells_coords()
        for i in self_coords:
            if 0 <= i[0] <= size - 1 and 0 <= i[1] <= size - 1:
                continue
            else:
                return True
        return False

    def collide_ships(self, ships):
        if not ships and self._x is None:
            return True
        for i in ships:
            if self.is_collide(i):
                return True
        return False

    def move(self, go, pole=None):
        if pole is None:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go
            return True
        if self._tp == 1:
            sp1 = Ship(self._length, self._tp, self._x + go, self._y)
            if not sp1.collide_ships(pole._ships) and not sp1.is_out_pole(pole._size):
                sp1._x += go
                pole._pole[sp1._y][sp1._x: sp1._x + sp1._length] = sp1._cells
                pole._pole[sp1._y][sp1._x + sp1._length + go] = 0

                return True

        elif self._tp == 2:
            sp1 = Ship(self._length, self._tp, self._x, self._y + go)
            if not sp1.collide_ships(pole._ships) and not sp1.is_out_pole(pole._size):
                sp1._y += go
                it = iter(sp1._cells)
                for i in pole._pole[self._y: self._y + sp1._length]:
                    i[self._x] = next(it)
                pole._pole[self._y + go][self._x] = 0

                return True

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:

    def __init__(self, size=10):
        self._size = size
        self._pole = [[0] * self._size for i in range(self._size)]

    def init(self):
        self._ships = [Ship(i, tp=randint(1, 2)) for i in [4] + [3] * 2 + [2] * 3 + [1] * 4]
        done_ships = []
        for ship in self._ships:
            if ship._tp == 1:
                while ship.collide_ships(done_ships):
                    x = randint(0, self._size - ship._length)
                    y = randint(0, self._size - 1)
                    ship.set_start_coords(x, y)
                self._pole[y][x :x + ship._length] = ship._cells
            else:
                while ship.collide_ships(done_ships):
                    x = randint(0, self._size - 1)
                    y = randint(0, self._size - ship._length)
                    ship.set_start_coords(x, y)
                it = iter(ship._cells)
                for i in self._pole[y: y + ship._length]:
                    i[x] = next(it)
            done_ships.append(ship)
        self._ships = done_ships

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for i in self._ships:
            if i._cells == [1] * i._length:
                if i.move(1, self):
                    i.move(1, self)
                else:
                    i.move(-1, self)

    def show(self):
        for i in self._pole:
            print(*i)

    def get_pole(self):
        return tuple((tuple(i) for i in self._pole))


class SeaBattle:

    def __init__(self, pole, enemy_pole):
        self._game_pole = pole
        self._bot_pole = enemy_pole
        self._game_shoot_pole = [[0] * self._bot_pole._size for i in range(self._bot_pole._size)]
        self._bot_shoot_cells = []
        self._done_cells_bot = [(None, None)]
        self._done_cells_game = [(None, None)]

    @staticmethod
    def _check_ships(pole):
        for i in pole._ships:
            if i._cells == [0] * i._length:
                print('\nЗнищений корабель')
                pole._ships.remove(i)
                return None

    def bot_shoot(self):
        x, y = None, None

        coords = []

        if len(self._bot_shoot_cells) == 0:
            while (x, y) in self._done_cells_bot:
                x = randint(0, len(self._game_pole._pole) - 1)
                y = randint(0, len(self._game_pole._pole) - 1)

        elif len(self._bot_shoot_cells) == 1:
            x1 = self._bot_shoot_cells[0][0] + 1
            x2 = self._bot_shoot_cells[0][0] - 1
            y = self._bot_shoot_cells[0][1]
            coords.append((x1, y))
            coords.append((x2, y))

            y1 = self._bot_shoot_cells[0][1] + 1
            y2 = self._bot_shoot_cells[0][1] - 1
            x = self._bot_shoot_cells[0][0]
            coords.append((x, y1))
            coords.append((x, y2))

            shuffle(coords)

            for i in coords:
                ch1 = (i[0], i[1]) not in self._done_cells_bot
                ch2 = 0 <= i[0] <= len(self._game_pole._pole)
                ch3 = 0 <= i[1] <= len(self._game_pole._pole)
                if ch1 and ch2 and ch3:
                    x, y = i
                    break

        else:
            if self._bot_shoot_cells[0][0] == self._bot_shoot_cells[1][0]:
                y1 = max([i[1] for i in self._bot_shoot_cells]) + 1
                y2 = min([i[1] for i in self._bot_shoot_cells]) - 1
                x = self._bot_shoot_cells[0][0]
                coords.append((x, y1))
                coords.append((x, y2))
            else:
                x1 = min([i[0] for i in self._bot_shoot_cells]) - 1
                x2 = max([i[0] for i in self._bot_shoot_cells]) + 1
                y = self._bot_shoot_cells[0][0]
                coords.append((x1, y))
                coords.append((x2, y))

            shuffle(coords)

            for i in coords:
                ch1 = (i[0], i[1]) not in self._done_cells_bot
                ch2 = 0 <= i[0] <= len(self._game_pole._pole)
                ch3 = 0 <= i[1] <= len(self._game_pole._pole)
                if ch1 and ch2 and ch3:
                    x, y = i
                    break

        self._done_cells_bot.append((x, y))

        if self._game_pole._pole[y][x] == 1:
            self._bot_shoot_cells.append((x, y))

            self._game_pole._pole[y][x] = 'Х'
            for i in self._game_pole._ships:
                try:
                    i._cells[i.get_cells_coords().index([x, y])] = 0
                    break
                except ValueError:
                    continue

            print('\nПоле попаданий по боту:           Поле попадание по вам\n')
            for i, j in zip(self._game_shoot_pole, self._game_pole._pole):
                print(*i, end='               ')
                print(*j)

            print('Бот влучив')
            old_len = len(self._game_pole._ships)
            self._check_ships(self._game_pole)
            if old_len > len(self._game_pole._ships):
                self._bot_shoot_cells.clear()
            if len(self._game_pole._ships) == 0:
                print('\nБот переміг')
                return None

            self.bot_shoot()

        else:
            self._game_pole._pole[y][x] = 'П'

            print('\nПоле попаданий по боту:           Поле попадание по вам\n')
            for i, j in zip(self._game_shoot_pole, self._game_pole._pole):
                print(*i, end='               ')
                print(*j)

            print('\nБот промахнувся')

            self.shoot()

    def shoot(self):
        print('\nПоле попаданий по боту:           Поле попадание по вам:\n')
        for i, j in zip(self._game_shoot_pole, self._game_pole._pole):
            print(*i, end='               ')
            print(*j)

        x, y = map(int, input('Введіть координати: ').split())
        self._done_cells_game.append((x, y))

        if self._bot_pole._pole[y][x] == 1 and (x, y) not in self._done_cells_game:
            self._game_shoot_pole[y][x] = 'Х'
            for i in self._bot_pole._ships:
                try:
                    i._cells[i.get_cells_coords().index([x, y])] = 0
                    break
                except ValueError:
                    continue
            print('Влучив')
            self._check_ships(self._bot_pole)
            if len(self._bot_pole._ships) == 0:
                print('\nВи перемогли')
                return None
            self.shoot()

        else:
            self._game_shoot_pole[y][x] = 'П'
            print('\nПромах лох')
            self.bot_shoot()




me = GamePole(10)
bot = GamePole(10)
battle = SeaBattle(me, bot)
me.init()
bot.init()
battle.shoot()
