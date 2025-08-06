from manim import *
from manim import MovingCameraScene, Text, FadeIn, Write, smooth
from manim.utils.rate_functions import ease_out_cubic
import numpy as np
import random


class Scene1_WZwyklymSwiecie(Scene):
    def construct(self):
        self.camera.background_color = "#0B1B3F"  # granatowe tło

        # Grupa gwiazdek ✦ - rozmieszczonych po całym ekranie
        stars = VGroup()
        star_data = []  # dane o każdej gwiazdce

        # Siatka gwiazdek z losowym przesunięciem
        for grid_x in range(-7, 8, 1):  # co 1 jednostkę (gęsto)
            for grid_y in range(-6, 7, 1): # co 1 jednostkę (gęsto)
                x = grid_x + random.uniform(-0.8, 0.8)  # lekkie przesunięcie
                y = grid_y + random.uniform(-0.8, 0.8)
                star = Text(random.choice(["✦", "✧", "★", "✴", "✶"]), font_size=random.randint(5, 25),
                            color=random.choice([WHITE, GOLD, BLUE, "#FFDAB9", "#C0E0FF"]))
                base_opacity = random.uniform(0.3, 0.7)
                star.set_opacity(base_opacity)
                star.move_to([x, y, 0])
                stars.add(star)

                # Zapisujemy dane dla efektu migotania - TUTAJ w tej samej pętli!
                star_data.append({
                    'base_opacity': base_opacity,
                    'twinkle_speed': random.uniform(2, 10),
                    'twinkle_phase': random.uniform(0, 2 * np.pi),
                    'should_twinkle': random.random() < 0.6  # 60% gwiazdek migocze
                })

        self.add(stars)

        # Funkcja updater - ciągłe migotanie
        def update_stars(group, dt):
            current_time = self.renderer.time
            for i, star in enumerate(group):
                if i < len(star_data):  # dodatkowe zabezpieczenie
                    data = star_data[i]
                    if data['should_twinkle']:
                        # Efekt migotania z funkcji sinus
                        time_factor = current_time * data['twinkle_speed'] + data['twinkle_phase']
                        twinkle_multiplier = 0.3 + 0.7 * (0.5 + 0.5 * np.sin(time_factor))
                        new_opacity = data['base_opacity'] * twinkle_multiplier
                        star.set_opacity(max(0.1, new_opacity))

        # Dodajemy updater do grupy gwiazdek
        stars.add_updater(update_stars)

        # Tekst: W zwykłym świecie…
        tekst = Text("W zwykłym świecie…", font="Rounded Mplus 1c",weight=MEDIUM,  font_size=48)
        tekst.set_color("#F0E68C")

        # Animujemy tylko tekst (gwiazdki migoczą w tle)
        self.play(
            Write(tekst),
            run_time=3
        )

        # Czekamy żeby podziwiać migoczące gwiazdki
        self.wait(5)

        # Usuwamy updater na końcu
        stars.remove_updater(update_stars)
        self.wait(2)



class Scene2_ZblizenieMarzenia(MovingCameraScene):
    def construct(self):
        # === Tło startowe: noc ===
        gradient_rect = Rectangle(width=20, height=15)
        gradient_rect.set_fill(color="#0B1B3F", opacity=1)
        gradient_rect.set_stroke(width=0)
        self.add(gradient_rect)

        try:
            # Opcja 2: PNG (jeśli nie masz SVG)
            upper_character = ImageMobject("character_scene2.png")
        except:
            # Fallback: prosty tekst jako placeholder
            upper_character = Text("👧", font_size=100)

        upper_character.scale(2)  # dostosuj rozmiar
        upper_character.move_to(DOWN * 8)  # poza ekranem
        self.add(upper_character)

        # === ANIMACJA: tło zmienia się + postać wpływa ===
        self.play(
            # Tło zmienia się na świt
            gradient_rect.animate.set_fill(
                color=["#0B1B3F", "#FFC0CB", "#87CEEB"]
            ),

            # Postać wpływa z dołu i ZATRZYMUJE SIĘ NA DOLE EKRANU
            upper_character.animate.move_to(DOWN * 2.5),  # dół ekranu!

            run_time=3
        )

        self.wait(1)

        # === Tekst na środku ekranu ===
        tekst = Text("...była dziewczyna z wielkimi marzeniami...",
                     font="Rounded Mplus 1c",
                     weight=MEDIUM,
                     font_size=48)
        tekst.set_color_by_gradient("#9370DB", "#FF69B4" )
        tekst.move_to(ORIGIN)  # środek ekranu

        self.play(Write(tekst), run_time=2)
        self.wait(2)



class Scene3_PytaniaIChaos(MovingCameraScene):
    def construct(self):
        # === TŁO i POSTAĆ ===
        gradient_rect = Rectangle(width=20, height=15)
        gradient_rect.set_fill(color=["#191970", "#483D8B", "#2F4F4F"], opacity=1)
        gradient_rect.set_stroke(width=0)
        self.add(gradient_rect)

        character = ImageMobject("character_scene3.png")
        character.scale(2.5)
        character.move_to(DOWN * 2.5)
        self.add(character)

        # === IKONY ROZRZUCONE PO CAŁYM EKRANIE ===
        css_icon = ImageMobject("css.png").scale(0.25)
        css_icon.move_to(UP * 3 + LEFT * 2)

        pc_icon = ImageMobject("pc.png").scale(0.35)
        pc_icon.move_to(UP * 2.5 + RIGHT * 3)

        js_icon = ImageMobject("js.png").scale(0.45)
        js_icon.move_to(UP * 1 + RIGHT * 4)

        html_icon = ImageMobject("html.png").scale(0.35)
        html_icon.move_to(UP * 3.5 + LEFT * 0.5)

        python_icon = ImageMobject("python.png").scale(0.55)
        python_icon.move_to(UP * 2 + LEFT * 4)

        typescript_icon = ImageMobject("ts.png").scale(0.25)
        typescript_icon.move_to(UP * 0.5 + LEFT * 3)

        react_icon = ImageMobject("react.png").scale(0.45)
        react_icon.move_to(UP * 1.5 + LEFT * 1)

        vscode_icon = ImageMobject("vscode.png").scale(0.65)
        vscode_icon.move_to(UP * 0.8 + RIGHT * 2)

        pycharm_icon = ImageMobject("pycharm.png").scale(0.55)
        pycharm_icon.move_to(UP * 3.2 + RIGHT * 1.5)

        # === WIĘCEJ ZNAKÓW ZAPYTANIA ===
        q1 = Text("?", font_size=80, color="#9370DB")
        q1.move_to(UP * 2.8 + RIGHT * 4.5)

        q2 = Text("?", font_size=70, color="#FF1493")
        q2.move_to(UP * 1.2 + LEFT * 4.5)

        q3 = Text("?", font_size=60, color="#BA55D3")
        q3.move_to(UP * 3.8 + LEFT * 3)

        q4 = Text("?", font_size=75, color="#8A2BE2")
        q4.move_to(UP * 0.2 + RIGHT * 5)

        q5 = Text("?", font_size=65, color="#DA70D6")
        q5.move_to(UP * 1.8 + RIGHT * 0.5)

        q6 = Text("?", font_size=55, color="#FF69B4")
        q6.move_to(UP * 3.5 + RIGHT * 2.8)

        icons = [css_icon, pc_icon, js_icon, html_icon, python_icon,
                 typescript_icon, react_icon, vscode_icon, pycharm_icon,
                 q1, q2, q3, q4, q5, q6]

        # === ANIMACJA ===
        self.play(
            LaggedStart(
                *[GrowFromCenter(icon) for icon in icons],
                lag_ratio=0.15  # szybko jedna po drugiej
            ),
            run_time=4
        )

        self.wait(1)

        # === TEKST ===
        tekst = Text("...która nic nie wiedziała o kodzie.",
                     font="Rounded Mplus 1c",
                     weight=MEDIUM,
                     font_size=48)
        tekst.set_color_by_gradient("#8282e3", "#9d95d0", "#9fc6c6"  )
        tekst.move_to(DOWN * 0.5)  # między postacią a środkiem

        self.play(Write(tekst), run_time=2)
        self.wait(2)



class Scene3_5_DecyzjaONauce(MovingCameraScene):
    def construct(self):
        # === KONTYNUACJA z Sceny 3 ===
        gradient_rect = Rectangle(width=20, height=15)
        gradient_rect.set_fill(color=["#191970", "#483D8B", "#2F4F4F"], opacity=1)
        gradient_rect.set_stroke(width=0)
        self.add(gradient_rect)

        # === STARA POSTAĆ (z poprzedniej sceny) ===
        character = ImageMobject("character_scene3.png")
        character.scale(2.5)
        character.move_to(DOWN * 2.5)  # Środek (bez przesunięcia na początku)
        self.add(character)

        # === ODTWARZAMY WSZYSTKIE IKONY z poprzedniej sceny ===
        css_icon = ImageMobject("css.png").scale(0.25)
        css_icon.move_to(UP * 3 + LEFT * 2)

        pc_icon = ImageMobject("pc.png").scale(0.35)
        pc_icon.move_to(UP * 2.5 + RIGHT * 3)

        js_icon = ImageMobject("js.png").scale(0.45)
        js_icon.move_to(UP * 1 + RIGHT * 4)

        html_icon = ImageMobject("html.png").scale(0.35)
        html_icon.move_to(UP * 3.5 + LEFT * 0.5)

        python_icon = ImageMobject("python.png").scale(0.55)
        python_icon.move_to(UP * 2 + LEFT * 4)

        typescript_icon = ImageMobject("ts.png").scale(0.25)
        typescript_icon.move_to(UP * 0.5 + LEFT * 3)

        react_icon = ImageMobject("react.png").scale(0.45)
        react_icon.move_to(UP * 1.5 + LEFT * 1)

        vscode_icon = ImageMobject("vscode.png").scale(0.65)
        vscode_icon.move_to(UP * 0.8 + RIGHT * 2)

        pycharm_icon = ImageMobject("pycharm.png").scale(0.55)
        pycharm_icon.move_to(UP * 3.2 + RIGHT * 1.5)

        q1 = Text("?", font_size=80, color="#9370DB")
        q1.move_to(UP * 2.8 + RIGHT * 4.5)

        q2 = Text("?", font_size=70, color="#FF1493")
        q2.move_to(UP * 1.2 + LEFT * 4.5)

        q3 = Text("?", font_size=60, color="#BA55D3")
        q3.move_to(UP * 3.8 + LEFT * 3)

        q4 = Text("?", font_size=75, color="#8A2BE2")
        q4.move_to(UP * 0.2 + RIGHT * 5)

        q5 = Text("?", font_size=65, color="#DA70D6")
        q5.move_to(UP * 1.8 + RIGHT * 0.5)

        q6 = Text("?", font_size=55, color="#FF69B4")
        q6.move_to(UP * 3.5 + RIGHT * 2.8)

        all_chaos_icons = [css_icon, pc_icon, js_icon, html_icon, python_icon,
                           typescript_icon, react_icon, vscode_icon, pycharm_icon,
                           q1, q2, q3, q4, q5, q6]

        # Dodajemy wszystkie ikony (jakby były już na ekranie)
        for icon in all_chaos_icons:
            self.add(icon)

        self.wait(1)

        # === IKONY ZNIKAJĄ ===
        icons_fadeout = LaggedStart(
            *[FadeOut(icon) for icon in all_chaos_icons],
            lag_ratio=0.1
        )

        self.play(icons_fadeout, run_time=2)

        # === ZMIANA POSTACI pod koniec znikania ikon ===
        new_character = ImageMobject("character_scene3_5.png")  # Obrazek 1
        new_character.scale(1)
        new_character.move_to(DOWN * 2.5 + RIGHT * 4.5)  # Po prawej stronie

        self.play(
            FadeOut(character),
            FadeIn(new_character),
            run_time=0.8
        )

        # Zastępujemy referencję do postaci
        character = new_character

        self.wait(0.5)

        # === TEKST – pionowe litery w kolumnach, od lewej do prawej ===
        lines = [
            "ale", "postanowiła",
            "coś", "zmienić",
            ["." , "." , "."]
        ]

        columns = VGroup()

        for line in lines:
            if isinstance(line, list):
                letters = VGroup(*[
                    Text(char, font="Rounded Mplus 1c", font_size=25)
                    for char in line
                ])
            else:
                letters = VGroup(*[
                    Text(char, font="Rounded Mplus 1c", font_size=25)
                    for char in line
                ])
            letters.arrange(DOWN, buff=0.15)
            columns.add(letters)

        columns.arrange(RIGHT, buff=0.8)  # Odstęp między kolumnami
        columns.to_edge(UL).shift(DOWN * 0.5 + RIGHT * 0.2)  # Pozycjonowanie

        # === POJAWIA SIĘ LAMPKA W TRAKCIE ANIMACJI LITER ===
        bulb_icon = ImageMobject("spare_bulb.png")
        bulb_icon.scale(0.3)
        bulb_icon.move_to(new_character.get_center() + UP * 2.5)

        # Jednoczesne pojawienie liter + lampki
        self.play(
            LaggedStart(*[
                FadeIn(letter, shift=UP, lag_ratio=0.05)
                for col in columns for letter in col
            ], lag_ratio=0.1),
            FadeIn(bulb_icon, scale=1.3),
            run_time=2.5
        )

        self.wait(0.5)  # Chwila z lampką

        # === LAMPKA ZNIKA zanim pojawi się HTML ===
        self.play(FadeOut(bulb_icon), run_time=0.8)

        # === POJAWIA SIĘ IKONA HTML5 ===
        html_book = ImageMobject("html_scene3_5.png")  # Obrazek 2
        html_book.scale(0.08)  # Dla dużego obrazka 7110x7110
        html_book.move_to(ORIGIN)  # Środek ekranu

        # HTML pojawia się w środku wraz z znikaniem lampki
        self.play(
            FadeIn(html_book, scale=1.3),  # ikona "wyrasta" w środku
            run_time=1.2
        )

        self.wait(0.8)

        # HTML rozpływa się na cały ekran
        self.play(
            html_book.animate.scale(15).set_opacity(0.3),  # Ogromne powiększenie i przezroczystość
            run_time=2.5
        )

        self.wait(2)
        new_background = Rectangle(width=20, height=15)
        new_background.set_fill(color=["#f8f9fa", "#e9ecef", "#dee2e6"], opacity=0)  # jasne tło z Scene3.75
        new_background.set_stroke(width=0)

        self.play(new_background.animate.set_fill(opacity=1), run_time=2)



class Scene3_75_PierwszeKrokiTrudnosci(MovingCameraScene):
    def construct(self):
        new_background = Rectangle(width=20, height=15)
        new_background.set_fill(color=["#f8f9fa", "#e9ecef", "#dee2e6"], opacity=0)
        new_background.set_stroke(width=0)

        self.play(new_background.animate.set_fill(opacity=1), run_time=2)


        # Płynne przejście tła + usunięcie poprzednich elementów
        self.play(
            new_background.animate.set_fill(opacity=1),
            run_time=2
        )

        words = "Zaczęła od podstaw...".split(" ")
        columns = VGroup()
        for word in words:
            letters = VGroup(*[Text(c, font="Rounded Mplus 1c", font_size=30, color="#49564f") for c in word])
            letters.arrange(DOWN, buff=0.08)
            columns.add(letters)
        columns.arrange(RIGHT, buff=0.3)

        columns.move_to(UP * 1.5 + LEFT * 5.5)
        self.add(columns)

        character = ImageMobject("character_learning.png").scale_to_fit_width(2)
        character.scale(2)
        character.move_to(DOWN * 2.3 + LEFT * 4.5)

        self.play(
            FadeIn(columns, run_time=2),
            FadeIn(character, shift=UP * 0.5),
            run_time=2
        )
        self.wait(1.2)


        # Okno edytora
        editor_window = Rectangle(width=7.5, height=5, color="#343a40", stroke_width=2)
        editor_window.set_fill(color="#ffffff", opacity=0.95)
        editor_window.move_to(RIGHT * 1.2 + DOWN * 0.1)

        title_bar = Rectangle(width=7.5, height=0.45, color="#e9ecef")
        title_bar.set_fill(color="#f8f9fa", opacity=1)
        title_bar.move_to(editor_window.get_top() - DOWN * 0.225)

        filename = Text("index.html", font_size=15, color="#495057", font="Consolas")
        filename.move_to(title_bar.get_center())

        close_btn = Circle(radius=0.06, color="#dc3545", fill_opacity=1)
        close_btn.move_to(title_bar.get_right() + LEFT * 0.3)

        min_btn = Circle(radius=0.06, color="#ffc107", fill_opacity=1)
        min_btn.move_to(close_btn.get_center() + LEFT * 0.25)

        max_btn = Circle(radius=0.06, color="#28a745", fill_opacity=1)
        max_btn.move_to(min_btn.get_center() + LEFT * 0.25)


        self.play(
            Create(editor_window),
            Create(title_bar),
            Write(filename),
            FadeIn(VGroup(close_btn, min_btn, max_btn)),
            run_time=1.8
        )

        # Kod pojawia się linia po linii
        code_lines = [
            "<!DOCTYPE html>",
            "<html>",
            "  <head>",
            "    <title>Moja pierwsza strona</title>",
            "  </head>",
            "  <body>",
            "    <h1>Witaj świecie!",  # BŁĄD - brak zamknięcia
            "    <p>To jest mój pierwszy kod.</p>",
            "  </body>",
            "</html>"
        ]

        code_text = VGroup()
        for i, line in enumerate(code_lines):
            color = "#e74c3c" if i == 6 else "#2c3e50"
            text_line = Text(line, font="Consolas", font_size=13, color=color)
            code_text.add(text_line)

        self.play(FadeOut(columns), run_time=1)

        code_text.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        code_text.move_to(editor_window.get_center() - UP * 0.1)

        self.play(
            LaggedStart(*[Write(line) for line in code_text], lag_ratio=0.35),
            run_time=4.5
        )
        self.wait(1.2)

        # Shake + zmiana postaci na zestresowaną
        shake_group = VGroup(editor_window, title_bar, filename, code_text, close_btn, min_btn, max_btn)

        character_stressed = ImageMobject("character_stressed.png").scale_to_fit_width(2)
        character_stressed.scale(2)
        character_stressed.move_to(DOWN * 2.3 + LEFT * 4.5)

        shake_animations = []
        for _ in range(10):
            shake_animations.extend([
                shake_group.animate.shift(RIGHT * 0.08),
                shake_group.animate.shift(LEFT * 0.16),
                shake_group.animate.shift(RIGHT * 0.08)
            ])

        self.play(
            AnimationGroup(*shake_animations, lag_ratio=0.015),
            FadeOut(character),
            run_time=1
        )
        self.play(
            FadeIn(character_stressed),
            run_time=1
        )
        character = character_stressed  # aktualizacja

        # Czerwony X i ramka błędu
        error_x = Text("✗", font_size=85, color="#e74c3c")
        error_x.move_to(editor_window.get_right() + RIGHT * 1)

        error_frame = Rectangle(width=7.8, height=5.3, color="#e74c3c", stroke_width=4)
        error_frame.move_to(editor_window.get_center())

        self.play(
            DrawBorderThenFill(error_x),
            Create(error_frame),
            Flash(error_x, color="#e74c3c", flash_radius=1.5),
            run_time=1.2
        )

        # Tekst motywacyjny 1
        text1 = Text("To nie było łatwe…",
                     font="Rounded Mplus 1c", font_size=28, color="#e74c3c")
        text1.move_to(DOWN * 3.5 + LEFT * 0.5)
        self.play(Write(text1), run_time=1.8)
        self.wait(2.2)

        # Postać myśląca
        character_thinking = ImageMobject("character_thinking.png")
        character_thinking.scale(0.7)
        character_thinking.move_to(DOWN * 2.3 + LEFT * 4.5)

        self.play(
            FadeOut(character),
            FadeIn(character_thinking),
            run_time=1
        )
        character = character_thinking

        self.play(FadeOut(text1), run_time=1)

        # Poprawa kodu
        fixed_line = Text("    <h1>Witaj świecie!</h1>",
                          font="Consolas", font_size=13, color="#27ae60")
        fixed_line.move_to(code_text[6].get_center())

        self.play(
            Transform(code_text[6], fixed_line),
            FadeOut(error_x),
            FadeOut(error_frame),
            run_time=1.8
        )


        # Szczęśliwa postać + sukces
        character_happy = ImageMobject("character_happy.png")
        character_happy.scale(0.7)
        character_happy.move_to(DOWN * 2.3 + LEFT * 4.5)

        success_check = Text("✓", font_size=85, color="#27ae60")
        success_check.move_to(editor_window.get_right() + RIGHT * 1.3)

        glow_frame = Rectangle(width=7.8, height=5.3, color="#27ae60", stroke_width=3)
        glow_frame.move_to(editor_window.get_center())
        glow_frame.set_stroke(opacity=0.8)

        glow_bg = Rectangle(width=8.2, height=5.7, color="#27ae60", stroke_width=0)
        glow_bg.set_fill(opacity=0.12)
        glow_bg.move_to(editor_window.get_center())

        self.play(
            FadeOut(character),
            FadeIn(character_happy),
            DrawBorderThenFill(success_check),
            Create(glow_frame),
            FadeIn(glow_bg),
            Flash(success_check, color="#27ae60", flash_radius=1.5),
            run_time=1.5
        )
        character = character_happy

        # Tekst motywacyjny 2
        text2 = Text("...ale nie poddała się.",
                     font="Rounded Mplus 1c", font_size=28, color="#27ae60")
        text2.move_to(DOWN * 3.5 + LEFT * 0.5)

        self.play(Write(text2), run_time=1.8)

        success_elements = VGroup(
            editor_window, code_text, success_check, glow_frame
        )

        self.wait(2.5)

        # Znikają wszystkie elementy poza jasnym tłem
        fade_elements = Group(
             editor_window, title_bar, filename, code_text,
            success_check, glow_frame, glow_bg, text2,
             character_happy,
            close_btn, min_btn, max_btn
        )

        self.play(
            FadeOut(fade_elements),
            run_time=2.2
        )



class Scene4_LevelUpHTML(Scene):
    def construct(self):
        # Previous scene background (Scene 3)
        prev_background = Rectangle(width=20, height=15)
        prev_background.set_fill(color=["#f8f9fa", "#e9ecef", "#dee2e6"], opacity=1)
        prev_background.set_stroke(width=0)

        # New scene background (darker, RPG-style)
        new_background = Rectangle(width=20, height=15)
        new_background.set_fill(color=["#1a1a2e", "#16213e", "#0f3460"], opacity=0)
        new_background.set_stroke(width=0)

        # Dodaj oba tła na scenę przed animacją przejścia
        self.add(prev_background, new_background)

        # Background transition
        self.play(
            prev_background.animate.set_fill(opacity=0),
            new_background.animate.set_fill(opacity=1),
            run_time=2
        )

        # Character image in bottom left
        character = ImageMobject("character_scene4.png").scale(0.4)
        character.move_to(LEFT * 5 + DOWN * 2.5)
        self.play(FadeIn(character), run_time=0.8)

        # Rozbudowany kod HTML - bardziej skomplikowany
        html_lines = [
            "<!DOCTYPE html>",
            "<html lang='pl'>",
            "<head>",
            "  <meta charset='UTF-8'>",
            "  <meta name='viewport' content='width=device-width'>",
            "  <title>Moja Pierwsza Strona Web</title>",
            "  <style>",
            "    body { font-family: Arial, sans-serif; }",
            "    .container { max-width: 800px; margin: 0 auto; }",
            "    .header { background: #333; color: white; }",
            "  </style>",
            "</head>",
            "<body>",
            "  <div class='container'>",
            "    <header class='header'>",
            "      <h1>Witaj w moim świecie kodu!</h1>",
            "      <nav>",
            "        <ul>",
            "          <li><a href='#home'>Strona główna</a></li>",
            "          <li><a href='#about'>O mnie</a></li>",
            "          <li><a href='#contact'>Kontakt</a></li>",
            "        </ul>",
            "      </nav>",
            "    </header>",
            "    <main>",
            "      <section id='home'>",
            "        <h2>Moja podróż z programowaniem</h2>",
            "        <p>Każda linia kodu to nowy krok naprzód!</p>",
            "        <img src='coding.jpg' alt='Programowanie'>",
            "      </section>",
            "      <section id='skills'>",
            "        <h3>Moje umiejętności:</h3>",
            "        <ul>",
            "          <li><strong>HTML</strong> - struktura stron</li>",
            "          <li><strong>CSS</strong> - stylowanie</li>",
            "          <li><strong>JavaScript</strong> - interaktywność</li>",
            "        </ul>",
            "      </section>",
            "    </main>",
            "    <footer>",
            "      <p>&copy; 2024 Moja Pierwsza Strona</p>",
            "    </footer>",
            "  </div>",
            "</body>",
            "</html>"
        ]

        # Okno edytora w stylu Scene 3.75 - przesunięte w prawo
        editor_window = Rectangle(width=8, height=6, color="#343a40", stroke_width=2)
        editor_window.set_fill(color="#1e1e1e", opacity=0.95)
        editor_window.move_to(RIGHT * 2 + UP * 0.2)  # Przesunięte w prawo

        title_bar = Rectangle(width=8, height=0.5, color="#2d2d30")
        title_bar.set_fill(color="#3c3c3c", opacity=1)
        title_bar.move_to(editor_window.get_top() - DOWN * 0.25)

        filename = Text("portfolio.html", font_size=16, color="#ffffff", font="Consolas")
        filename.move_to(title_bar.get_center())

        # Przyciski okna w ciemnym motywie
        close_btn = Circle(radius=0.07, color="#ff5f57", fill_opacity=1)
        close_btn.move_to(title_bar.get_right() + LEFT * 0.35)

        min_btn = Circle(radius=0.07, color="#ffbd2e", fill_opacity=1)
        min_btn.move_to(close_btn.get_center() + LEFT * 0.3)

        max_btn = Circle(radius=0.07, color="#28ca42", fill_opacity=1)
        max_btn.move_to(min_btn.get_center() + LEFT * 0.3)

        # Animacja tworzenia okna edytora
        self.play(
            Create(editor_window),
            Create(title_bar),
            Write(filename),
            FadeIn(VGroup(close_btn, min_btn, max_btn)),
            run_time=1
        )

        # Przygotowanie tekstu kodu
        code_text = VGroup()

        # Kolory syntaxu dla różnych elementów
        def get_line_color(line):
            line = line.strip()
            if line.startswith("<!DOCTYPE") or line.startswith("<html") or line.startswith("</html>"):
                return "#ff79c6"  # Magenta dla deklaracji
            elif line.startswith("<head") or line.startswith("</head>") or line.startswith("<body") or line.startswith(
                    "</body>"):
                return "#8be9fd"  # Cyan dla głównych sekcji
            elif line.startswith("<meta") or line.startswith("<title") or line.startswith("</title>"):
                return "#50fa7b"  # Zielony dla meta i title
            elif line.startswith("<style") or line.startswith("</style>") or "{" in line or "}" in line:
                return "#f1fa8c"  # Żółty dla CSS
            elif line.startswith("<h") or line.startswith("</h"):
                return "#ff5555"  # Czerwony dla nagłówków
            elif line.startswith("<p") or line.startswith("</p>") or line.startswith("<li") or line.startswith("</li>"):
                return "#bd93f9"  # Fioletowy dla paragrafów i list
            else:
                return "#f8f8f2"  # Biały dla reszty

        # Wyświetlanie kodu linia po linii (jak w Scene 3.75)
        visible_lines = []
        max_visible_lines = 15  # Maksymalna liczba widocznych linii

        for line_index, line in enumerate(html_lines):
            color = get_line_color(line)
            text_line = Text(line, font="Consolas", font_size=11, color=color)

            # Dodaj nową linię do listy widocznych
            visible_lines.append(text_line)

            # Jeśli mamy więcej linii niż maksimum, usuń najstarszą
            if len(visible_lines) > max_visible_lines:
                old_line = visible_lines.pop(0)
                self.remove(old_line)

            # Ułóż widoczne linie
            current_code = VGroup(*visible_lines)
            current_code.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            current_code.move_to(editor_window.get_center() - UP * 0.1)

            # Animacja pisania nowej linii
            self.play(Write(text_line), run_time=0.25)

            # Co kilka linii - animacja "LEVEL UP!"
            if (line_index + 1) % 4 == 0 and line_index < len(html_lines) - 5:
                level_text = Text("LEVEL UP!", font_size=28, color=GOLD, weight=BOLD)
                level_text.next_to(character, UP, buff=0.3)

                # Efekt błysku i powiększenia
                self.play(
                    DrawBorderThenFill(level_text),
                    Flash(level_text, color=GOLD, flash_radius=1.2),
                    run_time=0.4
                )
                self.play(
                    level_text.animate.scale(1.3).set_opacity(0.8),
                    run_time=0.3
                )
                self.play(
                    FadeOut(level_text),
                    run_time=0.4
                )

            self.wait(0.05)

        # Efekt końcowy - kod staje się półprzezroczysty
        final_code = VGroup(*visible_lines)
        self.play(
            final_code.animate.set_opacity(0.4),
            run_time=0.8
        )

        # Grupa elementów okna kodu
        code_elements = Group(editor_window, title_bar, filename, final_code, close_btn, min_btn, max_btn)

        # 1. Najpierw schowaj postać (jeśli chcesz, żeby najpierw zniknęła)
        self.play(FadeOut(character), run_time=0.5)
        self.remove(character)

        # 2. Schowaj okno kodu i elementy
        self.play(FadeOut(code_elements), run_time=0.8)
        self.remove(code_elements)

        # 3. Pokaż nową postać
        character_happy = ImageMobject("character_happy_scene4.png").scale(2.5)
        character_happy.move_to(DOWN * 2.8)
        self.play(FadeIn(character_happy), run_time=0.8)
        character = character_happy

        # Okno osiągnięcia w stylu gry RPG - przesunięte do góry
        achievement_bg = RoundedRectangle(
            width=7, height=4,
            corner_radius=0.3,
            fill_color="#1a1a1a",
            fill_opacity=0.95,
            stroke_color=GOLD,
            stroke_width=4
        )

        # Dodanie blasku wokół okna osiągnięć
        glow_bg = RoundedRectangle(
            width=7.4, height=4.4,
            corner_radius=0.4,
            fill_color=GOLD,
            fill_opacity=0.15,
            stroke_width=0
        )

        congrats_text = Text("🎉 GRATULACJE! 🎉", font_size=32, color=GOLD, weight=BOLD)
        skill_text = Text("Nowa umiejętność została opanowana!", font_size=18, color=WHITE)

        # HTML ikonka w oknie osiągnięć - z pliku
        html_achievement_icon = ImageMobject("html5_icon.png")
        html_achievement_icon.scale_to_fit_width(1.2)

        html_skill = Text("HTML DEVELOPER", font_size=28, color=GREEN, weight=BOLD)

        # Dodatkowy tekst opisowy
        desc_text = Text("Potrafisz już tworzyć strukturę stron internetowych!",
                         font_size=16, color="#cccccc")

        achievement_content = Group(
            congrats_text,
            skill_text,
            html_achievement_icon,
            html_skill,
            desc_text
        ).arrange(DOWN, buff=0.3)

        achievement_window = Group(glow_bg, achievement_bg, achievement_content)
        achievement_window.move_to(UP * 1.5)  # Przesunięte do góry


        # Ukrycie okna kodu i pojawienie się okna osiągnięć z przesunięciem postaci
        code_elements = Group(editor_window, title_bar, filename, final_code, close_btn, min_btn, max_btn)


        # Animacja pojawienia się okna osiągnięć
        self.play(
            FadeIn(achievement_window, scale=0.3),
            Flash(achievement_window, color=GOLD, flash_radius=2),
            run_time=1.8
        )

        self.wait(2.5)

        # Końcowe wygaszenie sceny
        fade_elements = Group(
            new_background, character_happy, achievement_window
        )

        self.play(
            FadeOut(fade_elements),
            run_time=2
        )



class Scene5_LevelUpCSS(Scene):
    def construct(self):
        # Background transition from Scene 4
        prev_background = Rectangle(width=20, height=15)
        prev_background.set_fill(color=["#1a1a2e", "#16213e", "#0f3460"], opacity=1)
        prev_background.set_stroke(width=0)

        # New CSS scene background
        new_background = Rectangle(width=20, height=15)
        new_background.set_fill(color=["#0d1421", "#1a2332", "#2a3441"], opacity=0)
        new_background.set_stroke(width=0)

        self.add(prev_background, new_background)

        # Background transition
        self.play(
            prev_background.animate.set_fill(opacity=0),
            new_background.animate.set_fill(opacity=1),
            run_time=2
        )

        # Character (podstawowa postać) - daleko w lewo
        character = ImageMobject("character_scene4.png").scale(0.5)
        character.move_to(LEFT * 4.5 + DOWN * 2.8)
        self.play(FadeIn(character), run_time=0.8)

        # === TWOJE PRAWDZIWE STRONY JAKO OBRAZKI ===
        # Lista nazw plików twoich stron (od prostej do mistrzowskiej)
        website_images = [
            "website_basic.png",  # Obrazek 8 - Nora Vale (najprostsze)
            "website_styled.png",  # Obrazek 4 - CV Bozheslavy (więcej stylowania)
            "website_intermediate.png",  # Obrazek 6 - Pizzeria (średniozaawansowana)
            "website_advanced.png",  # Obrazek 3 - Cukiernia z formularzem i galerią
            "website_master.png",  # Obrazek 1 - Portfolio z tortami (najzaawansowansza)
            "website_master_extended.png"  # Obrazek 2 - rozszerzone portfolio (ultimate)
        ]

        # Funkcja pokazywania "LEVEL UP!"
        def show_level_up():
            level_text = Text("LEVEL UP!", font_size=28, color=GOLD, weight=BOLD)
            level_text.next_to(character, UP, buff=0.3)

            self.play(
                DrawBorderThenFill(level_text),
                Flash(level_text, color=GOLD, flash_radius=1.2),
                run_time=0.6
            )
            self.play(
                level_text.animate.scale(1.3).set_opacity(0.8),
                run_time=0.4
            )
            self.play(FadeOut(level_text), run_time=0.5)

        # Pokaż kolejne strony
        current_website = None

        for i, image_file in enumerate(website_images):
            # Załaduj obraz strony
            website_image = ImageMobject(image_file)

            # Skaluj obrazek do rozsądnego rozmiaru (większy niż w oknie przeglądarki)
            website_image.scale_to_fit_width(9)
            website_image.scale_to_fit_height(6)

            # Umieść na środku sceny (trochę w prawo od postaci)
            website_image.move_to(RIGHT * 1 + UP * 0.2)

            if current_website is None:
                # Pierwsza strona - po prostu pokaż
                self.play(FadeIn(website_image), run_time=1)
                self.wait(2.5)  # Dłużej na pierwszą stronę
            else:
                # Zmiana na kolejną stronę
                self.play(
                    FadeOut(current_website),
                    FadeIn(website_image),
                    run_time=1.2
                )
                self.wait(2)  # Czas na obejrzenie strony

            current_website = website_image

            # Po każdej stronie - LEVEL UP! (ale różne intensywności)
            if i == len(website_images) - 1:  # Ostatnia strona - większy efekt
                level_text = Text("MASTER LEVEL!", font_size=32, color=GOLD, weight=BOLD)
                level_text.next_to(character, UP, buff=0.3)

                self.play(
                    DrawBorderThenFill(level_text),
                    Flash(level_text, color=GOLD, flash_radius=1.5),
                    run_time=0.8
                )
                self.play(
                    level_text.animate.scale(1.5).set_opacity(0.9),
                    run_time=0.5
                )
                self.play(FadeOut(level_text), run_time=0.6)
            else:
                # Zwykły level up
                show_level_up()

            self.wait(1)

        # === UKRYCIE WSZYSTKICH ELEMENTÓW PRZED EWOLUCJĄ ===
        elements_to_hide = Group(current_website, character)

        self.play(FadeOut(elements_to_hide), run_time=1)

        # === WIELKA TRANSFORMACJA POSTACI ===

        # Efekt ewolucji - białe światło
        evolution_light = Circle(radius=0.1, color=WHITE, fill_opacity=1)
        evolution_light.move_to(LEFT * 6 + DOWN * 2.8)

        self.play(
            evolution_light.animate.scale(50).set_opacity(0.9),
            run_time=1.8
        )

        # Tekst "EWOLUCJONOWAŁAŚ!"
        evolution_text = Text("EWOLUCJONOWAŁAŚ!", font_size=48, color=GOLD, weight=BOLD)
        evolution_text.move_to(ORIGIN)

        self.play(
            DrawBorderThenFill(evolution_text),
            Flash(evolution_text, color=GOLD, flash_radius=2.5),
            run_time=2
        )

        self.play(FadeOut(evolution_text), run_time=1)

        # Nowa ewoluowana postać - CSS Master
        character_evolved = ImageMobject("character_css_master.png").scale(1.2)
        character_evolved.move_to(DOWN * 2.5)

        self.play(
            evolution_light.animate.scale(0.02).set_opacity(0),
            FadeIn(character_evolved, scale=0.5),
            run_time=2.5
        )

        # Okno osiągnięcia CSS
        achievement_bg = RoundedRectangle(
            width=8, height=4.5,
            corner_radius=0.4,
            fill_color="#1a1a1a",
            fill_opacity=0.95,
            stroke_color="#1572b6",  # CSS blue
            stroke_width=4
        )

        glow_bg = RoundedRectangle(
            width=8.4, height=4.9,
            corner_radius=0.5,
            fill_color="#1572b6",
            fill_opacity=0.2,
            stroke_width=0
        )

        congrats_final = Text("🎨 GRATULACJE! 🎨", font_size=32, color="#1572b6", weight=BOLD)

        # Podziel tekst tam gdzie chcesz:
        skill_line_1 = Text("Nowa umiejętność", font_size=18, color=WHITE, weight=BOLD)
        skill_line_2 = Text("została opanowana!", font_size=18, color=WHITE, weight=BOLD)
        skill_final = Group(skill_line_1, skill_line_2).arrange(DOWN, buff=0.05)

        # CSS3 icon for achievement
        css_achievement_icon = ImageMobject("css3_icon.png")
        css_achievement_icon.scale_to_fit_width(1.2)

        css_final = Text("CSS MASTER", font_size=28, color="#1572b6", weight=BOLD)

        desc_line_1 = Text("Potrafisz już stylować strony", font_size=16, color="#cccccc", weight=BOLD)
        desc_line_2 = Text("i tworzyć piękne layouty!", font_size=16, color="#cccccc", weight=BOLD)
        desc_final = Group(desc_line_1, desc_line_2).arrange(DOWN, buff=0.05)

        # Finalna grupa z poprawnie podzielonymi tekstami
        achievement_content_final = Group(
            congrats_final,
            skill_final,
            css_achievement_icon,
            css_final,
            desc_final
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        achievement_window_final = Group(glow_bg, achievement_bg, achievement_content_final)
        achievement_window_final.move_to(UP * 1.5)

        # Achievement window appearance
        self.play(
            FadeIn(achievement_window_final, scale=0.3),
            Flash(achievement_window_final, color="#1572b6", flash_radius=2),
            run_time=2
        )

        self.wait(3)

        # Final scene fadeout
        fade_elements = Group(new_background, character_evolved, achievement_window_final)
        self.play(FadeOut(fade_elements), run_time=2)




class Scene5_5_Skills(Scene):
    def construct(self):
        # Tło
        self.camera.background_color = "#1a1a2e"
        # Grupa gwiazdek ✦ - rozmieszczonych po całym ekranie
        stars = VGroup()
        star_data = []  # dane o każdej gwiazdce
        # Siatka gwiazdek z losowym przesunięciem
        for grid_x in range(-7, 8, 1):  # co 1 jednostkę (gęsto)
            for grid_y in range(-6, 7, 1):  # co 1 jednostkę (gęsto)
                x = grid_x + random.uniform(-0.8, 0.8)  # lekkie przesunięcie
                y = grid_y + random.uniform(-0.8, 0.8)
                star = Text(random.choice(["✦", "✧", "★", "✴", "✶"]), font_size=random.randint(5, 25),
                            color=random.choice([WHITE, GOLD, BLUE, "#FFDAB9", "#C0E0FF"]))
                base_opacity = random.uniform(0.3, 0.7)
                star.set_opacity(base_opacity)
                star.move_to([x, y, 0])
                stars.add(star)

                # Zapisujemy dane dla efektu migotania - TUTAJ w tej samej pętli!
                star_data.append({
                    'base_opacity': base_opacity,
                    'twinkle_speed': random.uniform(2, 10),
                    'twinkle_phase': random.uniform(0, 2 * np.pi),
                    'should_twinkle': random.random() < 0.6  # 60% gwiazdek migocze
                })

        self.add(stars)

        # Funkcja updater - ciągłe migotanie
        def update_stars(group, dt):
            current_time = self.renderer.time
            for i, star in enumerate(group):
                if i < len(star_data):  # dodatkowe zabezpieczenie
                    data = star_data[i]
                    if data['should_twinkle']:
                        # Efekt migotania z funkcji sinus
                        time_factor = current_time * data['twinkle_speed'] + data['twinkle_phase']
                        twinkle_multiplier = 0.3 + 0.7 * (0.5 + 0.5 * np.sin(time_factor))
                        new_opacity = data['base_opacity'] * twinkle_multiplier
                        star.set_opacity(max(0.1, new_opacity))

        # Dodajemy updater do grupy gwiazdek
        stars.add_updater(update_stars)


        # === OKNO POWIADOMIENIA ===
        window = RoundedRectangle(
            width=10, height=6, corner_radius=0.3,
            fill_color="#2a5298", fill_opacity=0.95,
            stroke_color="#00FFFF", stroke_width=3
        ).move_to(UP * 0.5)

        # Efekt świecenia
        glow = RoundedRectangle(
            width=10.5, height=6.5, corner_radius=0.3,
            fill_color="#00FFFF", fill_opacity=0.1,
            stroke_color="#00FFFF", stroke_width=1
        ).move_to(UP * 0.5)

        # === TEKSTY ===
        title = Text(
            "ZDOBYTO PASYWNE UMIEJĘTNOŚCI!",
            font_size=32, color="#FFFF00", weight=BOLD
        ).move_to(UP * 2.5)

        skill_name = Text(
            "FIGMA + CANVA",
            font_size=36, color="#00FFFF", weight=BOLD
        ).move_to(UP * 1.8)

        description = Text(
            "Mistrzostwo w projektowaniu UI/UX i tworzeniu grafik!",
            font_size=20, color="#FFFFFF"
        ).move_to(UP * 1.3)

        # === IKONY Z OPISAMI ===
        # Figma
        figma_icon = ImageMobject("figma.png").scale(0.2)
        figma_desc = Text("Figma\nProjektowanie UI/UX", font_size=16, color="#FFFFFF")
        figma_group = Group(figma_icon, figma_desc).arrange(DOWN, buff=0.3)

        # Canva
        canva_icon = ImageMobject("canva.png").scale(0.1)
        canva_desc = Text("Canva\nGrafika i social media", font_size=16, color="#FFFFFF")
        canva_group = Group(canva_icon, canva_desc).arrange(DOWN, buff=0.3)

        # Układanie ikon obok siebie
        icons_row = Group(figma_group, canva_group).arrange(RIGHT, buff=2).move_to(UP * 0.2)


        # 3. Okno powiadomienia spada z góry
        window_group = VGroup(glow, window)
        window_group.shift(UP * 8)
        self.play(
            window_group.animate.shift(DOWN * 8),
            rate_func=rush_from,
            run_time=1.5
        )

        # 4. Błysk po pojawieniu się okna
        flash = Rectangle(width=16, height=10, fill_color="#FFFFFF", fill_opacity=0.6)
        self.add(flash)
        self.play(FadeOut(flash, run_time=0.3))
        character = ImageMobject("character_happy_scene5_5.png").scale(1)
        character.move_to(DOWN * 2.5)
        self.add(character)

        # 5. Teksty pojawiają się po kolei
        self.play(Write(title), run_time=1)
        self.wait(0.3)
        self.play(Write(skill_name), run_time=0.8)
        self.wait(0.3)
        self.play(Write(description), run_time=0.8)

        # 6. Ikony pojawiają się z efektem skali
        self.play(
            FadeIn(figma_group, scale=0.3),
            run_time=0.8
        )
        self.wait(0.4)
        self.play(
            FadeIn(canva_group, scale=0.3),
            run_time=0.8
        )

        # - Float ikon
        icon_float = [
            AnimationGroup(
                group.animate.shift(UP * 0.15),
                group.animate.shift(DOWN * 0.15),
                rate_func=there_and_back,
                run_time=2.5
            )
            for group in [figma_group, canva_group]
        ]

        # 10. Pauza żeby podziwiać efekt
        self.wait(2)

        # 11. Fade out wszystkiego
        all_objects = Group(
            character, window_group, title, skill_name, description,
            icons_row
        )

        self.play(FadeOut(all_objects), run_time=2)
        self.wait(0.5)




class Scene6_NewSkills(Scene):
    def construct(self):
        # Kolory dla języków programowania
        js_color = "#F7DF1E"  # JavaScript yellow
        python_color = "#3776AB"  # Python blue
        bg_color = "#1E1E2E"  # Ciemne tło

        # Ustawienie tła
        self.camera.background_color = bg_color

        # === POSTAĆ NA ŚRODKU ===
        character = ImageMobject("character_css_master.png").scale(0.8)
        character.move_to(ORIGIN + DOWN * 1)

        # Animacja pojawienia się postaci
        self.play(FadeIn(character), run_time=1)
        self.wait(0.5)

        # === FUNKCJA LEVEL UP ===
        def show_level_up(count=1):
            for i in range(count):
                level_text = Text("LEVEL UP!", font_size=24, color=GOLD, weight=BOLD)
                level_text.next_to(character, UP, buff=0.5 + i * 0.3)

                self.play(
                    DrawBorderThenFill(level_text),
                    Flash(level_text, color=GOLD, flash_radius=1),
                    run_time=0.4
                )
                self.play(
                    level_text.animate.scale(1.2).shift(UP * 0.2).set_opacity(0.7),
                    run_time=0.3
                )
                self.play(FadeOut(level_text), run_time=0.3)
                self.wait(0.1)

        # === OKIENKO POWIADOMIENIA JAVASCRIPT (ŻÓŁTE, PO LEWEJ) ===

        # Tło okienka JavaScript
        js_notification_bg = RoundedRectangle(
            width=4, height=3,
            corner_radius=0.2,
            fill_color="#2a2a2a",
            fill_opacity=0.95,
            stroke_color=js_color,
            stroke_width=3
        )
        js_notification_bg.to_edge(LEFT, buff=0.5).shift(UP * 2)

        # Ikona JavaScript z pliku
        js_icon = ImageMobject("javascript_icon.png")
        js_icon.scale_to_fit_width(0.8)

        # Teksty w okienku JS
        js_title = Text("Odkryto nową umiejętność!", font_size=16, color=WHITE, weight=BOLD)
        js_name = Text("JavaScript", font_size=20, color=js_color, weight=BOLD)
        js_desc = Text("Ucz się dalej, żeby opanować\ndaną umiejętność!",
                       font_size=12, color="#cccccc", line_spacing=1.2)

        # Układanie elementów w okienku JS
        js_content = Group(js_title, js_icon, js_name, js_desc)
        js_content.arrange(DOWN, buff=0.2)
        js_content.move_to(js_notification_bg.get_center())

        js_notification = Group(js_notification_bg, js_content)

        # Animacja pojawienia się okienka JS
        self.play(
            js_notification.animate.shift(DOWN * 2).set_opacity(0),
            run_time=0.001  # Startuje niewidoczne
        )

        self.play(
            js_notification.animate.shift(UP * 2).set_opacity(1),
            run_time=0.8
        )

        self.wait(0.5)

        # 3 x LEVEL UP po JavaScript
        show_level_up(3)

        self.wait(0.5)

        # === OKIENKO POWIADOMIENIA PYTHON (NIEBIESKIE, PO PRAWEJ) ===

        # Tło okienka Python
        python_notification_bg = RoundedRectangle(
            width=4, height=3,
            corner_radius=0.2,
            fill_color="#2a2a2a",
            fill_opacity=0.95,
            stroke_color=python_color,
            stroke_width=3
        )
        python_notification_bg.to_edge(RIGHT, buff=0.5).shift(UP * 2)

        # Ikona Python z pliku
        python_icon = ImageMobject("python_icon.png")
        python_icon.scale_to_fit_width(0.8)

        # Teksty w okienku Python
        python_title = Text("Odkryto nową umiejętność!", font_size=16, color=WHITE, weight=BOLD)
        python_name = Text("Python", font_size=20, color=python_color, weight=BOLD)

        # Dodatkowe wiedze
        manim_text = Text("+ Dodano wiedzę o Manim", font_size=11, color="#90EE90")  # Light green
        streamlit_text = Text("+ Dodano wiedzę o Streamlit", font_size=11, color="#90EE90")

        python_desc = Text("Ucz się dalej, żeby opanować\numiejętność!",
                           font_size=12, color="#cccccc", line_spacing=1.2)

        # Układanie elementów w okienku Python
        python_content = Group(
            python_title, python_icon, python_name,
            manim_text, streamlit_text, python_desc
        )
        python_content.arrange(DOWN, buff=0.15)
        python_content.move_to(python_notification_bg.get_center())

        python_notification = Group(python_notification_bg, python_content)

        # Animacja pojawienia się okienka Python
        self.play(
            python_notification.animate.shift(DOWN * 2).set_opacity(0),
            run_time=0.001  # Startuje niewidoczne
        )

        self.play(
            python_notification.animate.shift(UP * 2).set_opacity(1),
            run_time=0.8
        )

        self.wait(0.3)

        # 4 x LEVEL UP po Python
        show_level_up(4)

        self.wait(0.5)

        # === DODAWANIE DODATKOWYCH WIEDZ ===

        # Animacja dodawania Manim
        self.play(
            Flash(manim_text, color="#90EE90", line_length=0.3),
            manim_text.animate.scale(1.1),
            run_time=0.6
        )
        self.play(manim_text.animate.scale(1 / 1.1), run_time=0.3)

        self.wait(0.3)

        # Animacja dodawania Streamlit
        self.play(
            Flash(streamlit_text, color="#90EE90", line_length=0.3),
            streamlit_text.animate.scale(1.1),
            run_time=0.6
        )
        self.play(streamlit_text.animate.scale(1 / 1.1), run_time=0.3)

        self.wait(1)


        # # Efekty błysków na okienkach
        # self.play(
        #     Flash(js_notification, color=js_color, line_length=0.4, num_lines=12),
        #     Flash(python_notification, color=python_color, line_length=0.4, num_lines=12),
        #     run_time=1.5
        # )
        #
        # self.wait(2)

        # === FADE OUT ===

        all_elements = Group(
            character, js_notification, python_notification,

        )

        self.play(
            FadeOut(all_elements),
            run_time=1.5
        )

        self.wait(0.5)


class Scene7_Final(Scene):
    def construct(self):
        # Ustawienie tła w stylu poprzednich scen (ciemne, RPG-style)
        self.camera.background_color = "#1a1a2e"

        # Scena 7: Finał - transformacja bohaterki
        self.scene_7_transformation()

        # Scena 8: Zakończenie
        self.scene_8_finale()

    def scene_7_transformation(self):
        """Scena 7: Prosta transformacja - obrazek 1 znika, pojawia się "EWOLUCJA", pojawia się obrazek 2"""

        # Gradient background jak w poprzednich scenach
        prev_background = Rectangle(width=20, height=15)
        prev_background.set_fill(color=["#0d1421", "#1a2332", "#2a3441"], opacity=1)
        prev_background.set_stroke(width=0)
        self.add(prev_background)

        # === OBRAZEK 1 (programistka z pierwszego obrazka) ===
        # Używam ImageMobject dla prawdziwego obrazka
        programmer_image = ImageMobject("character_css_master.png")  # Twój pierwszy obrazek
        programmer_image.scale_to_fit_height(5)  # Dopasowanie rozmiaru
        programmer_image.move_to(ORIGIN)

        # === OBRAZEK 2 (wojowniczka z drugiego obrazka) ===
        warrior_image = ImageMobject("character_scene7_after.png")  # Twój drugi obrazek
        warrior_image.scale_to_fit_height(5)  # Dopasowanie rozmiaru
        warrior_image.move_to(ORIGIN)

        # === PROSTA ANIMACJA W STYLU TWOICH SCEN ===
        # 1. Pojawia się obrazek 1
        self.play(FadeIn(programmer_image), run_time=1)
        self.wait(1.5)

        # 2. Obrazek 1 znika
        self.play(FadeOut(programmer_image), run_time=0.8)

        # 3. Pojawia się napis "EWOLUCJA" w stylu Twoich "LEVEL UP!"
        evolution_text = Text("EWOLUOWAŁAŚ!", font_size=48, color=GOLD, weight=BOLD)
        evolution_text.move_to(ORIGIN)

        # Efekt jak w Twoich scenach
        self.play(
            DrawBorderThenFill(evolution_text),
            Flash(evolution_text, color=GOLD, flash_radius=2.5),
            run_time=2
        )

        # Dodatkowy efekt powiększenia jak w Twoich scenach
        self.play(
            evolution_text.animate.scale(1.3).set_opacity(0.9),
            run_time=0.5
        )

        self.wait(1)

        # 4. Napis znika
        self.play(FadeOut(evolution_text), run_time=0.8)

        # 5. Pojawia się obrazek 2 z efektem jak w Scene5
        self.play(FadeIn(warrior_image, scale=0.5), run_time=1.5)
        self.wait(1.5)

        # === KULA ENERGII ROZPRZESTRZENIA SIĘ (z drugiego obrazka) ===
        # Pozycja kuli na podstawie drugiego obrazka (między dłońmi postaci)
        ball_position = warrior_image.get_center() + DOWN * 0.8  # Dostosuj pozycję

        # Kula energii jak w Twoim stylu
        expanding_energy = Circle(
            radius=0.4, fill_color=YELLOW, fill_opacity=0.9, stroke_width=0
        ).move_to(ball_position)

        # Dodaj kulę na scenę
        self.add(expanding_energy)

        # Efekt rozprzestrzeniania się energii
        self.play(
            expanding_energy.animate.scale(25),  # Wypełnia cały ekran
            FadeOut(warrior_image),
            run_time=2.5
        )

        # Zmiana tła na nowe (bardziej magiczne)
        new_background = Rectangle(width=20, height=15)
        new_background.set_fill(color=["#0f1419", "#1a2850", "#2a4d69"], opacity=1)
        new_background.set_stroke(width=0)

        self.play(
            FadeOut(expanding_energy),
            FadeIn(new_background),
            run_time=1.5
        )

    def scene_8_finale(self):
        """Scena 8: Finałowe okienko z komunikatem w stylu Twoich achievement windows"""

        # Gwiazdki w tle jak w Scene5_5
        stars = VGroup()
        for _ in range(50):  # Mniej gwiazdek, żeby nie przesłaniały okienka
            x = random.uniform(-7, 7)
            y = random.uniform(-4, 4)
            star = Text(random.choice(["✦", "✧", "★", "✴", "✶"]),
                        font_size=random.randint(8, 20),
                        color=random.choice([WHITE, GOLD, "#FFDAB9"]))
            star.set_opacity(random.uniform(0.4, 0.8))
            star.move_to([x, y, 0])
            stars.add(star)

        self.add(stars)

        # Wypasione okienko achievement w stylu Twoich scen
        achievement_bg = RoundedRectangle(
            width=9, height=5.5,  # Zwiększona wysokość
            corner_radius=0.4,
            fill_color="#1a1a1a",
            fill_opacity=0.95,
            stroke_color=GOLD,
            stroke_width=4
        )

        # Efekt świecenia jak w Twoich scenach
        glow_bg = RoundedRectangle(
            width=9.5, height=6,  # Zwiększona wysokość
            corner_radius=0.5,
            fill_color=GOLD,
            fill_opacity=0.2,
            stroke_width=0
        )

        # Teksty w stylu Twoich achievement windows
        congrats_text = Text("🎉 GRATULACJE! 🎉", font_size=34, color=GOLD, weight=BOLD)

        # Ikona osiągnięcia
        achievement_icon = Text("💻", font_size=50)

        # Główny tekst profesji
        profession_text = Text("Junior Front-End Dev!", font_size=28, color=GREEN, weight=BOLD)

        # Opis w dwóch liniach
        desc_line_1 = Text("Potrafisz już tworzyć nowoczesne", font_size=16, color="#cccccc")
        desc_line_2 = Text("aplikacje webowe!", font_size=16, color="#cccccc")
        desc_text = Group(desc_line_1, desc_line_2).arrange(DOWN, buff=0.1)

        # Układanie zawartości okienka z większymi odstępami
        achievement_content = Group(
            congrats_text,
            achievement_icon,
            profession_text,
            desc_text
        ).arrange(DOWN, buff=0.4)  # Zwiększony odstęp

        achievement_window = Group(glow_bg, achievement_bg, achievement_content)
        achievement_window.move_to(UP * 0.5)  # Wyśrodkowane

        # === ANIMACJA FINAŁU W STYLU TWOICH SCEN ===

        # Okienko spada z góry jak w Scene5_5
        achievement_window.shift(UP * 8)
        self.play(
            achievement_window.animate.shift(DOWN * 8),
            rate_func=rush_from,
            run_time=1.8
        )

        # Błysk po pojawieniu się okna
        flash = Rectangle(width=20, height=15, fill_color=GOLD, fill_opacity=0.4, stroke_width=0)
        self.add(flash)
        self.play(FadeOut(flash), run_time=0.4)

        # Efekt Flash na okienko jak w Twoich scenach
        self.play(
            Flash(achievement_window, color=GOLD, flash_radius=2.5),
            run_time=1.5
        )

        self.wait(3)
        # Podpis autora
        signature = Text(
            "stworzone przez: Bozheslava",
            font_size=18,
            color="#cccccc",
            slant=ITALIC
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(signature), run_time=1)
        self.wait(1.5)

        # "To be continued..." w stylu konsoli jak w Twoich scenach
        continue_text = Text(
            ">>> to be continued...",
            font_size=22,
            color="#90EE90",  # Light green jak w Twoich Python scenach
            font="Consolas"
        ).move_to(DOWN * 2.8)

        self.play(Write(continue_text), run_time=2)
        self.wait(2)

        # Finalne wygaśnięcie jak w Twoich scenach
        all_elements = Group(
            stars, achievement_window, signature, continue_text
        )

        self.play(FadeOut(all_elements), run_time=2.5)
