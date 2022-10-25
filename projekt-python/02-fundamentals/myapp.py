import mymodule

print("Svetlo ujede vzdalenost 50000km za: " + str(mymodule.casSvetlo(50000, mymodule.SPEED_OF_LIGHT)) + "sekund")

print("Zvuk ujede vzdalenost 6000km za: " + str(mymodule.casSvetlo(6000, mymodule.SPEED_OF_SOUND)) + "sekund")

print("Tihova sila Zeme na teleso o hmotnosti 50kg je: " + str(mymodule.tihaZeme(50, mymodule.EARTH_GRAVITY)) + "N")

print("Tihova sila  Mesice na teleso o hmotnosti 50kg je: " + str(mymodule.tihaZeme(50, mymodule.MOON_GRAVITY)) + "N")