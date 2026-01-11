import streamlit as st
import re  # Fiyat temizleme için

st.set_page_config(page_title="Ekin Gayrimenkul Pro İlan", layout="wide")

st.image("logo.png", use_container_width=True)

st.markdown(
    "<h1 style='text-align: center; font-size: 2.8em; font-weight: bold;'>EKİN GAYRİMENKUL - PROFESYONEL İLAN OLUŞTURUCU</h1>",
    unsafe_allow_html=True
)
st.markdown("Daire, dükkan, ofis, arsa, tarla... Her türlü emlak ilanınızı saniyeler içinde profesyonelce hazırlayın!")

# 1. Emlak Türü ve İşlem Seçimi
col_tur1, col_tur2 = st.columns(2)
with col_tur1:
    emlak_turu = st.selectbox("📌 Emlak Türü", ["Daire", "Dükkan / Mağaza", "Ofis / İşyeri", "Arsa", "Tarla"])
with col_tur2:
    ilan_turu = st.radio("İşlem Türü", ["🟢 Satılık", "🔴 Kiralık"], horizontal=True)

# 2. İlan Tonu
st.subheader("📢 İlan Tonu Seçiniz")
if emlak_turu in ["Arsa", "Tarla"]:
    ton_options = ["🌟 Yatırıma Çok Uygun", "🏡 İmarlı & Hazır", "💰 Fırsat Arazi"]
else:
    if ilan_turu == "🟢 Satılık":
        ton_options = ["🌟 Ultra Lüks & Prestijli", "🏡 Modern & Konforlu", "💰 Fırsat & Yatırıma Uygun"]
    else:
        ton_options = ["🌟 Ultra Lüks & Prestijli", "🏡 Modern & Konforlu", "💰 Uygun Fiyat & Avantajlı"]

ton = st.radio("Segmentinize uygun ton:", ton_options, horizontal=True)

if "Lüks" in ton or "Prestij" in ton or "Yatırıma Çok" in ton:
    ton_key = "luks"
elif "Modern" in ton or "İmarlı" in ton:
    ton_key = "modern"
else:
    ton_key = "firsat"

# 3. Konum Bilgileri
st.subheader("📍 Konum Bilgileri")
col_loc1, col_loc2, col_loc3 = st.columns(3)
with col_loc1:
    il = st.selectbox("İl", ["Kırklareli", "İstanbul", "Tekirdağ", "Edirne", "Çanakkale", "Diğer"])
with col_loc2:
    ilce = st.text_input("İlçe (örn: Lüleburgaz)")
with col_loc3:
    mahalle = st.text_input("Mahalle / Cadde / Sokak (örn: Özerler Mah.)")

# 4. Temel Bilgiler
st.subheader("🔹 Temel Bilgiler")
col1, col2, col3 = st.columns(3)

oda_bilgi = kat_bilgi = fiyat_gir = kira_gir = depozito_gir = ""
alan_net = alan_brut = bina_kat_sayisi = yas = aidat = arsa_donum = imar_durumu = cephe_metre = ""
balkon_bilgi = ""
teras_var = False
kredi_uygun = "Bilinmiyor"
yol_durumu = "Bilinmiyor"

konum_oz = manzara = bina_oz = ic_oz = cephe = teknik_oz = isitma_secilen = []

with col1:
    if emlak_turu in ["Daire", "Dükkan / Mağaza", "Ofis / İşyeri"]:
        oda_bilgi = st.text_input("🛏️ Oda / Bölüm (Daire: 3+1, Dükkan: Açık Alan vb.)")
        kat_bilgi = st.text_input("🏢 Kat (örn: Zemin, 3. Kat)")
    if ilan_turu == "🟢 Satılık":
        fiyat_gir = st.text_input("💰 Satış Fiyatı (örn: 1250000 veya 1.250.000)")
    else:
        kira_gir = st.text_input("💰 Aylık Kira Bedeli (örn: 25000)")
        depozito_gir = st.text_input("🔒 Depozito (örn: 50000)", value="")

with col2:
    if emlak_turu in ["Arsa", "Tarla"]:
        arsa_donum = st.text_input(f"🌳 {'Arsa' if emlak_turu == 'Arsa' else 'Tarla'} Alanı (dönüm, örn: 5)")
        imar_durumu = st.text_input("📜 İmar Durumu (örn: İmarsız, Konut İmarlı, Tarım Dışı)")
        yol_durumu = st.selectbox("🛣️ Yol Durumu", 
            ["Yol Cephesi Var", "Yol Cephesi Yok", "Yolu Açılmış (Resmi Yol Var)", 
             "Stabilize Yol", "Asfalt Yol", "Bilinmiyor"])
    else:
        alan_net = st.text_input("📏 Kullanılabilir Alan m² (örn: 120)")
        alan_brut = st.text_input("📐 Brüt / Toplam Alan m² (örn: 150)")
        bina_kat_sayisi = st.text_input("🏢 Bina Kat Sayısı (varsa)")

    if ilan_turu == "🟢 Satılık":
        kredi_uygun = st.selectbox("🏦 Krediye Uygunluk", ["Evet", "Hayır", "Bilinmiyor"])

with col3:
    if emlak_turu not in ["Arsa", "Tarla"]:
        yas = st.text_input("🏗️ Bina Yaşı (örn: Sıfır)")
        aidat = st.text_input("💸 Aidat / Ortak Gider (örn: 1200 TL)")
    if emlak_turu in ["Dükkan / Mağaza", "Ofis / İşyeri"]:
        cephe_metre = st.text_input("🚪 Cephe Genişliği (metre, örn: 8 metre)")

# Balkon & Teras
if emlak_turu == "Daire":
    st.subheader("🏡 Balkon & Teras Bilgileri")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        balkon_bilgi = st.text_input("🎨 Balkon Bilgisi (örn: 2 balkonlu, 1 kapalı balkon, geniş balkon)")
    with col_b2:
        teras_var = st.checkbox("🌿 Teraslı")

# Isıtma & Klima
if emlak_turu not in ["Arsa", "Tarla"]:
    st.subheader("🌀 Isıtma & Klima Sistemi")
    isitma_secilen = st.multiselect(
        "Birden fazla seçebilirsiniz",
        ["Doğalgaz Kombi", "Yerden Isıtma", "Merkezi Isıtma (pay ölçerli)",
         "Merkezi Isıtma (merkezi paylaşımlı)", "Klimalı (multi/inverter)", "Klimalı (standart)",
         "Kat Kaloriferi", "Sobalı", "Isıtma Yok"]
    )

# Tapu
if ilan_turu == "🟢 Satılık":
    st.subheader("📜 Tapu Bilgileri")
    tapu_options = ["Kat Mülkiyeti", "Kat İrtifaklı", "Hisseli Tapu", "İskanlı", "İskansız", "Arsa Tapulu"]
    if emlak_turu == "Tarla":
        tapu_options.append("Tarım Arazisi Tapusu")
    tapu = st.multiselect("Tapu Durumu", tapu_options)

# 5. Özellikler
st.subheader("✅ İlan Özellikleri (Çoklu Seçim)")
tab1, tab2, tab3, tab4 = st.tabs(["Konum & Çevre", "Bina & Site", "İç Özellikler", "Teknik & Ekstra"])

with tab1:
    konum_oz = st.multiselect("Konum avantajları",
        ["Şehir merkezine yakın", "AVM yakın", "Çarşı yakın", "Toplu taşıma durağına yakın",
         "Okul yakın", "Hastane yakın", "Eczane yakın", "Market yakın",
         "Park/yeşil alan yakın", "Deniz manzaralı", "Ulaşım kolay (E-5/TEM)", "Köşe parsel"])
    manzara = st.multiselect("Manzara",
        ["Deniz", "Şehir", "Cadde", "Doğa/Orman", "Panoramik"])

with tab2:
    bina_oz = []
    if emlak_turu not in ["Arsa", "Tarla"]:
        bina_oz = st.multiselect("Bina & Site özellikleri",
            ["Asansör", "Kapalı otopark", "Açık otopark", "7/24 güvenlik", "Kamera sistemi",
             "Site içinde", "Kapıcı", "Çocuk parkı", "Yüzme havuzu", "Spor salonu", "Jeneratör"])

with tab3:
    ic_oz = []
    if emlak_turu == "Daire":
        ic_oz = st.multiselect("Daire içi özellikler",
            ["Geniş ferah", "Ebeveyn banyolu", "Giyinme odası", "Ankastre mutfak", "Çamaşır odası",
             "Çelik kapı", "Görüntülü diafon", "Laminant parke"])
    elif emlak_turu in ["Dükkan / Mağaza", "Ofis / İşyeri"]:
        ic_oz = st.multiselect("İç özellikler",
            ["Vitrinli", "Yüksek tavan", "WCli", "Hazır bölmeli", "Boyalı&Temiz", "Klimalı",
             "Panjur/Kepenk", "Yangın çıkışı", "Asma tavan", "Spot aydınlatma"])
    cephe = st.multiselect("Cephe", ["Güney", "Kuzey", "Doğu", "Batı", "Köşe cephe"])

with tab4:
    teknik_oz = st.multiselect("Teknik & Diğer",
        ["Deprem yönetmeliğine uygun", "Fiber internet", "Uydu altyapısı", "Eşyalı",
         "Takas mümkün", "Krediye uygun", "Kira getirisi yüksek"])

# Özellikleri birleştir
secilen_oz = konum_oz + manzara + bina_oz + ic_oz + cephe + teknik_oz + isitma_secilen
if emlak_turu == "Daire" and teras_var:
    secilen_oz.append("Teraslı")
secilen_madde = [f"• {oz}" for oz in secilen_oz if oz]

# YENİ: Özel Notlar bölümü
st.subheader("📝 Özel Notlar (İsteğe bağlı)")
ozel_notlar = st.text_area(
    "İlanla ilgili özel notlarınızı buraya yazın (her satır ayrı bir not olabilir):",
    height=150,
    placeholder="Örn:\nSahibi acil satmak istiyor\nTakas kabul edebilir\nEmlakçıya özel bilgi: Görüşme için önceden ara..."
)

# İLAN OLUŞTUR
if st.button("🚀 İLANI OLUŞTUR", type="primary", use_container_width=True):
    # Fiyat/Kira
    if ilan_turu == "🟢 Satılık":
        if fiyat_gir:
            temiz = re.sub(r'[^0-9]', '', str(fiyat_gir).strip())
            try:
                fiyat = int(temiz)
                if fiyat > 0:
                    fiyat_metni = f"{fiyat:,}.000 TL".replace(",", ".")
                else:
                    fiyat_metni = "İletişime geçiniz"
            except ValueError:
                fiyat_metni = "İletişime geçiniz"
        else:
            fiyat_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 FİYAT: {fiyat_metni} 💰"
    else:
        if kira_gir:
            temiz = re.sub(r'[^0-9]', '', str(kira_gir).strip())
            try:
                kira = int(temiz)
                if kira > 0:
                    kira_metni = f"{kira:,}.- TL".replace(",", ".")
                else:
                    kira_metni = "İletişime geçiniz"
            except ValueError:
                kira_metni = "İletişime geçiniz"
        else:
            kira_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 AYLIK KİRA: {kira_metni} 💰"
        if depozito_gir:
            temiz_depo = re.sub(r'[^0-9]', '', str(depozito_gir).strip())
            try:
                depo = int(temiz_depo)
                if depo > 0:
                    depo_metni = f"{depo:,}.- TL".replace(",", ".")
                    fiyat_satiri += f"\n🔒 DEPOZİTO: {depo_metni}"
            except ValueError:
                pass

    # Başlık ve metinler
    base_name = emlak_turu if emlak_turu != "Daire" else "DAİRE"
    islem_kisa = "SATILIK" if ilan_turu == "🟢 Satılık" else "KİRALIK"

    ton_metni = {
        "luks": (f"EKİN GAYRİMENKUL'DEN {islem_kisa} ULTRA LÜKS {base_name.upper()} 🏰",
                 f"En prestijli lokasyonda, üst düzey işçilik ve malzemelerle donatılmış eşsiz bir {emlak_turu.lower()}!",
                 "Elit yaşamın ve yüksek getirinin adresi, kaçırılmayacak fırsat!"),
        "modern": (f"EKİN GAYRİMENKUL'DEN {islem_kisa} MODERN {base_name.upper()} 🏢",
                   f"Merkezi konumda, şık tasarım ve kaliteli donanımıyla dikkat çeken modern bir {emlak_turu.lower()}.",
                   "Konfor, erişilebilirlik ve değer artışı bir arada."),
        "firsat": (f"EKİN GAYRİMENKUL'DEN {islem_kisa} FIRSAT {base_name.upper()} 💎",
                   f"Yüksek potansiyelli bölgede, uygun fiyatıyla hem kullanım hem yatırım için ideal {emlak_turu.lower()}.",
                   "Değerini hızla katlayacak bu fırsatı değerlendirin!")
    }

    if emlak_turu in ["Arsa", "Tarla"]:
        base_name = "ARSA" if emlak_turu == "Arsa" else "TARLA"
        ton_metni = {
            "luks": (f"EKİN GAYRİMENKUL'DEN YATIRIMA ÇOK UYGUN {base_name} 🌟",
                     f"Şehrin gelişen bölgesinde, yüksek prim potansiyelli {emlak_turu.lower()}!",
                     "Geleceğin kazanç kapısı bu {emlak_turu.lower()}da!"),
            "modern": (f"EKİN GAYRİMENKUL'DEN {base_name} İMARLI & HAZIR 🏞️",
                       f"Tüm altyapısı tamam, hemen kullanım için uygun {emlak_turu.lower()}.",
                       "Hayalinizdeki projeyi hayata geçirmek için ideal!"),
            "firsat": (f"EKİN GAYRİMENKUL'DEN FIRSAT {base_name} 💎",
                       f"Bütçe dostu fiyata, değeri hızla yükselen bölgede {emlak_turu.lower()}!",
                       "Yatırımın en güvenli adresi!")
        }

    baslik, giris, kapanis = ton_metni[ton_key]

    ilan = f"🏠 {baslik} 🏠\n\n"

    # Konum
    if ilce or mahalle:
        konum_str = il
        if ilce: konum_str += f" / {ilce}"
        if mahalle: konum_str += f" / {mahalle}"
        ilan += f"📍 Konum: {konum_str}\n\n"

    # Detaylar
    ilan += "🔹 DETAYLAR 🔹\n"
    if emlak_turu in ["Arsa", "Tarla"]:
        if arsa_donum:
            try:
                donum = float(arsa_donum.replace(",", "."))
                if donum < 1:
                    m2 = int(donum * 1000)
                    ilan += f"• {'Arsa' if emlak_turu == 'Arsa' else 'Tarla'} Alanı: {donum} dönüm ({m2} m²)\n"
                else:
                    ilan += f"• {'Arsa' if emlak_turu == 'Arsa' else 'Tarla'} Alanı: {donum} dönüm\n"
            except ValueError:
                ilan += f"• {'Arsa' if emlak_turu == 'Arsa' else 'Tarla'} Alanı: {arsa_donum} dönüm\n"
        if imar_durumu: ilan += f"• İmar: {imar_durumu}\n"
        if yol_durumu != "Bilinmiyor":
            ilan += f"• Yol Durumu: {yol_durumu}\n"
    else:
        if oda_bilgi: ilan += f"• {'Oda' if emlak_turu == 'Daire' else 'Düzen'}: {oda_bilgi}\n"
        if alan_net or alan_brut:
            ilan += f"• Alan: {alan_net or '?'} m² net / {alan_brut or '?'} m² brüt\n"
        if kat_bilgi: ilan += f"• Kat: {kat_bilgi}\n"
        if bina_kat_sayisi: ilan += f"• Bina: {bina_kat_sayisi} katlı\n"
        if yas: ilan += f"• Yaş: {yas}\n"
        if aidat: ilan += f"• Aidat: {aidat}\n"
        if cephe_metre: ilan += f"• Cephe: {cephe_metre} metre\n"
        if emlak_turu == "Daire" and balkon_bilgi:
            ilan += f"• Balkon: {balkon_bilgi}\n"
        if isitma_secilen:
            aktif_isitma = [i for i in isitma_secilen if i != "Isıtma Yok"]
            if aktif_isitma:
                ilan += f"• Isıtma: {', '.join(aktif_isitma)}\n"
            elif "Isıtma Yok" in isitma_secilen:
                ilan += "• Isıtma: Yok\n"

    # Krediye Uygunluk
    if ilan_turu == "🟢 Satılık" and kredi_uygun != "Bilinmiyor":
        ilan += f"• Krediye Uygunluk: {kredi_uygun}\n"

    if tapu: ilan += f"• Tapu: {', '.join(tapu)}\n"
    ilan += "\n"

    ilan += f"{fiyat_satiri}\n\n"
    ilan += f"{giris}\n\n"

    if secilen_madde:
        ilan += "⭐ ÖNE ÇIKAN ÖZELLİKLER ⭐\n" + "\n".join(secilen_madde) + "\n\n"

    ilan += f"{kapanis}\n\n"

    # Hashtag'ler
    hashtag_list = ["#EkinGayrimenkul", "#Emlak", "#Gayrimenkul"]
    hashtag_list.append("#Satılık" if ilan_turu == "🟢 Satılık" else "#Kiralık")
    hashtag_list.append(f"#{emlak_turu.replace(' / ', '').replace(' ', '')}")
    if ilce: hashtag_list.append(f"#{ilce.replace(' ', '')}")
    if mahalle: hashtag_list.append(f"#{mahalle.split()[0]}Mah")
    if ton_key == "luks": hashtag_list += ["#LüksEmlak", "#Prestij"]
    elif ton_key == "modern": hashtag_list += ["#ModernTasarım", "#Konfor"]
    else: hashtag_list += ["#Fırsat", "#Yatırım"]

    ilan += " ".join(hashtag_list) + "\n\n"

    ilan += "📞 Hemen bilgi ve görüşme için arayın:\n"
    ilan += "📞 0545 920 03 46\n📞 0545 920 03 40\n\n"
    ilan += "EKİN GAYRİMENKUL DANIŞMANLIĞI\nHayallerinize profesyonel dokunuş ✨"

    # YENİ: Özel Notlar ekleme
    if ozel_notlar.strip():
        ilan += "\n\n📝 ÖZEL NOTLAR:\n"
        ilan += ozel_notlar.strip() + "\n"

    st.success("✅ İlan başarıyla hazırlandı!")

    st.markdown("### 📋 Oluşturulan İlan")
    st.text_area("İlan Metni (Ctrl+A → Ctrl+C ile kopyala)", ilan, height=650)

    st.info("💡 Tüm platformlarda (Sahibinden, Hepsiemlak, WhatsApp, Instagram) doğrudan kullanabilirsiniz!")
