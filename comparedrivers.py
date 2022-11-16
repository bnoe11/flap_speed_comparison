import matplotlib.pyplot as plt
import fastf1.plotting

fastf1.Cache.enable_cache('Cache')

#fastf1.plotting.setup_mpl()
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1', misc_mpl_mods=True)


session = fastf1.get_session(2021, 'Monza', 'R')
session.load()

driver1 = 'NOR'
driver2 = 'RIC'

d1lap = session.laps.pick_driver(driver1).pick_fastest()
d2lap = session.laps.pick_driver(driver2).pick_fastest()

d1tel = d1lap.get_car_data()
d2tel = d2lap.get_car_data()

d1_col = fastf1.plotting.driver_color(driver1)
d2_col = fastf1.plotting.driver_color(driver2)

fig, ax = plt.subplots()

ax.plot(d1tel['Time'], d1tel['Speed'], color = d1_col, label = driver1)
ax.plot(d2tel['Time'], d2tel['Speed'], color = d2_col, label = driver2)

ax.set_xlabel('Time (min)\n@bnoebnoe | @ur_sac')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Top 2 Finishers Fastest Laps\n " f"{session.event['EventName']} {session.event.year} Race")

plt.show()