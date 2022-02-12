fail = open("jooks.txt", encoding="UTF-8")
kokku = 0
for rida in fail:
    kilomeetreid = float(rida)
    if kilomeetreid > 10:
        kokku += kilomeetreid
fail.close()
print("Kokku joosti pikki jookse " + str(kokku) + " kilomeetrit.")