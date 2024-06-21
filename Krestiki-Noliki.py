# ---------Создаем игровое поле----------
pole = [
	[" ", 1, 2, 3],
	[1, " ", " ", " "],
	[2, " ", " ", " "],
	[3, " ", " ", " "]
]


# ---------Вывод игрового поля----------
def out(pole):
	for row in pole:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


# ---------Проверка ввода----------
def pl_input(you_move, cord):
	while you_move not in ("1", "2", "3"):
		print("Введите корректную координату")
		you_move = input(f"Введите координату {cord}")
	return int(you_move)


print("Для игры нужно вводить координаты цифрами от 1 до 3\n")
for i in range(1, 19):
	if i % 2 == 0:
		name = "Player 2"
	else:
		name = "Player 1"
	out(pole)
	print(f"{name} ваш ход!")
	you_move_x = pl_input(input("Введите координату Х"), "Х")
	you_move_y = pl_input(input("Введите координату У"), "У")
	err = True
	while err:
		a = pole[you_move_y]
		if a[you_move_x] == ' ':
			list.pop(a, you_move_x)
			list.insert(a, you_move_x, 'x') if name == "Player 1" else list.insert(a, you_move_x, 'o')
			err = False
		else:
			err = True
			print("Эта клетка занята. Введите другие координаты")
			you_move_x = pl_input(input("Введите координату Х"), "Х")
			you_move_y = pl_input(input("Введите координату У"), "У")

	# ---------Проверка выигрыша----------
	line_1 = pole[1]
	line_2 = pole[2]
	line_3 = pole[3]
	if line_1[1] == line_1[2] == line_1[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_2[1] == line_2[2] == line_2[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_3[1] == line_3[2] == line_3[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_1[1] == line_2[1] == line_3[1] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_1[2] == line_2[2] == line_3[2] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_1[3] == line_2[3] == line_3[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_1[1] == line_2[2] == line_3[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
	if line_3[1] == line_2[2] == line_1[3] != " ":
		print(f"{name} выиграл!")
		out(pole)
		break
