from django.db import models

class Profile(models.Model):
    nama_lengkap   = models.CharField(max_length=100)
    nama_panggilan = models.CharField(max_length=50, blank=True)
    tagline        = models.CharField(max_length=200, help_text="Contoh: UI/UX Designer & Developer")
    foto           = models.ImageField(upload_to='profile/', blank=True, null=True)
    kota           = models.CharField(max_length=100, blank=True)
    negara         = models.CharField(max_length=100, default='Indonesia')
 
    class Meta:
        verbose_name = 'Profile'
 
    def __str__(self):
        return self.nama_lengkap
    
class RiwayatAkademik(models.Model):
    institusi  = models.CharField(max_length=200, help_text="Nama universitas/sekolah")
    jurusan    = models.CharField(max_length=200, blank=True)
    gelar      = models.CharField(max_length=100, blank=True, help_text="Contoh: S.Kom, S.T.")
    tahun_masuk = models.IntegerField()
    tahun_lulus = models.IntegerField(blank=True, null=True, help_text="Kosongkan jika masih berlangsung")
    deskripsi  = models.TextField(blank=True, help_text="Prestasi, aktivitas, dll.")
    urutan     = models.PositiveIntegerField(default=0, help_text="Urutan tampil (0 = paling atas)")
 
    class Meta:
        verbose_name        = 'Riwayat Akademik'
        verbose_name_plural = 'Riwayat Akademik'
        ordering            = ['urutan', '-tahun_masuk']
 
    def __str__(self):
        return f"{self.institusi} ({self.tahun_masuk})"
 
    @property
    def periode(self):
        akhir = self.tahun_lulus if self.tahun_lulus else 'Sekarang'
        return f"{self.tahun_masuk} – {akhir}"
    
KATEGORI_SKILL = [
    ('technical',  'Technical / Hard Skills'),
    ('design',     'Design'),
    ('language',   'Language'),
    ('soft',       'Soft Skills'),
    ('tools',      'Tools & Software'),
    ('other',      'Lainnya'),
]

class Skill(models.Model):
    nama     = models.CharField(max_length=100)
    kategori = models.CharField(max_length=20, choices=KATEGORI_SKILL, default='technical')
    ikon     = models.CharField(
        max_length=100, blank=True,
        help_text="Nama ikon Bootstrap Icons, contoh: bi-code-slash"
    )
    urutan   = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Skill'
        ordering     = ['kategori', 'urutan', 'nama']

    def __str__(self):
        return f"{self.nama} ({self.get_kategori_display()})"

 

class Project(models.Model):
    judul       = models.CharField(max_length=200)
    deskripsi   = models.TextField()
    teknologi   = models.CharField(max_length=300, blank=True, help_text="Pisah dengan koma, contoh: Python, Django, Bootstrap")
    gambar      = models.ImageField(upload_to='projects/', blank=True, null=True)
    url_dokumentasi   = models.URLField(blank=True, help_text="Link Dokumentasi")
    tanggal     = models.DateField(blank=True, null=True)
    unggulan    = models.BooleanField(default=False, help_text="Tampilkan sebagai proyek unggulan")
    urutan      = models.PositiveIntegerField(default=0)
 
    class Meta:
        verbose_name = 'Project'
        ordering     = ['urutan', '-tanggal']
 
    def __str__(self):
        return self.judul
 
    @property
    def list_teknologi(self):
        return [t.strip() for t in self.teknologi.split(',') if t.strip()]
    
class SosialMedia(models.Model):
    PLATFORM = [
        ('instagram', 'Instagram'),
        ('linkedin',  'LinkedIn'),
        ('github',    'GitHub'),
        ('email',     'Email'),
        ('twitter',   'Twitter / X'),
        ('other',     'Lainnya'),
    ]
 
    platform = models.CharField(max_length=20, choices=PLATFORM)
    url      = models.CharField(
        max_length=300,
        help_text="URL lengkap atau alamat email, contoh: https://instagram.com/zahra"
    )
    tampil   = models.BooleanField(default=True)
    urutan   = models.PositiveIntegerField(default=0)
 
    class Meta:
        verbose_name        = 'Sosial Media'
        verbose_name_plural = 'Sosial Media'
        ordering            = ['urutan']
 
    def __str__(self):
        return f"{self.get_platform_display()} — {self.url}"
 
 
class PesanMasuk(models.Model):
    """Menyimpan pesan yang dikirim pengunjung lewat form kontak."""
    nama       = models.CharField(max_length=100)
    email      = models.EmailField()
    subjek     = models.CharField(max_length=200, blank=True)
    pesan      = models.TextField()
    dikirim_at = models.DateTimeField(auto_now_add=True)
    sudah_dibaca = models.BooleanField(default=False)
 
    class Meta:
        verbose_name        = 'Pesan Masuk'
        verbose_name_plural = 'Pesan Masuk'
        ordering            = ['-dikirim_at']
 
    def __str__(self):
        return f"Pesan dari {self.nama} — {self.dikirim_at.strftime('%d %b %Y %H:%M')}"