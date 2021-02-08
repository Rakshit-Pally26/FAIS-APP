from django.contrib import admin
from .models import realtime_usgs_data,post_local,us_state,twitter_data,historical_usgs_data,flood_station_list,select_state,tweet_streamer, peak_rate
# Register your models here.

admin.site.register(realtime_usgs_data)
admin.site.register(post_local)
admin.site.register(us_state)
admin.site.register(twitter_data)
admin.site.register(historical_usgs_data)
admin.site.register(flood_station_list)
admin.site.register(select_state)
admin.site.register(tweet_streamer)
admin.site.register(peak_rate)