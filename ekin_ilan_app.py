import streamlit as st

st.set_page_config(page_title="Ekin Gayrimenkul Pro İlan", layout="wide")
st.title("🏠 EKİN GAYRİMENKUL - PROFESYONEL İLAN OLUŞTURUCU")
st.markdown("Gerçek ilan siteleri gibi kapsamlı seçeneklerle saniyeler içinde mükemmel ilanlar hazırlayın!")

# İlan Tonu
st.subheader("📢 İlan Tonu Seçiniz")
ton = st.radio("Dairenizin segmentine uygun ton:", 
               ["🌟 Ultra Lüks & Prestijli", "🏡 Modern & Konforlu", "💰 Fırsat & Yatırıma Uygun"],
               horizontal=True)

if "Ultra" in ton:
    ton_key = "luks"
elif "Modern" in ton:
    ton_key = "modern"
else:
    ton_key = "firsat"

# Temel Bilgiler
st.subheader("🔹 Temel Bilgiler")
col1, col2, col3 = st.columns(3)

with col1:
    fiyat_gir = st.text_input("💰 Fiyat (rakam olarak, örn: 6250000)")
    oda = st.text_input("🛏️ Oda Sayısı (örn: 3+1)")
    daire_kat = st.text_input("🏢 Dairenin Bulunduğu Kat (örn: 7)")

with col2:
    net = st.text_input("📏 Net m² (örn: 150)")
    brut = st.text_input("📐 Brüt m² (örn: 180)")
    bina_kat = st.text_input("🏢 Binanın Toplam Kat Sayısı (örn: 12)")

with col3:
    yas = st.text_input("🏗️ Bina Yaşı (örn: Sıfır)")
    aidat = st.text_input("💸 Aidat (örn: 800 TL)")
    krediye = st.selectbox("🏦 Krediye Uygunluk", ["Uygun", "Uygun Değil", "Bilinmiyor"])

# Tapu Durumu
st.subheader("📜 Tapu Bilgileri")
tapu = st.multiselect("Tapu Durumu (birden fazla seçilebilirse belirtin)",
    ["Kat Mülkiyeti Tapu", "Kat İrtifaklı Tapu", "Hisseli Tapu", "İskanlı", "İskansız"])

# Kategorili Özellikler
st.subheader("✅ İlan Özellikleri (Çoklu Seçim)")
tab1, tab2, tab3, tab4 = st.tabs(["Konum & Çevre", "Bina & Site", "Daire İçi", "Teknik & Ekstra"])

with tab1:
    konum_oz = st.multiselect("Konum avantajları",
        ["Şehir merkezine yakın", "AVM, çarşı yürüme mesafesi", "Metro/Metrobüs durağına yakın",
         "Okul, kreş, üniversite yakın", "Hastane, eczane yakın", "Market, pazar, fırın yakın",
         "Park, yeşil alan, yürüyüş yolu", "Deniz/manzara görünümlü", "Ulaşım kolay (E-5/TEM bağlantısı)"])

with tab2:
    bina_oz = st.multiselect("Bina & Site özellikleri",
        ["Asansörlü", "Kapalı otopark", "Açık otopark", "7/24 güvenlik", "Kamera sistemi",
         "Site içinde", "Kapıcı/Görevli", "Çocuk oyun parkı", "Yüzme havuzu (açık/kapalı)",
         "Fitness/Spor salonu", "Sauna/Hamam", "Kamelya/Barbekü alanı", "Jeneratör", "Hidrofor"])

with tab3:
    daire_oz = st.multiselect("Daire içi özellikler",
        ["Geniş ve ferah", "Güney cepheli", "Ebeveyn banyolu", "Giyinme odası",
         "Full ankastre mutfak", "Ada mutfak", "Çamaşır odası", "Kiler/Depo",
         "Çelik kapı", "Görüntülü diafon", "Laminant parke", "Seramik zemin",
         "Balkon (açık/kapalı)", "Teras", "Klimalı (multi/inverter)"])

with tab4:
    teknik_oz = st.multiselect("Teknik & Diğer",
        ["Doğalgaz kombili", "Yerden ısıtma", "Merkezi ısıtma", "Mantolamalı",
         "Deprem yönetmeliğine uygun", "Akıllı ev sistemi", "Yangın alarmı",
         "Fiber internet altyapısı", "Uydu TV hazır", "Eşyalı", "Takas mümkün"])

# Tüm seçilen özellikleri birleştir
secilen_oz = konum_oz + bina_oz + daire_oz + teknik_oz
secilen_madde = [f"• {oz}" for oz in secilen_oz]

if st.button("🚀 İLANI OLUŞTUR", type="primary", use_container_width=True):
    # Fiyat formatlama
    if fiyat_gir.isdigit():
        fiyat = f"{int(fiyat_gir):,}.000 TL".replace(",", ".")
    else:
        fiyat = "İletişime geçiniz"

    # Tonlara göre metinler
    ton_metni = {
        "luks": ("EKİN GAYRİMENKUL'DEN SATILIK ULTRA LÜKS DAİRE 🏰",
                 "Lüleburgaz'ın en prestijli lokasyonunda, modern mimarinin inceliklerini taşıyan, lüks ve konforun zirvesi bir başyapıt!",
                 "Elit yaşamın vazgeçilmezi, yüksek yatırım değeriyle kaçırılmayacak fırsat!"),
        "modern": ("EKİN GAYRİMENKUL'DEN SATILIK MODERN DAİRE 🏠",
                   "Merkezi konumda, ferah tasarımı ve kaliteli işçiliğiyle modern yaşamın tüm konforunu sunan harika bir daire.",
                   "Aileler için ideal, huzurlu ve prestijli bir yaşam alanı."),
        "firsat": ("EKİN GAYRİMENKUL'DEN SATILIK FIRSAT DAİRE 💎",
                   "Değeri hızla yükselen bölgede, uygun fiyatı ve sağlam yapısıyla hem oturum hem yatırım için mükemmel seçenek!",
                   "Yüksek kira getirisi potansiyeliyle dikkat çeken bu daireyi kaçırmayın.")
    }

    baslik, giris, kapanis = ton_metni[ton_key]

    ilan = f"🏠 {baslik} 🏠\n\n"

    # Detaylar
    ilan += "🔹 DETAYLAR 🔹\n"
    if oda: ilan += f"• Oda Sayısı: {oda}\n"
    if net or brut: ilan += f"• Alan: {net or '?'} m² net / {brut or '?'} m² brüt\n"
    if daire_kat or bina_kat: ilan += f"• Kat: {daire_kat or '?'} / {bina_kat or '?'} katlı bina\n"
    if yas: ilan += f"• Bina Yaşı: {yas}\n"
    if aidat: ilan += f"• Aidat: {aidat}\n"
    if krediye != "Bilinmiyor": ilan += f"• Krediye Uygunluk: {krediye}\n"
    if tapu: ilan += f"• Tapu: {', '.join(tapu)}\n"
    ilan += "\n"

    ilan += f"💰 FİYAT: {fiyat} 💰\n\n"
    ilan += f"{giris}\n\n"

    if secilen_madde:
        ilan += "⭐ ÖNE ÇIKAN ÖZELLİKLER ⭐\n" + "\n".join(secilen_madde) + "\n\n"

    ilan += f"{kapanis}\n\n"
    ilan += "📞 Detaylı bilgi ve randevu için hemen arayın:\n"
    ilan += "📞 0545 920 03 40\n📞 0545 920 03 46\n\n"
    ilan += "EKİN GAYRİMENKUL DANIŞMANLIĞI\nProfesyonel hizmetle hayallerinize ulaşıyoruz! ✨"

    st.success("✅ İlan başarıyla hazırlandı!")
    st.code(ilan, language=None)
    st.info("Metni seçip Ctrl+C ile kopyalayın → Sahibinden, WhatsApp, Instagram vs. yapıştırın!")
