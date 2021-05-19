from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.fields.core import RadioField
from wtforms.fields.simple import SubmitField


class data (Form):
    breathing_problem = RadioField("Apakah anda mengalami gangguan pernapasan?", choices=[
                                   ('Y', 'Ya'), ('T', 'Tidak')])
    fever = RadioField("Apakah anda mengalami demam (suhu >38 derajat)?", choices=[
                       ('Y', 'Ya'), ('T', 'Tidak')])
    dry_cough = RadioField("Apakah anda mengalami batuk kering?", choices=[
                           ('Y', 'Ya'), ('T', 'Tidak')])
    sore_throat = RadioField("Apakah anda mengalami sakit tenggorokan?", choices=[
                             ('Y', 'Ya'), ('T', 'Tidak')])
    running_nose = RadioField("Apakah anda mengalami hidung berair", choices=[
                              ('Y', 'Ya'), ('T', 'Tidak')])
    asthma = RadioField("Apakah anda memiliki riwayat penyakit asma?", choices=[
                        ('Y', 'Ya'), ('T', 'Tidak')])
    cronicc_lung_disease = RadioField(
        "Apakah anda memiliki riwayat penyakit paru-paru kronis?", choices=[('Y', 'Ya'), ('T', 'Tidak')])
    headache = RadioField("Apakah anda mengalami sakit kepala?", choices=[
                          ('Y', 'Ya'), ('T', 'Tidak')])
    heart_disease = RadioField("Apakah anda memiliki penyakit jantung?", choices=[
                               ('Y', 'Ya'), ('T', 'Tidak')])
    diabetes = RadioField("Apakah anda memiliki riwayat penyakit diabetes?", choices=[
                          ('Y', 'Ya'), ('T', 'Tidak')])
    hypertension = RadioField("Apakah anda memiliki hipertensi (darah tinggi)", choices=[
                              ('Y', 'Ya'), ('T', 'Tidak')])
    fatigue = RadioField("Apakah anda merasa kelelahan?",
                         choices=[('Y', 'Ya'), ('T', 'Tidak')])
    gastro = RadioField("Apakah anda memiliki masalah pencernaan atau lambung?", choices=[
                        ('Y', 'Ya'), ('T', 'Tidak')])
    abroad_travel = RadioField("Apakah anda dalam waktu 14 hari ini melakukan perjalanan keluar negeri?", choices=[
                               ('Y', 'Ya'), ('T', 'Tidak')])
    contact = RadioField("Apakah anda pernah melakukan kontak dengan seorang pengidap COVID dalam waktu 14 hari ini?", choices=[
                         ('Y', 'Ya'), ('T', 'Tidak')])
    attend_large_gath = RadioField("Apakah dalam waktu 14 hari ini anda menghadiri pertemuan yang dihari oleh banyak orang? ", choices=[
                                   ('Y', 'Ya'), ('T', 'Tidak')])
    visited_public = RadioField("Apakah dalam waktu 14 hari ini anda mengunjungi tempat publik?", choices=[
                                ('Y', 'Ya'), ('T', 'Tidak')])
    fams_working_in_pub = RadioField(
        "Apakah ada keluarga anda yang bekerja di tempat umum?", choices=[('Y', 'Ya'), ('T', 'Tidak')])
    wearing_mask = RadioField("Apakah anda tetap menggunakan masker?", choices=[
                              ('Y', 'Ya'), ('T', 'Tidak')])
    sanitation_from_market = RadioField(
        "Apakah anda membersikan/sanitize barang-barang yang dibeli dari supermarket?", choices=[('Y', 'Ya'), ('T', 'Tidak')])

    kirim = SubmitField("Kirim")
