import settings
import random
from utils import split_list


class Keg:
    # Бочонок

    def __init__(self, value=None):
        self._value = value		
        self._is_cross = False
    
    def __str__(self):		
        if self._is_cross:
            return "-"
        if self.value:
            return str(self.value)			
        return " "
    
    def __eq__(self, value) -> bool:
        return value == self.value
    
    def __repr__(self):
        return str(self)

    @property
    def value(self):
        return self._value
    
    def cross(self):
        self._is_cross = True	


class Card:
    # Карточка

    def __init__(self):
        self._kegs = []		
        self._count_cros_keg = 0
        self._create()   

    def __contains__(self, value):		
        return value in self._kegs

    def __str__(self) -> str:		
        str_kegs = list(map(str, self._kegs))		
        splited = split_list(str_kegs, settings.COUNT_COL)		
        return "\n".join([" ".join(row) for row in splited])	
       
    def __repr__(self) -> str:
        return str(self)
    
    def _index(self, value) -> int:
        return self._kegs.index(value)
    
    def __getitem__(self, index) -> Keg:
        return self._kegs[index]
    
    @property
    def count_cros_keg(self):
        return self._count_cros_keg

    def _create(self) -> None:				
        keg_values_range = range(settings.KEG_MIN_VAL, settings.KEG_MAX_VAL)
        count_empty_keg = settings.COUNT_COL - settings.COUNT_KEG
        for row in range(settings.COUNT_STR):			
            values = random.sample(keg_values_range, settings.COUNT_KEG)			
            values += [None]*(count_empty_keg)			
            random.shuffle(values)
            self._kegs += [Keg(value) for value in values]

    def cross_keg(self, value):
        self._count_cros_keg += 1
        keg_index = self._index(value)
        keg = self[keg_index]        
        keg.cross()

    