from django.db import models

# Create your models here.


class NumberCollection(models.Model):
    """
    Simply a collection of performance numbers.
    Redundant table used for easier referencing.
    """
    date_added = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

class Performance(models.Model):
    """
    A collection of performance data about one animal.
    Or a collection of averages from a single category of animals.
    """
    epds = models.OneToOneField(NumberCollection, related_name="epds_set")
    measured_data = models.OneToOneField(
                        NumberCollection,
                        related_name="measured_data_set",
    )

class EPDs(NumberCollection):
    """ One set of EPDs for a specific animal. """

    # Production EPDs and their accuracies
    CED = models.DecimalField(
                    "Calving Ease Direct",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CED_acc = models.DecimalField(
                    "Calving Ease Direct Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    BW = models.DecimalField(
                    "Birth Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    BW_acc = models.DecimalField(
                    "Birth Weight Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    WW = models.DecimalField(
                    "Weaning Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    WW_acc = models.DecimalField(
                    "Weaning Weight Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YW = models.DecimalField(
                    "Yearling Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YW_acc = models.DecimalField(
                    "Yearling Weight Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    RADG = models.DecimalField(
                    "Residual Average Daily Gain",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    RADG_acc = models.DecimalField(
                    "Residual Average Daily Gain Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    DMI = models.DecimalField(
                    "Dry Matter Intake",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    DMI_acc = models.DecimalField(
                    "Dry Matter Intake Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YH = models.DecimalField(
                    "Yearling Height",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YH_acc = models.DecimalField(
                    "Yearling Height Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    SC = models.DecimalField(
                    "Scrotal Circumference",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    SC_acc = models.DecimalField(
                    "Scrotal Circumference Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Doc = models.DecimalField(
                    "Docility",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Doc_acc = models.DecimalField(
                    "Docility Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )

    # Maternal EPDs
    HP = models.DecimalField(
                    "Heifer Pregnancy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    HP_acc = models.DecimalField(
                    "Heifer Pregnancy Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CEM = models.DecimalField(
                    "Calving Ease Maternal",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CEM_acc = models.DecimalField(
                    "Calving Ease Maternal Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Milk = models.DecimalField(
                    "Maternal Milk",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Milk_acc = models.DecimalField(
                    "Maternal Milk Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MkH = models.DecimalField(
                    "Maternal Herds",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MkH_acc = models.DecimalField(
                    "Maternal Herds Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MkD = models.DecimalField(
                    "Maternal Daughters",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MkD_acc = models.DecimalField(
                    "Maternal Daughters Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MW = models.DecimalField(
                    "Mature Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MW_acc = models.DecimalField(
                    "Mature Weight Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MH = models.DecimalField(
                    "Mature Height",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    MH_acc = models.DecimalField(
                    "Mature Height Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valEN = models.DecimalField(
                    "Cow Energy Value",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )

    # Carcass EPDs
    CW = models.DecimalField(
                    "Carcass Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CW_acc = models.DecimalField(
                    "Carcass Weight Acccuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Marb = models.DecimalField(
                    "Marbling",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Marb_acc = models.DecimalField(
                    "Marbling Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    RE = models.DecimalField(
                    "Ribeye Area",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    RE_acc = models.DecimalField(
                    "Ribeye Area Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Fat = models.DecimalField(
                    "Fat Thickness",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    Fat_acc = models.DecimalField(
                    "Fat Thickness Accuracy",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CGrp = models.DecimalField(
                    "Contemporary Groups",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    CPg = models.DecimalField(
                    "Contemporary Progeny",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    UGrp = models.DecimalField(
                    "Ultrasound Groups",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    UPg = models.DecimalField(
                    "Ultrasound Progeny",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )

    # Value Indexes
    valW = models.DecimalField(
                    "Weaned Calf Value",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valF = models.DecimalField(
                    "Feedlot Value",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valG = models.DecimalField(
                    "Grid Value",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valQG = models.DecimalField(
                    "Quality Grade",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valYG = models.DecimalField(
                    "Yield Grade",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    valB = models.DecimalField(
                    "Beef Value",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )

class MeasuredDated(NumberCollection):
    # Data collected by the owner
    BW_mes = models.DecimalField(
                    "Measured Birth Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    WW_mes = models.DecimalField(
                    "Measured Weaning Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    WH_mes = models.DecimalField(
                    "Measured Weaning Height",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YW_mes = models.DecimalField(
                    "Measured Yearling Weight",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    YH_mes = models.DecimalField(
                    "Measured Yearling Height",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
    SC_mes = models.DecimalField(
                    "Measured Scrotal Circumference",
                    max_digits=5,
                    decimal_places=5,
                    null=True,
                    blank=True,
    )
