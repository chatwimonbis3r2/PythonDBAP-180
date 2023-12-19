#Assignment 3
#2.1
userID = input("Your ID: ")
userName = input("Your Name: ")

#2.2
strMeterNumberOld = input("Your Meter Number Old: ")
meterNumberOld = int(strMeterNumberOld)
strMeterNumberNew = input("Your Meter Number New: ")
meterNumberNew = int(strMeterNumberNew)

#2.4 1
if meterNumberOld > meterNumberNew:
    print("================")
    print("Your Wrong Input")
    print("================")
#2.4 2
else:
    #2.5
    electricalUnit = meterNumberNew - meterNumberOld
    #2.6
    if electricalUnit <= 50:
        electricChargeBase = 5 * electricalUnit
    elif electricalUnit <= 100 :
        electricChargeBase = 10 * (electricalUnit - 50) + 250
    elif electricalUnit <= 300:
        electricChargeBase = 15 * (electricalUnit - 100) + (250 + 500)
    else:
        electricChargeBase = 20 * (electricalUnit - 300) + (250 + 500 + 3000)

    electricVariable = electricalUnit * 0.50
    vat = (electricChargeBase+electricVariable) * 0.07

    #2.7
    total = electricChargeBase + electricVariable + vat

    #2.8
    print("================================")
    print("{0:<1s}{1:>1,.2f} Unit".format(("Electrical Unit: "), electricalUnit))
    print("{0:<1s}{1:>1,.2f} THB".format(("Electrical Charge Base: "), electricChargeBase))
    print("{0:<1s}{1:>1,.2f} THB".format(("Electrical Variable: "), electricVariable))
    print("{0:<1s}{1:>1,.2f} THB".format(("Vat: "), vat))
    print("{0:<1s}{1:>1,.2f} THB".format(("Total: "), total))
    print("================================")