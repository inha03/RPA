def sumfunc(num):
    total = 0
    for j in range(1, num + 1):
        total += j
    return total

num_input = input("1 이상의 정수를 입력하세요: ")

if num_input.isdigit():
    num = int(num_input)
    if num < 1:
        print("정수를 다시 입력하세요.")
    else:
        total_sum = sumfunc(num)
        print(f"1~{num}까지의 정수의 합은 {total_sum}입니다.")
else:
    print("정수를 다시 입력하세요.")