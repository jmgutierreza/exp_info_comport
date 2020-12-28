from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Welcome(Page):
    """Welcome page"""
    def is_displayed(self):
        return self.round_number == 1

class Introduction(Page):
    """Description of the game"""
    def is_displayed(self):
        return self.round_number == 1
    pass


class Game(Page):
    """How to play and returns expected"""


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['precaution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to decide."


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return dict(costo_contagiado=self.player.prob_intrinseca)


page_sequence = [Welcome, Introduction, Game, Contribute, ResultsWaitPage, Results]
