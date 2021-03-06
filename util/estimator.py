#Helper module to calculate average and variance estimators
#Mean returning functions separated for legibility
import math
import scipy.stats

#t_student table value for alpha = 0.05
def t_st_value(samples):
    return scipy.stats.t.ppf(0.975, samples)

def mean(sum, samples):
    """Returns the estimated mean using the -sum- of the calculated values and the number of -samples- """
    return sum/float(samples)

def variance(sum, square_sum, samples):
    """Returns the estimated variance using the incremental form.
       sums -sum- and -square_sum- of each sample mean and the number -samples- of samples """
    return square_sum/float(samples-1) - (sum**2)/float(samples*(samples-1))
    
def confidence_interval(sum, square_sum, samples):
    """Returns the confidence interval bound, given the -sum- and -square_sum- of the values to calculate
       the standard deviation and the total number of -samples- """
    std_deviation = math.sqrt(variance(sum, square_sum, samples))
    return (t_st_value(samples)*std_deviation)/math.sqrt(samples)

if __name__ == "__main__":
    "Testing..."
    list1 = [11.0, 5.0, 10.0, 9.0, 15.0, 6.0, 18.0, 8.0, 12.0, 9.0, 5.0, 10.0, 7.0, 13.0, 15.0]
    list2 = [10.0, 2.0, 15.0, 4.0, 5.0, 16.0, 8.0, 4.0, 2.0, 19.0, 10.0, 2.0, 9.0, 10.0, 12.0]
    print "Mean sample 1: ", sample_mean(list1)
    print "Mean sample 2: ", sample_mean(list2)
    print "Samples mean: ", mean((mean(list1) + mean(list2)), 2)
    print "Samples variance: ", variance((mean(list1) + mean(list2)), ((mean(list1)**2) + (mean(list2)**2)), 2)
