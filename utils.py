
import numpy as np
from pandas import DataFrame
from consts import AUDIO_FIELD
from datetime import datetime, timedelta


def apply_filters(df: DataFrame, skipped=None, reason_start=None, reason_end=None, platform=None):

	if not skipped is None:
		df = df[df[AUDIO_FIELD.SKIPPED] == skipped]
	if not reason_start is None:
		df = df[df[AUDIO_FIELD.REASON_START] == reason_start]
	if not reason_end is None:
		df = df[df[AUDIO_FIELD.REASON_END] == reason_end]
	if not platform is None:
		df = df[df[AUDIO_FIELD.PLATFORM] == platform]

	return df

def filter_by_field(df, field, value):
	return df[df[field] == value]


def calc_listen_amount(df: DataFrame, field=None, value=None, skipped=None, reason_start=None, reason_end=None, platform=None, human_readable=True):

	df = apply_filters(df, skipped, reason_start, reason_end, platform)

	listen_amount_ms = df[AUDIO_FIELD.MS_PLAYED].sum()
	if human_readable:
		total_seconds = listen_amount_ms // 1000
		days = total_seconds // 86400
		hours = (total_seconds % 86400) // 3600
		minutes = (total_seconds % 3600) // 60
		seconds = total_seconds % 60

		listen_amount_hr = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds.'
		return listen_amount_hr
	else:
		return listen_amount_ms


def stats_most_listened(df: DataFrame, field, skipped=None, reason_start=None, reason_end=None, platform=None):

	df = apply_filters(df, skipped, reason_start, reason_end, platform)

	value_counts = df[field].value_counts(sort=True, ascending=False).reset_index()
	return value_counts
