"""
Map of chemical symbol -> atomic number and
atomic number -> checmical symbol
"""
atomic_number = {
  'H' : 1,      1: 'H',
  'He': 2,      2: 'He',
  'Li': 3,      3: 'Li',
  'Be': 4,      4: 'Be',
  'B' : 5,      5: 'B',
  'C' : 6,      6: 'C',
  'N' : 7,      7: 'N',
  'O' : 8,      8: 'O',
  'F' : 9,      9: 'F',
  'Ne': 10,    10: 'Ne',
  'Na': 11,    11: 'Na',
  'Mg': 12,    12: 'Mg',
  'Al': 13,    13: 'Al',
  'Si': 14,    14: 'Si',
  'P' : 15,    15: 'P',
  'S' : 16,    16: 'S',
  'Cl': 17,    17: 'Cl',
  'Ar': 18,    18: 'Ar',
  'K' : 19,    19: 'K',
  'Ca': 20,    20: 'Ca',
  'Sc': 21,    21: 'Sc',
  'Ti': 22,    22: 'Ti',
  'V' : 23,    23: 'V',
  'Cr': 24,    24: 'Cr',
  'Mn': 25,    25: 'Mn',
  'Fe': 26,    26: 'Fe',
  'Co': 27,    27: 'Co',
  'Ni': 28,    28: 'Ni',
  'Cu': 29,    29: 'Cu',
  'Zn': 30,    30: 'Zn',
  'Ga': 31,    31: 'Ga',
  'Ge': 32,    32: 'Ge',
  'As': 33,    33: 'As',
  'Se': 34,    34: 'Se',
  'Br': 35,    35: 'Br',
  'Kr': 36,    36: 'Kr',
  'Rb': 37,    37: 'Rb',
  'Sr': 38,    38: 'Sr',
  'Y' : 39,    39: 'Y',
  'Zr': 40,    40: 'Zr',
  'Nb': 41,    41: 'Nb',
  'Mo': 42,    42: 'Mo',
  'Tc': 43,    43: 'Tc',
  'Ru': 44,    44: 'Ru',
  'Rh': 45,    45: 'Rh',
  'Pd': 46,    46: 'Pd',
  'Ag': 47,    47: 'Ag',
  'Cd': 48,    48: 'Cd',
  'In': 49,    49: 'In',
  'Sn': 50,    50: 'Sn',
  'Sb': 51,    51: 'Sb',
  'Te': 52,    52: 'Te',
  'I' : 53,    53: 'I',
  'Xe': 54,    54: 'Xe',
  'Cs': 55,    55: 'Cs',
  'Ba': 56,    56: 'Ba',
  'La': 57,    57: 'La',
  'Ce': 58,    58: 'Ce',
  'Pr': 59,    59: 'Pr',
  'Nd': 60,    60: 'Nd',
  'Pm': 61,    61: 'Pm',
  'Sm': 62,    62: 'Sm',
  'Eu': 63,    63: 'Eu',
  'Gd': 64,    64: 'Gd',
  'Tb': 65,    65: 'Tb',
  'Dy': 66,    66: 'Dy',
  'Ho': 67,    67: 'Ho',
  'Er': 68,    68: 'Er',
  'Tm': 69,    69: 'Tm',
  'Yb': 70,    70: 'Yb',
  'Lu': 71,    71: 'Lu',
  'Hf': 72,    72: 'Hf',
  'Ta': 73,    73: 'Ta',
  'W' : 74,    74: 'W',
  'Re': 75,    75: 'Re',
  'Os': 76,    76: 'Os',
  'Ir': 77,    77: 'Ir',
  'Pt': 78,    78: 'Pt',
  'Au': 79,    79: 'Au',
  'Hg': 80,    80: 'Hg',
  'Tl': 81,    81: 'Tl',
  'Pb': 82,    82: 'Pb',
  'Bi': 83,    83: 'Bi',
  'Po': 84,    84: 'Po',
  'At': 85,    85: 'At',
  'Rn': 86,    86: 'Rn',
  'Fr': 87,    87: 'Fr',
  'Ra': 88,    88: 'Ra',
  'Ac': 89,    89: 'Ac',
  'Th': 90,    90: 'Th',
  'Pa': 91,    91: 'Pa',
  'U' : 92,    92: 'U',
  'Np': 93,    93: 'Np',
  'Pu': 94,    94: 'Pu',
  'Am': 95,    95: 'Am',
  'Cm': 96,    96: 'Cm',
  'Bk': 97,    97: 'Bk',
  'Cf': 98,    98: 'Cf',
  'Es': 99,    99: 'Es',
  'Fm': 100,  100: 'Fm',
  'Md': 101,  101: 'Md',
  'No': 102,  102: 'No',
  'Lr': 103,  103: 'Lr',
  'Rf': 104,  104: 'Rf',
  'Ha': 105,  105: 'Ha',
  'Sg': 106,  106: 'Sg',
  'Bh': 107,  107: 'Bh',
  'Hs': 108,  108: 'Hs',
  'Mt': 109,  109: 'Mt',
  'Ds': 110,  110: 'Ds',
  'Rg': 111,  111: 'Rg',
  'Cn': 112,  112: 'Cn',
 'Uut': 113,  113: 'Uut',
 'Uuq': 114,  114: 'Uuq',
 'Uup': 115,  115: 'Uup',
 'Uuh': 116,  116: 'Uuh',
 'Uus': 117,  117: 'Uus',
 'Uuo': 118,  118: 'Uuo',
};

"""
Ordered list of Chemical symbols for elements
"""
in_order = [atomic_number[i] for i in range(1,119)]


def periodic_table_index(Z):
  """
  Locations of elements in periodic table

  Parameters:
    Z: atomic number

  Returns:
    (row,col) 0-indexed

  Lanthanides and actinides rows are indexed 7 and 8
  """
  if 1 > Z or Z > 118:
    raise ValueError("Must have 1 <= Z <= 118")

  if 57 <= Z <= 70: # lanthanides
    return (7,3+Z-57)

  if 89 <= Z <= 102: # actinides
    return (8, 3+Z-89)

  # everything else
  lasts = [2,10,18,36,54,86,118]
  for i,l in enumerate(lasts):
    if Z <= l:
      if i == 0:
        col = 0 if Z == 1 else 17
      elif i == 1:
        col = Z-3 if Z < 5 else 12 + Z-5
      elif i == 2:
        col = Z-11 if Z < 13 else 12 + Z-13
      elif i == 3:
        col = Z - 19
      elif i == 4:
        col = Z - 37
      if i == 5:
        col = Z-55 if Z < 57 else 2 + Z-71
      elif i == 6:
        col = Z-87 if Z < 89 else 2 + Z-103
          
      return i,col
 
  raise ValueError()

