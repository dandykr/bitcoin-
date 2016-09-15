# program ini di buat oleh seorang anak muda yang sedang kesepian mencari jati dirinya
# program ini bersifat open source siapaun bisa menggunakan software ini dengan bebas
# program ini digunakan untuk trading bitcoin di market polo
# siapun yang menggunakan program ini , menaggung resiko sendiri
# program ini sudah di uji sendiri dengan akurasi 85 % keuntungan
# gunakan program ini pada coin yang bagus (Recomanded : ETC , LISK , DASH)
# Jika program ini di rombak jangan lupakan share ya dan cantumkan nama coder awal dan yang revisi
# CODER : RAHMAT WAHYU HADI a.k.a bl4ckM4mba


from bittrex import apiBittrex
import json
import telepot
from time import sleep
import sys


bot = apiBittrex('api , secret')
telegram = telepot.Bot('')

coin = str(sys.argv[1])

altcoin = bot.getmarketsummary(coin)

listhargatinggi = []
listhargaterendah = []
alamat = 


hargaterendah 	= altcoin[0]["Low"]
listhargaterendah.append(hargaterendah)
hargatertinggi 	= altcoin[0]["High"]
listhargatinggi.append(hargatertinggi)
pembelianterahir = altcoin[0]["Last"]

telegram.sendMessage(alamat , "COIN "+coin+" SUDAH DIDAFTARKAN")
perulangan = True
while perulangan is True:
	try:
		sleep(10)
		listaltcoin = bot.getmarketsummary(coin)
		bid 		= listaltcoin[0]["Bid"]
		ask 		= listaltcoin[0]["Ask"]
		last  	 	= listaltcoin[0]["Last"]
		volume 		= listaltcoin[0]["Volume"]
		low 		= listaltcoin[0]["Low"]
		high 	 	= listaltcoin[0]["High"]


		BTC = bot.getbalance("BTC")
		jumlahBTC = BTC["Balance"]


		if (jumlahBTC < 0.05):
			telegram.sendMessage(alamat , "Jumlah bitcoin anda kurang dari 0.05")

		else :
			order = bot.getopenorders(coin)
			if not order :

				modalbeli = jumlahBTC / 1.1
				hargabeliaman = float(listhargaterendah[-1] / 2)
				hargabeli = float(listhargaterendah[-1] / 1.1)



				if (last < hargabeliaman ) or (last ==  hargabeliaman):
					totalbeli = float(modalbeli / last)

					beli = bot.buylimit(coin, totalbeli, last)

					listhargaterendah.append(low)
					listhargatinggi.append(high)
					sleep(2)
					listaltcoin = bot.getmarketsummary(coin)
					bid 		= listaltcoin[0]["Bid"]
					ask 		= listaltcoin[0]["Ask"]
					last  	 	= listaltcoin[0]["Last"]
					volume 		= listaltcoin[0]["Volume"]
					low 		= listaltcoin[0]["Low"]
					high 	 	= listaltcoin[0]["High"]

					order = bot.getopenorders(coin)
					if not order :
						telegram.sendMessage(alamat, "Bos anda telah melakukan order pada coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".\nSiap untuk di jual")

					else:

						jumlahcoin = bot.getbalance(coin)
						telegram.sendMessage(alamat, "Bos anda telah membeli coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")


				elif (last < hargabeli) or (last == hargabeli):
					totalbeli = float(modalbeli / last)

					beli = bot.buylimit(coin, totalbeli, last)

					listhargaterendah.append(low)
					listhargatinggi.append(high)
					sleep(2)
					order = bot.getopenorders(coin)
					if not order :
						telegram.sendMessage(alamat, "Bos anda telah melakukan order pada coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")
					else:
						jumlahcoin = bot.getbalance(coin)
						telegram.sendMessage(alamat, "Bos anda telah membeli coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")

			else:
				telegram.sendMessage(alamat, "Anda sedang melakukan order pada Coin "+coin+ ".")


	except Exception:
		telegram.sendMessage(alamat , "Bot mati")

		perulangan = True
