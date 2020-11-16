Alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chaine= "BIENVENUEAPOLYTECHANGERS"

def calcstrprint(chaine):
    chaine=str.upper(chaine)
    while len(chaine) % 16 != 0:
        chaine += "A"

    matrix_int_list = []
    matrix_int_list = strtomatrix(matrix_int_list, chaine)
    #print_list_mat(matrix_int_list)
    sums = []
    for mat in matrix_int_list:
        sums.append(get_sum_by_col(mat))
    #print("sum of the matrix")
    #print(sums)

    #print("sliding mtraix")
    for mat in matrix_int_list:
        slide_rows(mat)
    sums2 = []
    for mat in matrix_int_list:
        sums2.append(get_sum_by_col(mat))
    #print_list_mat(matrix_int_list)
    #print("sum of the matrix step 2")
    #print(sums)
    #print(sums2)

    sum_tot = []
    for s in range(0, len(matrix_int_list)):
        sum_temp = []
        for i in range(0, 4):
            sum_temp.append((sums[s][i] + sums2[s][i]) % 26)
        sum_tot.append(sum_temp)
        for i in range(1, len(sum_tot)):
            for j in range(0, 4):
                sum_tot[i][j] = (sum_tot[i][j] + sum_tot[i - 1][j]) % 26
    #print("sum final")
    #print(sum_tot)

    #print_sum(sum_tot)

    list_sum = ""
    for s in sum_tot:
        for i in s:
            list_sum+=Alpha[i]

    return  list_sum

def strtomatrix(matrix_int_list,chaine):
    for i in range(0, int(len(chaine) / 16)):
        simple_matrix = []
        for j in range(0, 4):
            ligne = []
            for k in range(0, 4):
                z = 4 * j + k + 16 * i
                # print(z,"   ",len(chaine))
                #print(chaine[z])
                # ligne.append((chaine[z]))
                ligne.append(Alpha.index(chaine[z]))
            simple_matrix.append(ligne)
        matrix_int_list.append(simple_matrix)
    return matrix_int_list

def print_matrix(mat):
    for l in mat:
        print(l)

def print_list_mat(lmat):
    i=0
    for mat in lmat:
        print("Matrice : ",i)
        i+=1
        print_matrix(mat)


def get_sum_by_col(mat):
    i0 = 0
    i1 = 0
    i2=0
    i3=0
    for ligne in mat:
        i0+=ligne[0]
        i1 += ligne[1]
        i2 += ligne[2]
        i3 += ligne[3]
    sum=[]
    sum.append(i0%26)
    sum.append(i1%26)
    sum.append(i2%26)
    sum.append(i3%26)
    return sum

def slide_rows(mat):
    i=0
    for ligne in mat:
        if i==0:
            save=ligne[0]
            ligne[0]=ligne[1]
            ligne[1]=ligne[2]
            ligne[2]=ligne[3]
            ligne[3]=save
            i+=1
        elif i==1:
            save1 = ligne[0]
            save2 = ligne[1]
            ligne[0] = ligne[2]
            ligne[1] = ligne[3]
            ligne[2] = save1
            ligne[3] = save2
            i+=1
        elif i==2:
            save1 = ligne[0]
            save2 = ligne[1]
            save3 = ligne[2]
            ligne[0] = ligne[3]
            ligne[1] = save1
            ligne[2] = save2
            ligne[3] = save3
            i+=1
        elif i==3:
            save1 = ligne[0]
            save2 = ligne[1]
            ligne[0] = ligne[3]
            ligne[1] = ligne[2]
            ligne[2] = save2
            ligne[3] = save1
            i+=1

def print_sum(sum):
    list_sum=[]
    for s in sum:
        temp=[]
        for i in s:
            temp.append(Alpha[i])
        list_sum.append(temp)
    print(list_sum)



