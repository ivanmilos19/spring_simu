# test.def calculate_position

import calculate_position as cp
   
# delta < 0
   
position = cp.calculate_position(1, 1, 0, 15, 5, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(3, 1, 0, 15, 5, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(25, 1, 0, 15, 5, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(35, 1, 0, 15, 5, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)



# delta > 0

position = cp.calculate_position(0, 10, 0, 15, 2, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(7, 10, 0, 15, 2, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(15, 10, 0, 15, 2, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(30, 10, 0, 15, 2, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

    
# delta = 0

position = cp.calculate_position(0, 2, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(5, 2, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(8, 2, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(12, 2, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)


#pas de frottements

position = cp.calculate_position(0, 0, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(5, 0, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(8, 0, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)

position = cp.calculate_position(12, 0, 0, 15, 1, 1, 0, 9)
print("position:", position, "type", cp.type_de_courbe)