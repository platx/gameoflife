""" Round integers to closest number """
def round_int(value, closest):
    return closest * ((value + 5) // closest)
