test = {   'name': 'q1_d',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(slrcoef_se) == 2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> round(slrcoef_se[0], 1) == 0.3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (slrcoef_se == np.sqrt(slrcoef_vcov.diagonal())).all()\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
