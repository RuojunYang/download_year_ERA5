import cdsapi
from configparser import ConfigParser


def download(year='2021'):
    config = ConfigParser()
    config.read('./config.cfg')
    for each in [
        '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_wind', '10m_v_component_of_wind',
        '2m_temperature', 'total_precipitation', 'relative_humidity', 'snowfall', 'snowmelt'
    ]:
        print("start download " + each + " in " + year)
        c = cdsapi.Client()

        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': [
                    each
                ],
                'year': [year],
                'month': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                ],
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'area': [
                    config.getint('variables', 'max_lat'), config.getint('variables', 'min_lon'),
                    config.getint('variables', 'min_lat'), config.getint('variables', 'max_lon'),
                ],
                'format': 'netcdf',
            },
            './download/' + year + '_' + each + '.nc')
        print("end download " + each + " in " + year)


if __name__ == '__main__':
    config = ConfigParser()
    config.read('./config.cfg')
    download(config.get('variables', 'year'))
