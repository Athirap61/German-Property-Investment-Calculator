# coding: utf-8

import decimal


class BigDecimal(decimal.Decimal):
    """Compatibility class for decimal.Decimal"""

    ROUND_DOWN = decimal.ROUND_DOWN
    ROUND_UP = decimal.ROUND_UP

    @classmethod
    def _mk_exp(cls, prec):
        return cls("0." + "0" * prec)

    def divide(self, other, scale=None, rounding=None):
        if not scale and not rounding:
            return BigDecimal(self / other)
        if type(scale) is not int:
            raise ValueError("Expected integer value for scale")
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal((self / other).quantize(exp, rounding=rounding))

    @classmethod
    def valueOf(cls, value):
        return cls(value)

    def multiply(self, other):
        return BigDecimal(self * other)

    def setScale(self, scale, rounding):
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal(self.quantize(exp, rounding=rounding))

    def add(self, other):
        return BigDecimal(self + other)

    def subtract(self, other):
        return BigDecimal(self - other)

    def longValue(self):
        return int(self)

    def compareTo(self, other):
        return BigDecimal(self.compare(other))


BigDecimal.ZERO = BigDecimal(0)
BigDecimal.ONE = BigDecimal(1)
BigDecimal.TEN = BigDecimal(10)


class Lohnsteuer2025:
    TAB1 = [
        BigDecimal.valueOf(0),
        BigDecimal.valueOf(0.4),
        BigDecimal.valueOf(0.384),
        BigDecimal.valueOf(0.368),
        BigDecimal.valueOf(0.352),
        BigDecimal.valueOf(0.336),
        BigDecimal.valueOf(0.32),
        BigDecimal.valueOf(0.304),
        BigDecimal.valueOf(0.288),
        BigDecimal.valueOf(0.272),
        BigDecimal.valueOf(0.256),
        BigDecimal.valueOf(0.24),
        BigDecimal.valueOf(0.224),
        BigDecimal.valueOf(0.208),
        BigDecimal.valueOf(0.192),
        BigDecimal.valueOf(0.176),
        BigDecimal.valueOf(0.16),
        BigDecimal.valueOf(0.152),
        BigDecimal.valueOf(0.144),
        BigDecimal.valueOf(0.14),
        BigDecimal.valueOf(0.136),
        BigDecimal.valueOf(0.132),
        BigDecimal.valueOf(0.128),
        BigDecimal.valueOf(0.124),
        BigDecimal.valueOf(0.12),
        BigDecimal.valueOf(0.116),
        BigDecimal.valueOf(0.112),
        BigDecimal.valueOf(0.108),
        BigDecimal.valueOf(0.104),
        BigDecimal.valueOf(0.1),
        BigDecimal.valueOf(0.096),
        BigDecimal.valueOf(0.092),
        BigDecimal.valueOf(0.088),
        BigDecimal.valueOf(0.084),
        BigDecimal.valueOf(0.08),
        BigDecimal.valueOf(0.076),
        BigDecimal.valueOf(0.072),
        BigDecimal.valueOf(0.068),
        BigDecimal.valueOf(0.064),
        BigDecimal.valueOf(0.06),
        BigDecimal.valueOf(0.056),
        BigDecimal.valueOf(0.052),
        BigDecimal.valueOf(0.048),
        BigDecimal.valueOf(0.044),
        BigDecimal.valueOf(0.04),
        BigDecimal.valueOf(0.036),
        BigDecimal.valueOf(0.032),
        BigDecimal.valueOf(0.028),
        BigDecimal.valueOf(0.024),
        BigDecimal.valueOf(0.02),
        BigDecimal.valueOf(0.016),
        BigDecimal.valueOf(0.012),
        BigDecimal.valueOf(0.008),
        BigDecimal.valueOf(0.004),
        BigDecimal.valueOf(0),
    ]
    """
    Updated for 2025
    """

    TAB2 = [
        BigDecimal.valueOf(0),
        BigDecimal.valueOf(3000),
        BigDecimal.valueOf(2880),
        BigDecimal.valueOf(2760),
        BigDecimal.valueOf(2640),
        BigDecimal.valueOf(2520),
        BigDecimal.valueOf(2400),
        BigDecimal.valueOf(2280),
        BigDecimal.valueOf(2160),
        BigDecimal.valueOf(2040),
        BigDecimal.valueOf(1920),
        BigDecimal.valueOf(1800),
        BigDecimal.valueOf(1680),
        BigDecimal.valueOf(1560),
        BigDecimal.valueOf(1440),
        BigDecimal.valueOf(1320),
        BigDecimal.valueOf(1200),
        BigDecimal.valueOf(1140),
        BigDecimal.valueOf(1080),
        BigDecimal.valueOf(1050),
        BigDecimal.valueOf(1020),
        BigDecimal.valueOf(990),
        BigDecimal.valueOf(960),
        BigDecimal.valueOf(930),
        BigDecimal.valueOf(900),
        BigDecimal.valueOf(870),
        BigDecimal.valueOf(840),
        BigDecimal.valueOf(810),
        BigDecimal.valueOf(780),
        BigDecimal.valueOf(750),
        BigDecimal.valueOf(720),
        BigDecimal.valueOf(690),
        BigDecimal.valueOf(660),
        BigDecimal.valueOf(630),
        BigDecimal.valueOf(600),
        BigDecimal.valueOf(570),
        BigDecimal.valueOf(540),
        BigDecimal.valueOf(510),
        BigDecimal.valueOf(480),
        BigDecimal.valueOf(450),
        BigDecimal.valueOf(420),
        BigDecimal.valueOf(390),
        BigDecimal.valueOf(360),
        BigDecimal.valueOf(330),
        BigDecimal.valueOf(300),
        BigDecimal.valueOf(270),
        BigDecimal.valueOf(240),
        BigDecimal.valueOf(210),
        BigDecimal.valueOf(180),
        BigDecimal.valueOf(150),
        BigDecimal.valueOf(120),
        BigDecimal.valueOf(90),
        BigDecimal.valueOf(60),
        BigDecimal.valueOf(30),
        BigDecimal.valueOf(0),
    ]
    """
    Updated for 2025
    """

    TAB3 = [
        BigDecimal.valueOf(0),
        BigDecimal.valueOf(900),
        BigDecimal.valueOf(864),
        BigDecimal.valueOf(828),
        BigDecimal.valueOf(792),
        BigDecimal.valueOf(756),
        BigDecimal.valueOf(720),
        BigDecimal.valueOf(684),
        BigDecimal.valueOf(648),
        BigDecimal.valueOf(612),
        BigDecimal.valueOf(576),
        BigDecimal.valueOf(540),
        BigDecimal.valueOf(504),
        BigDecimal.valueOf(468),
        BigDecimal.valueOf(432),
        BigDecimal.valueOf(396),
        BigDecimal.valueOf(360),
        BigDecimal.valueOf(342),
        BigDecimal.valueOf(324),
        BigDecimal.valueOf(315),
        BigDecimal.valueOf(306),
        BigDecimal.valueOf(297),
        BigDecimal.valueOf(288),
        BigDecimal.valueOf(279),
        BigDecimal.valueOf(270),
        BigDecimal.valueOf(261),
        BigDecimal.valueOf(252),
        BigDecimal.valueOf(243),
        BigDecimal.valueOf(234),
        BigDecimal.valueOf(225),
        BigDecimal.valueOf(216),
        BigDecimal.valueOf(207),
        BigDecimal.valueOf(198),
        BigDecimal.valueOf(189),
        BigDecimal.valueOf(180),
        BigDecimal.valueOf(171),
        BigDecimal.valueOf(162),
        BigDecimal.valueOf(153),
        BigDecimal.valueOf(144),
        BigDecimal.valueOf(135),
        BigDecimal.valueOf(126),
        BigDecimal.valueOf(117),
        BigDecimal.valueOf(108),
        BigDecimal.valueOf(99),
        BigDecimal.valueOf(90),
        BigDecimal.valueOf(81),
        BigDecimal.valueOf(72),
        BigDecimal.valueOf(63),
        BigDecimal.valueOf(54),
        BigDecimal.valueOf(45),
        BigDecimal.valueOf(36),
        BigDecimal.valueOf(27),
        BigDecimal.valueOf(18),
        BigDecimal.valueOf(9),
        BigDecimal.valueOf(0),
    ]
    """
    Updated for 2025
    """

    TAB4 = [
        BigDecimal.valueOf(0),
        BigDecimal.valueOf(0.4),
        BigDecimal.valueOf(0.384),
        BigDecimal.valueOf(0.368),
        BigDecimal.valueOf(0.352),
        BigDecimal.valueOf(0.336),
        BigDecimal.valueOf(0.32),
        BigDecimal.valueOf(0.304),
        BigDecimal.valueOf(0.288),
        BigDecimal.valueOf(0.272),
        BigDecimal.valueOf(0.256),
        BigDecimal.valueOf(0.24),
        BigDecimal.valueOf(0.224),
        BigDecimal.valueOf(0.208),
        BigDecimal.valueOf(0.192),
        BigDecimal.valueOf(0.176),
        BigDecimal.valueOf(0.16),
        BigDecimal.valueOf(0.152),
        BigDecimal.valueOf(0.144),
        BigDecimal.valueOf(0.14),
        BigDecimal.valueOf(0.136),
        BigDecimal.valueOf(0.132),
        BigDecimal.valueOf(0.128),
        BigDecimal.valueOf(0.124),
        BigDecimal.valueOf(0.12),
        BigDecimal.valueOf(0.116),
        BigDecimal.valueOf(0.112),
        BigDecimal.valueOf(0.108),
        BigDecimal.valueOf(0.104),
        BigDecimal.valueOf(0.1),
        BigDecimal.valueOf(0.096),
        BigDecimal.valueOf(0.092),
        BigDecimal.valueOf(0.088),
        BigDecimal.valueOf(0.084),
        BigDecimal.valueOf(0.08),
        BigDecimal.valueOf(0.076),
        BigDecimal.valueOf(0.072),
        BigDecimal.valueOf(0.068),
        BigDecimal.valueOf(0.064),
        BigDecimal.valueOf(0.06),
        BigDecimal.valueOf(0.056),
        BigDecimal.valueOf(0.052),
        BigDecimal.valueOf(0.048),
        BigDecimal.valueOf(0.044),
        BigDecimal.valueOf(0.04),
        BigDecimal.valueOf(0.036),
        BigDecimal.valueOf(0.032),
        BigDecimal.valueOf(0.028),
        BigDecimal.valueOf(0.024),
        BigDecimal.valueOf(0.02),
        BigDecimal.valueOf(0.016),
        BigDecimal.valueOf(0.012),
        BigDecimal.valueOf(0.008),
        BigDecimal.valueOf(0.004),
        BigDecimal.valueOf(0),
    ]
    """
    Updated for 2025
    """

    TAB5 = [
        BigDecimal.valueOf(0),
        BigDecimal.valueOf(1900),
        BigDecimal.valueOf(1824),
        BigDecimal.valueOf(1748),
        BigDecimal.valueOf(1672),
        BigDecimal.valueOf(1596),
        BigDecimal.valueOf(1520),
        BigDecimal.valueOf(1444),
        BigDecimal.valueOf(1368),
        BigDecimal.valueOf(1292),
        BigDecimal.valueOf(1216),
        BigDecimal.valueOf(1140),
        BigDecimal.valueOf(1064),
        BigDecimal.valueOf(988),
        BigDecimal.valueOf(912),
        BigDecimal.valueOf(836),
        BigDecimal.valueOf(760),
        BigDecimal.valueOf(722),
        BigDecimal.valueOf(684),
        BigDecimal.valueOf(665),
        BigDecimal.valueOf(646),
        BigDecimal.valueOf(627),
        BigDecimal.valueOf(608),
        BigDecimal.valueOf(589),
        BigDecimal.valueOf(570),
        BigDecimal.valueOf(551),
        BigDecimal.valueOf(532),
        BigDecimal.valueOf(513),
        BigDecimal.valueOf(494),
        BigDecimal.valueOf(475),
        BigDecimal.valueOf(456),
        BigDecimal.valueOf(437),
        BigDecimal.valueOf(418),
        BigDecimal.valueOf(399),
        BigDecimal.valueOf(380),
        BigDecimal.valueOf(361),
        BigDecimal.valueOf(342),
        BigDecimal.valueOf(323),
        BigDecimal.valueOf(304),
        BigDecimal.valueOf(285),
        BigDecimal.valueOf(266),
        BigDecimal.valueOf(247),
        BigDecimal.valueOf(228),
        BigDecimal.valueOf(209),
        BigDecimal.valueOf(190),
        BigDecimal.valueOf(171),
        BigDecimal.valueOf(152),
        BigDecimal.valueOf(133),
        BigDecimal.valueOf(114),
        BigDecimal.valueOf(95),
        BigDecimal.valueOf(76),
        BigDecimal.valueOf(57),
        BigDecimal.valueOf(38),
        BigDecimal.valueOf(19),
        BigDecimal.valueOf(0),
    ]
    """
    Updated for 2025
    """

    ZAHL1 = BigDecimal.ONE
    """
    Numbers for often used bigdecimal values ​​in the plan    
    """

    ZAHL2 = BigDecimal(2)
    ZAHL5 = BigDecimal(5)
    ZAHL7 = BigDecimal(7)
    ZAHL12 = BigDecimal(12)
    ZAHL100 = BigDecimal(100)
    ZAHL360 = BigDecimal(360)
    ZAHL500 = BigDecimal(500)
    ZAHL700 = BigDecimal(700)
    ZAHL1000 = BigDecimal(1000)
    ZAHL10000 = BigDecimal(10000)

    def __init__(self, **kwargs):
        # input variables

        # 1 if the application of the factor procedure has been selected (only in tax class IV)
        self.af = 1
        if "af" in kwargs:
            self.setAf(kwargs["af"])

        # The following for the completion of the 64th year of life
        # Calendar year (required if age1 = 1)
        self.AJAHR = 0
        if "AJAHR" in kwargs:
            self.setAjahr(kwargs["AJAHR"])

        # 1, if the 64th year of life was completed at the beginning of the calendar year in which
        # The wage payment period ends (§ 24 a EStG), otherwise = 0
        self.ALTER1 = 0
        if "ALTER1" in kwargs:
            self.setAlter1(kwargs["ALTER1"])

        # entered factor with three decimal places
        self.f = 1.0
        if "f" in kwargs:
            self.setF(kwargs["f"])

        # Annual allowance for determining wage tax for the other remuneration
        # as well as for asset participations according to § 19a paragraph 1 and 4 EStG in accordance with the
        # electronic income tax deduction features according to § 39e EStG or the entry
        # on the certificate for the 2025 income tax deduction in cent (possibly 0)
        self.JFREIB = BigDecimal(0)
        if "JFREIB" in kwargs:
            self.setJfreib(kwargs["JFREIB"])

        # Annual detection amount for the determination of wage tax for the other remuneration
        # as well as for asset participations according to § 19a paragraph 1 and 4 EStG in accordance with the
        # electronic wage tax deduction features according to § 39e EStG or the entry on the
        # Certificate for the 2025 income tax deduction in cent (possibly 0)
        self.JHINZU = BigDecimal(0)
        if "JHINZU" in kwargs:
            self.setJhinzu(kwargs["JHINZU"])

        # An expected annual work wage without other references (i.e. even without
        # the taxable advantages for wealth participations,
        # § 19a paragraph 4 EStG) in cent.
        # Note: The entry of this field (possibly 0) is required for entries for other
        # References (other field).
        # Other payments have already been paid in a previous billing period,
        # So you can add the expected annual work wage. The same applies to too
        # Taxing advantages in asset participations (§ 19a paragraph 4 EStG).
        self.JRE4 = BigDecimal(0)
        if "JRE4" in kwargs:
            self.setJre4(kwargs["JRE4"])

        # Compensation contained in JRE4 according to § 24 number 1 EStG and too taxable
        # Advantages of asset participations (§ 19a paragraph 4 EStG in cent
        self.JRE4ENT = BigDecimal.ZERO
        if "JRE4ENT" in kwargs:
            self.setJre4ent(kwargs["JRE4ENT"])

        # Cents (possibly 0)
        self.JVBEZ = BigDecimal(0)
        if "JVBEZ" in kwargs:
            self.setJvbez(kwargs["JVBEZ"])

        # Merker for the pension flat rate
        # 0 = the employee is in the statutory pension insurance or one
        # Professional pension scheme compulsorily insured or exemption from the
        # Insurance obligation voluntarily insured; The general contribution ceiling applies
        #
        # 1 = if not 0
        #
        self.KRV = 0
        if "KRV" in kwargs:
            self.setKrv(kwargs["KRV"])

        # Cash register individual additional contribution rate for a legally health insured employee
        # in percent (e.g. 2.50 for 2.50 %) with 2 decimal places.
        # The full additional contribution rate must be specified. The division into employee and employer
        # Share takes place in the program process.
        self.KVZ = BigDecimal(0)
        if "KVZ" in kwargs:
            self.setKvz(kwargs["KVZ"])

        # Wage payment period:
        # 1 = year
        # 2 = month
        # 3 = week
        # 4 = day
        self.LZZ = 0
        if "LZZ" in kwargs:
            self.setLzz(kwargs["LZZ"])

        # The characteristic of the employer in accordance with Section 39e EStG
        # or in the certificate for the income tax deduction 2025 registered allowance for the
        # Wage payment period in cent
        self.LZZFREIB = BigDecimal(0)
        if "LZZFREIB" in kwargs:
            self.setLzzfreib(kwargs["LZZFREIB"])

        # The characteristic of the employer in accordance with Section 39e EStG
        # or in the certificate for the income tax deduction 2025 registered add -on amount for the
        # Wage payment period in cent
        self.LZZHINZU = BigDecimal(0)
        if "LZZHINZU" in kwargs:
            self.setLzzhinzu(kwargs["LZZHINZU"])

        # Not too taxable advantages for assets
        # (§ 19a paragraph 1 sentence 4 EStG) in cent
        self.MBV = BigDecimal(0)
        if "MBV" in kwargs:
            self.setMbv(kwargs["MBV"])

        # The employer informed the employee of the employee for private individuals
        # Health or long-term care insurance within the meaning of §10 Paragraph 1 No. 3 EStG 2010
        # as a monthly amount in cent (the value is always in terms of wage payment period
        # to specify as a monthly amount).
        self.PKPV = BigDecimal(0)
        if "PKPV" in kwargs:
            self.setPkpv(kwargs["PKPV"])

        # Health insurance:
        # 0 = statutory health insured workers
        # 1 = exclusively private health insured employees without an employer grant
        # 2 = exclusively private health insured employees with an employer subsidy
        self.PKV = 0
        if "PKV" in kwargs:
            self.setPkv(kwargs["PKV"])

        # Number of contributions to be taken into account at the employee in social long -term care insurance
        # with more than one child
        # 0 = no discount
        # 1 = contribution discount for the 2nd child
        # 2 = contribution discounts for the 2nd and 3rd child
        # 3 = contributions for 2. To 4. Children
        # 4 = contributions for 2. To 5. Or more children
        self.PVA = BigDecimal(0)
        if "PVA" in kwargs:
            self.setPva(kwargs["PVA"])

        # 1, if the special features in Saxony have to be taken into account in social long -term care insurance
        # would have to be taken into account, otherwise 0.
        self.PVS = 0
        if "PVS" in kwargs:
            self.setPvs(kwargs["PVS"])

        # 1, if the employee was awarded the contract for social long -term care insurance
        # has to pay, otherwise 0.
        self.PVZ = 0
        if "PVZ" in kwargs:
            self.setPvz(kwargs["PVZ"])

        # Religious community of the employee according to electronic income tax deduction features or the
        # Certificate for the 2025 income tax deduction (with no religious affiliation = 0)
        self.R = 0
        if "R" in kwargs:
            self.setR(kwargs["R"])

        # Taxable wages for the wage payment period before taking the
        # Pension allowance and the surcharge for the pension allowance, the age relief amount
        # and the characteristic determined as an electronic income tax deduction or in the certificate for
        # the profit tax deduction 2025 for the wage payment period entered or
        # Additional amount in cent
        self.RE4 = BigDecimal(0)
        if "RE4" in kwargs:
            self.setRe4(kwargs["RE4"])

        # Other remuneration, including taxable benefits in asset participations and death benefit for pension payments as well as
        # Capital payments/severance payments, in cent (possibly 0)
        self.SONSTB = BigDecimal(0)
        if "SONSTB" in kwargs:
            self.setSonstb(kwargs["SONSTB"])

        # Compensation contained in otherwise contained according to § 24 number 1 EStG
        self.SONSTENT = BigDecimal.ZERO
        if "SONSTENT" in kwargs:
            self.setSonstent(kwargs["SONSTENT"])

        # Distribution benefit for pension benefits as well as capital payments/severance payments,
        # (contained in otherwise) in cent
        self.STERBE = BigDecimal(0)
        if "STERBE" in kwargs:
            self.setSterbe(kwargs["STERBE"])

        # Tax class:
        # 1 = i
        # 2 = II
        # 3 = III
        # 4 = IV
        # 5 = V
        # 6 = VI
        self.STKL = 0
        if "STKL" in kwargs:
            self.setStkl(kwargs["STKL"])

        # Supplementary benefits included in Cents (possibly 0)
        self.VBEZ = BigDecimal(0)
        if "VBEZ" in kwargs:
            self.setVbez(kwargs["VBEZ"])

        # Prevention of pension in January 2005 or for the first full month
        # in Cents
        self.VBEZM = BigDecimal(0)
        if "VBEZM" in kwargs:
            self.setVbezm(kwargs["VBEZM"])

        # Estimated special payments in the calendar year of the start of care
        # In the case of recovery sensor gear without death benefit, capital payments/severance payments
        # In the case of care in Cents
        self.VBEZS = BigDecimal(0)
        if "VBEZS" in kwargs:
            self.setVbezs(kwargs["VBEZS"])

        # In otherwise contained supply, including death benefit
        # in Cents (possibly 0)
        self.VBS = BigDecimal(0)
        if "VBS" in kwargs:
            self.setVbs(kwargs["VBS"])

        # Year in which the supply cover was for the first time; become
        # Several care contributions paid, the firstest
        self.VJAHR = 0
        if "VJAHR" in kwargs:
            self.setVjahr(kwargs["VJAHR"])

        # Number of freely for children (a decimal point, only for tax classes
        # I, II, III and IV)
        self.ZKF = BigDecimal(0)
        if "ZKF" in kwargs:
            self.setZkf(kwargs["ZKF"])

        # Number of months, for the pension benefits (only
        # required for annual calculation (LZZ = 1)
        self.ZMVB = 0
        if "ZMVB" in kwargs:
            self.setZmvb(kwargs["ZMVB"])

        # output variables

        # Assessment basis for the church wage tax in Cents
        self.BK = BigDecimal(0)

        # Assessment basis of the other remuneration for the church wage tax in cent.
        # Note: Negative amounts that are made from not taxing advantages
        # Approaches (Section 19a paragraph 1 sentence 4 EStG) result, reduce BK
        # (maximum up to 0). The special expenditure deduction for actually provided pension expenses
        # As part of the assessment of income tax, remains unaffected.
        self.BKS = BigDecimal(0)

        # For the wage tax to be reserved for the wage payment period in cents
        self.LSTLZZ = BigDecimal(0)

        # For the wage payment period withheld
        self.SOLZLZZ = BigDecimal(0)

        # Solidarity surcharge for other remuneration (without remuneration for several years in cent.
        # Note: Negative amounts, which are made up of not taxing advantages in the event of asset participation
        # (§ 19a paragraph 1 sentence 4 EStG) result, reduce SolzlZZ (maximum up to 0). The
        # Special expenditure deduction for provisional expenses generated as part of the
        # Intended tax assessment remains unaffected.
        self.SOLZS = BigDecimal(0)

        # Wage tax for other remuneration in cent
        # Note: Negative amounts, which are made up of not taxing advantages in the event of asset participation
        # (§ 19a paragraph 1 sentence 4 EStG) result, reduce LStLZZ (maximum up to 0). The
        # Special expenditure deduction for provisional expenses generated as part of the
        # Intended tax assessment remains unaffected.
        self.STS = BigDecimal(0)

        # Contributions from the employee into account for the wage payment period for
        # Private basic health insurance and private nursing insurance (possibly also
        # the minimum pension flat rate) in cent on the current wages. For the purposes of wage
        # Tax certificate are the individual output values ​​outside the actual wage
        # to add the tax certificate program; The output values ​​must also be added
        # Vkvsonst
        self.VKVLZZ = BigDecimal(0)

        # Contributions from the employee into account for the wage payment period
        # for private basic health insurance and private care compulsory insurance (possibly
        # also the minimum pension flat rate) in cent for other references. The output value can
        # also be negative.
        self.VKVSONST = BigDecimal(0)

        # CONTRICATION FOR COME COLLITATION OF THE WORK SHOULD, in CENT
        self.VFRB = BigDecimal(0)

        # CONTRICATION FOR COME COLLEATION OF THE EARNATION OF THE YOUR AND WORK, CENT
        self.VFRBS1 = BigDecimal(0)

        # CONTRICATION FOR COME COLLEATION OF THE OFFICES, in CENT
        self.VFRBS2 = BigDecimal(0)

        # For the further consideration of the tax allowance according to DBA Türkiye, ZVE available
        # the basic allowance when calculating the ongoing wages, in cent
        self.WVFRB = BigDecimal(0)

        # For the further consideration of the tax allowance according to DBA Türkiye, ZVE available over the basic allowance
        # when calculating the expected annual work wage, in cent
        self.WVFRBO = BigDecimal(0)

        # For the further consideration of the tax allowance according to DBA Türkiye, ZVE available
        # About the basic allowance when calculating the other remuneration, in cent
        self.WVFRBM = BigDecimal(0)

        # internal variables

        # Age relief amount according to the age of the age of €, in €,
        # Cent (2 decimal places)
        self.ALTE = BigDecimal(0)

        # Employee lump sum in euros
        self.ANP = BigDecimal(0)

        # On the wage payment period due to the share of annual values
        # rounded down to entire centers
        self.ANTEIL1 = BigDecimal(0)

        # Assessment basis for age relief amount in €, cent
        # (2 decimal places)
        self.BMG = BigDecimal(0)

        # Contribution limit in statutory health insurance
        # and social long -term care insurance in euros
        self.BBGKVPV = BigDecimal(0)

        # General contribution ceiling in general pension insurance in euros
        self.BBGRV = BigDecimal(0)

        # Difference between ST1 and ST2 in euros
        self.DIFF = BigDecimal(0)

        # Relief amount for single parents in euros
        self.EFA = BigDecimal(0)

        # Pension allowance in €, cent (2 decimal places)
        self.FVB = BigDecimal(0)

        # Pension allowance in €, cent (2 decimal places) for the calculation
        # the wage tax for the other reference
        self.FVBSO = BigDecimal(0)

        # SUCTION OF THE POSITION FORMENT In Euro
        self.FVBZ = BigDecimal(0)

        # Coupling for the pension allowance in euros for the calculation
        # the wage tax in the other reference
        self.FVBZSO = BigDecimal(0)

        # Basic allowance in euros
        self.GFB = BigDecimal(0)

        # Maximum age relief amount in €
        self.HBALTE = BigDecimal(0)

        # Maximum pension allowance in euros, cent (2 decimal places)
        self.HFVB = BigDecimal(0)

        # A real maximum surcharge for pension allowance in €, cent
        # (2 decimal places)
        self.HFVBZ = BigDecimal(0)

        # A real maximum surcharge for pension allowance in €, cent
        # (2 decimal places) for calculating the wage tax for the
        # Other reference
        self.HFVBZSO = BigDecimal(0)

        # Intermediate field to x for the calculation of the tax according to § 39b
        # Para. 2 sentence 7 EStG in €
        self.HOCH = BigDecimal(0)

        # Number of the table values ​​for supply parameters
        self.J = 0

        # Annual tax according to § 51a EStG, from the solidarity surcharge and
        # Assessment basis for the church wage tax are determined in euros
        self.JBMG = BigDecimal(0)

        # On an annual wage of a newly calculated LZZFreib in €, cent
        # (2 decimal places)
        self.JLFREIB = BigDecimal(0)

        # Ged into an annual wage Lzzhinzu in €, cent
        # (2 decimal places)
        self.JLHINZU = BigDecimal(0)

        # Annual value, the proportion of which for a wage payment period in
        # Up content is to be calculated in cents
        self.JW = BigDecimal(0)

        # Number of the table values ​​for parameters in the case of age relief amount
        self.K = 0

        # Sum of the freely for children in euros
        self.KFB = BigDecimal(0)

        # Contribution sentence from the employer to health insurance
        self.KVSATZAG = BigDecimal(0)

        # Contribution rate of the employee on health insurance
        self.KVSATZAN = BigDecimal(0)

        # Key figure for the income tax type type:
        # 1 = basic table
        # 2 = splitting table
        self.KZTAB = 0

        # Annual wage tax in euros
        self.LSTJAHR = BigDecimal(0)

        # Intermediate fields of the annual wage tax in cent
        self.LSTOSO = BigDecimal(0)
        self.LSTSO = BigDecimal(0)

        # Minimum tax for tax classes V and VI in euros
        self.MIST = BigDecimal(0)

        # Contribution rate of the employer on long -term care insurance (6 decimal places)
        self.PVSATZAG = BigDecimal(0)

        # Contribution rate of the employee on long -term care insurance (6 decimal places)
        self.PVSATZAN = BigDecimal(0)

        # Contribution rate of the employee in general statutory pension insurance (4 decimal positions)
        self.RVSATZAN = BigDecimal(0)

        # Calculation value in sliding commadition
        self.RW = BigDecimal(0)

        # Special expenditure lump sum in euros
        self.SAP = BigDecimal(0)

        # Exemption for the solidarity surcharge in euros
        self.SOLZFREI = BigDecimal(0)

        # Solidaritaets surcharge on the annual wage tax in euros, C (2 decimal places)
        self.SOLZJ = BigDecimal(0)

        # Intermediate value for the solidarity surcharge on the annual wage tax
        # in Euro, C (2 decimal places)
        self.SOLZMIN = BigDecimal(0)

        # Rated basis of the solidarity surcharge to check the exemption limit for the solidarity surcharge for other remuneration in euros
        self.SOLZSBMG = BigDecimal(0)

        # Taxable income for the determination of the assessment basis of the solidarity surcharge to check the exemption limit for the solidarity surcharge for other remuneration in euros, cent (2 decimal places)
        self.SOLZSZVE = BigDecimal(0)

        # Assessment basis of the solidarity surcharge for the examination of the exemption limit in the solidarity surcharge for remuneration for several years of activity in euros
        self.SOLZVBMG = BigDecimal(0)

        # Tariff income tax in euros
        self.ST = BigDecimal(0)

        # Tariff income tax on 1.25 times ZX in euros
        self.ST1 = BigDecimal(0)

        # Tariff income tax on the 0.75-fold ZX in euros
        self.ST2 = BigDecimal(0)

        # Assessment basis for the pension allowance in Cents
        self.VBEZB = BigDecimal(0)

        # Assessment basis for the pension allowance in cent for
        # the other reference
        self.VBEZBSO = BigDecimal(0)

        # Intermediate field to x for the calculation of the tax according to § 39b
        # Para. 2 sentence 7 EStG in €
        self.VERGL = BigDecimal(0)

        # HOECHST amount The pension flat rate according to the age of the age of age in euros, C
        self.VHB = BigDecimal(0)

        # Annual value of the contributions to private basic health insurance and
        # private care compulsory insurance (possibly also the minimum pension flat rate) in cent.
        self.VKV = BigDecimal(0)

        # Pension flat rate in euros, C (2 decimal places)
        self.VSP = BigDecimal(0)

        # Pension flat rate according to the age of the age of the age, c
        self.VSPN = BigDecimal(0)

        # Intermediate value 1 when calculating the preventive flat rate after
        # the Age Einkuenftegesetz in Euro, C (2 decimal places)
        self.VSP1 = BigDecimal(0)

        # Intermediate value 2 when calculating the preventive flat rate
        # the Age Einkuenftegesetz in Euro, C (2 decimal places)
        self.VSP2 = BigDecimal(0)

        # Pension flat rate with partial amounts for the statutory health and
        # social long -term care insurance according to fictional amounts or if necessary for the
        # Private basic health insurance and private nursing care insurance
        # in Euro, cent (2 decimal places)
        self.VSP3 = BigDecimal(0)

        # First limit in tax class V/VI in euros
        self.W1STKL5 = BigDecimal(0)

        # Second limit in tax class v/VI in euros
        self.W2STKL5 = BigDecimal(0)

        # Third limit in tax class V/VI in euros
        self.W3STKL5 = BigDecimal(0)

        # Taxable income according to § 32a paragraphs 1 and 2 EStG €, c
        # (2 decimal places)
        self.X = BigDecimal(0)

        # In accordance with Section 32a (1) EStG (6 decimal places)
        self.Y = BigDecimal(0)

        # On an annual wage RE4 in €, C (2 decimal places)
        # after deducting the allowances according to § 39 b (2) sentence 3 and 4.
        self.ZRE4 = BigDecimal(0)

        # On an annual wage RE4 in €, C (2 decimal places)
        self.ZRE4J = BigDecimal(0)

        # On an annual wage RE4 in €, C (2 decimal places)
        # After deducting the pension allowance and the aging relief amount
        # To calculate the pension flat rate in €, cent (2 decimal places)
        self.ZRE4VP = BigDecimal(0)

        # Fixed table allowances (without a pension flat rate) in €, cent
        # (2 decimal places)
        self.ZTABFB = BigDecimal(0)

        # Reduced to an annual wage (VBZ to be negligible FVB) in
        # Euro, C (2 decimal places)
        self.ZVBEZ = BigDecimal(0)

        # To an annual wage, including VBZ in €, C (2 decimal places)
        self.ZVBEZJ = BigDecimal(0)

        # Taxable income in €, C (2 decimal places)
        self.ZVE = BigDecimal(0)

        # Intermediate field to x for the calculation of the tax according to § 39b
        # Para. 2 sentence 7 EStG in €
        self.ZX = BigDecimal(0)

        # Intermediate field to x for the calculation of the tax according to § 39b
        # Para. 2 sentence 7 EStG in €
        self.ZZX = BigDecimal(0)

    def setAf(self, value):
        self.af = value

    def setAjahr(self, value):
        self.AJAHR = value

    def setAlter1(self, value):
        self.ALTER1 = value

    def setF(self, value):
        self.f = value

    def setJfreib(self, value):
        self.JFREIB = BigDecimal(value)

    def setJhinzu(self, value):
        self.JHINZU = BigDecimal(value)

    def setJre4(self, value):
        self.JRE4 = BigDecimal(value)

    def setJre4ent(self, value):
        self.JRE4ENT = BigDecimal(value)

    def setJvbez(self, value):
        self.JVBEZ = BigDecimal(value)

    def setKrv(self, value):
        self.KRV = value

    def setKvz(self, value):
        self.KVZ = BigDecimal(value)

    def setLzz(self, value):
        self.LZZ = value

    def setLzzfreib(self, value):
        self.LZZFREIB = BigDecimal(value)

    def setLzzhinzu(self, value):
        self.LZZHINZU = BigDecimal(value)

    def setMbv(self, value):
        self.MBV = BigDecimal(value)

    def setPkpv(self, value):
        self.PKPV = BigDecimal(value)

    def setPkv(self, value):
        self.PKV = value

    def setPva(self, value):
        self.PVA = BigDecimal(value)

    def setPvs(self, value):
        self.PVS = value

    def setPvz(self, value):
        self.PVZ = value

    def setR(self, value):
        self.R = value

    def setRe4(self, value):
        self.RE4 = BigDecimal(value)

    def setSonstb(self, value):
        self.SONSTB = BigDecimal(value)

    def setSonstent(self, value):
        self.SONSTENT = BigDecimal(value)

    def setSterbe(self, value):
        self.STERBE = BigDecimal(value)

    def setStkl(self, value):
        self.STKL = value

    def setVbez(self, value):
        self.VBEZ = BigDecimal(value)

    def setVbezm(self, value):
        self.VBEZM = BigDecimal(value)

    def setVbezs(self, value):
        self.VBEZS = BigDecimal(value)

    def setVbs(self, value):
        self.VBS = BigDecimal(value)

    def setVjahr(self, value):
        self.VJAHR = value

    def setZkf(self, value):
        self.ZKF = BigDecimal(value)

    def setZmvb(self, value):
        self.ZMVB = value

    def getBk(self):
        return self.BK

    def getBks(self):
        return self.BKS

    def getLstlzz(self):
        return self.LSTLZZ

    def getSolzlzz(self):
        return self.SOLZLZZ

    def getSolzs(self):
        return self.SOLZS

    def getSts(self):
        return self.STS

    def getVkvlzz(self):
        return self.VKVLZZ

    def getVkvsonst(self):
        return self.VKVSONST

    def getVfrb(self):
        return self.VFRB

    def getVfrbs1(self):
        return self.VFRBS1

    def getVfrbs2(self):
        return self.VFRBS2

    def getWvfrb(self):
        return self.WVFRB

    def getWvfrbo(self):
        return self.WVFRBO

    def getWvfrbm(self):
        return self.WVFRBM

    def MAIN(self):
        """
        PROGRAMMABLAUFPLAN, Pap page 13"""
        self.MPARA()
        self.MRE4JL()
        self.VBEZBSO = BigDecimal.ZERO
        self.MRE4()
        self.MRE4ABZ()
        self.MBERECH()
        self.MSONST()

    def MPARA(self):
        """
        Allocation of values ​​for certain social security parameters Pap Page 14"""
        if self.KRV < 1:
            self.BBGRV = BigDecimal(96600)
            self.RVSATZAN = BigDecimal.valueOf(0.093)
        self.BBGKVPV = BigDecimal(66150)
        self.KVSATZAN = (
            self.KVZ.divide(Lohnsteuer2025.ZAHL2)
            .divide(Lohnsteuer2025.ZAHL100)
            .add(BigDecimal.valueOf(0.07))
        )
        self.KVSATZAG = BigDecimal.valueOf(0.0125).add(BigDecimal.valueOf(0.07))
        if self.PVS == 1:
            self.PVSATZAN = BigDecimal.valueOf(0.023)
            self.PVSATZAG = BigDecimal.valueOf(0.013)
        else:
            self.PVSATZAN = BigDecimal.valueOf(0.018)
            self.PVSATZAG = BigDecimal.valueOf(0.018)
        if self.PVZ == 1:
            self.PVSATZAN = self.PVSATZAN.add(BigDecimal.valueOf(0.006))
        else:
            self.PVSATZAN = self.PVSATZAN.subtract(
                self.PVA.multiply(BigDecimal.valueOf(0.0025))
            )
        self.W1STKL5 = BigDecimal(13785)
        self.W2STKL5 = BigDecimal(34240)
        self.W3STKL5 = BigDecimal(222260)
        self.GFB = BigDecimal(12096)
        self.SOLZFREI = BigDecimal(19950)

    def MRE4JL(self):
        """
        Determination of the year wages according to § 39b (2) sentence 2 EStG, Pap Page 15
        """
        if self.LZZ == 1:
            self.ZRE4J = self.RE4.divide(
                Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
            )
            self.ZVBEZJ = self.VBEZ.divide(
                Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
            )
            self.JLFREIB = self.LZZFREIB.divide(
                Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
            )
            self.JLHINZU = self.LZZHINZU.divide(
                Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
            )
        else:
            if self.LZZ == 2:
                self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL12).divide(
                    Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                )
                self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL12).divide(
                    Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                )
                self.JLFREIB = self.LZZFREIB.multiply(Lohnsteuer2025.ZAHL12).divide(
                    Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                )
                self.JLHINZU = self.LZZHINZU.multiply(Lohnsteuer2025.ZAHL12).divide(
                    Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                )
            else:
                if self.LZZ == 3:
                    self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL360).divide(
                        Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN
                    )
                    self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL360).divide(
                        Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN
                    )
                    self.JLFREIB = self.LZZFREIB.multiply(
                        Lohnsteuer2025.ZAHL360
                    ).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(
                        Lohnsteuer2025.ZAHL360
                    ).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                else:
                    self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL360).divide(
                        Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                    )
                    self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL360).divide(
                        Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
                    )
                    self.JLFREIB = self.LZZFREIB.multiply(
                        Lohnsteuer2025.ZAHL360
                    ).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(
                        Lohnsteuer2025.ZAHL360
                    ).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        if self.af == 0:
            self.f = 1

    def MRE4(self):
        """
        Occupations for pension payments, age relief amount (Section 39b (2) sentence 3 EStG), PAP PAGE 16
        """
        if self.ZVBEZJ.compareTo(BigDecimal.ZERO) == 0:
            self.FVBZ = BigDecimal.ZERO
            self.FVB = BigDecimal.ZERO
            self.FVBZSO = BigDecimal.ZERO
            self.FVBSO = BigDecimal.ZERO
        else:
            if self.VJAHR < 2006:
                self.J = 1
            else:
                if self.VJAHR < 2058:
                    self.J = self.VJAHR - 2004
                else:
                    self.J = 54
            if self.LZZ == 1:
                self.VBEZB = self.VBEZM.multiply(BigDecimal.valueOf(self.ZMVB)).add(
                    self.VBEZS
                )
                self.HFVB = (
                    Lohnsteuer2025.TAB2[self.J]
                    .divide(Lohnsteuer2025.ZAHL12)
                    .multiply(BigDecimal.valueOf(self.ZMVB))
                    .setScale(0, BigDecimal.ROUND_UP)
                )
                self.FVBZ = (
                    Lohnsteuer2025.TAB3[self.J]
                    .divide(Lohnsteuer2025.ZAHL12)
                    .multiply(BigDecimal.valueOf(self.ZMVB))
                    .setScale(0, BigDecimal.ROUND_UP)
                )
            else:
                self.VBEZB = (
                    self.VBEZM.multiply(Lohnsteuer2025.ZAHL12)
                    .add(self.VBEZS)
                    .setScale(2, BigDecimal.ROUND_DOWN)
                )
                self.HFVB = Lohnsteuer2025.TAB2[self.J]
                self.FVBZ = Lohnsteuer2025.TAB3[self.J]
            self.FVB = (
                self.VBEZB.multiply(Lohnsteuer2025.TAB1[self.J])
                .divide(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_UP)
            )
            if self.FVB.compareTo(self.HFVB) == 1:
                self.FVB = self.HFVB
            if self.FVB.compareTo(self.ZVBEZJ) == 1:
                self.FVB = self.ZVBEZJ
            self.FVBSO = self.FVB.add(
                self.VBEZBSO.multiply(Lohnsteuer2025.TAB1[self.J]).divide(
                    Lohnsteuer2025.ZAHL100
                )
            ).setScale(2, BigDecimal.ROUND_UP)
            if self.FVBSO.compareTo(Lohnsteuer2025.TAB2[self.J]) == 1:
                self.FVBSO = Lohnsteuer2025.TAB2[self.J]
            self.HFVBZSO = (
                self.VBEZB.add(self.VBEZBSO)
                .divide(Lohnsteuer2025.ZAHL100)
                .subtract(self.FVBSO)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            self.FVBZSO = self.FVBZ.add(
                self.VBEZBSO.divide(Lohnsteuer2025.ZAHL100)
            ).setScale(0, BigDecimal.ROUND_UP)
            if self.FVBZSO.compareTo(self.HFVBZSO) == 1:
                self.FVBZSO = self.HFVBZSO.setScale(0, BigDecimal.ROUND_UP)
            if self.FVBZSO.compareTo(Lohnsteuer2025.TAB3[self.J]) == 1:
                self.FVBZSO = Lohnsteuer2025.TAB3[self.J]
            self.HFVBZ = (
                self.VBEZB.divide(Lohnsteuer2025.ZAHL100)
                .subtract(self.FVB)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            if self.FVBZ.compareTo(self.HFVBZ) == 1:
                self.FVBZ = self.HFVBZ.setScale(0, BigDecimal.ROUND_UP)
        self.MRE4ALTE()

    def MRE4ALTE(self):
        """
        Age relief amount (Section 39b (2) sentence 3 EStG), Pap Page 17"""
        if self.ALTER1 == 0:
            self.ALTE = BigDecimal.ZERO
        else:
            if self.AJAHR < 2006:
                self.K = 1
            else:
                if self.AJAHR < 2058:
                    self.K = self.AJAHR - 2004
                else:
                    self.K = 54
            self.BMG = self.ZRE4J.subtract(self.ZVBEZJ)
            self.ALTE = self.BMG.multiply(Lohnsteuer2025.TAB4[self.K]).setScale(
                0, BigDecimal.ROUND_UP
            )
            self.HBALTE = Lohnsteuer2025.TAB5[self.K]
            if self.ALTE.compareTo(self.HBALTE) == 1:
                self.ALTE = self.HBALTE

    def MRE4ABZ(self):
        """
        Determination of the year wages after deducting the allowances according to § 39b (2) sentence 3 and 4 EStG, Pap Page 20
        """
        self.ZRE4 = (
            self.ZRE4J.subtract(self.FVB)
            .subtract(self.ALTE)
            .subtract(self.JLFREIB)
            .add(self.JLHINZU)
            .setScale(2, BigDecimal.ROUND_DOWN)
        )
        if self.ZRE4.compareTo(BigDecimal.ZERO) == -1:
            self.ZRE4 = BigDecimal.ZERO
        self.ZRE4VP = self.ZRE4J
        self.ZVBEZ = self.ZVBEZJ.subtract(self.FVB).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZVBEZ.compareTo(BigDecimal.ZERO) == -1:
            self.ZVBEZ = BigDecimal.ZERO

    def MBERECH(self):
        """
        Calculation for ongoing wage payment periods page 21"""
        self.MZTABFB()
        self.VFRB = (
            self.ANP.add(self.FVB.add(self.FVBZ))
            .multiply(Lohnsteuer2025.ZAHL100)
            .setScale(0, BigDecimal.ROUND_DOWN)
        )
        self.MLSTJAHR()
        self.WVFRB = (
            self.ZVE.subtract(self.GFB)
            .multiply(Lohnsteuer2025.ZAHL100)
            .setScale(0, BigDecimal.ROUND_DOWN)
        )
        if self.WVFRB.compareTo(BigDecimal.ZERO) == -1:
            self.WVFRB = BigDecimal.valueOf(0)
        self.LSTJAHR = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(
            0, BigDecimal.ROUND_DOWN
        )
        self.UPLSTLZZ()
        self.UPVKVLZZ()
        if self.ZKF.compareTo(BigDecimal.ZERO) == 1:
            self.ZTABFB = self.ZTABFB.add(self.KFB)
            self.MRE4ABZ()
            self.MLSTJAHR()
            self.JBMG = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(
                0, BigDecimal.ROUND_DOWN
            )
        else:
            self.JBMG = self.LSTJAHR
        self.MSOLZ()

    def MZTABFB(self):
        """
        Determination of the fixed table allowances (without a preventive flat rate), Pap Page 22
        """
        self.ANP = BigDecimal.ZERO
        if (
            self.ZVBEZ.compareTo(BigDecimal.ZERO) >= 0
            and self.ZVBEZ.compareTo(self.FVBZ) == -1
        ):
            self.FVBZ = BigDecimal.valueOf(self.ZVBEZ.longValue())
        if self.STKL < 6:
            if self.ZVBEZ.compareTo(BigDecimal.ZERO) == 1:
                if (
                    self.ZVBEZ.subtract(self.FVBZ).compareTo(BigDecimal.valueOf(102))
                    == -1
                ):
                    self.ANP = self.ZVBEZ.subtract(self.FVBZ).setScale(
                        0, BigDecimal.ROUND_UP
                    )
                else:
                    self.ANP = BigDecimal.valueOf(102)
        else:
            self.FVBZ = BigDecimal.valueOf(0)
            self.FVBZSO = BigDecimal.valueOf(0)
        if self.STKL < 6:
            if self.ZRE4.compareTo(self.ZVBEZ) == 1:
                if (
                    self.ZRE4.subtract(self.ZVBEZ).compareTo(BigDecimal.valueOf(1230))
                    == -1
                ):
                    self.ANP = (
                        self.ANP.add(self.ZRE4)
                        .subtract(self.ZVBEZ)
                        .setScale(0, BigDecimal.ROUND_UP)
                    )
                else:
                    self.ANP = self.ANP.add(BigDecimal.valueOf(1230))
        self.KZTAB = 1
        if self.STKL == 1:
            self.SAP = BigDecimal.valueOf(36)
            self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(
                0, BigDecimal.ROUND_DOWN
            )
        else:
            if self.STKL == 2:
                self.EFA = BigDecimal.valueOf(4260)
                self.SAP = BigDecimal.valueOf(36)
                self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(
                    0, BigDecimal.ROUND_DOWN
                )
            else:
                if self.STKL == 3:
                    self.KZTAB = 2
                    self.SAP = BigDecimal.valueOf(36)
                    self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(
                        0, BigDecimal.ROUND_DOWN
                    )
                else:
                    if self.STKL == 4:
                        self.SAP = BigDecimal.valueOf(36)
                        self.KFB = self.ZKF.multiply(BigDecimal.valueOf(4800)).setScale(
                            0, BigDecimal.ROUND_DOWN
                        )
                    else:
                        if self.STKL == 5:
                            self.SAP = BigDecimal.valueOf(36)
                            self.KFB = BigDecimal.ZERO
                        else:
                            self.KFB = BigDecimal.ZERO
        self.ZTABFB = (
            self.EFA.add(self.ANP)
            .add(self.SAP)
            .add(self.FVBZ)
            .setScale(2, BigDecimal.ROUND_DOWN)
        )

    def MLSTJAHR(self):
        """
        Determination annual wage tax, pap page 23
        """
        self.UPEVP()
        self.ZVE = self.ZRE4.subtract(self.ZTABFB).subtract(self.VSP)
        self.UPMLST()

    def UPVKVLZZ(self):
        """
        Pap page 24
        """
        self.UPVKV()
        self.JW = self.VKV
        self.UPANTEIL()
        self.VKVLZZ = self.ANTEIL1

    def UPVKV(self):
        """
        Pap page 24
        """
        if self.PKV > 0:
            if self.VSP2.compareTo(self.VSP3) == 1:
                self.VKV = self.VSP2.multiply(Lohnsteuer2025.ZAHL100)
            else:
                self.VKV = self.VSP3.multiply(Lohnsteuer2025.ZAHL100)
        else:
            self.VKV = BigDecimal.ZERO

    def UPLSTLZZ(self):
        """
        Pap page 25
        """
        self.JW = self.LSTJAHR.multiply(Lohnsteuer2025.ZAHL100)
        self.UPANTEIL()
        self.LSTLZZ = self.ANTEIL1

    def UPMLST(self):
        """
        Determination of the annual wage tax from the income tax tariff. Pap page 26
        """
        if self.ZVE.compareTo(Lohnsteuer2025.ZAHL1) == -1:
            self.ZVE = BigDecimal.ZERO
            self.X = BigDecimal.ZERO
        else:
            self.X = self.ZVE.divide(BigDecimal.valueOf(self.KZTAB)).setScale(
                0, BigDecimal.ROUND_DOWN
            )
        if self.STKL < 5:
            self.UPTAB25()
        else:
            self.MST5_6()

    def UPEVP(self):
        """
        Pension flat rate (§ 39b paragraph 2 sentence 5 number 3 and paragraph 4 EStG) Pap page 27
        """
        if self.KRV == 1:
            self.VSP1 = BigDecimal.ZERO
        else:
            if self.ZRE4VP.compareTo(self.BBGRV) == 1:
                self.ZRE4VP = self.BBGRV
            self.VSP1 = self.ZRE4VP.multiply(self.RVSATZAN).setScale(
                2, BigDecimal.ROUND_DOWN
            )
        self.VSP2 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.12)).setScale(
            2, BigDecimal.ROUND_DOWN
        )
        if self.STKL == 3:
            self.VHB = BigDecimal.valueOf(3000)
        else:
            self.VHB = BigDecimal.valueOf(1900)
        if self.VSP2.compareTo(self.VHB) == 1:
            self.VSP2 = self.VHB
        self.VSPN = self.VSP1.add(self.VSP2).setScale(0, BigDecimal.ROUND_UP)
        self.MVSP()
        if self.VSPN.compareTo(self.VSP) == 1:
            self.VSP = self.VSPN.setScale(2, BigDecimal.ROUND_DOWN)

    def MVSP(self):
        """
        Pension flat rate (§39b (2) sentence 5 No. 3 EStG) Comparative calculation for goodgain prerequisite, pap page 28
        """
        if self.ZRE4VP.compareTo(self.BBGKVPV) == 1:
            self.ZRE4VP = self.BBGKVPV
        if self.PKV > 0:
            if self.STKL == 6:
                self.VSP3 = BigDecimal.ZERO
            else:
                self.VSP3 = self.PKPV.multiply(Lohnsteuer2025.ZAHL12).divide(
                    Lohnsteuer2025.ZAHL100
                )
                if self.PKV == 2:
                    self.VSP3 = self.VSP3.subtract(
                        self.ZRE4VP.multiply(self.KVSATZAG.add(self.PVSATZAG))
                    ).setScale(2, BigDecimal.ROUND_DOWN)
        else:
            self.VSP3 = self.ZRE4VP.multiply(self.KVSATZAN.add(self.PVSATZAN)).setScale(
                2, BigDecimal.ROUND_DOWN
            )
        self.VSP = self.VSP3.add(self.VSP1).setScale(0, BigDecimal.ROUND_UP)

    def MST5_6(self):
        """
        Wage tax for tax classes V and VI (Section 39b (2) sentence 7 EStG), Pap page 29
        """
        self.ZZX = self.X
        if self.ZZX.compareTo(self.W2STKL5) == 1:
            self.ZX = self.W2STKL5
            self.UP5_6()
            if self.ZZX.compareTo(self.W3STKL5) == 1:
                self.ST = self.ST.add(
                    self.W3STKL5.subtract(self.W2STKL5).multiply(
                        BigDecimal.valueOf(0.42)
                    )
                ).setScale(0, BigDecimal.ROUND_DOWN)
                self.ST = self.ST.add(
                    self.ZZX.subtract(self.W3STKL5).multiply(BigDecimal.valueOf(0.45))
                ).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                self.ST = self.ST.add(
                    self.ZZX.subtract(self.W2STKL5).multiply(BigDecimal.valueOf(0.42))
                ).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.ZX = self.ZZX
            self.UP5_6()
            if self.ZZX.compareTo(self.W1STKL5) == 1:
                self.VERGL = self.ST
                self.ZX = self.W1STKL5
                self.UP5_6()
                self.HOCH = self.ST.add(
                    self.ZZX.subtract(self.W1STKL5).multiply(BigDecimal.valueOf(0.42))
                ).setScale(0, BigDecimal.ROUND_DOWN)
                if self.HOCH.compareTo(self.VERGL) == -1:
                    self.ST = self.HOCH
                else:
                    self.ST = self.VERGL

    def UP5_6(self):
        """
        Sub -program for wage tax for tax classes V and VI (Section 39b (2) sentence 7 EStG), PAP page 30
        """
        self.X = self.ZX.multiply(BigDecimal.valueOf(1.25)).setScale(
            2, BigDecimal.ROUND_DOWN
        )
        self.UPTAB25()
        self.ST1 = self.ST
        self.X = self.ZX.multiply(BigDecimal.valueOf(0.75)).setScale(
            2, BigDecimal.ROUND_DOWN
        )
        self.UPTAB25()
        self.ST2 = self.ST
        self.DIFF = self.ST1.subtract(self.ST2).multiply(Lohnsteuer2025.ZAHL2)
        self.MIST = self.ZX.multiply(BigDecimal.valueOf(0.14)).setScale(
            0, BigDecimal.ROUND_DOWN
        )
        if self.MIST.compareTo(self.DIFF) == 1:
            self.ST = self.MIST
        else:
            self.ST = self.DIFF

    def MSOLZ(self):
        """
        Solidaritaets surcharge, pap page 31"""
        self.SOLZFREI = self.SOLZFREI.multiply(BigDecimal.valueOf(self.KZTAB))
        if self.JBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZJ = (
                self.JBMG.multiply(BigDecimal.valueOf(5.5))
                .divide(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            self.SOLZMIN = (
                self.JBMG.subtract(self.SOLZFREI)
                .multiply(BigDecimal.valueOf(11.9))
                .divide(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            if self.SOLZMIN.compareTo(self.SOLZJ) == -1:
                self.SOLZJ = self.SOLZMIN
            self.JW = self.SOLZJ.multiply(Lohnsteuer2025.ZAHL100).setScale(
                0, BigDecimal.ROUND_DOWN
            )
            self.UPANTEIL()
            self.SOLZLZZ = self.ANTEIL1
        else:
            self.SOLZLZZ = BigDecimal.ZERO
        if self.R > 0:
            self.JW = self.JBMG.multiply(Lohnsteuer2025.ZAHL100)
            self.UPANTEIL()
            self.BK = self.ANTEIL1
        else:
            self.BK = BigDecimal.ZERO

    def UPANTEIL(self):
        """
        Part of the annual pregnancy for a LZZ (Section 39b (2) sentence 9 EStG), PAP page 32
        """
        if self.LZZ == 1:
            self.ANTEIL1 = self.JW
        else:
            if self.LZZ == 2:
                self.ANTEIL1 = self.JW.divide(
                    Lohnsteuer2025.ZAHL12, 0, BigDecimal.ROUND_DOWN
                )
            else:
                if self.LZZ == 3:
                    self.ANTEIL1 = self.JW.multiply(Lohnsteuer2025.ZAHL7).divide(
                        Lohnsteuer2025.ZAHL360, 0, BigDecimal.ROUND_DOWN
                    )
                else:
                    self.ANTEIL1 = self.JW.divide(
                        Lohnsteuer2025.ZAHL360, 0, BigDecimal.ROUND_DOWN
                    )

    def MSONST(self):
        """
        Calculation of other reference according to § 39b (3) Saetze 1 to 8 EStG), Pap page 33
        """
        self.LZZ = 1
        if self.ZMVB == 0:
            self.ZMVB = 12
        if (
            self.SONSTB.compareTo(BigDecimal.ZERO) == 0
            and self.MBV.compareTo(BigDecimal.ZERO) == 0
        ):
            self.VKVSONST = BigDecimal.ZERO
            self.LSTSO = BigDecimal.ZERO
            self.STS = BigDecimal.ZERO
            self.SOLZS = BigDecimal.ZERO
            self.BKS = BigDecimal.ZERO
        else:
            self.MOSONST()
            self.UPVKV()
            self.VKVSONST = self.VKV
            self.ZRE4J = (
                self.JRE4.add(self.SONSTB)
                .divide(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            self.ZVBEZJ = (
                self.JVBEZ.add(self.VBS)
                .divide(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            self.VBEZBSO = self.STERBE
            self.MRE4SONST()
            self.MLSTJAHR()
            self.WVFRBM = (
                self.ZVE.subtract(self.GFB)
                .multiply(Lohnsteuer2025.ZAHL100)
                .setScale(2, BigDecimal.ROUND_DOWN)
            )
            if self.WVFRBM.compareTo(BigDecimal.ZERO) == -1:
                self.WVFRBM = BigDecimal.ZERO
            self.UPVKV()
            self.VKVSONST = self.VKV.subtract(self.VKVSONST)
            self.LSTSO = self.ST.multiply(Lohnsteuer2025.ZAHL100)
            self.STS = (
                self.LSTSO.subtract(self.LSTOSO)
                .multiply(BigDecimal.valueOf(self.f))
                .divide(Lohnsteuer2025.ZAHL100, 0, BigDecimal.ROUND_DOWN)
                .multiply(Lohnsteuer2025.ZAHL100)
            )
            self.STSMIN()

    def STSMIN(self):
        """
        Pap page 34"""
        if self.STS.compareTo(BigDecimal.ZERO) == -1:
            if self.MBV.compareTo(BigDecimal.ZERO) == 0:
                pass
            else:
                self.LSTLZZ = self.LSTLZZ.add(self.STS)
                if self.LSTLZZ.compareTo(BigDecimal.ZERO) == -1:
                    self.LSTLZZ = BigDecimal.ZERO
                self.SOLZLZZ = self.SOLZLZZ.add(
                    self.STS.multiply(
                        BigDecimal.valueOf(5.5).divide(Lohnsteuer2025.ZAHL100)
                    )
                ).setScale(0, BigDecimal.ROUND_DOWN)
                if self.SOLZLZZ.compareTo(BigDecimal.ZERO) == -1:
                    self.SOLZLZZ = BigDecimal.ZERO
                self.BK = self.BK.add(self.STS)
                if self.BK.compareTo(BigDecimal.ZERO) == -1:
                    self.BK = BigDecimal.ZERO
            self.STS = BigDecimal.ZERO
            self.SOLZS = BigDecimal.ZERO
        else:
            self.MSOLZSTS()
        if self.R > 0:
            self.BKS = self.STS
        else:
            self.BKS = BigDecimal.ZERO

    def MSOLZSTS(self):
        """
        Calculation of the SOLZ on other remuneration, Pap page 35"""
        if self.ZKF.compareTo(BigDecimal.ZERO) == 1:
            self.SOLZSZVE = self.ZVE.subtract(self.KFB)
        else:
            self.SOLZSZVE = self.ZVE
        if self.SOLZSZVE.compareTo(BigDecimal.ONE) == -1:
            self.SOLZSZVE = BigDecimal.ZERO
            self.X = BigDecimal.ZERO
        else:
            self.X = self.SOLZSZVE.divide(
                BigDecimal.valueOf(self.KZTAB), 0, BigDecimal.ROUND_DOWN
            )
        if self.STKL < 5:
            self.UPTAB25()
        else:
            self.MST5_6()
        self.SOLZSBMG = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(
            0, BigDecimal.ROUND_DOWN
        )
        if self.SOLZSBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZS = self.STS.multiply(BigDecimal.valueOf(5.5)).divide(
                Lohnsteuer2025.ZAHL100, 0, BigDecimal.ROUND_DOWN
            )
        else:
            self.SOLZS = BigDecimal.ZERO

    def MOSONST(self):
        """
        Special calculation without any other references for calculation for other references or remuneration for several years, PAP page 36
        """
        self.ZRE4J = self.JRE4.divide(Lohnsteuer2025.ZAHL100).setScale(
            2, BigDecimal.ROUND_DOWN
        )
        self.ZVBEZJ = self.JVBEZ.divide(Lohnsteuer2025.ZAHL100).setScale(
            2, BigDecimal.ROUND_DOWN
        )
        self.JLFREIB = self.JFREIB.divide(
            Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
        )
        self.JLHINZU = self.JHINZU.divide(
            Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN
        )
        self.MRE4()
        self.MRE4ABZ()
        self.ZRE4VP = self.ZRE4VP.subtract(self.JRE4ENT.divide(Lohnsteuer2025.ZAHL100))
        self.MZTABFB()
        self.VFRBS1 = (
            self.ANP.add(self.FVB.add(self.FVBZ))
            .multiply(Lohnsteuer2025.ZAHL100)
            .setScale(2, BigDecimal.ROUND_DOWN)
        )
        self.MLSTJAHR()
        self.WVFRBO = (
            self.ZVE.subtract(self.GFB)
            .multiply(Lohnsteuer2025.ZAHL100)
            .setScale(2, BigDecimal.ROUND_DOWN)
        )
        if self.WVFRBO.compareTo(BigDecimal.ZERO) == -1:
            self.WVFRBO = BigDecimal.ZERO
        self.LSTOSO = self.ST.multiply(Lohnsteuer2025.ZAHL100)

    def MRE4SONST(self):
        """
        Special calculation with other references for calculation for other references or remuneration for several years, PAP page 37
        """
        self.MRE4()
        self.FVB = self.FVBSO
        self.MRE4ABZ()
        self.ZRE4VP = (
            self.ZRE4VP.add(self.MBV.divide(Lohnsteuer2025.ZAHL100))
            .subtract(self.JRE4ENT.divide(Lohnsteuer2025.ZAHL100))
            .subtract(self.SONSTENT.divide(Lohnsteuer2025.ZAHL100))
        )
        self.FVBZ = self.FVBZSO
        self.MZTABFB()
        self.VFRBS2 = (
            self.ANP.add(self.FVB)
            .add(self.FVBZ)
            .multiply(Lohnsteuer2025.ZAHL100)
            .subtract(self.VFRBS1)
        )

    def UPTAB25(self):
        """
        Income tax §32a EStG, Pap page 38
        """
        if self.X.compareTo(self.GFB.add(Lohnsteuer2025.ZAHL1)) == -1:
            self.ST = BigDecimal.ZERO
        else:
            if self.X.compareTo(BigDecimal.valueOf(17444)) == -1:
                self.Y = self.X.subtract(self.GFB).divide(
                    Lohnsteuer2025.ZAHL10000, 6, BigDecimal.ROUND_DOWN
                )
                self.RW = self.Y.multiply(BigDecimal.valueOf(932.3))
                self.RW = self.RW.add(BigDecimal.valueOf(1400))
                self.ST = self.RW.multiply(self.Y).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                if self.X.compareTo(BigDecimal.valueOf(68481)) == -1:
                    self.Y = self.X.subtract(BigDecimal.valueOf(17443)).divide(
                        Lohnsteuer2025.ZAHL10000, 6, BigDecimal.ROUND_DOWN
                    )
                    self.RW = self.Y.multiply(BigDecimal.valueOf(176.64))
                    self.RW = self.RW.add(BigDecimal.valueOf(2397))
                    self.RW = self.RW.multiply(self.Y)
                    self.ST = self.RW.add(BigDecimal.valueOf(1015.13)).setScale(
                        0, BigDecimal.ROUND_DOWN
                    )
                else:
                    if self.X.compareTo(BigDecimal.valueOf(277826)) == -1:
                        self.ST = (
                            self.X.multiply(BigDecimal.valueOf(0.42))
                            .subtract(BigDecimal.valueOf(10911.92))
                            .setScale(0, BigDecimal.ROUND_DOWN)
                        )
                    else:
                        self.ST = (
                            self.X.multiply(BigDecimal.valueOf(0.45))
                            .subtract(BigDecimal.valueOf(19246.67))
                            .setScale(0, BigDecimal.ROUND_DOWN)
                        )
        self.ST = self.ST.multiply(BigDecimal.valueOf(self.KZTAB))
