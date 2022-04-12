def fill_dashboard( player, pos, matrix ):
    if pos > 9:
        print( "Not possible" )
        return None
    elif pos > 6:
        for i in range( len( matrix[ 2 ] ) ):
            if matrix[ 2 ][ i ] == pos:
                matrix[ 2 ][ i ] = player
    elif pos > 3:
        for i in range( len( matrix[ 1 ] ) ):
            if matrix[ 1 ][ i ] == pos:
                matrix[ 1 ][ i ] = player
    elif pos > 0:
        for i in range( len( matrix[ 0 ] ) ):
            if matrix[ 0 ][ i ] == pos:
                matrix[ 0 ][ i ] = player
    else:
        print( "Not possible" )
        return None
    return matrix

def print_dashboard( matri ):
    print( f"{ matri[ 0 ][ 0 ] }  |  { matri[ 0 ][ 1 ] }  |  { matri[ 0 ][ 2 ] }" )
    print( "--------------" )
    print( f"{ matri[ 1 ][ 0 ] }  |  { matri[ 1 ][ 1 ] }  |  { matri[ 1 ][ 2 ] }" )
    print( "--------------" )
    print( f"{ matri[ 2 ][ 0 ] }  |  { matri[ 2 ][ 1 ] }  |  { matri[ 2 ][ 2 ] }" )
    print( "--------------" )


def verify_winner( mat ):
    if ( mat[ 0 ][ 0 ] == mat[ 1 ][ 0 ] == mat[ 2 ][ 0 ] ) or ( mat[ 0 ][ 1 ] == mat[ 1 ][ 1 ] == mat[ 2 ][ 1 ] ) or ( mat[ 0 ][ 2 ] == mat[ 1 ][ 2 ] == mat[ 2 ][ 2 ] ):
        return True
    elif ( mat[ 0 ][ 0 ] == mat[ 0 ][ 1 ] == mat[ 0 ][ 2 ] ) or ( mat[ 1 ][ 0 ] == mat[ 1 ][ 1 ] == mat[ 1 ][ 2 ] ) or ( mat[ 2 ][ 0 ] == mat[ 2 ][ 1 ] == mat[ 2 ][ 2 ] ):
        return True
    elif ( mat[ 0 ][ 0 ] == mat[ 1 ][ 1 ] == mat[ 2 ][ 2 ] ) or ( mat[ 0 ][ 2 ] == mat[ 1 ][ 1 ] == mat[ 2 ][ 0 ] ):
        return True
    return False

def switch_player():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    else:
        curr_player = "X"


print( "Hola, bienvenido a este gato" )
win = False
dashboard = [ [ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ] ]
set_historico = set()
characte = ""
position = 0
curr_player = "X"
print( "Las posiciones son de la siguiente manera:" )
print_dashboard( dashboard )
while len( set_historico ) < 10 and win == False:
    position = int( input( f"Insert the position where you want to insert {characte}: " ) )
    if position in set_historico:
        print( "Not possible" )
        continue
    set_historico.add( position )
    dashboard = fill_dashboard( curr_player, position, dashboard )
    print_dashboard( dashboard )
    switch_player( )
    if len( set_historico ) < 4:
        continue
    if verify_winner( dashboard ):
        win = True
        switch_player( )
        print( f"There is a winner\nCONGRATULATIONS { curr_player }" )
