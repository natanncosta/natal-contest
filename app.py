[N, M] = map(int, input().split())

chields = []
for i in range(N):
  chields.append(0)

for i in range(M):
  [I, J] = map(int, input().split())
  if i % 2 == 0:
    numberOfGifts = 1
    j = 0
    while I+j<=J:
      chields[I+j] += numberOfGifts
      numberOfGifts += 1
  else:
    numberOfGifts = -1
    j = 0
    while I+j<=J:
      chields[I+j] += numberOfGifts
      numberOfGifts -= 1

result = True
for i in chields:
  if (i < 0):
    print('UOY SI SAMTSIRHC ROF TNAW I LLA')
    result = False
if result:
  print('ALL I WANT FOR CHRISTMAS IS YOU')
