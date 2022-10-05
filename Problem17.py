digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
          18: 'eighteen', 19: 'nineteen', 0: ''}

dozens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 0: ''}

ln = 0
for i in range(1, 1000):
    if i < 20:
        ln += len(digits[i])
    if 100 > i >= 20:
        ln += len(dozens[int(str(i)[0])] + digits[int(str(i)[1])])
    if i >= 100:
        if str(i)[1:] == '00':
            ln += len(digits[int(str(i)[0])] + 'hundred')
        elif int(str(i)[1:]) <= 19:
            ln += len(digits[int(str(i)[0])] + 'hundred' + 'end' + digits[int(str(i)[1:])])
        else:
            ln += len(digits[int(str(i)[0])] + 'hundred' + 'end' + dozens[int(str(i)[1])] + digits[int(str(i)[2])])
print(ln + 11)
