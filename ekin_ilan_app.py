import streamlit as st

st.set_page_config(page_title="Ekin Gayrimenkul Pro İlan", layout="wide")
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 40px;">
        <img src="logo.png" width="420">
    </div>
    """,
    unsafe_allow_html=True
)
st.title("🏠 EKİN GAYRİMENKUL - PROFESYONEL İLAN OLUŞTURUCU")
st.markdown("Daire, dükkan, ofis, arsa... Her türlü emlak ilanınızı saniyeler içinde profesyonelce hazırlayın!")

# 1. Emlak Türü ve İşlem Seçimi
col_tur1, col_tur2 = st.columns(2)
with col_tur1:
    emlak_turu = st.selectbox("📌 Emlak Türü", ["Daire", "Dükkan / Mağaza", "Ofis / İşyeri", "Arsa"])
with col_tur2:
    ilan_turu = st.radio("İşlem Türü", ["🟢 Satılık", "🔴 Kiralık"], horizontal=True)

# 2. İlan Tonu
st.subheader("📢 İlan Tonu Seçiniz")
if emlak_turu == "Arsa":
    ton_options = ["🌟 Yatırıma Çok Uygun", "🏡 İmarlı & Hazır", "💰 Fırsat Arsa"]
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

# Değişkenleri önceden tanımla (güvenlik için)
oda_bilgi = ""
kat_bilgi = ""
fiyat_gir = ""
kira_gir = ""
depozito_gir = ""
alan_net = ""
alan_brut = ""
bina_kat_sayisi = ""
yas = ""
aidat = ""
arsa_m2 = ""
imar_durumu = ""
cephe_metre = ""
balkon_bilgi = ""
teras_var = False

with col1:
    if emlak_turu in ["Daire", "Dükkan / Mağaza", "Ofis / İşyeri"]:
        oda_bilgi = st.text_input("🛏️ Oda / Bölüm (Daire: 3+1, Dükkan: Açık Alan vb.)")
        kat_bilgi = st.text_input("🏢 Kat (örn: Zemin, 3. Kat)")
    if ilan_turu == "🟢 Satılık":
        fiyat_gir = st.text_input("💰 Satış Fiyatı (rakam, örn: 12500000)")
    else:
        kira_gir = st.text_input("💰 Aylık Kira Bedeli (rakam, örn: 25000)")
        depozito_gir = st.text_input("🔒 Depozito (rakam, örn: 50000)", value="")

with col2:
    if emlak_turu != "Arsa":
        alan_net = st.text_input("📏 Kullanılabilir Alan m² (örn: 120)")
        alan_brut = st.text_input("📐 Brüt / Toplam Alan m² (örn: 150)")
        bina_kat_sayisi = st.text_input("🏢 Bina Kat Sayısı (varsa)")
    else:
        arsa_m2 = st.text_input("🌳 Arsa Alanı m² (örn: 500)")
        imar_durumu = st.text_input("📜 İmar Durumu (örn: Konut İmarlı, 0.60 Emsal)")

with col3:
    if emlak_turu != "Arsa":
        yas = st.text_input("🏗️ Bina Yaşı (örn: Sıfır)")
        aidat = st.text_input("💸 Aidat / Ortak Gider (örn: 1200 TL)")
    if emlak_turu in ["Dükkan / Mağaza", "Ofis / İşyeri"]:
        cephe_metre = st.text_input("🚪 Cephe Genişliği (metre, örn: 8 metre)")

# Balkon & Teras (Sadece Daire için)
if emlak_turu == "Daire":
    st.subheader("🏡 Balkon & Teras Bilgileri")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        balkon_bilgi = st.text_input("🎨 Balkon Bilgisi (örn: 2 balkonlu, 1 kapalı balkon, geniş balkon)")
    with col_b2:
        teras_var = st.checkbox("🌿 Teraslı")

# Isıtma & Klima (Çoklu seçim - Arsa hariç)
if emlak_turu != "Arsa":
    st.subheader("🌀 Isıtma & Klima Sistemi")
    isitma_secilen = st.multiselect(
        "Birden fazla seçenek işaretleyebilirsiniz (örn: Kombi + Yerden Isıtma)",
        [
            "Doğalgaz Kombi",
            "Yerden Isıtma",
            "Merkezi Isıtma (pay ölçerli)",
            "Merkezi Isıtma (merkezi paylaşımlı)",
            "Klimalı (multi/inverter)",
            "Klimalı (standart)",
            "Kat Kaloriferi",
            "Sobalı",
            "Isıtma Yok"
        ],
        help="Gerçek hayatta birçok daire hem kombili hem yerden ısıtmalıdır."
    )
else:
    isitma_secilen = []

# Tapu (Sadece satılık)
if ilan_turu == "🟢 Satılık":
    st.subheader("📜 Tapu Bilgileri")
    tapu = st.multiselect("Tapu Durumu",
        ["Kat Mülkiyeti", "Kat İrtifaklı", "Hisseli Tapu", "İskanlı", "İskansız", "Arsa Tapulu"])
else:
    tapu = []

# 5. Özellikler
st.subheader("✅ İlan Özellikleri (Çoklu Seçim)")
tab1, tab2, tab3, tab4 = st.tabs(["Konum & Çevre", "Bina & Site", "İç Özellikler", "Teknik & Ekstra"])

with tab1:
    konum_oz = st.multiselect("Konum avantajları",
        ["Merkeze yakın", "Cadde üstü", "AVM/Çarşı yakın", "Toplu taşıma yakın",
         "Okul/Hastane yakın", "Deniz manzaralı", "Ulaşım kolay (E-5/TEM)", "Köşe parsel"])
    manzara = st.multiselect("Manzara",
        ["Deniz", "Şehir", "Cadde", "Doğa/Orman", "Panoramik"])

with tab2:
    bina_oz = []
    if emlak_turu != "Arsa":
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

# Tüm özellikleri birleştir (ısıtma + teras dahil)
secilen_oz = konum_oz + manzara + bina_oz + ic_oz + cephe + teknik_oz + isitma_secilen
if emlak_turu == "Daire" and teras_var:
    secilen_oz.append("Teraslı")
secilen_madde = [f"• {oz}" for oz in secilen_oz if oz]

# İLAN OLUŞTUR
if st.button("🚀 İLANI OLUŞTUR", type="primary", use_container_width=True):

    # Fiyat/Kira
    if ilan_turu == "🟢 Satılık":
        if fiyat_gir.isdigit() and fiyat_gir != "0":
            fiyat_metni = f"{int(fiyat_gir):,}.000 TL".replace(",", ".")
        else:
            fiyat_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 FİYAT: {fiyat_metni} 💰"
    else:
        if kira_gir.isdigit():
            kira_metni = f"{int(kira_gir):,}.- TL".replace(",", ".")
        else:
            kira_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 AYLIK KİRA: {kira_metni} 💰"
        if depozito_gir and depozito_gir.isdigit():
            depo_metni = f"{int(depozito_gir):,}.- TL".replace(",", ".")
            fiyat_satiri += f"\n🔒 DEPOZİTO: {depo_metni}"

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

    if emlak_turu == "Arsa":
        ton_metni = {
            "luks": ("EKİN GAYRİMENKUL'DEN YATIRIMA ÇOK UYGUN ARSA 🌟",
                     "Şehrin gelişen bölgesinde, yüksek prim potansiyelli, imarlı arsa!",
                     "Geleceğin kazanç kapısı bu arsada!"),
            "modern": ("EKİN GAYRİMENKUL'DEN İMARLI & HAZIR ARSA 🏡",
                       "Tüm altyapısı tamam, hemen yapılaşmaya uygun köşe parsel arsa.",
                       "Hayalinizdeki projeyi hayata geçirmek için ideal!"),
            "firsat": ("EKİN GAYRİMENKUL'DEN FIRSAT ARSA 💎",
                       "Bütçe dostu fiyata, değeri hızla yükselen bölgede satılık arsa!",
                       "Yatırımın en güvenli adresi: Toprak!")
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
    if emlak_turu != "Arsa":
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
        # Isıtma çoklu
        if isitma_secilen:
            aktif_isitma = [i for i in isitma_secilen if i != "Isıtma Yok"]
            if aktif_isitma:
                ilan += f"• Isıtma: {', '.join(aktif_isitma)}\n"
            elif "Isıtma Yok" in isitma_secilen:
                ilan += "• Isıtma: Yok\n"
    else:
        if arsa_m2: ilan += f"• Arsa Alanı: {arsa_m2} m²\n"
        if imar_durumu: ilan += f"• İmar: {imar_durumu}\n"

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
    ilan += "📞 0545 920 03 40\n📞 0545 920 03 46\n\n"
    ilan += "EKİN GAYRİMENKUL DANIŞMANLIĞI\nHayallerinize profesyonel dokunuş ✨"

    # Sahibinden kısa başlık
    alan_kisa = ""
    if emlak_turu == "Arsa" and arsa_m2:
        alan_kisa = arsa_m2 + "m² "
    elif emlak_turu != "Arsa" and alan_net:
        alan_kisa = alan_net + "m² "

    kisa_baslik = f"{alan_kisa}{ilce or ''} {mahalle or ''} {ilan_turu[2:]} {emlak_turu}".strip()
    kisa_baslik = " ".join(kisa_baslik.split())
    if len(kisa_baslik) > 70:
        kisa_baslik = kisa_baslik[:67] + "..."

    st.success("✅ İlan başarıyla hazırlandı!")

    st.markdown("### 📋 Oluşturulan İlan")
    st.text_area("İlan Metni (Ctrl+A → Ctrl+C ile kopyala)", ilan, height=650)

    st.markdown("### 📌 Sahibinden.com İçin Önerilen Başlık")
    st.code(kisa_baslik, language=None)

    st.info("💡 Tüm platformlarda (Sahibinden, Hepsiemlak, WhatsApp, Instagram) doğrudan kullanabilirsiniz!")
