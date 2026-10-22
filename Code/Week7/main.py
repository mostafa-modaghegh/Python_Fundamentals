import inputs , average , state
from inputs import get_inputs

#import inputs as IN
math , english , programming = get_inputs()
ave = average.cal_average(math , english , programming)
state.print_state(ave)
