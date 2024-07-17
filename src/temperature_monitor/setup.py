import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'temperature_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch/'),
         glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sami',
    maintainer_email='samitrad7@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'temp_pubNode= temperature_monitor.temp_publisher:main',
        	'alert_node=temperature_monitor.alert_publ:main',
        	'threshold_node=temperature_monitor.threshold_sub:main'
        
        
        ],
    },
)
