wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)
a = "달러"
b = "원"
print(f"{1}시간에 {wage * 1}{a} 벌었습니다.")
print(f"{5}시간에 {wage * 5}{a} 벌었습니다.")
print(f"{1}시간에 {wage * 1 * exchange_rate}{b} 벌었습니다.")
print(f"{5}시간에 {wage * 5 * exchange_rate:.0f}{b} 벌었습니다.")
