        if input_name_ in result_names:
            index = result_names.index(input_name_)
            transform_ = result.transforms[index]
        else:
            transform_ = -1
