from .critical_exponent import critical_exponent


def check_all_extensions(prefix, alphabet, rt):
    if critical_exponent(prefix, max_exp=rt)>=rt:
        return len(prefix)
    else:
        max_letters=len(prefix)
        for a in alphabet:
            max_letters=max(max_letters, check_all_extensions(prefix+a,alphabet,rt))
        return max_letters   