from django.contrib import admin

from django.contrib import admin
from .models import (
    Profile, RiwayatAkademik, Skill, Project, SosialMedia, PesanMasuk
)
 
 
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'tagline', 'kota')
 
 
@admin.register(RiwayatAkademik)
class RiwayatAkademikAdmin(admin.ModelAdmin):
    list_display  = ('institusi', 'jurusan', 'periode', 'urutan')
    list_editable = ('urutan',)
    ordering      = ('urutan', '-tahun_masuk')
 
 
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('nama', 'kategori', 'ikon', 'urutan')
    list_editable = ('urutan',)
    list_filter   = ('kategori',)
 
 
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('judul', 'tanggal', 'unggulan', 'urutan')
    list_editable = ('unggulan', 'urutan')
    list_filter   = ('unggulan',)
 
 
@admin.register(SosialMedia)
class SosialMediaAdmin(admin.ModelAdmin):
    list_display  = ('platform', 'url', 'tampil', 'urutan')
    list_editable = ('tampil', 'urutan')
 
 
@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'subjek', 'dikirim_at', 'sudah_dibaca')
    list_filter  = ('sudah_dibaca',)
    readonly_fields = ('nama', 'email', 'subjek', 'pesan', 'dikirim_at')
 
