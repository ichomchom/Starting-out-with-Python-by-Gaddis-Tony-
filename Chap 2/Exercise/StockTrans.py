purchased = 2000
perShare = 40
commision = .03
sold = 2000
soldPerShare = 42.75

amountPaid = 2000 * 40
amountSold = 2000 * 42.75
commisionPaid = amountPaid *commision
commisionSold = amountSold *commision
print('Amount Joe paid for stock: $',
      format(float(amountPaid), ',.2f'), sep = '')
print('Commision when brought stock: $'
      ,format(float(commisionPaid), ',.2f'), sep ='')
print('Amount Joe sold for stock: $',
      format(float(amountSold), ',.2f'), sep = '')
print('Commision when sold stock: $'
      ,format(float(commisionSold), ',.2f'), sep ='')
print('Money lef: $',
      format(float(amountSold - commisionPaid - commisionSold - amountPaid)
             , ',.2f'), sep = '')
