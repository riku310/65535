P6 = [229.1, 229.1, 5.67, 35.79, 7.3]
P5 = [240.1, 268.6, 5.76, 35.82, 7.3]
P4 = [254, 290, 5.84, 35.89, 7.3]
P3 = [266.4, 336.1, 5.84, 37.04, 7.3]
P2 = [270.8, 385.5, 5.84, 38.29, 7.3]
P1 = [273.1, 409.6, 5.92, 38.43, 7.3]

for P in P1:
    def find_nearest_n():
        target_fraction = 1 / P
        target_numerator = round(target_fraction * 65535)
        target_denominator = 65535

        # 最大公約数を求める関数
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # 分数の約分
        divisor = gcd(target_numerator, target_denominator)
        reduced_numerator = target_numerator // divisor
        reduced_denominator = target_denominator // divisor

        return reduced_numerator, reduced_denominator

    nearest_numerator, nearest_denominator = find_nearest_n()
    print(f"{nearest_numerator}/{nearest_denominator}")
