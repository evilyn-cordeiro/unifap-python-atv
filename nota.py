avp_01 = input('AVP01:');
avp_02 = input('AVP02:');
# tdes
tde_01 = input('TDE01:');
tde_02 = input('TDE02:');
tde_03 = input('TDE03:');
tde_04 = input('TDE04:');
# medias
media_tde = (float(tde_01) + float(tde_02) + float(tde_03) + float(tde_04)) / 4
media = ((float(avp_01) + float(avp_02)) * 0.4 ) + ((media_tde) * 0.2)

print('sua média final é: %.2f' %media)