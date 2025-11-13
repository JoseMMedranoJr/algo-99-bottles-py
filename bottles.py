def bottle_song(i):

	while i > 0:
		j = i - 1
		if i == 1:
			print('1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall')	
		else:
			print(f'{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {j} bottles of beer on the wall.{j} of bottles')
		i = j

		
bottle_song(99)
