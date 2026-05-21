from django.shortcuts import render, redirect
from django.contrib   import messages
from django.core.mail import send_mail
from django.conf      import settings

from .models import (
    Profile, RiwayatAkademik, Skill, Project, SosialMedia, PesanMasuk
)

def _base_context():
    profile = Profile.objects.first()
    sosmed  = SosialMedia.objects.filter(tampil=True)
    return {'profile': profile, 'sosmed': sosmed}

def home(request):
    ctx = _base_context()
    return render(request, 'webportofolio/html/home.html', ctx)

def about(request):
    ctx = _base_context()
    ctx['riwayat'] = RiwayatAkademik.objects.all()
    return render(request, 'webportofolio/html/about.html', ctx)

def skills(request):
    ctx = _base_context()

    semua_skill = Skill.objects.all()
    kategori_dict = {}
    for skill in semua_skill:
        label = skill.get_kategori_display()
        kategori_dict.setdefault(label, []).append(skill)

    ctx['kategori_skill'] = kategori_dict
    return render(request, 'webportofolio/html/skills.html', ctx)


def projects(request):
    ctx = _base_context()
    ctx['projects']  = Project.objects.all()
    ctx['unggulan']  = Project.objects.filter(unggulan=True)
    return render(request, 'webportofolio/html/projects.html', ctx)


def contact(request):
    ctx = _base_context()

    if request.method == 'POST':
        nama  = request.POST.get('nama', '').strip()
        email = request.POST.get('email', '').strip()
        subjek = request.POST.get('subjek', '').strip()
        pesan = request.POST.get('pesan', '').strip()

        if nama and email and pesan:
            PesanMasuk.objects.create(
                nama=nama, email=email, subjek=subjek, pesan=pesan
            )


            try:
                send_mail(
                    subject=f"[Portofolio] {subjek or 'Pesan baru dari ' + nama}",
                    message=f"Dari   : {nama} <{email}>\n\n{pesan}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass  

            messages.success(request, 'Pesanmu sudah terkirim! Terima kasih 😊')
            return redirect('contact')
        else:
            messages.error(request, 'Mohon isi semua kolom yang wajib diisi.')

    return render(request, 'webportofolio/html/contact.html', ctx)
