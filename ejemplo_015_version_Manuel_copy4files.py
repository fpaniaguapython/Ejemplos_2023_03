finput = './modulos/20230309/'
fdest = ('./modulos/20230309/fld1/','./modulos/20230309/fld2/','./modulos/20230309/fld3/','./modulos/20230309/fld4/')
blksize = 1 

fname = input("Nombre de fichero: ")

with open(f'{finput}{fname}','rb') as finput:
    for dest in fdest:
        with open(f'{dest}{fname}','wb') as fdest:
            binput = finput.read(blksize)
            while binput:
                fdest.write(binput)
                binput = finput.read(blksize)
        finput.seek(0)
