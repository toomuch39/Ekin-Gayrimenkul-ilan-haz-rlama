import streamlit as st

st.set_page_config(page_title="Ekin Gayrimenkul Pro İlan", layout="wide")

st.image("logo.png", use_container_width=True)

st.title("🏠 EKİN GAYRİMENKUL - PROFESYONEL İLAN OLUŞTURUCU")
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

# Değişkenler
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
arsa_donum = ""  # Arsa ve Tarla için ortak
imar_durumu = ""
cephe_metre = ""
balkon_bilgi = ""
teras_var = False
kredi_uygun = "Bilinmiyor"
yol_durumu = "Bilinmiyor"

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
else:
    isitma_secilen = []

# Tapu
if ilan_turu == "🟢 Satılık":
    st.subheader("📜 Tapu Bilgileri")
    tapu_options = ["Kat Mülkiyeti", "Kat İrtifaklı", "Hisseli Tapu", "İskanlı", "İskansız", "Arsa Tapulu"]
    if emlak_turu == "Tarla":
        tapu_options.append("Tarım Arazisi Tapusu")
    tapu = st.multiselect("Tapu Durumu", tapu_options)
else:
    tapu = []

# Özellikler (değişmedi, kısalttım)
st.subheader("✅ İlan Özellikleri (Çoklu Seçim)")
tab1, tab2, tab3, tab4 = st.tabs(["Konum & Çevre", "Bina & Site", "İç Özellikler", "Teknik & Ekstra"])
# ... (özellik seçimleri aynı kalıyor, kısalttım)

# Özellikleri birleştir (kısaltılmış)
secilen_oz = []  # Gerçek kodda burası dolu olacak
secilen_madde = [f"• {oz}" for oz in secilen_oz if oz]

if st.button("🚀 İLANI OLUŞTUR", type="primary", use_container_width=True):
    # Fiyat düzeltmesi
    if ilan_turu == "🟢 Satılık":
        try:
            fiyat = int(fiyat_gir)
            if fiyat > 0:
                fiyat_metni = f"{fiyat:,}.000 TL".replace(",", ".")
            else:
                fiyat_metni = "İletişime geçiniz"
        except ValueError:
            fiyat_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 FİYAT: {fiyat_metni} 💰"
    else:
        try:
            kira = int(kira_gir)
            if kira > 0:
                kira_metni = f"{kira:,}.- TL".replace(",", ".")
            else:
                kira_metni = "İletişime geçiniz"
        except ValueError:
            kira_metni = "İletişime geçiniz"
        fiyat_satiri = f"💰 AYLIK KİRA: {kira_metni} 💰"
        if depozito_gir:
            try:
                depo = int(depozito_gir)
                if depo > 0:
                    depo_metni = f"{depo:,}.- TL".replace(",", ".")
                    fiyat_satiri += f"\n🔒 DEPOZİTO: {depo_metni}"
            except ValueError:
                pass

    # ... (başlık, giriş, kapanış aynı)

    # Detaylar - Alan kısmı düzeltildi
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
        # Diğer türler aynı

    # ... (ilan metninin geri kalanı aynı kalıyor)

    # Kısa başlık için alan
    alan_kisa = ""
    if emlak_turu in ["Arsa", "Tarla"] and arsa_donum:
        alan_kisa = arsa_donum + " dönüm "
    elif alan_net:
        alan_kisa = alan_net + "m² "

    # ... (gerisi aynı)
