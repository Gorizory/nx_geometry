from .operations import printer, CreateManager
from .nx_math import (distTwoPoint,
					  eqTwoPoint,
					  perpTwoLines,
					  parTwoLines, 
					  angleTwoLines, 
					  hor, 
					  ver)

mapped_operations = [
	('create_point', CreateManager.create_point),
	('create_line', CreateManager.create_line),

	('drag_point', None),
	('drag_line', None),

	('horizontal', hor),
	('vertical', ver),
	('parallel', parTwoLines),
	('perpendicular', perpTwoLines),

	('connect_points', eqTwoPoint), 

	('attache_point_to_line', None),
	('angle_between_lines', None),
	
	('dist_between_points', distTwoPoint),

	('test', printer)
]
