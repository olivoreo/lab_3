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
    param.lines[0].lableText = "k"
    param.lines[0].validatorType = TypeValidator.natural

    param.lists[0].validatorTypeElementList = TypeValidator.natural
    param.lists[0].lableText = "Введите M:"
    param.lists[0].nameElement = "m%d:"
    param.lists[0].startIndex = 1
    param.lists[0].numOfLineEditListenerList = 0
    param.lists[0].visibility = True
    param.lists[0].needValues = True

    param.lists[1].validatorTypeElementList = TypeValidator.probaility
    param.lists[1].lableText = "Введите P:"
    param.lists[1].nameElement = "p%d:"
    param.lists[1].startIndex = 1
    param.lists[1].numOfLineEditListenerList = 0
    param.lists[1].visibility = True
    param.lists[1].needValues = True

    param.pictureResult.name = "Полиномиальная формула"
    param.function = lambda values: probabilityFunctions.functionPolynomial(values.lists[0], values.lists[1])
    return param
