SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53
Todas = SP + RJ + MG + ES + Outros

percentual=Todas/100

percentual_SP = SP/percentual
percentual_RJ = RJ/percentual
percentual_MG = MG/percentual
percentual_ES = ES/percentual
percentual_Outras = Outros/percentual

percentual=Todas/100

print("\nO percenteual da tributa de X empresa :")

print("\nSP Com fatura bruta de:",SP,"=",'{:.2f}%'.format(percentual_SP))
print("\nRJ Com fatura bruta de:",RJ,"=",'{:.2f}%'.format(percentual_RJ))
print("\nMG Com fatura bruta de:",MG,"=",'{:.2f}%'.format(percentual_MG))
print("\nES Com fatura bruta de:",ES,"=",'{:.2f}%'.format(percentual_ES))
print("\nOutros Estados Com fatura bruta de:",Outros,"=",'{:.2f}%'.format(percentual_Outras))

