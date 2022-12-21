import pyupbit

access = "GCTz4GYKuJCaxA9imYO6AKqBpx766xSXJQgnVa5G"          # 본인 값으로 변경
secret = "Q0OKhx8yvfgPcdwY6uVwAJvEJw3I5eF7FJ4xm3ZY"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ARDR"))      # KRW-ARDR 조회
print(upbit.get_balance("KRW-IOST"))      # KRW-IOST 조회
print(upbit.get_balance("KRW-WAVES"))     # KRW-WAVES 조회
print(upbit.get_balance("KRW-MBL"))     # KRW-MBL 조회
print(upbit.get_balance("KRW-STEEM"))     # KRW-STEEM 조회
print(upbit.get_balance("KRW-BORA"))     # KRW-BORA 조회

print(upbit.get_balance("KRW"))         # 보유 현금 조회