# -*- coding: utf-8 -*-
from django.core.management.base import CommandError
from mieli.cli import MieliCommand
from django.core import management
from django.core.mail import send_mail
from mieli.api import user, organization
from django.conf import settings
import random
import string
import time

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where load will be done',
            required=True)

    def send_notification(self, to, raw_password, org):
        subject = u"Comú de Lleida: Recordatori d'usuari i contrasenya per a la votació sobre la participació del Comú de Lleida el 26J"
        msg = u"""Respecte a la votació oberta sobre la participació del Comú de Lleida al 26J, com a membre pots participar-hi amb les següents credencials:

  - Usuari: %s
  - Contrasenya: %s


Entra a https://participa.comudelleida.cat/identity/login/ i empra-les per a identificar-te. Et recomanem canviar la contrasenya a 'Canviar contrasenya'.

Recorda, la proposta d'acord és la següent:

El Comú de Lleida va a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem i condiciona la seua participació a:

  - La signatura dels acords polítics que inclouen els documents proposta de codi ètic [0] i l'annex als estatuts de la coalició [1], orientats a millorar la transparència, el rendiment de comptes i els mecanismes de participació ciutadana.
  - Mantenir, si s'escau, la mateixa llista electoral però amb un major equilibri de protagonisme dels diferents actors confluents.

I les opcions de vot:

  - Estic a favor que el Comú de Lleida participi a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem segons els termes de la proposta d'acord.
  - Estic en contra que el Comú de Lleida participi a les eleccions generals del 26J.

Si vols ampliar informació, aquí tens el resum de l'assemblea [2].

Gràcies,
Comú de Lleida

[0] http://comudelleida.cat/wp-content/uploads/PROPOSTA-CODI-%%C3%%88TIC-PER-A-ECP-Ponent.docx
[1] http://comudelleida.cat/wp-content/uploads/ANEXO-A-LOS-ESTATUTOS-DE-LA-COALICI%%C3%%93N.docx
[2] http://comudelleida.cat/wp-content/uploads/Resum-aportacions-assemblea-dijous-12-de-maig.pdf
""" % (to.username.split('@')[0], raw_password)
        html_msg = u"""<p>Respecte a la votació oberta sobre la participació del Comú de Lleida al 26J, com a membre pots participar-hi amb les següents credencials:</p>
<ul>
<li>Usuari: %s</li>
<li>Contrasenya: %s</li>
</ul>
<p>Entra a <a href="https://participa.comudelleida.cat/identity/login/">https://participa.comudelleida.cat/identity/login/</a> i empra-les per a identificar-te. Et recomanem canviar la contrasenya a 'Canviar contrasenya'.</p>
<p>Recorda, la <strong>proposta d'acord</strong> és la següent:</p>
<p>El Comú de Lleida va a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem i condiciona la seua participació a:</p>
<ul>
<li>La signatura dels acords polítics que inclouen els documents <a href="http://comudelleida.cat/wp-content/uploads/PROPOSTA-CODI-%%C3%%88TIC-PER-A-ECP-Ponent.docx">proposta de codi ètic</a> i l'<a href="http://comudelleida.cat/wp-content/uploads/ANEXO-A-LOS-ESTATUTOS-DE-LA-COALICI%%C3%%93N.docx">annex als estatuts de la coalició</a>, orientats a millorar la transparència, el rendiment de comptes i els mecanismes de participació ciutadana.</li>
<li>Mantenir, si s'escau, la mateixa llista electoral però amb un major equilibri de protagonisme dels diferents actors confluents.</li>
</ul>
<p>I les <strong>opcions de vot</strong>:</p>
<ul>
<li>Estic a favor que el Comú de Lleida participi a les eleccions generals del 26J donant suport a la candidatura de En Comú Podem segons els termes de la proposta d'acord.</li>
<li>Estic en contra que el Comú de Lleida participi a les eleccions generals del 26J.</li>
</ul>
<p>Si vols ampliar informació, aquí tens el <a href="http://comudelleida.cat/wp-content/uploads/Resum-aportacions-assemblea-dijous-12-de-maig.pdf">resum de l'assemblea</a>: <a href="http://comudelleida.cat/wp-content/uploads/Resum-aportacions-assemblea-dijous-12-de-maig.pdf">http://comudelleida.cat/wp-content/uploads/Resum-aportacions-assemblea-dijous-12-de-maig.pdf</a></p>
<p>Gràcies,<br/>Comú de Lleida</p>
""" % (to.username.split('@')[0], raw_password)
        send_mail(subject, msg, org.contact, [ to.email ], fail_silently=False, html_message=html_msg)

    def invoke(self, *args, **options):
        org = organization.get(domain=options['organization'])
        settings.SITE_ID = 13
        forbidden = [
            "enricsantacana@gmail.com",
            "emmaijordi@xtec.cat",
            "ivan.abadia.moreno@gmail.com",
            "dorets@hotmail.com",
            "wester.claes@gmail.com",
            "jmanelg@gmail.com",
            "maeskinas@gmail.com",
            "pausaez@hotmail.com",
            "jovazor68@gmail.com",
            "robertpinol1982@gmail.com",
            "raquel_jf28@hotmail.com",
            "xavier@hotmail.com",
            "tantxuuu@gmail.com",
            "lartdereciclar@hotmail.com",
            "sergi.bertran.pericon@gmail.com",
            "geherag@gmail.com",
            "Ingrid83miguel82@hotmail.com",
            "espejosuros.javier@gmail.com",
            "josrocq@gmail.com",
            "cfgs1.garciaf@gmail.com",
            "immaroige@Hotmail.com",
            "ana.alonso.ba@gmail.com",
            "iamugo@hotmail.com",
            "ahngeoffrey@gmail.com",
            "bruja4@msn.com",
            "cmaal@hotmail.com",
            "marta.alpuentellavall@gmail.com",
            "mirulina3@hotmail.com",
            "mercerb3@gmail.com",
            "cristian_89eb@hotmail.com",
            "odranoeldv@hotmail.com",
            "fxavier.esteve@hotmail.com",
            "mnuria68@gmail.com",
            "claragp97@gmail.com",
            "joanpique@hotmail.com",
            "info@jesusreinoso.es",
            "scastel8@gmail.com",
            "mcarmeri@gmail.com",
            "oniatomas@hotmail.com",
            "ccazcune@hotmail.com",
            "elitomas82@gmail.com",
            "zapadreams@hotmail.com",
            "madoteto3@gmail.com",
            "nikitalare@hotmail.com",
            "romallaspe@gmail.com",
            "eguija@gmail.com",
            "desipeal@hotmail.com",
            "meriolives@hotmail.es",
            "marcsct@hotmail.com",
            "mariajosebermudez22@gmail.com",
            "sergiglo@hotmail.com",
            "gfgorges@gmail.com",
            "rfarrero@xtec.cat",
            "angelamg365@gmail.com",
            "nuriasanta@gmail.com",
            "victorlinde72@hotmail.com",
            "tere_05_1989@hotmail.com",
            "nurhug@gmail.com",
            "ramongrau68@hotmail.com",
            "juanasoto22@gmail.com",
            "anauk171@hotmail.com",
            "melero.bernal.clara@gmail.com",
            "arosa.buixadera@gmail.com",
            "jorgeguro1968@gmail.com",
            "rogaesther@gmail.com",
            "nuriafarre@yahoo.com",
            "oscarbarran@yahoo.com",
            "montse7p@yahoo.es",
            "jalcalde@xtec.cat",
            "danvila@hotmail.com",
            "ventubegue@gmail.com",
            "cristina_0712@hotmail.com",
            "joanescola1@homtial.com",
            "parestorresolanilla@hotmail.com",
            "jacaros_cap@hotmail.com",
            "xbaro@peritax.com",
            "jesus@grupf.com",
            "xell2424@hotmail.com",
            "mcarola123@gmail.com",
            "guidiseco@gmail.com",
            "mariaacosta30@hotmail.com",
            "danielferrerlaboral@gmail.com",
            "pueyo007@hotmail.com",
            "a.arandavazquez@gmail.com",
            "esetete@hotmail.com",
            "mmsqu@gmail.com",
            "mmspui@gmail.com",
            "mestiarte@despatxsm.cat",
            "danielmir23@hotmail.com",
            "keieni24@rambler.ru",
            "sabiola@gmail.com",
            "conchitallavasu@hotmail.com",
            "ercat75@yahoo.es",
            "toni-el-gitano@hotmail.com",
            "sanchezJ@telefonica.net",
            "emmagarcia_24@hotmail.com",
            "lorry_anna7201@yahoo.com",
            "joancastm@gmail.com",
            "carlitosojeda@hotmail.es",
            "xavicarpin@gmail.com",
            "judee06@hotmail.com",
            "ramon_elgitano@hotmail.com",
            "izanzoar1314@hotmail.es",
            "silvia_serrano_n@yahoo.es",
            "silviap82@hotmail.com",
            "Caspe56@hotmail.com",
            "rmm-ramon@hotmail.com",
            "gemmmar@hotmail.com",
            "pepromero3@yahoo.es",
            "fisna2@hotmail.com",
            "xloscos@yahoo.es",
            "xicorubio12@hotmail.com",
            "yisusrm@yahoo.es",
            "jsendra@ono.com",
            "felgalfer@gmail.com",
            "francescvilella@hotmail.com",
            "mvila.morell@gmail.com",
            "jatena@servistock.com",
            "juanxo92@hotmail.com",
            "largiles@xtec.cat",
            "joannito23@gmail.com",
            "nlabartr@xtec.cat",
            "vfigueras75@hotmail.com",
            "eugenia.iborra@gmail.com",
            "martinvegasmaria@yahoo.es",
            "aleolmo@gmail.com",
            "lebarcha@gmail.com",
            "cardif24@hotmail.es",
            "minxu4@hotmail.com",
            "anaseral27@gmail.com",
            "chapo@hotmail.com",
            "rodatint@gmail.com",
            "autosprintmecanica@gmail.com",
            "rubenfonseca2@hotmail.com",
            "canoqueraltadam@hotmail.com",
            "javierribes@hotmail.es",
            "antonrts40@gmail.com",
            "raguila6@xtex.cat",
            "ramllaspe@gmail.com",
            "daniyeregui@hotmail.com",
            "fidelnp@gmail.com",
            "toniguiteras@lleida.org",
            "ohnamed@hotmail.com",
            "julia-13-94@hotmail.com",
            "mercur0-x-luna@hotmail.com",
            "albadelsol92@gmail.com",
            "ivanlozaperete@gmail.com",
            "caims@hotmail.es",
            "danimedinarodes@hotmail.com",
            "granvos@gmail.com",
            "angels.real@gmail.com",
            "joan_arnau11@hotmail.com",
            "diegonza1966@gmail.com",
            "ares.mateus.2012@gmail.com",
            "d.anfi88@gmail.com",
            "cristianmpinol@gmail.com",
            "raidtxu@hotmail.com",
            "claraberge@hotmail.com",
            "cesaralbas@hotmail.com",
            "albanaudi@gmail.com",
            "marynel_a@hotmail.com",
            "mtjyunior@yahoo.com",
            "dariojuste@hotmail.com",
            "abuelosaloon@hotmail.com",
            "jesusfilella1975@gmail.com",
            "carmonamanuel@gmail.com",
            "meritxell.prunera@gmail.com",
            "perebadi@msn.com",
            "jcespedes@catsalut.cat",
            "jmigsoro@gmail.com",
            "miulina0307@hotmail.com",
            "lomarracolamarraca@gmail.com",
            "malcolm.hayes@ono.com",
            "milaramanuel@yahoo.com",
            "manoliplopez@hotmail.com",
            "saye@hotmail.es",
            "waslala09@hotmail.com",
            "didacmontero@gmail.com",
            "silviamoyamoll@gmail.com",
            "Eduardo.RodriguezXuarez@e-campus.uab.cat",
            "patriciadelgado.f@gmail.com",
            "jguardia88@gmail.com",
            "amespinar@gmail.com",
            "albertreig77@gmail.com",
            "vicens@cmail.cat",
            "info@merinoadvocats.com",
            "orusra@hotmail.com",
            "sansmartisans@gmail.con",
            "racsofr.ong@gmail.com",
            "earendel_38@hotmail.com",
            "cabaalberto@gmail.com",
            "sebasx5@hotmail.com",
            "lidiapardo@ono.com",
            "lorenagipe@gmail.com",
            "Mireia_ms18@hotmail.com",
            "antonio@agrotecnicadelsegria.com",
            "dolorsortizlopez44@gmail.com",
            "mahafassia@hotmail.com",
            "jordi.roca@macs.udl.cat",
            "imarquezdominguez@gmail.com",
            "JAZAL1@YAHOO.ES",
            "pilar_bosch@hotmail.com",
            "diegoguillenperez@gmail.com",
            "crifijo@gmail.com",
            "Cmv20066@yahoo.es",
            "jchg20085@yahoo.es",
            "sergi.morlok@gmail.com",
            "francinavo@gmail.com",
            "cafuera@gmail.com",
            "gobafna@Yahoo.com",
            "yanucrespi@hotmail.com",
            "david@delorenzo.com",
            "cristina.catarecha@gmail.com",
            "pere.r@me.com",
            "esterribes@hotmail.com",
            "davidgeachacon@yahoo.es"
        ]
        for u in user.from_organization(org):
            if u.email in forbidden:
                continue
            try:
                print(u.username)
                raw_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10))
                u.set_password(raw_password)
                u.save()
                self.send_notification(u, raw_password, org)
                time.sleep(2)
            except Exception as e:
                print(u, e)
