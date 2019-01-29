""" Simple Option module(using QuantLib)

Example1
---------
from simpleOption import *

#Simple Example

o = Option('02/P20500')
op_price = o.v(20625, 20.8, 20190124)
print(f"{o}@{op_price:.2f}  (nk=20625,IV=20.8%)  jan24 ")

OUTPUT 1
---------
02/P20500@285.49  (nk=20625,IV=20.8%)  jan24


Example2
---------
#underlying change: 20625 >>20500

op_price2 = o.v(20500)
print(f"{o}@{op_price2:.2f} (nk=20500,IV=20.8%)  jan24")

OUTPUT 2
---------
02/P20500@285.49  (nk=20625,IV=20.8%)  jan24


Example3
---------
#underlying & IV change: 20625>>20000 &IV=25%
op_price3 = o.v(20000, 25)
print(f"{o}@{op_price3:.2f} (nk=20000,IV=25%)  jan24")

OUTPUT 3
---------
02/P20500@703.62 (nk=20000,IV=25%)  jan24

Example4
---------
#use keyword
op = Option('02/P20500')
op_price4 = op(
    underlying=20250,
    iv=25,
    evaluationDate=20190122
)

"""

import QuantLib as qb
from parse import parse


class Date(qb.Date):
    def __init__(self, intDate):
        self.name = str(intDate)
        year = int(self.name[0:4])
        month = int(self.name[4:6])
        date = int(self.name[6:8])
        super().__init__(date, month, year)


def sqDate(strSQDate):
    """Returns :SQ_Date(qb.Date)
    Parameters
    type1(monthly):  '02'
    type2(weekly) :  '02w3'
    """

    month = int(strSQDate[0:2])
    week = 2 if len(strSQDate) < 2 else int(strSQDate[-1])
    year = qb.Date.todaysDate().year()  # todo:check otherCase
    return qb.Date.nthWeekday(week, 6, month, year)


# init marketData
u = qb.SimpleQuote(20040)
r = qb.SimpleQuote(0.01)
sigma = qb.SimpleQuote(25 / 100)


def setEvaluationDate(date): qb.Settings.instance().setEvaluationDate(date)


def setting(
        underlying=None,
        iv=None,
        evaluationDate=None,
        rate=None):
    """ Market Data Setting """
    if underlying is not None: u.setValue(float(underlying))
    if iv is not None: sigma.setValue(float(iv) / 100)
    if rate is not None: r.setValue(float(rate))
    if evaluationDate is not None: setEvaluationDate(Date(evaluationDate))


def view():
    print(f"EvaluationDate={qb.Settings.instance().evaluationDate}")
    print(f"u={u.value()}")
    print(f"iv={sigma.value()}")


riskFreeCurve = qb.FlatForward(0, qb.Japan(), qb.QuoteHandle(r), qb.Actual360())
volatility = qb.BlackConstantVol(0, qb.Japan(), qb.QuoteHandle(sigma), qb.Actual360())
process = qb.BlackScholesProcess(qb.QuoteHandle(u),
                                 qb.YieldTermStructureHandle(riskFreeCurve),
                                 qb.BlackVolTermStructureHandle(volatility))
engine = qb.AnalyticEuropeanEngine(process)


class Payoff(qb.PlainVanillaPayoff):
    def __init__(self, strPayoff):
        self.name = strPayoff
        x = parse("{op_type}{strike:d}", strPayoff)
        super().__init__(
            qb.Option.Call if x['op_type'] == 'C' else qb.Option.Put, x['strike'])

    def __str__(self): return self.name


class Option(qb.EuropeanOption):
    def __init__(self, strOption):
        self.name = strOption
        x = parse("{sq_date}/{payoff}", strOption)
        self.payoff = Payoff(x['payoff'])
        super().__init__(
            self.payoff, qb.EuropeanExercise(sqDate(x['sq_date'])))
        self.setPricingEngine(engine)

    def __str__(self): return self.name

    def v(self, underlying=None, iv=None, evoluationDate=None):
        setting(underlying, iv, evoluationDate)
        return self.NPV()

    def pay(self, underlying): return self.payoff(float(underlying))
