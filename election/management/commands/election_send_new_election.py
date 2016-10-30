# -*- coding: utf-8 -*-
from django.core.management.base import CommandError
from mieli.cli import MieliCommand
from django.core import management
from django.core.mail import send_mail
from mieli.api import user, organization
from django.conf import settings
import time

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where load will be done',
            required=True)

    def send_notification(self, to, org):
        subject = u"Nova votació del Comú de Lleida: Participació del Comú de Lleida a les eleccions generals del 26J"
        msg = u"""Les 2.254 persones adherides al Comú de Lleida podreu participar des del dilluns 16 de maig i fins el dimecres 18 (a les 00:00 de la nit) en la votació telemàtica per decidir quin paper ha de jugar l'agrupació d'electors en els comicis del 26 de juny. Rebeu aquest correu per poder votar a favor o en contra de la proposta d'acord que va sorgir de l'assemblea del passat dijous. Considerem necessari ampliar a la màxima participació una decisió transcendent i per això hem implementat amb urgència aquest mecanisme de vot telemàtic.

Podeu votar a https://participa.comudelleida.cat/. La proposta d'acord és la següent:

El Comú de Lleida va a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem i condiciona la seua participació a:

- La signatura dels acords polítics que inclouen els documents proposta de codi ètic [0] i l'annex als estatuts de la coalició [1], orientats a millorar la transparència, el rendiment de comptes i els mecanismes de participació ciutadana.
- Mantenir, si s'escau, la mateixa llista electoral però amb un major equilibri de protagonisme dels diferents actors confluents.

Gràcies,
%s

[0] http://comudelleida.cat/wp-content/uploads/PROPOSTA-CODI-%%C3%%88TIC-PER-A-ECP-Ponent.docx
[1] http://comudelleida.cat/wp-content/uploads/ANEXO-A-LOS-ESTATUTOS-DE-LA-COALICI%%C3%%93N.docx
""" % org.name
        html_msg = u"""<p>Les 2.254 persones adherides al Comú de Lleida podreu participar des del dilluns 16 de maig i fins el dimecres 18 (a les 00:00 de la nit) en la <a href="https://participa.comudelleida.cat/">votació telemàtica</a> per decidir quin paper ha de jugar l'agrupació d'electors en els comicis del 26 de juny. Rebeu aquest correu per poder votar a favor o en contra de la proposta d'acord que va sorgir de l'assemblea del passat dijous. Considerem necessari ampliar a la màxima participació una decisió transcendent i per això hem implementat amb urgència aquest mecanisme de vot telemàtic.</p>
<p>Podeu votar a <a href="https://participa.comudelleida.cat/">https://participa.comudelleida.cat/</a>. La <strong>proposta d'acord</strong> és la següent:</p>
<p>El Comú de Lleida va a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem i condiciona la seua participació a:</p>
<ul>
<li>La signatura dels acords polítics que inclouen els documents <a href="http://comudelleida.cat/wp-content/uploads/PROPOSTA-CODI-%%C3%%88TIC-PER-A-ECP-Ponent.docx">proposta de codi ètic</a> i l'<a href="http://comudelleida.cat/wp-content/uploads/ANEXO-A-LOS-ESTATUTOS-DE-LA-COALICI%%C3%%93N.docx">annex als estatuts de la coalició</a>, orientats a millorar la transparència, el rendiment de comptes i els mecanismes de participació ciutadana.</li>
<li>Mantenir, si s'escau, la mateixa llista electoral però amb un major equilibri de protagonisme dels diferents actors confluents.</li>
</ul>
<p>Gràcies,<br/>%s</p>
""" % org.name
        send_mail(subject, msg, org.contact, [ to.email ], fail_silently=False, html_message=html_msg)

    def invoke(self, *args, **options):
        org = organization.get(domain=options['organization'])
        settings.SITE_ID = 13
        forbidden = [
            "krykhaluk@cdl",
            "CARLOS_pruebas@cdl",
            "gmartinez@cdl",
            "montcla@cdl",
            "david6vn@cdl",
            "jop@cdl",
            "mcorder6@cdl",
            "susanajarana@cdl",
            "bernattorelli@cdl",
            "mgalle46@cdl",
            "alexbreso@cdl",
            "lboix@cdl",
            "baldolopezt@cdl",
            "Baldolopezt_mc@cdl",
            "erueloi@cdl",
            "ccasano8@cdl",
            "ibancalzada@cdl",
            "damianot@cdl",
            "roger@cdl",
            "cris_vi@cdl",
            "carlosgonizubieta@cdl",
            "ramoncamatsguardia@cdl",
            "miguemonfort@cdl",
            "elenarelancio@cdl",
            "polpotet@cdl",
            "musicaire@cdl",
            "nopatiskos@cdl",
            "asalazar@cdl",
            "silvestre22gm@cdl",
            "coordinacio@cdl",
            "osistere@cdl",
            "carles18@cdl",
            "jbueno1@cdl",
            "amaia@cdl",
            "juanubieta@cdl",
            "natxopi@cdl",
            "txema2011@cdl",
            "carlos1377@cdl",
            "dccarrr@cdl",
            "antjehey@cdl",
            "fmcanela@cd",
            "laura@cdl",
            "paurrgg@cdl",
            "Elpain_13@cdl",
            "viski51@cdl",
            "virginiasanagustin@cdl",
            "mdolcet@cdl",
            "lamaba53@cdl",
            "dabulle24@cdl",
            "spammoogle@cdl",
            "gabgove@cdl",
            "eduardvalenzuela@cdl",
            "mtrepa3@cdl",
            "ricardsuarez77@cdl",
            "jandro_corbella@cdl",
            "viraoc@cdl",
            "maite@cdl",
            "ecomajuncosas@cdl",
            "malenaoliver@cdl",
            "alfredsesma@cdl",
            "rubenchevecha@cdl",
            "ncasanovas150@cdl",
            "Johanavillarraga@cdl",
            "francesccatala@cdl",
            "carlesvale@cdl",
            "xavier@cdl",
            "paurrgg_p@cdl",
            "Reiganna@cdl",
            "claudiamarchal@cdl",
            "scampanera@cdl",
            "vespre35@cdl",
            "oscarcv84@cdl",
            "imarques84@cdl",
            "rafelsegarra@cdl",
            "cipriano@cdl",
            "sambola2@cdl",
            "sambola2_c@cdl",
            "sambola2_m@cdl",
            "jerofestino@cdl",
            "silvestre22gm_m@cdl",
            "sporte8@cdl",
            "dmolins@cdl",
            "npa1978@cdl",
            "irenesampedro@cdl",
            "rgm@cdl",
            "isaacfg@cdl",
            "elenitablue@cdl",
            "asiuraneta@cdl",
            "lrexach@cdl",
            "eblasia@cdl",
            "judithortiguela@cdl",
            "martasallachopo@cdl",
            "diegocanabal@cdl",
            "nihilant_@cdl",
            "laudvilanova@cdl",
            "rosaprats@cdl",
            "victorcorral93@cdl",
            "joseplleida@cdl",
            "flletjos@cdl",
            "maranses@cdl"
        ]
        for u in user.from_organization(org):
            if u.username in forbidden:
                continue
            try:
                print(u.username)
                self.send_notification(u, org)
                time.sleep(10)
            except Exception as e:
                print(u, e)
