if __name__ == '__main__':
    my_string = 'y3tds23o12345dujderpvpasdtgxaefs3gss5432fjs24fsswe098765d'
    current_slice = my_string.replace('3tds23', '')
    current_slicea = current_slice.replace('12345d', '')
    current_sliceb = current_slicea.replace('jderpv', '')
    current_slicec = current_sliceb.replace('dtgxaefs3g', '')
    current_sliced = current_slicec.replace('s5432fjs24f', '')
    current_slicee = current_sliced.replace('ssw', '')
    current_slicef = current_slicee.replace('098765', '')
    current_slicef = current_slicef.capitalize()
    print(current_slicef)
