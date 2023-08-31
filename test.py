
import numpy
import random
from numpy.random import seed
from numpy.random import randn
from numpy.random import normal
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from matplotlib import pyplot
# create two independent sample groups
sample1= normal(3, 1, 100)
sample2= normal(4, 2, 100)
print('Sample 1: ',sample1)
print('Sample 2: ',sample2)

t_stat, p_value = ttest_ind(sample1, sample2)
print("T-statistic value: ", t_stat)  
print("P-Value: %.2f",  p_value)
if p_value <= 0.05:
    print("Conclusion Reject H0")
else:
    print("Conclusion Do Not Reject H0")


bins = numpy.linspace(-10, 10,100)

# create histograms of the two sample groups
pyplot.hist(sample1, bins,alpha=0.5, label='Sample 1')
pyplot.hist(sample2, bins,alpha=0.5, label='Sample 2')
pyplot.legend(loc='upper right')
pyplot.title('Histogram of Two Independent Sample Groups')
pyplot.xlabel('Values')
pyplot.ylabel('Frequency')
pyplot.xlim(-12,12)
# pyplot.ylim(0,45)
pyplot.show()
