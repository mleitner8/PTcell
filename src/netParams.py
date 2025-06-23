"""
netParams.py

High-level specifications for M1 network model using NetPyNE

"""

from netpyne import specs
from cfg import cfg

cfg.update()
#try:
#    from __main__ import cfg # import SimConfig object with params from parent module
#except:
#    from src.cfg import cfg

#########################################################################################
#
#NETWORK PARAMETERS
#
#########################################################################################
netParams = specs.NetParams() # Object class NetParams to store network parameters


###############################################################################
# Cell parameters
###############################################################################

#------------------------------------------------------------------------------
# Load cell rules previously saved using netpyne format
#------------------------------------------------------------------------------
loadCellParams = True
saveCellParams = False

if loadCellParams:
   netParams.loadCellParamsRule(label='PT5B_full', fileName='../cells/Na12HH16HH_TF.json')
   netParams.addCellParamsWeightNorm('PT5B_full', '../conn/PT5B_full_weightNorm.pkl',
                                     threshold=cfg.weightNormThreshold)


###############################################################################
# Population parameters
###############################################################################

netParams.popParams['PT5B'] =	{'cellModel': 'HH_full', 'cellType': 'PT', 'numCells': 1}


###############################################################################
# Synaptic Mechanism parameters
###############################################################################

netParams.synMechParams['AMPA'] = {'mod':'MyExp2SynBB', 'tau1': 0.05, 'tau2': 5.3, 'e': 0}
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1NMDA': 15, 'tau2NMDA': 150, 'e': 0}


###############################################################################
# Stimulation parameters
###############################################################################

# ------------------------------------------------------------------------------
# Current inputs (IClamp)
# ------------------------------------------------------------------------------
if cfg.addIClamp:
    for key in [k for k in dir(cfg) if k.startswith('IClamp')]:
        params = getattr(cfg, key, None)
        [pop, sec, loc, start, dur, amp] = [params[s] for s in ['pop', 'sec', 'loc', 'start', 'dur', 'amp']]

        # add stim source
        netParams.stimSourceParams[key] = {
            'type': 'IClamp', 
            'delay': start, 
            'dur': dur, 
            'amp': amp}

        # connect stim source to target
        netParams.stimTargetParams[key + '_' + pop] = {
            'source': key,
            'conds': {'pop': pop},
            'sec': sec,
            'loc': loc}

# ------------------------------------------------------------------------------
# NetStim inputs
# ------------------------------------------------------------------------------
if cfg.addNetStim:
    for key in [k for k in dir(cfg) if k.startswith('NetStim')]:
        params = getattr(cfg, key, None)
        [pop, sec, loc, synMech, synMechWeightFactor, start, interval, noise, number, weight, delay] = \
            [params[s] for s in
             ['pop', 'sec', 'loc', 'synMech', 'synMechWeightFactor', 'start', 'interval', 'noise', 'number',
              'weight', 'delay']]

        # add stim source
        netParams.stimSourceParams[key] = {
            'type': 'NetStim', 
            'start': start, 
            'interval': interval, 
            'noise': noise,
            'number': number}

        # connect stim source to target
        netParams.stimTargetParams[key + '_' + pop] = {
            'source': key,
            'conds': {'pop': pop},
            'sec': sec,
            'loc': loc,
            'synMech': synMech,
            'weight': weight,
            'synMechWeightFactor': synMechWeightFactor,
            'delay': delay}
