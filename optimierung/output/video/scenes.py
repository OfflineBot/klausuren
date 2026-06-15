from manim import *

config.background_color = "#12161C"
BLUE_A  = "#6CB6FF"
GREEN_A = "#7FD18C"
AMBER   = "#FFD479"
TXT     = "#E8E8E8"
MUTE    = "#7A8290"
RED_A   = "#FF7B72"
F = "DejaVu Sans"

def T(s, size=34, color=TXT, w=BOLD):
    return Text(s, font=F, font_size=size, color=color, weight=w)

def title_bar(s):
    t = Text(s, font=F, font_size=40, color=BLUE_A, weight=BOLD).to_edge(UP, buff=0.35)
    line = Line(LEFT, RIGHT, color=BLUE_A).set_opacity(0.5).set_width(12).next_to(t, DOWN, buff=0.12)
    return VGroup(t, line)

# ---------------- 1 INTRO ----------------
class S01(Scene):
    def construct(self):
        t = Text("Optimierungsverfahren", font=F, font_size=64, color=BLUE_A, weight=BOLD)
        s = Text("Crashkurs mit Animationen — von Null zur Klausur", font=F, font_size=28, color=TXT)
        s.next_to(t, DOWN, buff=0.3)
        self.play(Write(t), run_time=1.2)
        self.play(FadeIn(s, shift=UP*0.3))
        self.wait(0.3)
        topics = ["Grundlagen", "Lineare Optimierung", "Transport",
                  "Nichtlinear & KKT", "Gradientenfrei", "Metaheuristiken", "Mehrziel"]
        items = VGroup(*[Text("•  "+x, font=F, font_size=26, color=GREEN_A) for x in topics])
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.18).scale(0.95).next_to(s, DOWN, buff=0.5)
        self.play(VGroup(t, s).animate.shift(UP*0.6))
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT*0.3) for i in items], lag_ratio=0.25), run_time=2.2)
        self.wait(0.8)

# ---------------- 2 GRUNDLAGEN ----------------
class S02(Scene):
    def construct(self):
        head = title_bar("1   Was ist Optimierung?")
        self.play(FadeIn(head))
        ax = Axes(x_range=[0,6,1], y_range=[0,5,1], x_length=8.5, y_length=4.2,
                  axis_config={"color":MUTE, "include_tip":True}).shift(DOWN*0.5)
        xlab = T("x  (Variable)", 22, MUTE, NORMAL).next_to(ax.x_axis, RIGHT, buff=0.1)
        ylab = T("f(x)", 22, MUTE, NORMAL).next_to(ax.y_axis, UP, buff=0.1)
        f = lambda x: 0.45*((x-1)**2)*((x-4)**2)/3 + 0.6
        graph = ax.plot(f, x_range=[0.2,5.4], color=BLUE_A)
        self.play(Create(ax), FadeIn(xlab), FadeIn(ylab), run_time=1.0)
        self.play(Create(graph), run_time=1.4)
        # local minima
        locmins = [1.0, 4.0]
        dots = VGroup(*[Dot(ax.c2p(x, f(x)), color=AMBER, radius=0.07) for x in locmins])
        labloc = T("lokale Minima", 22, AMBER, NORMAL).next_to(dots[0], UP, buff=0.2)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.4), FadeIn(labloc))
        # global min ball drop
        gx = 4.0
        ball = Dot(ax.c2p(gx, 4.2), color=GREEN_A, radius=0.12)
        self.play(FadeIn(ball))
        self.play(ball.animate.move_to(ax.c2p(gx, f(gx))), run_time=1.0, rate_func=rate_functions.ease_in_quad)
        gl = T("globales Minimum", 22, GREEN_A, NORMAL).next_to(ball, DOWN, buff=0.2)
        self.play(Write(gl))
        note = T("multimodal = mehrere Minima", 24, TXT, NORMAL).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note))
        self.wait(1.0)

# ---------------- 3 ANALYTISCHE OPTIMA ----------------
class S03(Scene):
    def construct(self):
        head = title_bar("2   Optimum rechnen:  f '(x) = 0")
        self.play(FadeIn(head))
        ax = Axes(x_range=[-1,3,1], y_range=[0,6,1], x_length=7.5, y_length=4.3,
                  axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*1.2)
        f = lambda x: (x-1)**2+2
        graph = ax.plot(f, x_range=[-0.7,3], color=BLUE_A)
        flabel = T("f(x) = x² − 2x + 3", 26, BLUE_A, NORMAL).to_corner(UR).shift(DOWN*1.2+LEFT*0.4)
        self.play(Create(ax), Create(graph), FadeIn(flabel), run_time=1.5)
        # moving tangent
        xt = ValueTracker(-0.4)
        def tangent():
            x = xt.get_value(); slope = 2*x-2; y = f(x)
            p = ax.c2p(x,y)
            dx = 0.9
            a = ax.c2p(x-dx, y - slope*dx); b = ax.c2p(x+dx, y + slope*dx)
            return Line(a, b, color=AMBER, stroke_width=5)
        tan = always_redraw(tangent)
        moving = always_redraw(lambda: Dot(ax.c2p(xt.get_value(), f(xt.get_value())), color=AMBER))
        self.play(Create(tan), FadeIn(moving))
        self.play(xt.animate.set_value(1.0), run_time=2.2, rate_func=linear)
        self.wait(0.2)
        dmin = Dot(ax.c2p(1, f(1)), color=GREEN_A, radius=0.1)
        steps = VGroup(
            T("f '(x) = 2x − 2 = 0", 26, TXT, NORMAL),
            T("⇒  x = 1", 28, GREEN_A, BOLD),
            T("f ''(x) = 2 > 0  ⇒  Minimum", 24, AMBER, NORMAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_corner(UR).shift(DOWN*2.4+LEFT*0.2)
        self.play(GrowFromCenter(dmin), Flash(dmin, color=GREEN_A))
        self.play(LaggedStart(*[FadeIn(s, shift=UP*0.2) for s in steps], lag_ratio=0.6), run_time=2.2)
        self.wait(0.8)

# ---------------- 4 LINEARE OPTIMIERUNG ----------------
class S04(Scene):
    def construct(self):
        head = title_bar("3   Lineare Optimierung (grafisch)")
        self.play(FadeIn(head))
        ax = Axes(x_range=[0,8,1], y_range=[0,7,1], x_length=7.6, y_length=4.6,
                  axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*1.6)
        self.play(Create(ax), run_time=0.8)
        goal = T("max  2x₁ + 3x₂", 26, BLUE_A, NORMAL).to_corner(UR).shift(DOWN*1.1+LEFT*0.3)
        self.play(FadeIn(goal))
        # constraints: x1<=4, x2<=5, x1+x2<=7
        c1 = Line(ax.c2p(4,0), ax.c2p(4,7), color=RED_A)
        c2 = Line(ax.c2p(0,5), ax.c2p(8,5), color=RED_A)
        c3 = Line(ax.c2p(7,0), ax.c2p(0,7), color=RED_A)
        self.play(Create(c1)); self.play(Create(c2)); self.play(Create(c3))
        verts = [ax.c2p(0,0), ax.c2p(4,0), ax.c2p(4,3), ax.c2p(2,5), ax.c2p(0,5)]
        region = Polygon(*verts, color=GREEN_A, fill_color=GREEN_A, fill_opacity=0.18, stroke_width=2)
        rlab = T("zulässiger Bereich", 22, GREEN_A, NORMAL).move_to(ax.c2p(2,1.6))
        self.play(FadeIn(region), FadeIn(rlab), run_time=1.0)
        # sliding isoline 2x1+3x2 = c  (perp to (2,3))
        iso = DashedLine(ax.c2p(0,1), ax.c2p(1.5,0), color=AMBER, stroke_width=4)
        iso_full = DashedLine(ax.c2p(-1,2.33), ax.c2p(3.5,-0.5), color=AMBER, stroke_width=4)
        def isoline(c):
            # 2x+3y=c -> endpoints
            p1 = ax.c2p(0, c/3); p2 = ax.c2p(c/2, 0)
            return DashedLine(p1, p2, color=AMBER, stroke_width=4)
        ct = ValueTracker(4.0)
        iso = always_redraw(lambda: isoline(ct.get_value()))
        isolab = T("Isolinie", 22, AMBER, NORMAL).to_corner(UR).shift(DOWN*2.0+LEFT*0.6)
        self.play(FadeIn(iso), FadeIn(isolab))
        self.play(ct.animate.set_value(19.0), run_time=2.6, rate_func=linear)
        opt = Dot(ax.c2p(2,5), color=GREEN_A, radius=0.1)
        optlab = T("Optimum (2, 5)", 24, GREEN_A, BOLD).next_to(opt, UR, buff=0.1).shift(RIGHT*0.2)
        self.play(GrowFromCenter(opt), Flash(opt, color=GREEN_A), FadeIn(optlab))
        note = T("Optimum liegt immer in einer Ecke", 24, TXT, NORMAL).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(note)); self.wait(0.8)

# ---------------- 5 TRANSPORT ----------------
class S05(Scene):
    def construct(self):
        head = title_bar("4   Transportproblem")
        self.play(FadeIn(head))
        S = [("S₁",30),("S₂",40),("S₃",20)]
        D = [("L₁",25),("L₂",35),("L₃",30)]
        ldots, rdots = VGroup(), VGroup()
        for i,(n,v) in enumerate(S):
            y = 1.3 - i*1.3
            d = Dot([-3.6, y, 0], color=BLUE_A, radius=0.12)
            lab = T(f"{n}: {v}", 22, BLUE_A, NORMAL).next_to(d, LEFT, buff=0.15)
            ldots.add(VGroup(d,lab))
        for j,(n,v) in enumerate(D):
            y = 1.3 - j*1.3
            d = Dot([3.6, y, 0], color=AMBER, radius=0.12)
            lab = T(f"{n}: {v}", 22, AMBER, NORMAL).next_to(d, RIGHT, buff=0.15)
            rdots.add(VGroup(d,lab))
        sl = T("Angebot", 22, BLUE_A, NORMAL).next_to(ldots, UP, buff=0.3)
        dl = T("Nachfrage", 22, AMBER, NORMAL).next_to(rdots, UP, buff=0.3)
        self.play(FadeIn(ldots), FadeIn(rdots), FadeIn(sl), FadeIn(dl))
        edges = VGroup()
        for i in range(3):
            for j in range(3):
                edges.add(Line(ldots[i][0].get_center(), rdots[j][0].get_center(),
                               color=MUTE, stroke_width=1.2).set_opacity(0.35))
        self.play(Create(edges), run_time=1.2)
        # NWE allocations on edges (i,j,amount)
        allocs = [(0,0,25),(0,1,5),(1,1,30),(1,2,10),(2,2,20)]
        anims=[]
        for i,j,a in allocs:
            e = Line(ldots[i][0].get_center(), rdots[j][0].get_center(), color=GREEN_A, stroke_width=3)
            mid = e.point_from_proportion(0.5)
            amt = T(str(a), 20, GREEN_A, BOLD).move_to(mid+UP*0.18)
            anims.append(AnimationGroup(Create(e), FadeIn(amt)))
        self.play(LaggedStart(*anims, lag_ratio=0.5), run_time=3.0)
        note = T("Start: Nordwesteck · Matrix-Minimum · Vogel", 23, TXT, NORMAL).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(note)); self.wait(0.8)

# ---------------- 6 KKT ----------------
class S06(Scene):
    def construct(self):
        head = title_bar("5   Nichtlinear & KKT")
        self.play(FadeIn(head))
        ax = Axes(x_range=[-1,3,1], y_range=[-1,3,1], x_length=5.2, y_length=4.4,
                  axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*3.2)
        self.play(Create(ax), run_time=0.7)
        center = ax.c2p(2,2)
        contours = VGroup(*[Circle(radius=r, color=BLUE_A, stroke_width=2).set_opacity(0.6).move_to(center)
                            for r in [0.45,0.9,1.4,1.95]])
        clab = T("Ziel: min (x−2)²+(y−2)²", 22, BLUE_A, NORMAL).next_to(ax, UP, buff=0.05).shift(RIGHT*0.2)
        self.play(LaggedStart(*[Create(c) for c in contours], lag_ratio=0.2), FadeIn(clab), run_time=1.6)
        circ = Circle(color=GREEN_A, stroke_width=4)
        circ.move_to(ax.c2p(0,0))
        # radius = 1 in data units
        circ.set_width(ax.c2p(1,0)[0]-ax.c2p(-1,0)[0])
        circ.move_to(ax.c2p(0,0))
        glab = T("g: x²+y² ≤ 1", 22, GREEN_A, NORMAL).next_to(circ, DOWN, buff=0.1)
        self.play(Create(circ), FadeIn(glab))
        d = Dot(ax.c2p(0,1), color=AMBER, radius=0.1)
        self.play(FadeIn(d))
        target = ax.c2p(0.707,0.707)
        self.play(d.animate.move_to(target), run_time=1.5)
        self.play(Flash(d, color=AMBER))
        kkt = VGroup(
            T("Lagrange: L = f + b·g", 24, AMBER, NORMAL),
            T("1) Stationarität:  ∇L = 0", 22, TXT, NORMAL),
            T("2) Zulässigkeit:  g ≤ 0", 22, TXT, NORMAL),
            T("3) Komplementär:  b·g = 0", 22, TXT, NORMAL),
            T("4) Vorzeichen:  b ≥ 0", 22, TXT, NORMAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_edge(RIGHT, buff=0.5).shift(DOWN*0.2)
        self.play(LaggedStart(*[FadeIn(k, shift=UP*0.2) for k in kkt], lag_ratio=0.5), run_time=2.8)
        self.wait(0.6)

# ---------------- 7 GRADIENTENFREI ----------------
class S07(Scene):
    def construct(self):
        head = title_bar("6   Gradientenfrei: Nelder-Mead")
        self.play(FadeIn(head))
        ax = Axes(x_range=[-3,3,1], y_range=[-2,3,1], x_length=7.5, y_length=4.6,
                  axis_config={"color":MUTE}).shift(DOWN*0.4)
        self.play(Create(ax), run_time=0.6)
        center = ax.c2p(0,0.5)
        contours = VGroup(*[Circle(radius=r, color=BLUE_A, stroke_width=1.6).set_opacity(0.5).move_to(center)
                            for r in [0.5,1.0,1.6,2.2]])
        self.play(LaggedStart(*[Create(c) for c in contours], lag_ratio=0.15), run_time=1.2)
        # triangle (worst far from center)
        A = ax.c2p(2,2.4); B = ax.c2p(2.3,0.2); C = ax.c2p(0.4,2.0)
        tri = Polygon(A,B,C, color=AMBER, fill_color=AMBER, fill_opacity=0.12, stroke_width=3)
        dA,dB,dC = Dot(A,color=AMBER), Dot(B,color=AMBER), Dot(C,color=AMBER)
        wlab = T("schlechtester", 20, RED_A, NORMAL).next_to(dA, UP, buff=0.1)
        self.play(Create(tri), *[GrowFromCenter(x) for x in (dA,dB,dC)], FadeIn(wlab))
        # reflect worst A across centroid of B,C
        import numpy as np
        cen = (np.array(B)+np.array(C))/2
        refl = 2*cen - np.array(A)
        cdot = Dot(cen, color=MUTE, radius=0.05)
        arr = Arrow(A, refl, color=GREEN_A, buff=0, stroke_width=4)
        rlab = T("reflect", 22, GREEN_A, NORMAL).next_to(arr.get_end(), DOWN, buff=0.1)
        self.play(FadeIn(cdot), GrowArrow(arr), FadeIn(rlab))
        newtri = Polygon(refl, B, C, color=GREEN_A, fill_color=GREEN_A, fill_opacity=0.12, stroke_width=3)
        self.play(Transform(tri, newtri), FadeOut(wlab), FadeOut(dA))
        steps = T("reflect → expand / contract / shrink", 24, TXT, NORMAL).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(steps)); self.wait(0.8)

# ---------------- 8 METAHEURISTIK ----------------
class S08(Scene):
    def construct(self):
        head = title_bar("7   Metaheuristiken: (1+1)-ES")
        self.play(FadeIn(head))
        ax = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=5.4, y_length=4.6,
                  axis_config={"color":MUTE}).shift(LEFT*3.0+DOWN*0.3)
        self.play(Create(ax), run_time=0.6)
        center = ax.c2p(0,0)
        contours = VGroup(*[Circle(radius=r, color=BLUE_A, stroke_width=1.6).set_opacity(0.5).move_to(center)
                            for r in [0.5,1.1,1.8,2.5]])
        star = Star(color=GREEN_A, fill_opacity=1).scale(0.12).move_to(center)
        self.play(LaggedStart(*[Create(c) for c in contours], lag_ratio=0.15), FadeIn(star), run_time=1.2)
        import numpy as np
        pts = [(-2.2,2.2),(-1.3,1.4),(-0.6,1.0),(-0.2,0.4),(0.1,0.15)]
        cur = Dot(ax.c2p(*pts[0]), color=AMBER, radius=0.1)
        self.play(FadeIn(cur))
        for k in range(1,len(pts)):
            cloud = VGroup(*[Dot(ax.c2p(pts[k-1][0]+0.4*np.cos(a), pts[k-1][1]+0.4*np.sin(a)),
                                 color=MUTE, radius=0.04) for a in np.linspace(0,2*np.pi,8,endpoint=False)])
            self.play(FadeIn(cloud, scale=0.5), run_time=0.3)
            self.play(cur.animate.move_to(ax.c2p(*pts[k])), FadeOut(cloud), run_time=0.5)
        self.play(Flash(cur, color=GREEN_A))
        info = VGroup(
            T("mutieren → behalten wenn besser", 24, TXT, NORMAL),
            T("1/5-Regel: Erfolg > 1/5 → σ↑", 24, AMBER, NORMAL),
            T("auch: Sim. Annealing, PSO, ACO", 24, GREEN_A, NORMAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.5)
        self.play(LaggedStart(*[FadeIn(i, shift=UP*0.2) for i in info], lag_ratio=0.5), run_time=2.2)
        self.wait(0.6)

# ---------------- 9 MEHRZIEL ----------------
class S09(Scene):
    def construct(self):
        head = title_bar("8   Mehrzieloptimierung: Pareto")
        self.play(FadeIn(head))
        ax = Axes(x_range=[0,8,1], y_range=[0,8,1], x_length=6.0, y_length=5.0,
                  axis_config={"color":MUTE}).shift(DOWN*0.3+LEFT*1.4)
        x1 = T("f₁", 22, MUTE, NORMAL).next_to(ax.x_axis, RIGHT, buff=0.1)
        x2 = T("f₂", 22, MUTE, NORMAL).next_to(ax.y_axis, UP, buff=0.1)
        self.play(Create(ax), FadeIn(x1), FadeIn(x2), run_time=0.8)
        pareto = [(1,6),(2,4),(3,2.5),(5,1.5)]
        dom = [(3,5),(4.5,4),(5,5.5),(6,3)]
        pdots = VGroup(*[Dot(ax.c2p(*p), color=GREEN_A, radius=0.09) for p in pareto])
        ddots = VGroup(*[Dot(ax.c2p(*p), color=AMBER, radius=0.09) for p in dom])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in [*pdots, *ddots]], lag_ratio=0.15), run_time=2.0)
        self.wait(0.3)
        # dominated fade to grey
        domlab = T("dominiert", 22, MUTE, NORMAL).next_to(ddots[2], UR, buff=0.1)
        self.play(*[d.animate.set_color(MUTE).scale(0.7) for d in ddots], FadeIn(domlab))
        front = VMobject(color=GREEN_A, stroke_width=3)
        front.set_points_as_corners([ax.c2p(*p) for p in pareto])
        flab = T("Pareto-Front", 24, GREEN_A, BOLD).next_to(pdots[0], UP, buff=0.2)
        self.play(Create(front), FadeIn(flab))
        info = VGroup(
            T("dominiert: in allem ≤,", 22, TXT, NORMAL),
            T("irgendwo <", 22, TXT, NORMAL),
            T("Pareto = bester", 22, GREEN_A, NORMAL),
            T("Kompromiss", 22, GREEN_A, NORMAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.5)
        self.play(LaggedStart(*[FadeIn(i) for i in info], lag_ratio=0.4), run_time=2.0)
        self.wait(0.6)

# ---------------- 10 OUTRO ----------------
class S10(Scene):
    def construct(self):
        t = Text("So bestehst du die Klausur", font=F, font_size=44, color=BLUE_A, weight=BOLD).to_edge(UP, buff=0.7)
        self.play(Write(t), run_time=1.0)
        pts = [
            "Aktiv rechnen: Übungen + 3 Probeklausuren",
            "Pro Aufgabentyp ein Rezept auswendig",
            "Erst verdeckt lösen, dann Musterlösung",
            "Grafik-Aufgaben: zulässigen Bereich sauber zeichnen",
        ]
        items = VGroup(*[Text("✓  "+p, font=F, font_size=27, color=GREEN_A) for p in pts])
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.32).next_to(t, DOWN, buff=0.6)
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT*0.3) for i in items], lag_ratio=0.4), run_time=2.6)
        vg = Text("Viel Erfolg!", font=F, font_size=40, color=AMBER, weight=BOLD).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(vg, scale=1.2)); self.wait(1.0)
