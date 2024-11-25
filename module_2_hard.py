number_1 = int(input('Число: '))
vt_vst_2 = ''
for i in range(1, number_1, 1):
    for j in range(i, number_1, 1):
        if number_1 % (i + j) == 0:
             vt_vst_2 = vt_vst_2 + str(i) + str(j)
print (vt_vst_2)


