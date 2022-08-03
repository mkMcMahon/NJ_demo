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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='What is your area code?', min=100, max=999)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'],  ['X', 'X']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    crt_bat = models.StringField(
        label='''
        What is the name of your favorite living dog?'''
    )

    crt_widget = models.IntegerField(
        label='''
        "If it takes 5 woodchucks 5 minutes to chuck 5 cords,
        how many minutes would it take 100 woodchucks to chuck 100 cords?"
        '''
    )

    crt_lake = models.IntegerField(
        label='''
        How many lasagnas did Garfield the cat eat on Monday morning?
        '''
    )
