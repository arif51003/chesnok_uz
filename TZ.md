# Tizim Talablari

**Loyiha nomi:** Chesnok.uz
**Tavsif:** Mualliflar yangiliklarni joylay oladigan, oddiy foydalanuvchilar esa ularni o‘qiydigan platforma. Faqat tizimga kirgan foydalanuvchilar o‘zaro interaksiya qila oladi.

---

## Asosiy obyektlar (Entities)

* Post (Maqola/Yangilik)
* User (Foydalanuvchi)
* Category (Kategoriya)
* Tag (Teg)
* Comment (Izoh)
* Like (Layk)

---

## API Talablar

### Postlar

**R1:** Eng ko‘p qidirilgan kalit so‘zlar ro‘yxatini olish.
**R2:** Foydalanuvchilar postlarni kategoriya va teg bo‘yicha filtrlashlari, shu bilan birga kategoriyalar va teglar ro‘yxatini ko‘rishlari kerak.
**R3:** Oxirgi 5 ta trenddagi (mashhur) postlar ro‘yxatini ko‘rish imkoniyati bo‘lishi kerak.
**R4:** Foydalanuvchilar Toshkent shahrining joriy ob-havosini ko‘rishlari kerak.
**R5:** Foydalanuvchilar postlarni (sarlavha, kategoriya, teg) va mualliflar bo‘yicha qidirishlari mumkin bo‘lishi kerak.
**R6:** Postlar bo‘yicha analitika kerak: foydalanuvchilar nimani ko‘proq layk qilayotganini bilishim kerak.
**R7:** Adminlar biznes panelga login/logout qila olishlari kerak.
**R8:** Adminlar barcha obyektlarni boshqara olishlari kerak: post, kategoriya, teg, kasb (profession), foydalanuvchi, izoh.
**R9:** Postlarga rasm, fayl va audio yuklash imkoniyati bo‘lishi kerak.
**R10:** Foydalanuvchilar postlarga layk bosish va izoh qoldirishlari mumkin bo‘lishi kerak. Login qilinmagan holatda ham — faqat analitika uchun.
**R11:** Veb-sayt 3 ta tilda ishlashi kerak: o‘zbek, ingliz, turk.
**R12:** Har bir so‘rov uchun javob vaqtini hisoblaydigan middleware kerak.
**R13:** So‘rovlar sonini daqiqasiga hisoblaydigan va limitdan oshsa bloklaydigan rate limiter middleware kerak.
**R14:** Hech kim platformamni yomon ko‘rmasligi kerak 😄 Barcha nomaqbul (trash) izohlarni o‘chirib tashlaydigan background task yozish kerak.

---

## API Endpointlar

### Postlar

* `GET /posts/` — Postlar ro‘yxati
* `GET /posts/{post_id}` — Bitta postni olish
* `POST /posts/` — Yangi post qo‘shish
* `PUT /posts/{post_id}` — Postni tahrirlash
* `DELETE /posts/{post_id}` — Postni o‘chirish

### Filtrlash

* `GET /posts/?category_id={category_id}&tag_id={tag_id}` — Kategoriya va teg bo‘yicha filtrlash
* `GET /categories/` — Kategoriyalar ro‘yxati
* `GET /tags/` — Teglar ro‘yxati

### Trend postlar

* `GET /posts/trending/` — Trenddagi postlar

### Ob-havo

* `GET /weather/` — Toshkent ob-havosi

### Qidiruv

* `GET /posts/search/?query={query}` — Post va mualliflarni qidirish

### Analitika

* `GET /posts/analytics/` — Postlar analitikasi

### Avtorizatsiya

* `POST /auth/login/` — Login
* `POST /auth/logout/` — Logout

---

## CRUD Amallar

* Post CRUD
* Category CRUD
* Tag CRUD
* Profession CRUD
* User CRUD
* Comment CRUD

-----------------------------------------------------------------------------------------------------------------------------------


# System Requirements

Project Name: Chesnok.uz
Description: News platform that authors can post news, regular users read them and only logged-in users can interact.

## Main Entities

- Post
- User
- Category
- Tag
- Comment
- Like


## APIs

### Posts

R1: Most searched keywords.
R2: Users should be able to filter posts by category and tag, while also seeing list of categories and tags.
R3: Users should be able to see list of last 5 trending posts.
R4: Users should see current weather in Tashkent.
R5: Users should be able to search posts (by title, category and tag) and authors.
R6: I should be able to know analytics about posts: what people are liking most?
R7: Admins should be able to log in/logout to business panel.
R8: Admins should manage all entities: posts, category, tag, profession, user, comment.
R9: I should be able to upload images, files and audios to posts.
R10: Users should be able to like and comment posts. Without logging in, just for analytics.
R11: Website should have 3 languages: Uzbek, English, Turkish.
R12: I need middleware to compute response time per request.
R13: I need rate limiter middleware which counts requests per minute and blocks requests if limit is exceeded.
R14: Noone must dare to hate my platform. Write a background task to delete all trash comments.

- `GET /posts/`
- `GET /posts/{post_id}`
- `POST /posts/`
- `PUT /posts/{post_id}`
- `DELETE /posts/{post_id}`


- `GET /posts/?category_id={category_id}&tag_id={tag_id}`
- `GET /categories/`
- `GET /tags/`


- `GET /posts/trending/`


- `GET /weather/`


- `GET /posts/search/?query={query}`


- `GET /posts/analytics/`


- `POST /auth/login/`
- `POST /auth/logout/`


- posts CRUD
- category CRUD
- tag CRUD
- profession CRUD
- user CRUD
- comment CRUD
