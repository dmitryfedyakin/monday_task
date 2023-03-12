import ru_local

start_dist = 16637000000
voyage_speed = 38241
wave_speed = 299792458 * 2.237

days = int(input(ru_local.INPUT))
dist_ml = start_dist + days * voyage_speed
dist_km = dist_ml * 1.609
dist_astro_unit = dist_ml * 1.076 * 10**(-8)
wave_time = dist_ml / wave_speed

print(ru_local.DIST_ML, dist_ml)
print(ru_local.DIST_KM, dist_km)
print(ru_local.DIST_ASTRO_UNIT, dist_astro_unit)
print(ru_local.WAVE_TIME, wave_time)
