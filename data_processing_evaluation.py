def __confusion_matrix(result_data, pattern_data):
    p, n, tp, tn, fp, fn = (0,) * 6

    width = len(processing_result)
    height = len(processing_result[0])

    for x in range(width):
        for y in range(height):
            if pattern_data[x][y] == 1:
                p += 1
                if result_data[x][y] == 1:
                    tp += 1
                else:
                    fn += 1
            else:
                n += 1
                if result_data[x][y] == 0:
                    tn += 1
                else:
                    fp += 1

    return p, n, tp, tn, fp, fn


def __tpr(tp, p):
    return tp / p


def __tnr(tn, n):
    return tn / n


def __fpr(fn, n):
    return fn / n


def __fnr(fn, p):
    return fn / p


def __ppv(tp, top):
    return tp / top


def __npv(tn, ton):
    return tn / ton


def __fdr(fp, top):
    return fp / top


def __for(fn, ton):
    return fn / ton


def __acc(tp, tn, p, n):
    return (tp + tn) / (p + n)


def __pre(p, n):
    return p / (p + n)


def __plr(tpr, fpr):
    return tpr / fpr


def __nlr(fnr, tnr):
    return fnr / tnr


def __dor(plr, nlr):
    return plr / nlr


def __f_score(tp, fp, fn):
    return 2 * tp / (2 * tp + fp + fn)


def __mcc(tp, tn, fp, fn, p, n, top, ton):
    return (tp * tn - fp * fn) / ((top * p * n * ton) ** 0.5)


def get_coefficients(processing_data, ground_truth_data):
    p, n, tp, tn, fp, fn = __confusion_matrix(processing_data,
                                              ground_truth_data)

    top = tp + fp
    ton = tn + fn

    coefficients = {'tpr': __tpr(tp, p),
                    'tnr': __tnr(tn, n),
                    'fpr': __fpr(fp, n),
                    'fnr': __fnr(fn, p),
                    'ppv': __ppv(tp, top),
                    'npv': __npv(tn, ton),
                    'fdr': __fdr(fp, top),
                    'for': __for(fn, ton),
                    'acc': __acc(tp, tn, p, n),
                    'pre': __pre(p, n),
                    'f_score': __f_score(tp, fp, fn),
                    'mcc': __mcc(tp, tn, fp, fn, p, n, top, ton)
                    }
    coefficients['plr'] = __plr(coefficients.get('tpr'),
                                coefficients.get('fpr'))
    coefficients['nlr'] = __nlr(coefficients.get('fnr'),
                                coefficients.get('tnr'))
    coefficients['dor'] = __plr(coefficients.get('plr'),
                                coefficients.get('nlr'))

    return coefficients


if __name__ == "__main__":
    processing_result = [[1, 0, 0, 1, 1],
                         [1, 1, 0, 0, 0],
                         [1, 0, 1, 0, 1],
                         [0, 1, 0, 0, 0],
                         [0, 0, 0, 1, 0]]

    ground_truth = [[1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1]]

    print(get_coefficients(processing_result, ground_truth))
