from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
doc = """
This is a ten period pandemic-response game
"""


class Constants(BaseConstants):
    name_in_url = 'pandemia'
    players_per_group = 3
    num_rounds = 10
    endowment = c(150)
    instructions_template = 'pandemia/instructions.html'
    prob_intrinseca = int(20)
    prob_contagio = float(0.4)

class Subsession(BaseSubsession):

    def creating_session(self):

        for p in self.get_players():
            if self.round_number == 1:
                p.prob_intrinseca = int(random.randint(c(5),c(50)))
            else:
                p.prob_intrinseca = p.in_round(1).prob_intrinseca


    def vars_for_admin_report(self):
        precautions = [
            p.precaution for p in self.get_players() if p.precaution != None
        ]
        if precautions:
            return dict(
                avg_precaution=sum(precautions) / len(precautions),
                min_precaution=min(precautions),
                max_precaution=max(precautions),
            )
        else:
            return dict(
                avg_precaution='(no data)',
                min_precaution='(no data)',
                max_precaution='(no data)',
            )


class Group(BaseGroup):
    mean_precaution = models.FloatField()

    individual_share = models.FloatField()

    def set_payoffs(self):
        self.mean_precaution = sum([p.precaution for p in self.get_players()])/Constants.players_per_group
        self.individual_share = (
            0.6/ Constants.players_per_group
        )
        for p in self.get_players():
            p.payoff = (Constants.endowment - c(p.precaution) * c(p.precaution))
            p.prob_contagio = p.prob_intrinseca + (5 - 0.4 * p.precaution - 0.6 * self.mean_precaution) * 10





class Player(BasePlayer):

    prob_intrinseca = models.IntegerField()
    precaution = models.IntegerField(
        min=0, max=5, doc="""The level of precaution taken by the player""",
        label="¿Cuánto nivel de precaución elegirás adoptar (del 0 al 5)?" ,
        choices = [0, 1, 2, 3, 4, 5]
    )
    prob_contagio = models.FloatField()
    contagiado = models.IntegerField()
