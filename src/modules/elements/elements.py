#Structural Area (Sofistik SAR) - whole structural element (wall, slab, etc)
class StructuralArea():
    def __init__(self,id):
        self.id = id

    group = 0
    
    material = 0
    thickness = 0
    _elements = []

    @property
    def elements(self):
        return self._elements
    
    @elements.setter
    def elements(self,packed_list):
        self._elements = list(range(packed_list[0],packed_list[1]*-1+1))


#Primitive finite quad element
class AreaElement():
    def __init__(self,id_fe):
        self.id_fe = id_fe

    forces = []

    def get_force(self,lc):
        for f in self.forces:
            if f.lc == lc:
                print(f.lc)
                return f
            return QuadForces(lc)

    def set_force(self,lc,nxx,nyy,mxx,myy,mxy):
        self.forces.append(QuadForces(lc,nxx,nyy,mxx,myy,mxy))



#Container for internal forces   
class QuadForces():
    def __init__(self,lc):
        self.lc = lc
    
    def __init__(self,lc,nxx,nyy,mxx,myy,mxy):
        self.lc = lc    
        self.nxx = nxx
        self.nyy = nyy
        self.mxx = mxx
        self.myy = myy
        self.mxy = mxy

    nxx = 0
    nyy = 0
    mxx = 0
    myy = 0
    mxy = 0
