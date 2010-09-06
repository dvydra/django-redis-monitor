from django.conf import settings
import random

def is_sampling_request():
    sample_percentage = getattr(settings, 'REDIS_MONITOR_SAMPLE_PERCENTAGE', 100)
    return sample_percentage <= random.randint(1, 100)

def calculate_estimate(sample_value):
    sample_percentage = getattr(settings, 'REDIS_MONITOR_SAMPLE_PERCENTAGE', 100)
    if sample_percentage <= 0:
        return sample_value
    elif sample_percentage > 100:
        return sample_value * 100
    else:
        return (100 / sample_percentage) * sample_value