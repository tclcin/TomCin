lugar_do_show = input()
vip_count = 0
codigo = -1

suporte = "string"
while not (codigo == 0000 or codigo == "" or suporte == "Ajudou"):
    codigo = input()
    if codigo != '':
        codigo = int(codigo)

    if codigo == 1000:
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
        vip_count += 1 
    
    elif codigo == 1001:
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    
    elif codigo == 1002:
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")

    elif codigo == 1003:
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")

    elif codigo == 1004:
        print("Esse código não existe! O sistema quebrou...")
        print("Vamos aguardar até que o suporte nos ajude.")
        while suporte != "Ajudou":
            suporte = input()
            if suporte != "Ajudou":
                print("Ainda não...")
    
print(f"O show da Taylor Swift será em {lugar_do_show} e contará com {vip_count} VIPs!")