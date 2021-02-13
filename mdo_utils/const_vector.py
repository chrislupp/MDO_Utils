

from numpy import ones
from openmdao.api import ExplicitComponent




class ConstVector(ExplicitComponent):
    """
    A component that takes a scalar input and outputs an n-dimensional array
    with constant values.
    """


    def initialize(self):
        self.options.declare('N', default=2)

        self.options.declare('input', default='const')
        self.options.declare('output', default='vec')



    def setup(self):
        N = self.options['N']
        inp = self.options['input']
        out = self.options['output']


        # add the constant input
        self.add_input(inp, val=0.0)

        # add the output vector
        self.add_output(out, shape=(N))



    def setup_partials(self):
        N = self.options['N']
        inp = self.options['input']
        out = self.options['output']

        # define the gradients
        self.declare_partials(out, inp, val=ones(N))



    def compute(self, inputs, outputs):
        N = self.options['N']
        inp = self.options['input']
        out = self.options['output']

        outputs[out] = inputs[inp] * ones(N)