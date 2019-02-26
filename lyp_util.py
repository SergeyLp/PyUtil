import pickle

def allfiles_in(path: str) -> []:
    return [os.path.join(path, file) for file in os.listdir(path)]


def load_or_execute(fname: str, fn, force_execute: bool = False) ->  (object, bool):
    ''''Load pickle file or execution function if error or forsed.'''
    try:
        if force_execute:
            raise UserWarning
        else:
            with open(fname, 'rb') as f:
                obj = pickle.load(f)
            was_ececuted = False
    except:
        obj = fn()
        with open(fname, 'wb') as f:
            pickle.dump(obj, f)
        was_ececuted = True

    return obj, was_ececuted
