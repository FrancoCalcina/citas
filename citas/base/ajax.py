from django.views import View
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
import json
from django.http import HttpResponse
from .constant import MSG_NOT_AJAX

class ComboUpdateView(View):
    """!
    Clase que actualiza los datos de un select dependiente de los datos de otro selec

    """

    def get(self, request, *args, **kwargs):
        """!
        Función que obtiene los datos recibidos por el método get

        """

        try:
            if not request.is_ajax():
                return HttpResponse(json.dumps({'result': False, 'error': str(MSG_NOT_AJAX)}))

            
            cod = request.GET.get('option', None)

            
            app = request.GET.get('app', None)

           
            mod = request.GET.get('mod', None)

           
            field = request.GET.get('field', None)

            
            n_value = request.GET.get('n_value', None)

         
            n_text = request.GET.get('n_text', None)

            
            bd = request.GET.get('bd', 'default')

            filter = {}

            if app and mod and field and n_value and n_text and bd:
                model = apps.get_model(app, mod)

                if cod:
                    filter = {field: cod}

                out = "<option value=''>%s...</option>" % str(_("Seleccione"))

                combo_disabled = "false"

                if cod != "" and cod != "0":
                    for o in model.objects.using(bd).filter(**filter).order_by(n_text):
                        out = "%s<option value='%s'>%s</option>" \
                              % (out, str(o.__getattribute__(n_value)),
                                 o.__getattribute__(n_text))
                else:
                    combo_disabled = "true"

                return HttpResponse(json.dumps({'result': True, 'combo_disabled': combo_disabled, 'combo_html': out}))

            else:
                return HttpResponse(json.dumps({'result': False,
                                                'error': str(_('No se ha especificado el registro'))}))

        except Exception as e:
            return HttpResponse(json.dumps({'result': False, 'error': e}))
