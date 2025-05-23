# Copyright 2020-2021 Ecole Nationale des Ponts et Chaussées
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Original author Lucas Vivier <vivier@centre-cired.fr>

from pandas import DataFrame, Series, read_csv
from project.utils import get_pandas, get_series

resources_data = dict()

performance_stock = get_pandas('project/input/resources_dir/performance_stock.csv', lambda x: read_csv(x, index_col=[0], header=[0]).squeeze())
resources_data['performance_stock'] = performance_stock

consumption_hist = get_pandas('project/input/resources_dir/hist_consumption.csv', lambda x: read_csv(x, index_col=[0], header=[0])).T
consumption_hist.index = consumption_hist.index.astype(int)
resources_data['consumption_hist'] = {k: Series(item, name='Historic') for k, item in consumption_hist.to_dict().items()}

consumption_hist = get_series('project/input/resources_dir/hist_consumption_total.csv')
consumption_hist.index = consumption_hist.index.astype(int)
resources_data['consumption_total_hist'] = consumption_hist.rename('Historic')

# resources_data['consumption_total_objectives'] = Series([176, 146], index=[2030, 2050], name='Objectives')
# resources_data['emissions_total_objectives'] = Series([0.6, 0.9], index=[2030, 2050], name='Objectives')

resources_data['retrofit_hist'] = get_pandas('project/input/resources_dir/hist_retrofit.csv', lambda x: read_csv(x, index_col=[0], header=[0]))
resources_data['retrofit_hist'] = {k: DataFrame({2019: item}).T / 10 ** 3 for k, item in
                                   resources_data['retrofit_hist'].T.to_dict().items()}

retrofit_comparison = get_pandas('project/input/resources_dir/retrofit_comparison_resirf3.csv', lambda x: read_csv(x, index_col=[0], header=[0]))
resources_data['retrofit_comparison'] = retrofit_comparison

"""resources_data['public_policies_2019'] = DataFrame([1.88, 1.05, 0, 1.32, 0.56, 0.5],
                                                   index=['Cee', 'Cite', 'Mpr', 'Reduced vat', 'Zero interest loan', 'Mpr serenite'],
                                                   columns=[2019])"""
resources_data['policies_hist'] = get_pandas('project/input/resources_dir/hist_policies.csv', lambda x: read_csv(x, index_col=[0], header=[0]))


calibration_data = get_pandas('project/input/resources_dir/data_ceren.csv', lambda x: read_csv(x, index_col=[0]).squeeze())
resources_data['data_calibration'] = calibration_data

data_validation = get_pandas('project/input/resources_dir/data_validation.csv', lambda x: read_csv(x, index_col=[0], header=[0]).squeeze())
resources_data['data_validation'] = data_validation

resources_data['investment_per_renovating_houshold_decision_maker'] = {k: DataFrame([9100], index=['TREMI 2019'],
                                                                                      columns=[2019]).T for k in [
    'Single-family - {}'.format(i) for i in ['Owner-occupied', 'Privately rented', 'Social-housing']] + [
    'Multi-family - {}'.format(i) for i in ['Owner-occupied', 'Privately rented', 'Social-housing']]}

resources_data['investment_per_renovating_houshold_income_owner'] = {k:  DataFrame([9100], index=['TREMI 2019'], columns=[2019]).T for k in
                                  ['D{}'.format(i) for i in range(1, 11)]}

resources_data['index'] = {'Income tenant': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'],
                           'Income owner': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'],
                           'Occupancy status': ['Owner-occupied', 'Privately rented', 'Social-housing'],
                           'Housing type': ['Single-family', 'Multi-family'],
                           'Performance': ['G', 'F', 'E', 'D', 'C', 'B', 'A'],
                           'Energy': ['Electricity', 'Natural gas', 'Oil fuel', 'Wood fuel', 'Heating'],
                           'Heater': ['Direct electric', 'Heat pump', 'Natural gas', 'Oil fuel', 'Wood fuel', 'District heating'],
                           'Decision maker': ['Single-family - Owner-occupied', 'Multi-family - Owner-occupied',
                                              'Single-family - Privately rented', 'Multi-family - Privately rented',
                                              'Single-family - Social-housing', 'Multi-family - Social-housing'
                                              ],
                           'Insulation': ['Wall', 'Floor', 'Roof', 'Windows'],
                           'Heating system': ['Electricity-Heat pump water', 'Electricity-Heat pump air',
                                              'Electricity-Direct electric',
                                              'Natural gas-Performance boiler', 'Natural gas-Collective boiler',
                                              'Oil fuel-Performance boiler', 'Oil fuel-Collective boiler',
                                              'Wood fuel-Performance boiler', 'Heating-District heating'],
                           'Fossil': ['Natural gas-Performance boiler', 'Natural gas-Collective boiler',
                                      'Oil fuel-Performance boiler', 'Oil fuel-Collective boiler'],
                           'Low Carbon': ['Electricity-Heat pump water', 'Electricity-Heat pump air',
                                          'Wood fuel-Performance boiler', 'Heating-District heating'],
                           'Count': [1, 2, 3, 4, 5],
                           'Heat pumps': ['Electricity-Heat pump water', 'Electricity-Heat pump air'],
                           'Dwelling': ['Existing', 'Housing type', 'Occupancy status', 'Wall', 'Floor', 'Roof', 'Windows', 'Heating system']
                           }

resources_data['heating2heater'] = {
    'Electricity-Heat pump water': 'Heat pump',
    'Electricity-Heat pump air': 'Heat pump',
    'Electricity-Direct electric': 'Direct electric',
    'Natural gas-Performance boiler': 'Natural gas',
    'Natural gas-Collective boiler': 'Natural gas',
    'Oil fuel-Performance boiler': 'Oil fuel',
    'Oil fuel-Collective boiler': 'Oil fuel',
    'Wood fuel-Performance boiler': 'Wood fuel',
    'Heating-District heating': 'District heating'
}
resources_data['quintiles'] = ['C1', 'C2', 'C3', 'C4', 'C5']

colors = {
    "Owner-occupied": "lightcoral",
    "Privately rented": "chocolate",
    "Social-housing": "orange",
    "Single-family": "brown",
    "Multi-family": "darkolivegreen",
    "Single-family - Owner-occupied": "firebrick",
    "Multi-family - Owner-occupied": "salmon",
    "Single-family - Privately rented": "darkgreen",
    "Multi-family - Privately rented": "mediumseagreen",
    "Single-family - Social-housing": "chocolate",
    "Multi-family - Social-housing": "darkorange",
    "G": "black",
    "F": "dimgrey",
    "E": "grey",
    "D": "darkgrey",
    "C": "darkgreen",
    "B": "forestgreen",
    "A": "limegreen",
    1: "dimgrey",
    2: "grey",
    3: "darkgreen",
    4: "forestgreen",
    5: "limegreen",
    "C1": "black",
    "C2": "darkred",
    "C3": "firebrick",
    "C4": "orangered",
    "C5": "lightcoral",
    "D1": "black",
    "D2": "maroon",
    "D3": "darkred",
    "D4": "brown",
    "D5": "firebrick",
    "D6": "orangered",
    "D7": "tomato",
    "D8": "lightcoral",
    "D9": "lightsalmon",
    "D10": "darksalmon",
    "Others": "saddlebrown",
    "Heat pump": "gold",
    "Electricity": "darkorange",
    "Natural gas": "slategrey",
    "Oil fuel": "black",
    "Wood fuel": "saddlebrown",
    "Heating": "forestgreen",
    "District heating": "forestgreen",
    "Electricity-Heat pump water": "sandybrown",
    "Electricity-Heat pump air": "gold",
    "Electricity-Direct electric": "darkorange",
    "Direct electric": "darkorange",
    "Natural gas-Performance boiler": "slategrey",
    "Natural gas-Standard boiler": "grey",
    "Natural gas-Collective boiler": "lightgrey",
    "Oil fuel-Performance boiler": "black",
    "Oil fuel-Standard boiler": "black",
    "Oil fuel-Collective boiler": "dimgray",
    "Wood fuel-Performance boiler": "saddlebrown",
    "Wood fuel-Standard boiler": "saddlebrown",
    "Heating-District heating": "forestgreen",
    "Saving heater": "royalblue",
    "Saving insulation": "darksalmon",
    "Saving prices": "grey",
    "VAT": "grey",
    "Energy taxes": "blue",
    "Energy vat": "red",
    "Taxes expenditure": "darkorange",
    "Energy expenditure": "darkorange",
    "Energy": "darkorange",
    "Existing": "tomato",
    "New": "lightgrey",
    "Renovation": "brown",
    "Construction": "dimgrey",
    'Investment': 'firebrick',
    "Financing": "darksalmon",
    'Cost': 'firebrick',
    'Annuities heater': 'lightcoral',
    'Annuities insulation': 'firebrick',
    "Insulation": 'firebrick',
    "Heater": 'royalblue',
    "Subsidies heater": 'lightblue',
    'Embodied emission': 'darkgreen',
    'Embodied emission additional': 'darkgreen',
    'Indirect emission': 'darkgreen',
    'COFP': 'grey',
    'Opportunity cost': 'grey',
    'Unobserved value': 'darkmagenta',
    'Comfort prices': 'saddlebrown',
    'Comfort price': 'saddlebrown',
    'Saving price': 'peachpuff',
    'Thermal comfort prices': 'saddlebrown',
    'Thermal comfort': 'chocolate',
    'Comfort EE': 'chocolate',
    'Comfort': 'chocolate',
    'Energy saving': 'darkorange',
    'Saving EE': 'darkorange',
    'Emission saving': 'forestgreen',
    'Direct emission': 'forestgreen',
    'Health cost': 'royalblue',
    'Well-being benefit': 'royalblue',
    'Health savings': 'blue',
    'Mortality reduction benefit': 'lightblue',
    'Social NPV': 'black',
    'Windows': 'royalblue',
    'Roof': 'darkorange',
    'Floor': 'grey',
    'Wall': 'darkslategrey',
    "Very low income global renovation": "darkorange",
    "Low income global renovation": "darkslategrey",
    "Global renovation": "grey",
    "Best efficiency": 'lightblue',
    "Best efficiency fg": 'lightblue',
    "Global renovation fg": 'lightblue',
    "Global renovation fge": 'lightblue',
    "Fg": 'lightblue'
}

colors_policies = {
    "Subsidies": "royalblue",
    "Taxes": "grey",
    "Subsidies heater": "lightblue",
    "Subsidies insulation": "darksalmon",
    "Reduced vat": "darkolivegreen",
    "Reduced VAT": "darkolivegreen",
    "Cee": "tomato",
    "White certificate": "tomato",
    "White certificate obligations": "tomato",
    "Cee tax": "red",
    "Cite": "blue",
    "Zero interest loan": "darkred",
    "Zero interest": "darkred",
    "Over cap": "grey",
    "Carbon tax": "darkgreen",
    "Mpr": "darkmagenta",
    "Mpr efficacite": "darkmagenta",
    "Mpr multifamily": "pink",
    "Mpr multifamily updated": "pink",
    "Mpr multifamily deep": "pink",
    "Mpr serenite": "violet",
    "Mpr performance": "purple",
    "Valorem insulation": "darkorange",
    'Sub ad valorem': "darkorange",
    "Sub merit": "slategrey",
    "Sub obligation": "darkorange",
    "Subsidy": "darkmagenta",
    "Subsidy proportional": "lightblue",
    "Direct subsidies": "blue"
}

colors.update(colors_policies)

resources_data['colors'] = colors
