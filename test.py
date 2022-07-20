import pyupbit

access = "FxZzW6x8S6MybctoQOQRvjxjT4eQPnKjwKZmioXK"          # 본인 값으로 변경
secret = "rtT1RKtsDepAqG3DJFyu2NflxT9AD7WafWdwxs9Q"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회