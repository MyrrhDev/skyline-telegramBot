import random
import pickle


class Skyline:
    # variables donde se asignan edificios
    area = 0
    max_height = 0

    xmin = 0
    height = []
    width = []
    x_pos = []
    xmax = 0

    def __init__(self, xmin, height, xmax):
        self.xmin = xmin
        self.height = [height] * ((xmax - xmin) + 1)
        self.xmax = xmax
        self.area = (xmax - xmin) * height
        self.max_height = height
        times = self.xmax - self.xmin
        width_array = [1.0] * times
        width_array.append(-0.5)
        self.width = width_array

    # Devuelve una lista para hacer el plot de la(s) alturas del skyline
    def get_height(self):
        return self.height

    # Devuelve una lista para hacer el plot de las posicion en el eje x
    # e.g. [1, 2, 3]
    def get_x_pos(self):
        if len(self.x_pos) == 0:
            return list(range(self.xmin, self.xmax + 1))
        else:
            return self.x_pos

    def get_width(self):
        return self.width

    def get_area(self):
        return self.area

    def get_max_height(self):
        return self.max_height

    # Cargar skyline en un archivo "[id].sky"
    def load_sky(self, name):
        with open(name + '.sky', 'rb') as f:
            return pickle.load(f)

    # Guardar skyline en un archivo "[id].sky"
    def save_sky(self, obj, name):
        with open(name + '.sky', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    # Update tabla de simbolos context
    # TODO: value or self???????
    def update_symbols(name_id, ts_dict, value):
        ts_dict[name_id] = value
        return ts_dict

    # Retorna type = NoneType si no encuentra el simbolo en la ts
    # sino, retorna el valor
    def find_symbol(name_id, ts_dict):
        if name_id in ts_dict:
            return ts_dict[name_id]

    # Functions:

    # Mover el skyline a la derecha
    def move_right(self, N):
        self.xmin += N
        self.xmax += N

    # Mover el skyline a la izquierda
    # Verificar que xmin no se coniverta en NEGATIVO!!! (??)
    # igual antes de mandarloa  eso....asi que en bot.py
    # aqui confiamos
    def move_left(self, N):
        self.xmin -= N
        self.xmax -= N

    # replicacion del mismo skyline
    def multiply_N(self, N):
        mul_heights = self.get_height().copy()
        mul_width = self.get_width().copy()

        # Calcular nuevas x_coords:
        mul_x_pos = self.get_x_pos().copy()
        size = len(mul_x_pos)
        m_min = m_max = self.xmax

        for i in range(N - 1):
            m_min = m_max
            m_max = m_max + size - 1
            mul_x_pos += list(range(m_min, m_max + 1))

        return (mul_x_pos, mul_heights * N, mul_width * N)

    def sm_calculate_width(self, x_pos_mn, x_pos_mx, s_width):
        times = x_pos_mx - x_pos_mn
        sp_width = [s_width] * times
        sp_width.append(-0.5)
        return sp_width

    def sm_modify_heights(self, l_heights, i, j, s_height):
        while i < j:
            if (s_height > l_heights[i]):
                l_heights[i] = s_height
            i += 1
        return l_heights

    # *********
    # Suma una skyline

    def sumar_skyline(self, s_xmin, s_height, s_xmax, s_width=1):
        sum_x_pos = []
        sum_heights = []
        sum_width = []

        # separado, izq o der:
        if ((s_xmin < self.xmin and s_xmax < self.xmin) or (s_xmin > self.xmax and s_xmax > self.xmax)):
            # datos individuales
            sp_height = [s_height] * ((s_xmax - s_xmin) + 1)
            sp_width = self.sm_calculate_width(s_xmin, s_xmax, s_width)

            # left add
            if (s_xmin < self.xmin and s_xmax < self.xmin):
                # orden y rellenar de 0's
                print("Here s")
                diff = ((self.xmax - s_xmin) + 1) - len(sp_height) - len(self.get_height())
                sp_cero_fill = [0] * diff
                sum_x_pos = list(range(s_xmin, self.xmax + 1))
                sum_heights = sp_height + sp_cero_fill + self.get_height()
                sum_width = sp_width + sp_cero_fill + self.get_width()
            # right add
            elif (s_xmin > self.xmax and s_xmax > self.xmax):
                print("Here dbdb")
                # orden y rellenar de 0's
                diff = ((s_xmax - self.xmin) + 1) - len(sp_height) - len(self.get_height())
                sp_cero_fill = [0] * diff

                sum_x_pos = list(range(self.xmin, s_xmax + 1))
                sum_heights = self.get_height() + sp_cero_fill + sp_height
                sum_width = self.get_width() + sp_cero_fill + sp_width

        # completamente adentro
        elif (s_xmin >= self.xmin and s_xmax <= self.xmax):
            sum_heights = self.get_height()
            print("in add")
            sum_x_pos = self.get_x_pos()
            i = sum_x_pos.index(s_xmin)
            j = sum_x_pos.index(s_xmax)
            sum_heights = self.sm_modify_heights(sum_heights, i, j, s_height)
            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        # completamente afuera
        elif (s_xmin < self.xmin and s_xmax > self.xmax):
            sp_height = self.get_height().copy()
            print("old: ", sp_height)
            sum_heights = [s_height] * ((s_xmax - s_xmin) + 1)
            print("new: ", sum_heights)

            print("in add")
            sum_x_pos = list(range(s_xmin, s_xmax + 1))
            i = sum_x_pos.index(self.xmin)
            j = sum_x_pos.index(self.xmax)

            k = 0
            while i < j:
                if (sp_height[k] > sum_heights[i]):
                    sum_heights[i] = sp_height[k]
                i += 1
                k += 1

            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        # solo uno adentro
        elif ((s_xmin < self.xmin and s_xmax <= self.xmax) or (s_xmin >= self.xmin and s_xmax > self.xmax)):
            sum_heights = self.get_height()
            if ((s_xmin < self.xmin) and (s_xmax <= self.xmax)):
                # left add
                sum_x_pos = list(range(s_xmin, self.xmax + 1))
                s_fill = len(sum_x_pos) - len(sum_heights)
                zero = [0] * s_fill
                sum_heights = zero + sum_heights
                print("left add")
                i = sum_x_pos.index(s_xmin)
                j = sum_x_pos.index(s_xmax)
                sum_heights = self.sm_modify_heights(sum_heights, i, j + 1, s_height)

            else:
                print("right add")
                sum_x_pos = list(range(self.xmin, s_xmax + 1))
                s_fill = len(sum_x_pos) - len(sum_heights)
                zero = [0] * s_fill
                sum_heights = sum_heights + zero
                i = sum_x_pos.index(s_xmin)
                j = sum_x_pos.index(s_xmax)
                sum_heights = self.sm_modify_heights(sum_heights, i, j + 1, s_height)

            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        return (sum_x_pos, sum_heights, sum_width)

    # Crea un skyline de la informacion de lists
    def c_skyline(self, c_x_pos, c_heights, c_width):
        self.xmin = c_x_pos[0]
        self.height = c_heights
        self.xmax = c_x_pos[-1]
        self.x_pos = c_x_pos
        self.area = (self.xmax - self.xmin) * self.height
        self.max_height = max(c_heights)
        self.width = c_width

    def inter_skyline(self, s_xmin, s_height, s_xmax):
        sum_x_pos = []

        # completamente adentro
        if (self.xmin <= s_xmin and s_xmax <= self.xmax):
            sum_x_pos = list(range(s_xmin, s_xmax + 1))
            print(sum_x_pos)
        # left out
        elif ((s_xmin < self.xmin) and (s_xmax <= self.xmax)):
            sum_x_pos = list(range(self.xmin, s_xmax + 1))
            print(sum_x_pos)
        # right out
        elif ((s_xmin >= self.xmin) and (s_xmax > self.xmax)):
            sum_x_pos = list(range(s_xmin, self.xmax + 1))
            print(sum_x_pos)

        sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], 1)

        sum_heights = self.get_height()
        print(sum_x_pos)
        print(sum_heights)
        i = sum_x_pos.index(sum_x_pos[0])
        j = sum_x_pos.index(sum_x_pos[-1])
        sum_heights = sum_heights[i:j + 1]

        print(sum_heights)
        x = 0
        while x < len(sum_heights):
            if (sum_heights[x] > s_height):
                sum_heights[x] = s_height
            x += 1

        return (sum_x_pos, sum_heights, sum_width)

    def reflect_skyline(self):
        # cambia heights
        reflect_heights = self.get_height().copy()
        reflect_heights.reverse()
        print(self.get_height())
        print(reflect_heights)
        reflect_heights.pop(0)
        reflect_heights.append(reflect_heights[-1])

        r_width = self.get_width().copy()
        r_x_pos = self.get_x_pos().copy()

        return (r_x_pos, reflect_heights, r_width)

    # n - numero de edificios creados
    # h - una altura de 0 a h aleatoria
    # w - una width de 1 a w aleatoria
    # xmin, xmax - una posicion de inicio/final entre xmin, xmax
    def random_skylines(self, n, h, w, xmin, xmax):
        # creamos un primero
        rd_x_pos = []
        rd_heights_list = []
        width_array = []

        rd_xmin = random.randint(xmin, xmax - 1)
        rd_xmax = random.randint(rd_xmin + 1, xmax)
        rd_x_pos = list(range(rd_xmin, rd_xmax + 1))
        # print(rd_x_pos)
        rd_height = random.randint(0, h)
        # print("height: ", rd_height)
        rd_heights_list = [rd_height] * ((rd_xmax - rd_xmin) + 1)
        # print(rd_heights_list)
        rd_width = random.randint(1, w)
        times = rd_xmax - rd_xmin
        width_array = [rd_width] * times
        width_array.append(-0.5)
        # print(width_array)

        self.c_skyline(rd_x_pos, rd_heights_list, width_array)

        i = 0
        while i < n - 1:
            rd_xmin = random.randint(xmin, xmax - 1)
            rd_xmax = random.randint(rd_xmin + 1, xmax)
            rd_height = random.randint(0, h)
            rd_width = random.randint(1, w)
            # print("attributes: ", rd_xmin, rd_height, rd_xmax, rd_width)
            (rd_x_pos, rd_heights_list, rd_width_array) = self.sumar_skyline(rd_xmin, rd_height, rd_xmax, rd_width)
            # print(rd_x_pos, rd_heights_list, rd_width_array)
            self.c_skyline(rd_x_pos, rd_heights_list, rd_width_array)
            i += 1

        return (rd_x_pos, rd_heights_list, rd_width_array)

    # recalcular el area
    def calcula_area(self, n_min, n_max):
        n_area = (n_max - n_min) * self.height
        self.area += n_area
