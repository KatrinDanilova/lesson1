#def get_vat(payment):
#    vat = payment / 100 * 18
#    return vat
#    print(vat)
#get_vat(100)

def get_vat(payment, percent=18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = round((payment / 100 * percent),2)
        return "НДС составляет {}".format(vat)
    except (TypeError, ValueError):
        return "Не могу посчитать НДС"
    

pay = input("Введите сумму платежа: ")
percent = input("Введите процент: ")
vat = get_vat(pay, percent)
print(f"Сумма платежа составляет: {pay}, {vat}")