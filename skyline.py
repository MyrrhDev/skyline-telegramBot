import random


class Skyline:
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
        self.x_pos = list(range(xmin, xmax + 1))
        self.area = sum(self.height[:-1])
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
        return self.x_pos

    # Devuelve una lista para hacer el plot de las width
    def get_width(self):
        return self.width

    # Devuelve el valor acumulado del area del Skyline
    def get_area(self):
        return self.area

    # Devuelve el valor maximo de altura de un Skyline
    def get_max_height(self):
        return self.max_height

    # Update tabla de simbolos context
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
    def move_right(self, num):
        self.xmin = self.xmin + num
        self.xmax = self.xmax + num
        self.x_pos = [x + num for x in self.x_pos]

    # Mover el skyline a la izquierda
    def move_left(self, num):
        self.xmin = self.xmin - num
        self.xmax = self.xmax - num
        self.x_pos = [x - num for x in self.x_pos]

    # Replicacion del mismo skyline
    def multiply_n(self, n, num):
        mul_heights = self.get_height().copy()
        mul_width = self.get_width().copy()
        mul_x_pos = self.get_x_pos().copy()
        size = len(mul_x_pos)
        m_max = self.xmax
        for i in range(n - 1):
            m_min = m_max
            m_max = m_max + size - 1
            mul_x_pos += list(range(m_min, m_max + 1))

        mult_skl = Skyline(0, 0, 0)
        mult_skl.c_skyline(mul_x_pos, mul_heights * n, mul_width * n, num)
        return mult_skl

    def sm_calculate_width(self, x_pos_mn, x_pos_mx, s_width):
        times = x_pos_mx - x_pos_mn
        sp_width = [s_width] * times
        sp_width.append(-0.5)
        return sp_width

    def sm_modify_heights(self, l_heights, i, j, s_height):
        k = 0
        while i < j:
            if l_heights[i] < s_height[k]:
                l_heights[i] = s_height[k]
            i += 1
            k += 1
        return l_heights

    def clean_heights(self, x_pos, h_pos):
        n_he = {}
        for i, j in zip(x_pos, h_pos):
            n_he[i] = j
        return list(n_he.keys()), list(n_he.values())

    # Suma una skyline
    def sumar_skyline(self, sky_in, s_width=1):
        sum_x_pos = []
        sum_heights = []
        sum_width = []

        s_xmin = sky_in.xmin
        s_height = sky_in.height
        s_xmax = sky_in.xmax

        if s_xmin == 0 and s_xmax == 0 and s_height[0] == 0:
            return self

        if (s_xmin < self.xmin and s_xmax < self.xmin) or (s_xmin > self.xmax and s_xmax > self.xmax):
            sp_width = self.sm_calculate_width(s_xmin, s_xmax, s_width)

            # left add
            if s_xmin < self.xmin and s_xmax < self.xmin:
                diff = ((self.xmax - s_xmin) + 1) - len(s_height) - len(self.get_height())
                sp_cero_fill = [0] * diff
                sum_x_pos = list(range(s_xmin, self.xmax + 1))
                sum_heights = s_height + sp_cero_fill + self.get_height()
                sum_width = sp_width + sp_cero_fill + self.get_width()

            # right add
            elif s_xmin > self.xmax and s_xmax > self.xmax:
                diff = ((s_xmax - self.xmin) + 1) - len(s_height) - len(self.get_height())
                sp_cero_fill = [0] * diff
                sum_x_pos = list(range(self.xmin, s_xmax + 1))
                sum_heights = self.get_height() + sp_cero_fill + s_height
                sum_width = self.get_width() + sp_cero_fill + sp_width

        # completamente adentro
        elif s_xmin >= self.xmin and s_xmax <= self.xmax:
            sum_heights = self.get_height().copy()
            sum_x_pos = self.get_x_pos().copy()
            i = sum_x_pos.index(s_xmin)
            j = sum_x_pos.index(s_xmax)
            sum_heights = self.sm_modify_heights(sum_heights, i, j, s_height)
            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        # completamente afuera
        elif s_xmin < self.xmin and s_xmax > self.xmax:
            sp_height = self.get_height().copy()
            sum_heights = s_height.copy()
            sum_x_pos = list(range(s_xmin, s_xmax + 1))
            i = sum_x_pos.index(self.xmin)
            j = sum_x_pos.index(self.xmax)
            k = 0
            while i < j:
                if sp_height[k] > sum_heights[i]:
                    sum_heights[i] = sp_height[k]
                i += 1
                k += 1

            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        # solo uno adentro
        elif (s_xmin < self.xmin and s_xmax <= self.xmax) or (s_xmin >= self.xmin and s_xmax > self.xmax):
            sum_heights = self.get_height().copy()
            if (s_xmin < self.xmin) and (s_xmax <= self.xmax):
                # left add
                sum_x_pos = list(range(s_xmin, self.xmax + 1))
                s_fill = len(sum_x_pos) - len(sum_heights)
                zero = [0] * s_fill
                sum_heights = zero + sum_heights
                i = sum_x_pos.index(s_xmin)
                j = sum_x_pos.index(s_xmax)
                sum_heights = self.sm_modify_heights(sum_heights, i, j, s_height)

            else:
                sum_x_pos = list(range(self.xmin, s_xmax + 1))
                s_fill = len(sum_x_pos) - len(sum_heights)
                zero = [0] * s_fill
                k = -1
                p = self.xmax - s_xmin
                if s_height[p + 1] < sum_heights[-1]:
                    k = sum_x_pos.index(self.xmax)
                sum_heights = sum_heights + zero
                i = sum_x_pos.index(s_xmin)
                j = sum_x_pos.index(s_xmax)
                sum_heights = self.sm_modify_heights(sum_heights, i, j + 1, s_height)
                if k > -1:
                    sum_heights[k] = s_height[p]

            sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], s_width)

        new_sky_s = Skyline(0, 0, 0)
        new_sky_s.c_skyline(sum_x_pos, sum_heights, sum_width)
        return new_sky_s

    # Crea un skyline de la informacion de lists
    def c_skyline(self, c_x_pos, c_heights, c_width, m_num=-1, area=-1):
        self.xmin = c_x_pos[0]
        self.height = c_heights
        self.xmax = c_x_pos[-1]
        self.x_pos = c_x_pos
        if m_num > -1:
            self.area = sum(c_heights) - m_num
        elif area > -1:
            self.area = area
        else:
            self.area = sum(c_heights[:-1])
        self.max_height = max(c_heights)
        self.width = c_width

    def inter_skyline(self, inter_sky):
        sum_x_pos = []
        s_xmin = inter_sky.xmin
        s_height = inter_sky.height
        s_xmax = inter_sky.xmax

        if (self.xmin <= s_xmin) and (s_xmax <= self.xmax):
            sum_x_pos = list(range(s_xmin, s_xmax + 1))
            s_x_pos = inter_sky.get_x_pos().copy()
            (c_x_pos, s_height) = self.clean_heights(s_x_pos, s_height)
            r_ind_i = c_x_pos.index(s_xmin)
            r_ind_j = c_x_pos.index(s_xmax)
            s_height = s_height[r_ind_i:r_ind_j + 1]

        # left out
        elif (s_xmin < self.xmin) and (s_xmax <= self.xmax):
            sum_x_pos = list(range(self.xmin, s_xmax + 1))
            s_x_pos = inter_sky.get_x_pos().copy()
            (c_x_pos, s_height) = self.clean_heights(s_x_pos, s_height)
            l_ind = c_x_pos.index(self.xmin)
            s_height = s_height[l_ind:]

        # right out
        elif (s_xmin >= self.xmin) and (s_xmax > self.xmax):
            sum_x_pos = list(range(s_xmin, self.xmax + 1))
            s_x_pos = inter_sky.get_x_pos().copy()
            (c_x_pos, s_height) = self.clean_heights(s_x_pos, s_height)
            r_ind = c_x_pos.index(self.xmax)
            s_height = s_height[:r_ind + 1]
        else:
            sum_x_pos = list(range(self.xmin, self.xmax + 1))
            s_x_pos = inter_sky.get_x_pos().copy()
            (c_x_pos, s_height) = self.clean_heights(s_x_pos, s_height)
            r_ind_i = c_x_pos.index(self.xmin)
            r_ind_j = c_x_pos.index(self.xmax)
            s_height = s_height[r_ind_i:r_ind_j + 1]

        sum_width = self.sm_calculate_width(sum_x_pos[0], sum_x_pos[-1], 1)
        sum_heights = self.get_height().copy()
        m_x_pos = self.get_x_pos().copy()
        (m_x_pos, sum_heights) = self.clean_heights(m_x_pos, sum_heights)
        i = m_x_pos.index(sum_x_pos[0])
        j = m_x_pos.index(sum_x_pos[-1])
        sum_heights = sum_heights[i:j + 1]
        x = 0
        while x < len(sum_heights):
            if sum_heights[x] > s_height[x]:
                sum_heights[x] = s_height[x]
            x += 1

        inter_skl = Skyline(0, 0, 0)
        inter_skl.c_skyline(sum_x_pos, sum_heights, sum_width)
        return inter_skl

    def reflect_skyline(self, area):
        reflect_heights = self.get_height().copy()
        reflect_heights.reverse()
        reflect_heights.pop(0)
        reflect_heights.append(reflect_heights[-1])
        r_width = self.get_width().copy()
        r_x_pos = self.get_x_pos().copy()
        reflect_skl = Skyline(0, 0, 0)
        reflect_skl.c_skyline(r_x_pos, reflect_heights, r_width, -1, area)
        return reflect_skl

    # n - numero de edificios creados
    # h - una altura de 0 a h aleatoria
    # w - una width de 1 a w aleatoria
    # xmin, xmax - una posicion de inicio/final entre xmin, xmax
    def random_skylines(n, h, w, xmin, xmax):
        temp_sky = Skyline(0, 0, 0)
        i = 0
        while i < n:
            rd_xmin = random.randint(xmin, xmax - 1)
            rd_xmax = random.randint(rd_xmin + 1, xmax)
            rd_height = random.randint(0, h)
            rd_width = random.randint(1, w)

            rd_x_pos = list(range(rd_xmin, rd_xmax + 1))
            rd_heights_list = [rd_height] * ((rd_xmax - rd_xmin) + 1)

            times = rd_xmax - rd_xmin
            width_array = [rd_width] * times
            width_array.append(-0.5)
            tp_sky = Skyline(0, 0, 0)
            tp_sky.c_skyline(rd_x_pos, rd_heights_list, width_array)
            temp_sky = temp_sky.sumar_skyline(tp_sky)
            i += 1
        return temp_sky
