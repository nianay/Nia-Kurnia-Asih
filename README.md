Capstone Project Module 3
context

Daegu adalah kota terbesar keempat di Korea Selatan dan merupakan pusat ekonomi dan budaya yang penting. Pasar apartemen di Daegu telah mengalami berbagai dinamika yang dipengaruhi oleh kondisi perekonomian, kebijakan pemerintah, dan perubahan demografi.
Harga apartemen di Daegu bervariasi tergantung pada lokasi, ukuran, dan fasilitas.

Metric Evaluation

Evaluasi metrik yang akan digunakan adalah RMSE, MAE, dan MSE, di mana RMSE adalah nilai rataan akar kuadrat dari error, MAE adalah rataan nilai absolut dari error, sedangkan MAPE adalah rataan persentase error yang dihasilkan oleh model regresi. Semakin kecil nilai RMSE, MAE, dan MAPE yang dihasilkan, berarti model semakin akurat dalam memprediksi harga sewa sesuai dengan limitasi fitur yang digunakan. 
Selain itu, kita juga bisa menggunakan nilai R-squared atau adj. R-squared jika model yang nanti terpilih sebagai final model adalah model linear. Nilai R-squared digunakan untuk mengetahui seberapa baik model dapat merepresentasikan varians keseluruhan data. Semakin mendekati 1, maka semakin fit pula modelnya terhadap data observasi. Namun, metrik ini tidak valid untuk model non-linear.

Attribute Information

HallwayType: Jenis lorong (misalnya, teras, campuran).

TimeToSubway: Waktu yang dibutuhkan untuk mencapai stasiun kereta bawah tanah terdekat (misalnya, 0-5 menit, 10-15 menit).
SubwayStation: Stasiun kereta bawah tanah terdekat.

N_FacilitiesNearBy(ETC): Jumlah fasilitas terdekat (Lainnya).

N_FacilitiesNearBy(PublicOffice): Jumlah kantor publik terdekat.

N_SchoolNearBy(University): Jumlah universitas terdekat.

N_Parkinglot(Basement): Jumlah tempat parkir (di basement).

YearBuilt: Tahun dibangun.

N_FacilitiesInApt: Jumlah fasilitas dalam apartemen.

Size(sqf): Ukuran apartemen dalam kaki persegi.

SalePrice: Harga jual.
