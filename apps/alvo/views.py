from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import folium
from .models import Alvo


class IndexView(ListView):
    models = Alvo
    template_name = 'index.html'
    queryset = Alvo.objects.all()
    context_object_name = 'alvos'

    def get_context_data(self, **kwargs):
        alvos_obj = Alvo.objects.all()
        brasil = folium.Map(width='100%', height='100%', location=[-16.1237611, -59.9219642], zoom_start=4)

        for alvo in alvos_obj:
            nome_alvo = alvo.nome
            latitude = alvo.latitude
            longitude = alvo.longitude
            folium.Marker([latitude, longitude],
                          popup=nome_alvo,
                          icon=folium.Icon(color='blue', icon='bar-chart', prefix='fa')
                          ).add_to(brasil)

        brasil = brasil._repr_html_()
        context = {
            'map': brasil,
        }

        return context


class CreateAlvoView(CreateView):
    model = Alvo
    template_name = 'alvo_form.html'
    fields = ['nome', 'latitude', 'longitude', 'data_expiracao']
    success_url = reverse_lazy('index')


class UpdateAlvoView(UpdateView):
    model = Alvo
    template_name = 'alvo_form.html'
    fields = ['nome', 'latitude', 'longitude', 'data_expiracao']
    success_url = reverse_lazy('index')


class DeleteAlvoView(DeleteView):
    model = Alvo
    template_name = 'alvo_del.html'
    success_url = reverse_lazy('index')
