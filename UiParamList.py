import Validators
from UIParam import UiParam
from Validators import TypeValidator
import probabilityFunctions


def paramList():
    paramList = []
    paramList.append(initializationParam0())
    paramList.append(initializationParam1())
    paramList.append(initializationParam2())
    paramList.append(initializationParam3())
    paramList.append(initializationParam4())
    paramList.append(initializationParam5())
    paramList.append(initializationParam6())

    return paramList


def initializationParam0():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "p (0 <= p <= 1):"
    param.lines[0].validatorType = TypeValidator.probaility

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "n (n > 0):"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "m (m <= n):"
    param.lines[2].validatorType = TypeValidator.natural

    param.pictureResult.name = "Формула Бернулли k = m"

    param.function = lambda values: probabilityFunctions.functionBernoulli(values.nums[1], values.nums[2],
                                                                           values.nums[0])
    return param


def initializationParam1():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "p (0 <= p <= 1):"
    param.lines[0].validatorType = TypeValidator.probaility

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "n (n > 0):"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "m (m <= n):"
    param.lines[2].validatorType = TypeValidator.natural

    param.pictureResult.name = "Формула Бернулли k меньше m"

    param.function = lambda values: round(
        sum(probabilityFunctions.functionBernoulli(values.nums[1], k, values.nums[0]) for k in range(values.nums[2])),
        probabilityFunctions.roundParam)
    return param


def initializationParam2():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "p (0 <= p <= 1):"
    param.lines[0].validatorType = TypeValidator.probaility

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "n (n > 0):"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "m (m <= n):"
    param.lines[2].validatorType = TypeValidator.natural

    param.pictureResult.name = "Формула Бернулли k не меньше m"

    param.function = lambda values: round(1 - sum(
        probabilityFunctions.functionBernoulli(values.nums[1], k, values.nums[0]) for k in range(values.nums[2])),
                                          probabilityFunctions.roundParam)
    return param


def initializationParam3():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "p (0 <= p <= 1):"
    param.lines[0].validatorType = TypeValidator.probaility

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "n (n > 0):"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[3].visibility = True
    param.lines[3].needValue = True
    param.lines[3].lableText = "m1 (m1 <= n):"
    param.lines[3].validatorType = TypeValidator.natural

    param.lines[4].visibility = True
    param.lines[4].needValue = True
    param.lines[4].lableText = "m2 (m2 <= n):"
    param.lines[4].validatorType = TypeValidator.natural

    param.pictureResult.name = "Формула Бернулли k в диапазоне "

    param.function = lambda values: round(sum(
        probabilityFunctions.functionBernoulli(values.nums[1], k, values.nums[0]) for k in
        range(values.nums[3], values.nums[4] + 1)),
        probabilityFunctions.roundParam)
    return param

def initializationParam4():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "p:"
    param.lines[0].validatorType = TypeValidator.probaility

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "n:"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "m:"
    param.lines[2].validatorType = TypeValidator.natural

    param.pictureResult.name = "Формула Пуассона"
    param.function = lambda values: probabilityFunctions.functionPuasson(values.nums[0], values.nums[1], values.nums[2])
    return param
def initializationParam5():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "n (n >= 0):"
    param.lines[0].validatorType = TypeValidator.natural

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "m (m <= n):"
    param.lines[1].validatorType = TypeValidator.natural

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "p (0 <= p <= 1):"
    param.lines[2].validatorType = TypeValidator.probaility

    param.pictureResult.name = "локальная теорема Муавра-Лапласа"
    param.function = lambda values: probabilityFunctions.funcMoivreLaplace(values.nums[0], values.nums[1], values.nums[2])
    return param

def initializationParam6():
    param = UiParam()

    param.lines[0].visibility = True
    param.lines[0].needValue = True
    param.lines[0].lableText = "n (n >= 0):"
    param.lines[0].validatorType = TypeValidator.natural

    param.lines[1].visibility = True
    param.lines[1].needValue = True
    param.lines[1].lableText = "p (0 <= p <= 1):"
    param.lines[1].validatorType = TypeValidator.probaility

    param.lines[2].visibility = True
    param.lines[2].needValue = True
    param.lines[2].lableText = "m1:"
    param.lines[2].validatorType = TypeValidator.natural

    param.lines[3].visibility = True
    param.lines[3].needValue = True
    param.lines[3].lableText = "m2:"
    param.lines[3].validatorType = TypeValidator.natural

    param.pictureResult.name = "интегральная теорема Муавра-Лапласа"
    param.function = lambda values: probabilityFunctions.funcIntegralTeoremMoivreLaplace(values.nums[0], values.nums[1], values.nums[2], values.nums[3])
    return param
