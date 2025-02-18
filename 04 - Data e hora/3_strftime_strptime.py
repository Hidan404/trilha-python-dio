from datetime import datetime, time, date, timedelta

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))


#pequeno programa de datas

data_atual = datetime.date(datetime.now())


def modificar_padrao_data(data):
    return data.strftime("%d/%m/%Y %a")

def trabalhar_datas(data):
    if data.weekday() == 5:
        return data + timedelta(days=2)
    elif data.weekday() == 6:
        return data + timedelta(days=1)
    elif data.weekday() == 3:
        return data + timedelta(days = 10)
    else:
        return modificar_padrao_data(data)

print(modificar_padrao_data(data_atual), trabalhar_datas(data_atual))

