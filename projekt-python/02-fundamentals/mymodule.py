

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def tihaZeme(hmotnost, earthG):
    '''
    zadame hmotnost v kg
    vrati tihovou silu zeme
    '''
    return hmotnost * earthG

def tihaMesice(hmotnost, moonG):
    '''
    zadame hmotnost v kg
    vrati tihovou silu mesice
    '''
    return hmotnost * moonG

def casSvetlo(vzdalenost, svetlo):
    '''
    dame vzdalenost v km
    dostaneme cas v sekundach
    '''
    return round((vzdalenost * 1000) / svetlo, 3)

def casZvuk(cas, zvuk):
    '''
    dame vzdalenost v km
    dostaneme cas v sekundach
    '''
    return round((cas * 1000) / zvuk, 3)