
def pasa_pasa(num1, num2):
    nums = [num1, num2]
    for i in range(2):
    # convertimos a cadena
        nums[i] = str(nums[i])
        # separamos los digitos y creamos una lista
        nums[i] =' '.join(nums[i]).split()

    nums[1].append(nums[0].pop(-1))

    # volvemos a unir la lista y la convertimos a entero
    for i in range(2):
        nums[i] = int(''.join(nums[i]))

    return nums
