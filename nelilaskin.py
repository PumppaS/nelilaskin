# nelilaskin codecamppiin kayttiskurssille
# laskee plus- minus- kerto- ja jakolaskuja
#gunnar 
#hilpi
#karjanmaa
#tonteri

eka = int(input("Anna luku: "))
toka = int(input("Anna toinen luku: "))

def vaihtoehdot():
	print("1) Summa")
	print("2) Erotus")
	print("3) Tulo")
	print("4) Osamäärä")
	print("0) Lopetus")

while True:
	vaihtoehdot()
	valinta = int(input("Valitse toiminto: "))
	if valinta == 1:
		summa = eka + toka 
		print("Summa on ", summa)
	elif valinta == 2:
		erotus = eka - toka
		print("Erotus on ", erotus)
	elif valinta == 3:
		#tulo
	elif valinta == 4:
		#osamäärä
	elif valinta == 0:
		print("Kiitos ohjelman käytöstä.")
		break
	else:
		print("Valinta virheellinen")
			
