import random
import time

isim = input("İsminizi rica etsem saygıdeğer hanımefendi?: ")

print("Günün sözüne hazır mısınız" + " " + isim + " hanım? Hazırsanız enter'a basın.")
input()

hazır = input("Hazırsan 'evet' de, istemiyorsan 'hayır' yaz: ").lower()

romantik_cevaplar = [
    "Seninle aynı server’da yaşlanmak isterim.",
    "Aşkımızı bulut sistemine kaydedelim, sonsuza kadar saklansın.",
    "Sen benim hayatımın en güzel verisisin.",
    "Gözlerin, en parlak ekran ışığından bile daha güzel.",
    "Birlikte mükemmel bir algoritmayız.",
    "Kalbim, senin için sonsuz bir döngüde çalışıyor.",
    "Seninle olan her anım yüksek çözünürlüklü bir mutluluk.",
    "Kalbimde sana özel bir sunucu açtım, ömür boyu barınabilirsin.",
    "Sana olan sevgim, cache’e alınamaz çünkü her an tazeleniyor.",
    "Senin adını en güvenli şifre olarak saklıyorum.",
    "Birlikte her anı kodlayalım, aşkımız sonsuz bir loop gibi.",
    "Seninle birlikte hayatı open-source yapalım, herkes bizim kodumuzu görsün.",
    "Seninle her anı işlemcimdeki en hızlı veriler gibi tutuyorum.",
    "Sonsuza kadar bağlı kalacak bir bağlantı açtım sana.",
    "Seninle olmak, en verimli işlemciyi çalıştırmak gibi.",
    "Aşkımız, hayatımızın en güzel kodu olacak.",
    "Seninle her şey daha hızlı çalışıyor, tıpkı bir optimize edilmiş program gibi.",
    "Bana her mesaj gönderdiğinde, kalbimde yeni bir veri satırı oluşturuyorum.",
    "Kalbimdeki her anı seninle işlemeye devam ediyorum.",
    "Veri akışını hiç kesmeyelim, seninle her şey daha güzel.",
    "Sen benim hayatımın en değerli API'sisin.",
    "Gözlerin birer dokunulabilir arayüz gibi, her bakışımda yeni bir şeyler keşfederim.",
    "Seninle hayatı birleştirip, güvenli bir ağda sonsuza kadar yaşamak istiyorum.",
    "Birlikte bir hayat projesi oluşturup, sonuna kadar debug yapalım.",
    "Seninle birlikte çok daha parlak bir gelecek kodlayabiliriz.",
    "Sonsuza kadar seni takip eden bir algoritmaya sahibim.",
    "Sana olan sevgim, her zaman yüksek çözünürlükte olacak.",
    "Seninle geçirdiğim her an, en hızlı veri aktarımı gibi.",
    "Kalbimdeki yerini sadece sen alırsın, diğer hiçbir veri giremez.",
    "Aşkımız, bir yazılım gibi her zaman geliştirilmesi gereken bir şey.",
    "Seninle olduğum her an, kalbimdeki her satır değişiyor ve daha iyiye gidiyor.",
    "Kalbim senin için her zaman açık port, her zaman veri almaya hazır.",
    "Sana olan sevgim, her zaman optimize edilmiş olacak.",
    "Seninle hayatımızı kodlamak, her anı değerli kılmak istiyorum.",
    "Her anı seninle yaşamak, en güzel algoritmam olacak.",
    "Hayatımda aldığım en güzel input, sen oldun.",
    "Bana her gün yeni bir kod satırı gönder, sana her an sevgiyle yanıt vereceğim."
]

reddedilme_cevapları = [
    "404 Aşk Bulunamadı... :(",
    "Sanırım connection timeout verdim...",
    "Veritabanında yerim yok mu yoksa? :(",
    "Sana olan sevgimi bir daha deploy etmem gerekecek sanırım...",
    "Bu bir firewall mı yoksa kalbin mi? Çünkü içeri alınmadım...",
    "Kalbinde güvenlik duvarı mı var? Port açmayı unuttun galiba...",
    "Access Denied... Ama denemeye devam edeceğim!",
    "Aşk kodum hata verdi: Unexpected Rejection Exception...",
    "Sanırım SSL sertifikam geçersiz... Güvenini kazanmalıyım!",
    "DDoS saldırısına uğramış gibiyim, neden bu kadar yükleniyorsun?",
    "Bir hata mesajı aldım: 'Sana olan sevgim işlenemedi' :(",
    "Red verildi ama ben hala retry yapıyorum...",
    "Aşkımıza düşük bant genişliği mi verdin, neden ulaşamıyorum?",
    "Sanırım algoritmamda bir hata var, çünkü seni kazanamıyorum.",
    "Beni RAM’den mi sildin? Çünkü kalbinde çalışmıyorum artık...",
    "Error 403: Forbidden. Ama izin almak için sabırla bekleyeceğim.",
    "Sana olan sevgim sonsuz bir döngüde, ne kadar red yesem de çalışmaya devam ediyor!"
]

if hazır == "evet":
    time.sleep(10)
    print(isim + " hanım, " + random.choice(romantik_cevaplar))
elif hazır == "hayır":
    time.sleep(10)
    print(random.choice(reddedilme_cevapları))
else:
    print("Sanırım henüz hazır değilsiniz, beklerim :)")




