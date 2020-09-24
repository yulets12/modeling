ItK = [[0.5, 6700, 0.5],
    [1,	6790, 0.55],
    [5,	7150, 1.7],
    [10, 7270, 3],
    [50, 8010, 11],
    [200, 9185, 32],
    [400, 10010, 40],
    [800, 11140, 41],
    [1200, 12010, 39]]

Tsigma = [
[4000, 0.031],
[5000, 0.27],
[6000, 2.05],
[7000, 6.06],
[8000, 12.0],
[9000, 19.9],
[10000, 29.6],
[11000, 41.1],
[12000, 54.1],
[13000, 67.7],
[14000, 81.5]]

resetData = {
    "R": 0.35,
    "Le": 12,
    "Lk": 0.000187,
    "Ck": 0.000268,
    "Rk": 0.25,
    "Uc0": 1400,
    "I0": 0.5,
    "Tw": 2000,
    "Tbegin":0,
    "Tend": 0.0006,
    "Tstep": 0.000001,
}

data = {
    "R": 0.35,
    "Le": 12,
    "Lk": 0.000187,
    "Ck": 0.000268,
    "Rk": 0.25,
    "Uc0": 1400,
    "I0": 0.5,
    "Tw": 2000,
    "Tbegin": 0,
    "Tend": 0,
    "Tstep": 0,
}

graph1 = [[] for i in range(2)]
graph2 = [[] for i in range(2)]
graph3 = [[] for i in range(2)]
graph4 = [[] for i in range(2)]
graph5 = [[] for i in range(2)]

graph1_1 = [[] for i in range(2)]
graph2_1 = [[] for i in range(2)]
graph3_1 = [[] for i in range(2)]
graph4_1 = [[] for i in range(2)]