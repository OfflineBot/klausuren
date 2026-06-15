from manim import *
import numpy as np

config.background_color = "#12161C"
BLUE_A="#6CB6FF"; GREEN_A="#7FD18C"; AMBER="#FFD479"; TXT="#E8E8E8"; MUTE="#7A8290"; RED_A="#FF7B72"
F="DejaVu Sans"

def T(s, size=30, color=TXT, w=NORMAL):
    return Text(s, font=F, font_size=size, color=color, weight=w)

def title_bar(s):
    t=Text(s, font=F, font_size=38, color=BLUE_A, weight=BOLD).to_edge(UP, buff=0.32)
    ln=Line(LEFT,RIGHT,color=BLUE_A).set_opacity(0.5).set_width(12.2).next_to(t,DOWN,buff=0.1)
    return VGroup(t,ln)

def bullets(lines, size=26, buff=0.26, colors=None):
    g=VGroup()
    for i,l in enumerate(lines):
        c = colors[i] if colors else TXT
        g.add(Text(l, font=F, font_size=size, color=c))
    g.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    return g

def reveal(scene, mobs, lag=0.5, rt=2.2, shift=0.2):
    scene.play(LaggedStart(*[FadeIn(m, shift=UP*shift) for m in mobs], lag_ratio=lag), run_time=rt)

def contours(center, radii, color=BLUE_A):
    return VGroup(*[Circle(radius=r, color=color, stroke_width=1.6).set_opacity(0.5).move_to(center) for r in radii])

# ---------- D01 Intro ----------
class D01(Scene):
    def construct(self):
        t=Text("Optimierungsverfahren", font=F, font_size=58, color=BLUE_A, weight=BOLD)
        s=Text("Komplettkurs: ALLE Verfahren mit Formeln", font=F, font_size=30, color=AMBER)
        s.next_to(t,DOWN,buff=0.3)
        self.play(Write(t), run_time=1.1); self.play(FadeIn(s,shift=UP*0.3))
        self.play(VGroup(t,s).animate.shift(UP*1.4))
        cols=bullets([
            "Grundlagen · analytische Optima · Gradient · Newton",
            "Linear · Standardform · Simplex · Ganzzahlig",
            "Transport: Konstruktion + Stepping-Stone/MODI",
            "Nichtlinear: KKT · SQO · Konvexität",
            "Gradientenfrei: Nelder-Mead · DIRECT · SMBO",
            "Metaheuristiken: ES · EA · SA · PSO · ACO",
            "Mehrziel: Pareto · Crowding · Hypervolumen",
        ], size=23, buff=0.18, colors=[GREEN_A]*7).next_to(s,DOWN,buff=0.4)
        reveal(self, cols, lag=0.2, rt=2.6); self.wait(0.6)

# ---------- D02 Grundlagen ----------
class D02(Scene):
    def construct(self):
        h=title_bar("1   Grundlagen & Klassifikation"); self.play(FadeIn(h))
        form=T("min  f(x)      u.d.N.   g(x) ≤ 0 ,   h(x) = 0", 30, BLUE_A).next_to(h,DOWN,buff=0.5)
        self.play(Write(form))
        b=bullets([
            "Zielfunktion f, Variablen x, Nebenbedingungen g, h",
            "linear  vs.  nichtlinear  (Wurzel, x², sin …)",
            "Variablen reell (ℝⁿ)  oder  ganzzahlig (ℤⁿ)",
            "ein-  oder  mehrkriteriell",
            "unimodal = 1 Optimum   ·   multimodal = mehrere",
        ], size=26, colors=[TXT,AMBER,TXT,TXT,GREEN_A]).next_to(form,DOWN,buff=0.5)
        reveal(self,b,lag=0.4,rt=2.8); self.wait(0.6)

# ---------- D03 Analytisch 1D ----------
class D03(Scene):
    def construct(self):
        h=title_bar("2   Optima analytisch — 1 Variable"); self.play(FadeIn(h))
        ax=Axes(x_range=[-0.3,3.3,1],y_range=[0,7,2],x_length=6.2,y_length=4.2,axis_config={"color":MUTE}).shift(DOWN*0.5+LEFT*2.6)
        f=lambda x:2*x**3-9*x**2+12*x
        g=ax.plot(f,x_range=[-0.1,3.05],color=BLUE_A)
        self.play(Create(ax),Create(g),run_time=1.4)
        mx=Dot(ax.c2p(1,f(1)),color=RED_A); mn=Dot(ax.c2p(2,f(2)),color=GREEN_A)
        self.play(GrowFromCenter(mx),GrowFromCenter(mn))
        steps=bullets([
            "f(x)=2x³−9x²+12x",
            "f '(x)=6x²−18x+12=0",
            "⇒ x=1 (Max), x=2 (Min)",
            "f ''(x)=12x−18",
            "f ''(1)<0 Max · f ''(2)>0 Min",
        ],size=24,colors=[BLUE_A,TXT,AMBER,TXT,GREEN_A]).to_edge(RIGHT,buff=0.4)
        reveal(self,steps,lag=0.5,rt=2.8); self.wait(0.5)

# ---------- D04 Analytisch nD ----------
class D04(Scene):
    def construct(self):
        h=title_bar("2   Optima analytisch — mehrere Variablen"); self.play(FadeIn(h))
        b=bullets([
            "Gradient null setzen:  ∇f(x) = 0",
            "Hesse-Matrix H = Matrix der 2. Ableitungen",
            "Eigenwerte von H entscheiden:",
            "   alle > 0  →  Minimum",
            "   alle < 0  →  Maximum",
            "   gemischt  →  Sattelpunkt",
        ],size=27,colors=[TXT,TXT,AMBER,GREEN_A,GREEN_A,RED_A]).next_to(h,DOWN,buff=0.45).to_edge(LEFT,buff=0.7)
        reveal(self,b,lag=0.4,rt=2.8)
        ex=VGroup(
            T("Bsp: f = x₁³−3x₁+x₂²", 24, BLUE_A),
            T("∇f=0 ⇒ (1,0), (−1,0)", 24, TXT),
            T("H = [[6x₁,0],[0,2]]", 24, TXT),
            T("(1,0): Min · (−1,0): Sattel", 24, GREEN_A),
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_edge(RIGHT,buff=0.5).shift(DOWN*0.3)
        reveal(self,ex,lag=0.4,rt=2.0); self.wait(0.5)

# ---------- D05 Gradientenabstieg ----------
class D05(Scene):
    def construct(self):
        h=title_bar("3   Gradientenabstieg"); self.play(FadeIn(h))
        form=T("x_neu = x − λ · ∇f(x)", 34, AMBER).next_to(h,DOWN,buff=0.4)
        self.play(Write(form))
        ax=Axes(x_range=[-3,3,1],y_range=[-3,3,1],x_length=5.0,y_length=4.2,axis_config={"color":MUTE}).shift(DOWN*0.5+LEFT*3.0)
        cen=ax.c2p(0,0); self.play(Create(ax),*[Create(c) for c in contours(cen,[0.6,1.2,1.9,2.6])],run_time=1.2)
        pts=[(-2.4,2.2),(-1.4,1.2),(-0.7,0.6),(-0.2,0.2)]
        d=Dot(ax.c2p(*pts[0]),color=AMBER)
        path=VGroup(); self.play(FadeIn(d))
        for k in range(1,len(pts)):
            seg=Arrow(ax.c2p(*pts[k-1]),ax.c2p(*pts[k]),color=GREEN_A,buff=0,stroke_width=4)
            self.play(GrowArrow(seg),d.animate.move_to(ax.c2p(*pts[k])),run_time=0.6)
        info=bullets([
            "Gradient zeigt bergauf",
            "→ Minimierung: Gegenrichtung",
            "λ = Schrittweite",
        ],size=25,colors=[TXT,GREEN_A,TXT]).to_edge(RIGHT,buff=0.6)
        reveal(self,info,lag=0.4,rt=1.8); self.wait(0.4)

# ---------- D06 Newton ----------
class D06(Scene):
    def construct(self):
        h=title_bar("3   Newton-Verfahren"); self.play(FadeIn(h))
        form=T("x_{n+1} = x_n − f '(x_n) / f ''(x_n)", 32, AMBER).next_to(h,DOWN,buff=0.5)
        self.play(Write(form))
        b=bullets([
            "nutzt zusätzlich die Krümmung (2. Ableitung)",
            "konvergiert schneller als Gradientenabstieg",
            "Bsp: f=⅓x³−2x, x₀=2",
            "x₁ = 2 − (4−2)/4 = 1,5",
            "konvergiert gegen √2 ≈ 1,414",
        ],size=26,colors=[TXT,GREEN_A,BLUE_A,TXT,AMBER]).next_to(form,DOWN,buff=0.5)
        reveal(self,b,lag=0.45,rt=2.6); self.wait(0.5)

# ---------- D07 Linear & Simplex ----------
class D07(Scene):
    def construct(self):
        h=title_bar("4   Lineare Opt.: Standardform & Simplex"); self.play(FadeIn(h))
        ax=Axes(x_range=[0,8,2],y_range=[0,7,2],x_length=6.0,y_length=4.4,axis_config={"color":MUTE}).shift(DOWN*0.45+LEFT*2.7)
        self.play(Create(ax),run_time=0.6)
        verts=[ax.c2p(0,0),ax.c2p(4,0),ax.c2p(4,3),ax.c2p(2,5),ax.c2p(0,5)]
        reg=Polygon(*verts,color=GREEN_A,fill_color=GREEN_A,fill_opacity=0.16,stroke_width=2)
        self.play(FadeIn(reg))
        # simplex walk
        walk=[(0,0),(0,5),(2,5)]
        d=Dot(ax.c2p(*walk[0]),color=AMBER); self.play(FadeIn(d))
        for k in range(1,len(walk)):
            self.play(d.animate.move_to(ax.c2p(*walk[k])),run_time=0.7)
        self.play(Flash(d,color=GREEN_A))
        b=bullets([
            "Standardform: nur = und x ≥ 0",
            "Slack s: g≤b → g+s=b",
            "Simplex läuft Ecke zu Ecke",
            "Optimum in einer Ecke",
        ],size=24,colors=[TXT,AMBER,TXT,GREEN_A]).to_edge(RIGHT,buff=0.5)
        reveal(self,b,lag=0.4,rt=2.2); self.wait(0.4)

# ---------- D08 Ganzzahlig ----------
class D08(Scene):
    def construct(self):
        h=title_bar("4   Ganzzahlige Optimierung"); self.play(FadeIn(h))
        ax=Axes(x_range=[0,6,1],y_range=[0,6,1],x_length=5.2,y_length=4.4,axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*3.0)
        self.play(Create(ax),run_time=0.6)
        verts=[ax.c2p(0,0),ax.c2p(4,0),ax.c2p(2.5,2.25),ax.c2p(0,3.5)]
        reg=Polygon(*verts,color=GREEN_A,fill_color=GREEN_A,fill_opacity=0.14,stroke_width=2)
        self.play(FadeIn(reg))
        grid=VGroup(*[Dot(ax.c2p(x,y),color=MUTE,radius=0.05) for x in range(5) for y in range(5)
                      if 3*x+2*y<=12 and x+2*y<=7])
        self.play(FadeIn(grid))
        cont=Dot(ax.c2p(2.5,2.25),color=RED_A,radius=0.09)
        intp=Dot(ax.c2p(2,2),color=AMBER,radius=0.09)
        self.play(GrowFromCenter(cont)); self.play(GrowFromCenter(intp),Flash(intp,color=AMBER))
        b=bullets([
            "Variablen ∈ ℤ",
            "1) kontin. lösen (rot)",
            "2) Schnittebene/Branch",
            "→ ganzzahliges Opt. (gelb)",
            "f_ℤ ≤ f_kontinuierlich",
        ],size=23,colors=[TXT,RED_A,TXT,AMBER,GREEN_A]).to_edge(RIGHT,buff=0.5)
        reveal(self,b,lag=0.4,rt=2.4); self.wait(0.4)

# ---------- D09 Transport Konstruktion ----------
class D09(Scene):
    def construct(self):
        h=title_bar("5   Transport — Startlösung"); self.play(FadeIn(h))
        # 3x3 grid of costs
        costs=[[8,6,10],[9,12,13],[14,9,16]]
        cells=VGroup()
        for i in range(3):
            for j in range(3):
                sq=Square(side_length=0.95,color=MUTE,stroke_width=1.5)
                sq.move_to([(-1.0+j*1.0),(1.0-i*1.0),0])
                num=T(str(costs[i][j]),22,MUTE).move_to(sq.get_center())
                cells.add(VGroup(sq,num))
        grid=VGroup(*cells).shift(LEFT*2.6+DOWN*0.3)
        self.play(Create(grid),run_time=1.4)
        b=bullets([
            "Angebot = Nachfrage (klassisch)",
            "Ziel: Σ c·x  minimieren",
            "Nordwesteck — oben links",
            "Matrix-Minimum — günstigste Zelle",
            "Vogel — über Strafkosten (beste)",
        ],size=24,colors=[TXT,AMBER,TXT,TXT,GREEN_A]).to_edge(RIGHT,buff=0.4)
        reveal(self,b,lag=0.4,rt=2.6); self.wait(0.4)

# ---------- D10 Transport Optimierung ----------
class D10(Scene):
    def construct(self):
        h=title_bar("5   Transport — Optimierung (MODI)"); self.play(FadeIn(h))
        b=bullets([
            "Startlösung ist meist noch nicht optimal",
            "Stepping-Stone / MODI verbessern sie",
            "Potentiale:  u_i + v_j = c_ij  (Basiszellen)",
            "reduzierte Kosten:  c_ij − u_i − v_j",
            "negativ  →  über Zyklus Menge umverteilen",
            "alle ≥ 0  →  optimal",
        ],size=26,colors=[TXT,GREEN_A,AMBER,AMBER,TXT,GREEN_A]).next_to(h,DOWN,buff=0.5)
        reveal(self,b,lag=0.45,rt=3.0); self.wait(0.5)

# ---------- D11 KKT ----------
class D11(Scene):
    def construct(self):
        h=title_bar("6   Nichtlinear: KKT-Bedingungen"); self.play(FadeIn(h))
        ax=Axes(x_range=[-1,3,1],y_range=[-1,3,1],x_length=4.6,y_length=4.2,axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*3.3)
        cen=ax.c2p(2,2); self.play(Create(ax),*[Create(c) for c in contours(cen,[0.45,0.95,1.5])],run_time=1.0)
        circ=Circle(color=GREEN_A,stroke_width=4); circ.set_width(ax.c2p(1,0)[0]-ax.c2p(-1,0)[0]); circ.move_to(ax.c2p(0,0))
        self.play(Create(circ))
        d=Dot(ax.c2p(0,1),color=AMBER); self.play(FadeIn(d)); self.play(d.animate.move_to(ax.c2p(0.707,0.707))); self.play(Flash(d,color=AMBER))
        b=bullets([
            "L = f + a·h + b·g",
            "1) ∇L = 0  (Stationarität)",
            "2) h=0 , g ≤ 0  (zulässig)",
            "3) b·g = 0  (komplementär)",
            "4) b ≥ 0",
            "Trick: Fälle b=0 / g=0",
        ],size=23,colors=[AMBER,TXT,TXT,TXT,TXT,GREEN_A]).to_edge(RIGHT,buff=0.45)
        reveal(self,b,lag=0.4,rt=2.8); self.wait(0.5)

# ---------- D12 SQO & Konvex ----------
class D12(Scene):
    def construct(self):
        h=title_bar("6   SQO & Konvexität"); self.play(FadeIn(h))
        b=bullets([
            "SQO = Sequentielle Quadratische Optimierung",
            "approximiert f quadratisch, NB linear",
            "löst Folge einfacher Teilprobleme",
            "Konvex: f ''(x) ≥ 0  bzw.  Hesse pos. semidefinit",
            "konvex ⇒ lokales = globales Optimum",
        ],size=26,colors=[BLUE_A,TXT,TXT,AMBER,GREEN_A]).next_to(h,DOWN,buff=0.5)
        reveal(self,b,lag=0.45,rt=2.8)
        ax=Axes(x_range=[-2,2,1],y_range=[0,4,2],x_length=3.4,y_length=2.4,axis_config={"color":MUTE}).to_edge(DOWN,buff=0.35).shift(RIGHT*3.6)
        g=ax.plot(lambda x:x**2,x_range=[-2,2],color=GREEN_A)
        self.play(Create(ax),Create(g),run_time=1.0); self.wait(0.4)

# ---------- D13 Nelder-Mead ----------
class D13(Scene):
    def construct(self):
        h=title_bar("7   Gradientenfrei: Nelder-Mead"); self.play(FadeIn(h))
        ax=Axes(x_range=[-3,3,1],y_range=[-2,3,1],x_length=6.4,y_length=4.4,axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*1.6)
        cen=ax.c2p(0,0.5); self.play(Create(ax),*[Create(c) for c in contours(cen,[0.5,1.0,1.6,2.2])],run_time=1.0)
        A=ax.c2p(2,2.4);B=ax.c2p(2.3,0.2);C=ax.c2p(0.4,2.0)
        tri=Polygon(A,B,C,color=AMBER,fill_color=AMBER,fill_opacity=0.12,stroke_width=3)
        self.play(Create(tri))
        cenp=(np.array(B)+np.array(C))/2; refl=2*cenp-np.array(A)
        arr=Arrow(A,refl,color=GREEN_A,buff=0,stroke_width=4)
        self.play(GrowArrow(arr)); self.play(Transform(tri,Polygon(refl,B,C,color=GREEN_A,fill_color=GREEN_A,fill_opacity=0.12,stroke_width=3)))
        b=bullets([
            "Simplex = D+1 Punkte",
            "reflect (spiegeln)",
            "→ expand / contract / shrink",
            "lokal; DIRECT = global",
        ],size=23,colors=[TXT,GREEN_A,TXT,AMBER]).to_edge(RIGHT,buff=0.45)
        reveal(self,b,lag=0.4,rt=2.2); self.wait(0.4)

# ---------- D14 DIRECT & SMBO ----------
class D14(Scene):
    def construct(self):
        h=title_bar("7   DIRECT & SMBO"); self.play(FadeIn(h))
        ax=Axes(x_range=[0,7,1],y_range=[0,9,2],x_length=5.0,y_length=4.0,axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*3.0)
        xl=T("d (Größe)",18,MUTE).next_to(ax.x_axis,DOWN,buff=0.1); yl=T("f(c)",18,MUTE).next_to(ax.y_axis,UP,buff=0.05)
        self.play(Create(ax),FadeIn(xl),FadeIn(yl),run_time=0.7)
        P=[(1,5),(1,8),(2,4),(2,7),(4,3),(4,6),(6,5)]
        dots=VGroup(*[Dot(ax.c2p(*p),color=MUTE,radius=0.07) for p in P])
        self.play(FadeIn(dots))
        por=[(4,3),(6,5)]
        pd=VGroup(*[Dot(ax.c2p(*p),color=GREEN_A,radius=0.1) for p in por])
        hull=DashedLine(ax.c2p(4,3),ax.c2p(6,5),color=GREEN_A)
        self.play(*[GrowFromCenter(d) for d in pd],Create(hull))
        b=bullets([
            "DIRECT: Suchraum in Rechtecke",
            "potentiell optimal = große + niedrige f",
            "(untere-rechte Hülle)",
            "SMBO: Surrogatmodell, wertet dessen",
            "Minimum aus → Modell verbessern",
        ],size=22,colors=[TXT,GREEN_A,MUTE,BLUE_A,TXT]).to_edge(RIGHT,buff=0.4)
        reveal(self,b,lag=0.4,rt=2.6); self.wait(0.4)

# ---------- D15 ES & EA ----------
class D15(Scene):
    def construct(self):
        h=title_bar("8   Metaheuristiken: ES & EA"); self.play(FadeIn(h))
        b=bullets([
            "(1+1)-ES: 1 Lösung mutieren, behalten wenn besser",
            "1/5-Regel:  Erfolg > 1/5  →  σ = σ·a",
            "                    Erfolg < 1/5  →  σ = σ/a",
            "Evolutionärer Algorithmus = ganze Population:",
            "Mutation (Bitflip) · Crossover · Selektion",
        ],size=25,colors=[TXT,GREEN_A,GREEN_A,BLUE_A,AMBER]).next_to(h,DOWN,buff=0.5)
        reveal(self,b,lag=0.45,rt=2.8)
        x=T("x = (1,0,1,1,0)  →  Bitflip  →  (1,0,1,1,1)",22,MUTE).to_edge(DOWN,buff=0.4)
        self.play(FadeIn(x)); self.wait(0.4)

# ---------- D16 SA PSO ACO ----------
class D16(Scene):
    def construct(self):
        h=title_bar("8   Simulated Annealing · PSO · ACO"); self.play(FadeIn(h))
        b=bullets([
            "Simulated Annealing: akzeptiert Schlechteres",
            "    mit  p = e^(−Δf / T)  ·  T sinkt langsam",
            "PSO (Partikelschwarm): v = Trägheit",
            "    + kognitiv (eigenes Best) + sozial (Schwarm-Best)",
            "ACO (Ameisen): Pheromone + Verdunstung",
        ],size=25,colors=[GREEN_A,AMBER,BLUE_A,TXT,RED_A]).next_to(h,DOWN,buff=0.5)
        reveal(self,b,lag=0.45,rt=3.0); self.wait(0.5)

# ---------- D17 Mehrziel ----------
class D17(Scene):
    def construct(self):
        h=title_bar("9   Mehrziel: Pareto, Crowding, Hypervolumen"); self.play(FadeIn(h))
        ax=Axes(x_range=[0,8,2],y_range=[0,8,2],x_length=4.8,y_length=4.2,axis_config={"color":MUTE}).shift(DOWN*0.4+LEFT*3.2)
        x1=T("f₁",18,MUTE).next_to(ax.x_axis,RIGHT,buff=0.1);x2=T("f₂",18,MUTE).next_to(ax.y_axis,UP,buff=0.05)
        self.play(Create(ax),FadeIn(x1),FadeIn(x2),run_time=0.7)
        par=[(1,6),(2,4),(3,2.5),(5,1.5)]; dom=[(3,5),(4.5,4),(6,3)]
        pd=VGroup(*[Dot(ax.c2p(*p),color=GREEN_A,radius=0.08) for p in par])
        dd=VGroup(*[Dot(ax.c2p(*p),color=MUTE,radius=0.07) for p in dom])
        front=VMobject(color=GREEN_A,stroke_width=3); front.set_points_as_corners([ax.c2p(*p) for p in par])
        self.play(FadeIn(pd),FadeIn(dd)); self.play(Create(front))
        b=bullets([
            "dominiert: in allem ≤, irgendwo <",
            "Pareto = nicht dominiert",
            "NDS-Rang: Schichten abtragen",
            "Crowding: Σ Δfᵢ/Spanneᵢ (Rand=∞)",
            "Hypervolumen: Fläche zu Ref.-Punkt",
            "NSGA-II (CD) vs. SMS-EMOA (HV)",
        ],size=22,colors=[TXT,GREEN_A,TXT,AMBER,AMBER,BLUE_A]).to_edge(RIGHT,buff=0.4)
        reveal(self,b,lag=0.4,rt=2.8); self.wait(0.5)

# ---------- D18 Outro ----------
class D18(Scene):
    def construct(self):
        t=Text("Das sind alle Verfahren.", font=F, font_size=42, color=BLUE_A, weight=BOLD).to_edge(UP,buff=0.8)
        self.play(Write(t))
        b=bullets([
            "Jedes Verfahren = ein festes Rezept",
            "Übungen + 3 Probeklausuren aktiv rechnen",
            "Erst verdeckt lösen, dann Musterlösung",
            "Formeln auf dein Open-Book-Blatt",
        ],size=27,colors=[GREEN_A]*4).next_to(t,DOWN,buff=0.6)
        reveal(self,b,lag=0.4,rt=2.6)
        v=Text("Viel Erfolg!", font=F, font_size=40, color=AMBER, weight=BOLD).to_edge(DOWN,buff=0.8)
        self.play(FadeIn(v,scale=1.2)); self.wait(0.8)
