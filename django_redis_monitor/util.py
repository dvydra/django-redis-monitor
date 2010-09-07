from django.conf import settings
import random

def is_sampling_request():
    sample_percentage = getattr(settings, 'REDIS_MONITOR_SAMPLE_PERCENTAGE', 100)
    return random.randint(1, 100) <= sample_percentage

def calculate_estimate(sample_value):
    sample_percentage = int(getattr(settings, 'REDIS_MONITOR_SAMPLE_PERCENTAGE', 100))
    if sample_percentage <= 0:
        return int(sample_value)
    elif sample_percentage >= 100:
        return int(sample_value) * 100
    else:
        return int(100 / sample_percentage) * int(sample_value)