from declear_var import COLOR_BLACK
def item_effect_off():
    global pl_col,pl_scope,pl_fast
    global item_use,item_time

    item_use = False
    item_time = 0


    pl_col = COLOR_BLACK
    pl_fast = False
    pl_scope = 0
