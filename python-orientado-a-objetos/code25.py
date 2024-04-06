class ExcecaoCustomizada(exception): 
    pass
    
    def throws(): (2)
        raise ExcecaoCustomizada
        try: 
            throws()
        except ExcecaoCustomizada as ex:
            print ("Excecao lançada")