import copy

player1 = [['A','K'],['Q','J']]
player2 = player1
player3 = copy.copy(player1)
player4 = copy.deepcopy(player1)
print(f"p1:{player1},p2:{player2}")
print(f"p3:{player3},p4:{player4}")
player1.append('JOKER')
print(f"[II]p1:{player1},p2:{player2}")
print(f"[II]p3:{player3},p4:{player4}")
player1[0][0]='10'
print(f"[III]p1:{player1},p2:{player2}")
print(f"[III]p3:{player3},p4:{player4}")
player4[1][1]='8'
print(f"[IV]p1:{player1},p2:{player2}")
print(f"[IV]p3:{player3},p4:{player4}")