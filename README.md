Ali Kemal Turan

Port Analizi
Gelişmiş Script ve Otamasyon Geliştirme
Rapor ve Analiz Dokümantasyonu
Klasör Düzeni Dosya Yönetimi ve Bağımlılık Listesi Oluşturma
Yakalama Filtrelerinin Oluşturulması ve Geliştirilmesi
Görüntüleme Filtrelerinin Oluşturulması ve Geliştirilmesi

Burhan Yavaş - Github (Gawgaci)

Yakalama Filtrelerinin Oluşturulması ve Geliştirilmesi
Görüntüleme Filtrelerinin Oluşturulması ve Geliştirilmesi
Python Script Geliştirme
IP Adreslerinin ve Aralıklarının Belirlenmesi
WHOIS Sorguları oluşturulması

Fatma Yeliz Apaydın (fatmayeliz)

Ham Trafik Yakalama
Filtrelenmiş Trafik Oluşturma
IP Adreslerinin Toplanması
IP Adreslerinin Belirlenmesi
Klasör Düzeni Dosya Yönetimi ve Bağımlılık Listesi Oluşturma
Ek Notların Derlenmesi


- Diğer bilgiler proje klasörünün içinde ki Sunu.docx içerisinde yer alıyor. Deepsearch analizi aşağıda bulunuyor.
2025 Yılı İçin Wireshark ve Python Otomasyonu ile Ağda Yayıncıların Tespiti: En Yenilikçi 10 Teknik/Trend

Başlık: Makine Öğrenimi ile Yayıncıların Ağ Trafiği Örüntülerinin Tespiti

Açıklama: Makine öğrenimi (ML) modelleri, yayıncıların tipik ağ trafiği örüntülerini (örneğin, RTMP/RTMPS, SRT protokolleri üzerinden sürekli yüksek upload, belirli CDN'lere bağlantılar) öğrenerek, ağdaki yayın aktivitelerini otomatik olarak tespit eder. Wireshark'tan alınan veri setleri bu modelleri eğitmek için kullanılır.
Etkiler ve Uygulama Alanları: 2025'te, bu teknik özellikle kurumsal ağlarda veya internet servis sağlayıcıları (ISP) tarafından yetkisiz yayınları, aşırı bant genişliği tüketimini veya telif hakkı ihlallerini tespit etmek için kullanılabilir. Ayrıca, yayın platformları tarafından bot veya sahte yayıncı hesaplarını belirlemede de etkili olabilir.
Kaynak: (Genel ML ve Ağ Trafiği Analizi) [PDF] A Survey on Machine Learning Approaches for Network Traffic Classification - researchgate.net (Bu genel bir kaynaktır, yayıncı özelinde spesifik bir makale bulmak zor olabilir ancak prensip aynıdır.)
Başlık: Python ile Wireshark Verilerinin Gerçek Zamanlı İşlenerek Anlık Yayıncı Tespiti

Açıklama: Python (örneğin PyShark kütüphanesi ile), Wireshark tarafından yakalanan ağ paketlerini gerçek zamanlı olarak analiz eder. Belirli yayın protokolleri (RTMP, SRT, WebRTC), hedef IP adresleri (bilinen yayın platformu sunucuları) veya yüksek upload hızları gibi göstergeler anında tespit edilerek uyarı mekanizmaları tetiklenir.
Etkiler ve Uygulama Alanları: Canlı etkinliklerde veya anlık müdahale gerektiren durumlarda (örneğin, bir kurum ağında izinsiz canlı yayın başlatılması) hızlı tespit ve aksiyon alınmasını sağlar. Ağ yöneticileri için anlık görünürlük sunar.
Kaynak: (PyShark ve Gerçek Zamanlı Analiz) "Threat Hunting with Pyshark: Using Open Source Python Libraries to Automate Network Analysis" - insanecyber.com
Başlık: Yayıncı Aktivitelerini Belirlemek İçin Davranışsal Ağ Analitiği (BNA)

Açıklama: BNA, bir kullanıcının veya cihazın normal ağ davranış profilini oluşturur. Bu profilden sapmalar (örneğin, normalde düşük upload yapan bir kullanıcının aniden saatlerce yüksek upload yapması, belirli yayın platformlarına sürekli veri göndermesi) yayın aktivitesi olarak işaretlenir.
Etkiler ve Uygulama Alanları: Özellikle daha önce yayın yapmayan ancak sonradan yayın yapmaya başlayan veya gizlenmeye çalışan yayıncıları tespit etmede etkilidir. Kurumsal ağlarda politika ihlallerini veya ev ağlarında çocukların kontrolsüz yayınlarını belirlemede kullanılabilir.
Kaynak: (Genel BNA) "Behavioral Network Analysis for Anomaly Detection" - SANS Institute Whitepaper (Spesifik yayıncı odaklı BNA için genel prensipler uygulanır.)
Başlık: Şifreli Yayın Trafiğinde Meta Veri Analizi ve Parmak İzi Çıkarma (TLS/SSL)

Açıklama: Yayınların çoğu artık şifreli (RTMPS, HTTPS üzerinden WebRTC/SRT) olsa da, TLS el sıkışmalarındaki SNI (Server Name Indication) gibi meta veriler hedef platformu (örn. live.twitch.tv) açığa çıkarabilir. Python ile bu meta veriler ve akış karakteristikleri (paket boyutları, zamanlamaları) analiz edilerek şifreli yayınlar bile tespit edilebilir.
Etkiler ve Uygulama Alanları: Şifrelemenin yaygınlaştığı günümüzde, içeriği görmeden bile yayın aktivitesini yüksek doğrulukla tespit etmeyi sağlar. Bu, gizlilik odaklı ağlarda bile politika uygulamasına olanak tanır.
Kaynak: "Reading Snis: A Guide To The Server Name Indication Tls Extension" - F5 Labs (SNI analizi üzerine genel bir kaynak.)
Başlık: Python ile Dinamik Yayın Platformu İmza Veritabanı Oluşturma ve Güncelleme

Açıklama: Yayın platformlarının (Twitch, YouTube Live, Kick vb.) kullandığı ingest sunucularının IP adresleri ve alan adları zamanla değişebilir. Python scriptleri, bu platformların API'lerini veya bilinen listeleri periyodik olarak sorgulayarak Wireshark filtreleri ve analiz modülleri için güncel bir imza veritabanı oluşturur ve bunu otomatik olarak günceller.
Etkiler ve Uygulama Alanları: Tespit sisteminin güncel kalmasını ve yeni yayın platformlarını veya değişen altyapıları hızla tanımasını sağlar, böylece tespit doğruluğu artar ve yanlış negatifler azalır.
Kaynak: Proje özelinde geliştirilecek bir otomasyon aracıdır. Temel prensipler API kullanımı ve veri yönetimine dayanır.
Başlık: Yeni Nesil Yayın Protokollerinin (SRT, WebRTC) Derinlemesine Analizi ve Tespiti

Açıklama: RTMP'nin yanı sıra SRT (Secure Reliable Transport) ve WebRTC gibi daha modern ve verimli yayın protokollerinin kullanımı artmaktadır. Wireshark ve Python, bu protokollerin özgün ağ ayak izlerini (port kullanımı, el sıkışma mekanizmaları, paket yapıları) analiz ederek yayıncıları daha etkin bir şekilde tespit eder.
**Etkiler
7. Başlık: Bulut Tabanlı Wireshark Entegrasyonları ile Ölçeklenebilir Yayıncı Tespiti ve Otomasyonu * Açıklama: Büyük ağlarda veya dağıtık ortamlarda (örneğin, çok şubeli bir şirket veya geniş bir kampüs ağı) yayıncı tespiti için bulut tabanlı Wireshark çözümleri ve analiz platformları kullanılır. Python scriptleri, yakalanan verileri buluta gönderir, burada merkezi analiz ve otomasyon araçları (örneğin, uyarı sistemleri, raporlama) devreye girer. * Etkiler ve Uygulama Alanları: Özellikle ISP'ler veya büyük kuruluşlar için ağ genelinde yayın aktivitelerini izlemeyi ve yönetmeyi kolaylaştırır. Ölçeklenebilirlik, merkezi yönetim ve gelişmiş analitik yetenekleri sunar. * Kaynak: (Genel Bulut Ağ İzleme) "Cloud Native Network Monitoring: Challenges and Opportunities" - IEEE Xplore (Bu genel bir kaynaktır, Wireshark'ın bulut entegrasyonları spesifik çözümlere bağlıdır.)

Başlık: Coğrafi Konum (GeoIP) Analizi ile Yayın Kaynaklarının ve Hedeflerinin Belirlenmesi

Açıklama: Wireshark'tan elde edilen IP adresleri, Python ile GeoIP veritabanları kullanılarak coğrafi konumlara eşleştirilir. Bu, yayıncının yaklaşık konumunu ve yayının hangi coğrafi bölgelerdeki sunuculara gittiğini belirlemeye yardımcı olur.
Etkiler ve Uygulama Alanları: Telif hakkı kısıtlamaları olan içeriklerin yayınlandığı bölgeleri tespit etmede, bölgesel ağ trafiği analizinde veya şüpheli uluslararası yayın aktivitelerini belirlemede kullanılabilir. Örneğin, bir kurum ağından beklenmedik bir ülkedeki yayın sunucusuna sürekli veri akışı tespit edilebilir.
Kaynak: MaxMind GeoIP2 Python API gibi kütüphaneler ve GeoLite2 gibi ücretsiz veritabanları bu amaçla kullanılabilir.
Başlık: Yayın Yazılımlarının (OBS, Streamlabs vb.) Ağ İletişim Parmak İzlerinin Çıkarılması

Açıklama: Popüler yayın yazılımları (OBS Studio, Streamlabs Desktop, XSplit vb.) başlatıldıklarında veya yayın yaptıklarında kendilerine özgü ağ iletişim örüntüleri (belirli sunucularla kontrol iletişimi, güncelleme kontrolleri, eklenti trafiği) sergilerler. Python ve Wireshark ile bu parmak izleri tanımlanarak, sadece yayın trafiği değil, yayın yapma potansiyeli olan yazılımların kullanımı da tespit edilebilir.
Etkiler ve Uygulama Alanları: Bir ağda yayın yapılmasa bile, yayın yapmaya hazırlanan veya bu tür yazılımları kullanan kullanıcıları proaktif olarak belirlemeyi sağlar. Kurumsal politikalara aykırı yazılım kullanımını tespit etmede faydalıdır.
Kaynak: Bu, genellikle tersine mühendislik ve ağ trafiği analizi ile elde edilen özel bir araştırma gerektirir. Belirli yazılımların ağ davranışları üzerine topluluk forumlarında veya güvenlik bloglarında bilgiler bulunabilir.
Başlık: Gelişmiş Python Scriptleri ile Otomatik Raporlama ve Görselleştirme

Açıklama: Tespit edilen yayıncı aktiviteleri, kullanılan protokoller, yayın süreleri, bant genişliği tüketimi gibi veriler Python scriptleri ile otomatik olarak toplanır. Bu veriler, Matplotlib, Seaborn veya web tabanlı dashboard'lar (örneğin, Dash/Plotly) aracılığıyla yöneticilerin kolayca anlayabileceği raporlar ve görselleştirmeler haline getirilir.
Etkiler ve Uygulama Alanları: Ağ yöneticilerine ve güvenlik ekiplerine yayın aktiviteleri hakkında net, eyleme geçirilebilir bilgiler sunar. Trend analizi, kapasite planlaması ve politika uygulama süreçlerini destekler.
Kaynak: (Python Veri Görselleştirme) Matplotlib (matplotlib.org), Seaborn (seaborn.pydata.org), Plotly Dash (plotly.com/dash/).
Bu 10 teknik ve trend, 2025 yılında Wireshark ve Python otomasyonu kullanarak ağdaki yayıncıların tespit edilmesi konusunda projenize yenilikçi ve etkili yaklaşımlar sunacaktır. Her bir başlık, projenizin spesifik ihtiyaçlarına göre daha da detaylandırılabilir ve özelleştirilebilir.

