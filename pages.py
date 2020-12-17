from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Introduction(Page):
    """¡Bienvenido! Estás a punto de participar en un experimento económico. Trata de ser cuidadoso con las decisiones que tomes, pues de tus elecciones y las de los demás participantes dependerán tus ganancias. Por ello, lee bien las instrucciones y no empieces el juego hasta estar 100% seguro de haberlas entendido. Las ganancias que obtengas serán proporcionales a los puntos que acumules a lo largo del experimento mediante la tasa de conversión 1 punto = S/ 0.1. Tú puedes ganar hasta un total de S/ 60.00, dependiendo, principalmente, de tu desempeño. Los pagos se realizarán vía transferencia al término del experimento.
       Es importante que no te comuniques, de ninguna manera, con los otros participantes del experimento. Si tienes preguntas o necesitas asistencia, por favor levanta la mano para que un experimentador te ayude. Cualquier violación a esta regla ocasionará que seas retirado del experimento y pierdas el derecho a recibir tu pago. Toda la información sobre tu desempeño en este experimento es anónima y confidencial.
       A continuación, presentaremos las instrucciones del juego."""

    

class GeneralInstructions(Page):
    """ Poner instrucciones aquí (¿cómo añadir ecuaciones o imágenes?) """
    

class SpecificInstructions(Page):
    """ Un último reporte del Ministerio de Salud acaba de confirmar la existencia de una nueva enfermedad respiratoria en el Perú. Hasta el momento, se tiene muy poca información del virus que la ocasiona. Sin embargo, diversos estudios coinciden en lo siguiente:
    (¿cómo añadir ecuaciones, bullets e imágenes?)"""
    

class Choose(Page):
    """Si tuviera que salir a interactuar con los demás, ¿Qué nivel de prevención elegiría?"""

    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Esperando a que los otros participantes ingresen sus niveles de prevención."


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return dict(total_earnings=self.group.total_contribution * Constants.multiplier)


page_sequence = [Introduction, GeneralInstructions, SpecificInstructions, Choose, ResultsWaitPage, Results]
