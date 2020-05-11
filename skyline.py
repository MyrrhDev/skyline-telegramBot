class Skyline:
    #variables donde se asignan edificios
    area = 0
    max_height = 0
    
    xmin = 0
    height = []
    xmax = 0
        
    
    def __init__(self, xmin, height, xmax):
        self.xmin = xmin
        self.height = [height] * ((xmax-xmin)+1)
        self.xmax = xmax
        self.area = (xmax - xmin) * height
        self.max_height = height
    
    
    #***DONE***
    #Devuelve una lista para hacer el plot de la(s) alturas del skyline
    def get_height(self):
        return self.height
    
    #Devuelve una lista para hacer el plot de las posicion en el eje x
    #e.g. [1, 2, 3]
    def get_x_pos(self):        
        return list(range(self.xmin, self.xmax+1))
    
    #Devuelve una lista del width de las barras del plot
    #e.g. [1.0, 1.0, 1.0, 1.0, 1.0, -0.5]
    def get_width(self):
        times = self.xmax - self.xmin
        width_array = [1.0] * times
        width_array.append(-0.5)    
        return width_array
    
    def get_area(self):
        return self.area
    
    def get_max_height(self):
        return self.max_height
    
    
    #Mover el skyline a la derecha
    def move_right(self, N):
        self.xmin += N
        self.xmax += N
    
    #Mover el skyline a la izquierda
    #Verificar que xmin no se coniverta en NEGATIVO!!! (??)
    #igual antes de mandarloa  eso....asi que en bot.py
    #aqui confiamos
    def move_left(self, N):
        self.xmin -= N
        self.xmax -= N
    
    
    #replicacion del mismo skyline
    def multiply_N(self, N):
        mul_heights = self.get_height()
        mul_width = self.get_width()
        
        #Calcular nuevas x_coords:
        mul_x_pos = self.get_x_pos()
        size = len(mul_x_pos)
        m_min = m_max = self.xmax
        
        for i in range(N-1):
            m_min = m_max
            m_max = m_max + size - 1
            mul_x_pos += list(range(m_min, m_max+1))      
        
        return (mul_x_pos, mul_heights*N, mul_width*N)
    
    
    #*********
    #Suma una skyline
    #esta funcion esta hecha para unos valores individuales del skyline nuevo
    #NO para un caso en el que tengo dos variables de sky y las quiero unir...
    #ojo....
    def sumar_skyline(self, s_xmin, s_height, s_xmax):
        sum_x_pos = []
        sum_heights = []
        sum_width = []
        
        #separado, izq o der:
        if((s_xmin < self.xmin and s_xmax < self.xmax) or (s_xmin > self.xmin and s_xmax > self.xmax)):
            #datos individuales
            sp_height = [s_height] * ((s_xmax-s_xmin)+1)
            times = s_xmax - s_xmin
            sp_width = [1.0] * times
            sp_width.append(-0.5)
            #sp_x_pos = list(range(s_xmin, s_xmax+1)
            
            #left add
            if(s_xmin < self.xmin and s_xmax < self.xmax):
                #orden y rellenar de 0's
                diff = ((self.xmax - s_xmin) + 1) - len(sp_height) - len(self.get_height())
                sp_cero_fill = [0] * diff
                sum_x_pos = list(range(s_xmin, self.xmax+1))
                sum_heights = sp_height + sp_cero_fill + self.get_height()
                sum_width = sp_width + sp_cero_fill + self.get_width()
            #right add
            elif(s_xmin > self.xmin and s_xmax > self.xmax):
                #orden y rellenar de 0's
                diff = ((s_xmax - self.xmin) + 1) - len(sp_height) - len(self.get_height())
                sp_cero_fill = [0] * diff
                
                sum_x_pos = list(range(self.xmin, s_xmax+1))
                sum_heights = self.get_height() + sp_cero_fill + sp_height 
                sum_width = self.get_width() + sp_cero_fill + sp_width 
        #
        elif():
            
        
        
        #if (xmin < self.xmin):
            #self.xmin = xmin
        #if (xmax > self.xmax):
            #self.xmax = xmax
        #in case new height is higher    
        #if(height > max_height):
            #self.max_height = height
        
        return (sum_x_pos, sum_heights, sum_width)
         
    #Interseccion
    def inter_skyline():
        
    
    
    
    #devuelve todo el skyline reflejado
    #Se mantiene x_pos y los width, pero cambia la lista de height
    def reflect_skyline():
        #cambia heights
        reflect_heights = 
        
        r_width = self.get_width()
        r_x_pos = self.get_x_pos()
        
        return (r_x_pos, reflect_heights, r_width)
        
    
    #recalcular el area???
    def calcula_area():
        self.area = m_area
    
    
    
