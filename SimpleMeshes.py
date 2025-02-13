import gmsh
import sys

gmsh.initialize()

gmsh.model.add("cube_circle_cylinder")

lc = 1e-2
'''
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 2)
gmsh.model.geo.addPoint(0, 0, 0.1, lc, 3)
gmsh.model.geo.addPoint(0, 0, 0, lc, 4)
gmsh.model.geo.addPoint(0.1, 0.1, 0.1, lc, 5)
gmsh.model.geo.addPoint(0.1, 0.1, 0, lc, 6)
gmsh.model.geo.addPoint(0, 0.1, 0.1, lc, 7)
gmsh.model.geo.addPoint(0.1, 0, 0.1, lc, 8)

gmsh.model.geo.addLine(4, 3, 1)

gmsh.model.geo.addLine(3, 8, 2)
gmsh.model.geo.addLine(3, 7, 3)

gmsh.model.geo.addLine(8, 1, 4)
gmsh.model.geo.addLine(7, 2, 5)

gmsh.model.geo.addLine(1, 4, 6)
gmsh.model.geo.addLine(2, 4, 7)

gmsh.model.geo.addLine(7, 5, 8)
gmsh.model.geo.addLine(8, 5, 9)

gmsh.model.geo.addLine(5, 6, 10)

gmsh.model.geo.addLine(6, 2, 11)
gmsh.model.geo.addLine(6, 1, 12)

gmsh.model.geo.addCurveLoop([1, 2, 4, 6], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([1, 3, 5, 7], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([10, 12, -4, 9], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([10, 11, -5, 8], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([2, 9, -8, -3], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([11, 7, -6, -12], 6)
gmsh.model.geo.addPlaneSurface([6], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])
'''
'''
gmsh.model.geo.addPoint(0.1, 0.1, 0, lc, 0)
gmsh.model.geo.addPoint(0.1, 0.2, 0, lc, 1)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 2)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 3)
gmsh.model.geo.addPoint(0.2, 0.1, 0, lc, 4)

gmsh.model.geo.addCircleArc(3, 0, 4, 1)
gmsh.model.geo.addCircleArc(4, 0, 1, 2)
gmsh.model.geo.addCircleArc(1, 0, 2, 3)
gmsh.model.geo.addCircleArc(2, 0, 3, 4)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)

gmsh.model.geo.addPlaneSurface([1], 1)
'''

gmsh.model.geo.addPoint(0.1, 0.1, 0.25, 0)
gmsh.model.geo.addPoint(0.1, 0.1, 0, lc, 10)
gmsh.model.geo.addPoint(0.1, 0.2, 0, lc, 11)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 12)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 13)
gmsh.model.geo.addPoint(0.2, 0.1, 0, lc, 14)

gmsh.model.geo.addCircleArc(13, 10, 14, 11)
gmsh.model.geo.addCircleArc(14, 10, 11, 12)
gmsh.model.geo.addCircleArc(11, 10, 12, 13)
gmsh.model.geo.addCircleArc(12, 10, 13, 14)
gmsh.model.geo.addCurveLoop([11, 12, 13, 14], 11)
gmsh.model.geo.addPlaneSurface([11], 11)

gmsh.model.geo.addPoint(0.1, 0.1, 0.5, lc, 20)
gmsh.model.geo.addPoint(0.1, 0.2, 0.5, lc, 21)
gmsh.model.geo.addPoint(0, 0.1, 0.5, lc, 22)
gmsh.model.geo.addPoint(0.1, 0, 0.5, lc, 23)
gmsh.model.geo.addPoint(0.2, 0.1, 0.5, lc, 24)

gmsh.model.geo.addCircleArc(23, 20, 24, 21)
gmsh.model.geo.addCircleArc(24, 20, 21, 22)
gmsh.model.geo.addCircleArc(21, 20, 22, 23)
gmsh.model.geo.addCircleArc(22, 20, 23, 24)
gmsh.model.geo.addCurveLoop([21, 22, 23, 24], 21)
gmsh.model.geo.addPlaneSurface([21], 21)

gmsh.model.geo.addLine(11, 21, 1)
gmsh.model.geo.addLine(22, 12, 2)
gmsh.model.geo.addLine(13, 23, 3)
gmsh.model.geo.addLine(24, 14, 4)

gmsh.model.geo.addCurveLoop([1, 23, 2, -13], 1)
gmsh.model.geo.addCurveLoop([2, 14, 3, -24], 2)
gmsh.model.geo.addCurveLoop([3, 21, 4, -11], 3)
gmsh.model.geo.addCurveLoop([4, 12, 1, -22], 4)

gmsh.model.geo.addPlaneSurface([1], 1)

# Цилиндр не вышел, надо через циклы делать

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(2)

gmsh.write("cube_circle_cylinder.msh")
# gmsh.write("cube_circle_cylinder.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

