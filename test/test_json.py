"""Tests for json data, retrieved from n2yo api's
"""

# File header for Doxygen document generator:
## @file test_json.py
## @brief Tests for json data, retrieved from n2yo api's

import json

testdata = """
{
  "info": {
    "satid": 25338,
    "satname": "NOAA 15",
    "transactionscount": 0,
    "passescount": 23
  },
  "passes": [
    {
      "startAz": 22.83,
      "startAzCompass": "NNE",
      "startUTC": 1692945215,
      "maxAz": 91.47,
      "maxAzCompass": "E",
      "maxEl": 26.38,
      "maxUTC": 1692945635,
      "endAz": 161.44,
      "endAzCompass": "SSE",
      "endUTC": 1692946055
    },
    {
      "startAz": 12.48,
      "startAzCompass": "N",
      "startUTC": 1692951195,
      "maxAz": 291.65,
      "maxAzCompass": "WNW",
      "maxEl": 57.12,
      "maxUTC": 1692951645,
      "endAz": 211.39,
      "endAzCompass": "SW",
      "endUTC": 1692952085
    },
    {
      "startAz": 105.87,
      "startAzCompass": "ESE",
      "startUTC": 1692980505,
      "maxAz": 51.22,
      "maxAzCompass": "NE",
      "maxEl": 15.75,
      "maxUTC": 1692980870,
      "endAz": 354.28,
      "endAzCompass": "N",
      "endUTC": 1692981245
    },
    {
      "startAz": 154.66,
      "startAzCompass": "SSE",
      "startUTC": 1692986360,
      "maxAz": 71.58,
      "maxAzCompass": "ENE",
      "maxEl": 70.41,
      "maxUTC": 1692986810,
      "endAz": 346.53,
      "endAzCompass": "N",
      "endUTC": 1692987260
    },
    {
      "startAz": 205.05,
      "startAzCompass": "SSW",
      "startUTC": 1692992420,
      "maxAz": 270.64,
      "maxAzCompass": "W",
      "maxEl": 21.52,
      "maxUTC": 1692992830,
      "endAz": 335.21,
      "endAzCompass": "NNW",
      "endUTC": 1692993235
    },
    {
      "startAz": 26.62,
      "startAzCompass": "NNE",
      "startUTC": 1693030095,
      "maxAz": 86.54,
      "maxAzCompass": "E",
      "maxEl": 17.06,
      "maxUTC": 1693030485,
      "endAz": 146.95,
      "endAzCompass": "SE",
      "endUTC": 1693030870
    },
    {
      "startAz": 14.64,
      "startAzCompass": "N",
      "startUTC": 1693036065,
      "maxAz": 302.89,
      "maxAzCompass": "NW",
      "maxEl": 86.73,
      "maxUTC": 1693036515,
      "endAz": 199,
      "endAzCompass": "SSW",
      "endUTC": 1693036960
    },
    {
      "startAz": 6.79,
      "startAzCompass": "N",
      "startUTC": 1693042075,
      "maxAz": 307.83,
      "maxAzCompass": "NW",
      "maxEl": 18.83,
      "maxUTC": 1693042460,
      "endAz": 247.81,
      "endAzCompass": "WSW",
      "endUTC": 1693042845
    },
    {
      "startAz": 142.39,
      "startAzCompass": "SE",
      "startUTC": 1693071245,
      "maxAz": 65.73,
      "maxAzCompass": "ENE",
      "maxEl": 46.07,
      "maxUTC": 1693071685,
      "endAz": 348.79,
      "endAzCompass": "N",
      "endUTC": 1693072120
    },
    {
      "startAz": 191.5,
      "startAzCompass": "S",
      "startUTC": 1693077250,
      "maxAz": 264.53,
      "maxAzCompass": "W",
      "maxEl": 32.99,
      "maxUTC": 1693077680,
      "endAz": 338.62,
      "endAzCompass": "NNW",
      "endUTC": 1693078110
    },
    {
      "startAz": 17.04,
      "startAzCompass": "NNE",
      "startUTC": 1693120930,
      "maxAz": 103.58,
      "maxAzCompass": "E",
      "maxEl": 61.32,
      "maxUTC": 1693121385,
      "endAz": 186.4,
      "endAzCompass": "S",
      "endUTC": 1693121825
    },
    {
      "startAz": 8.67,
      "startAzCompass": "N",
      "startUTC": 1693126935,
      "maxAz": 301.81,
      "maxAzCompass": "NW",
      "maxEl": 26.86,
      "maxUTC": 1693127350,
      "endAz": 235.09,
      "endAzCompass": "SW",
      "endUTC": 1693127760
    },
    {
      "startAz": 130.17,
      "startAzCompass": "SE",
      "startUTC": 1693156140,
      "maxAz": 60.46,
      "maxAzCompass": "ENE",
      "maxEl": 31.15,
      "maxUTC": 1693156565,
      "endAz": 350.77,
      "endAzCompass": "N",
      "endUTC": 1693156985
    },
    {
      "startAz": 178.52,
      "startAzCompass": "S",
      "startUTC": 1693162095,
      "maxAz": 259.81,
      "maxAzCompass": "W",
      "maxEl": 51.27,
      "maxUTC": 1693162540,
      "endAz": 341.74,
      "endAzCompass": "NNW",
      "endUTC": 1693162985
    },
    {
      "startAz": 19.93,
      "startAzCompass": "NNE",
      "startUTC": 1693205805,
      "maxAz": 97.17,
      "maxAzCompass": "E",
      "maxEl": 39.13,
      "maxUTC": 1693206245,
      "endAz": 173.64,
      "endAzCompass": "S",
      "endUTC": 1693206680
    },
    {
      "startAz": 10.65,
      "startAzCompass": "N",
      "startUTC": 1693211795,
      "maxAz": 297.55,
      "maxAzCompass": "WNW",
      "maxEl": 39.16,
      "maxUTC": 1693212230,
      "endAz": 222.71,
      "endAzCompass": "SW",
      "endUTC": 1693212660
    },
    {
      "startAz": 117.67,
      "startAzCompass": "ESE",
      "startUTC": 1693241050,
      "maxAz": 55.18,
      "maxAzCompass": "NE",
      "maxEl": 21.71,
      "maxUTC": 1693241450,
      "endAz": 352.78,
      "endAzCompass": "N",
      "endUTC": 1693241845
    },
    {
      "startAz": 165.94,
      "startAzCompass": "S",
      "startUTC": 1693246955,
      "maxAz": 255.49,
      "maxAzCompass": "W",
      "maxEl": 79.82,
      "maxUTC": 1693247405,
      "endAz": 344.39,
      "endAzCompass": "NNW",
      "endUTC": 1693247855
    },
    {
      "startAz": 23.17,
      "startAzCompass": "NNE",
      "startUTC": 1693290680,
      "maxAz": 91.9,
      "maxAzCompass": "E",
      "maxEl": 25.44,
      "maxUTC": 1693291100,
      "endAz": 160.23,
      "endAzCompass": "SSE",
      "endUTC": 1693291515
    },
    {
      "startAz": 12.64,
      "startAzCompass": "N",
      "startUTC": 1693296660,
      "maxAz": 290.36,
      "maxAzCompass": "WNW",
      "maxEl": 59.31,
      "maxUTC": 1693297110,
      "endAz": 210.32,
      "endAzCompass": "SW",
      "endUTC": 1693297550
    },
    {
      "startAz": 104.65,
      "startAzCompass": "E",
      "startUTC": 1693325975,
      "maxAz": 49.78,
      "maxAzCompass": "NE",
      "maxEl": 15.25,
      "maxUTC": 1693326340,
      "endAz": 354.65,
      "endAzCompass": "N",
      "endUTC": 1693326705
    },
    {
      "startAz": 153.59,
      "startAzCompass": "SSE",
      "startUTC": 1693331825,
      "maxAz": 69.67,
      "maxAzCompass": "ENE",
      "maxEl": 67.83,
      "maxUTC": 1693332275,
      "endAz": 346.76,
      "endAzCompass": "N",
      "endUTC": 1693332720
    },
    {
      "startAz": 203.86,
      "startAzCompass": "SSW",
      "startUTC": 1693337880,
      "maxAz": 269.63,
      "maxAzCompass": "W",
      "maxEl": 22.3,
      "maxUTC": 1693338290,
      "endAz": 335.57,
      "endAzCompass": "NNW",
      "endUTC": 1693338700
    }
  ]
}
"""


def test_json():
    """Load testdata and print pass information
    """
    d = json.loads(testdata)
    print(d)
    name = d.get('info').get('satname')
    print(name)
    passes = d.get('passes')
    for passinfo in passes:
        print(passinfo)
