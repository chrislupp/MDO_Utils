


from openmdao.api import Problem
from mdo_utils import ConstVector


prob = Problem()


model = prob.model


model.add_subsystem('const', ConstVector(input='in', output='out', N=10))


prob.setup()


prob['const.in'] = 2.0


prob.run_model()

print(prob['const.out'])