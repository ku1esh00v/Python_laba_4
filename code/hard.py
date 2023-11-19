y = int(input('Enter the angle value in DEGREES: '))

if y > 0 and y <= 360:
    if y % 30 == 0:
        hours = y // 30
        print("Full hours: ", hours)
        minute_nand_angle = 0
        print('Minute nand angle: ', minute_nand_angle)
        minutes = 0
        print('Full minutes:', minutes)
    else:
        x = y % 30 #counting the remaining minutes (1 hour = 30 degrees)
        minutes = x * 2
        minute_nand_angle = minutes * 6
        print('Full hours:', y // 30)
        print('Full minutes:', minutes)
        print('Minute nand angle:', minute_nand_angle)
else:
    print('The angle should be greater than 0 degrees, but not exceed 360 degrees!')
