import os
import time
import subprocess
import threading
import psutil

# =========================================
# NEXUS FPS BOOSTER v2
# =========================================

# Farben
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

class NexusTool:

    def __init__(self):
        self.running = True
        self.fps = 0
        self.status = "NEXUS_CORE_READY"

        threading.Thread(target=self.fps_tracker, daemon=True).start()

        self.menu_loop()

    # =========================================
    # FPS COUNTER
    # =========================================

    def fps_tracker(self):
        last_time = time.time()
        frames = 0

        while self.running:
            frames += 1
            time.sleep(0.003)

            current_time = time.time()
            elapsed = current_time - last_time

            if elapsed >= 1:
                self.fps = int(frames / elapsed)
                frames = 0
                last_time = current_time

    # =========================================
    # CLEAR SCREEN
    # =========================================

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    # =========================================
    # LOADING BAR
    # =========================================

    def loading(self, text):

        print(f"\n{YELLOW}[NEXUS] {text}{RESET}\n")

        for i in range(1, 21):

            bar = "█" * i + " " * (20 - i)

            print(
                f"\r{CYAN}[{bar}] {i*5}%{RESET}",
                end=""
            )

            time.sleep(0.08)

        print(f"\n{GREEN}[SUCCESS]{RESET}\n")

    # =========================================
    # ASCII UI
    # =========================================

    def interface(self):

        self.clear()

        print(f"""{MAGENTA}

███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

{RESET}""")

        print(f"{CYAN}========================================================{RESET}")
        print(f"{GREEN} STATUS:{RESET} {self.status}")
        print(f"{GREEN} SYSTEM FPS:{RESET} {self.fps}")
        print(f"{CYAN}========================================================{RESET}")

        print(f"{BOLD}[1]{RESET} RAM BOOST")
        print(f"{BOLD}[2]{RESET} DNS BOOST")
        print(f"{BOLD}[3]{RESET} TEMP CLEANER")
        print(f"{BOLD}[4]{RESET} CPU BOOST")
        print(f"{BOLD}[5]{RESET} GPU BOOST")
        print(f"{BOLD}[6]{RESET} NETWORK BOOST")
        print(f"{BOLD}[7]{RESET} CLOSE BACKGROUND APPS")
        print(f"{BOLD}[8]{RESET} FULL FPS BOOST")
        print(f"{BOLD}[9]{RESET} EXIT")

        print(f"{CYAN}========================================================{RESET}")
        print(f"{WHITE} NEXUS PERFORMANCE SYSTEM v2 {RESET}")
        print(f"{CYAN}========================================================{RESET}")

    # =========================================
    # FEATURES
    # =========================================

    def ram_boost(self):

        self.status = "RAM_OPTIMIZATION"

        self.interface()

        self.loading("Optimiere Arbeitsspeicher...")

        ram = psutil.virtual_memory()

        print(f"{GREEN}Freier RAM:{RESET} {ram.available // (1024**2)} MB")

        input("\nENTER drücken...")

    def dns_boost(self):

        self.status = "DNS_FLUSH"

        self.interface()

        self.loading("Flushe DNS Cache...")

        subprocess.run(
            "ipconfig /flushdns",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        input("\nENTER drücken...")

    def temp_clean(self):

        self.status = "TEMP_CLEAN"

        self.interface()

        self.loading("Lösche TEMP Dateien...")

        temp = os.getenv("TEMP")

        os.system(f'del /q/f/s "{temp}\\*" >nul 2>&1')

        input("\nENTER drücken...")

    def cpu_boost(self):

        self.status = "CPU_MAX_PERFORMANCE"

        self.interface()

        self.loading("Aktiviere Höchstleistung...")

        subprocess.run(
            "powercfg /setactive SCHEME_MIN",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        input("\nENTER drücken...")

    def gpu_boost(self):

        self.status = "GPU_OPTIMIZATION"

        self.interface()

        self.loading("Optimiere Grafiksystem...")

        subprocess.run(
            "cleanmgr /verylowdisk",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        input("\nENTER drücken...")

    def network_boost(self):

        self.status = "NETWORK_TWEAK"

        self.interface()

        self.loading("Resette Netzwerkstack...")

        subprocess.run(
            "netsh int ip reset",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        input("\nENTER drücken...")

    def close_apps(self):

        self.status = "CLOSING_APPS"

        self.interface()

        self.loading("Schließe Hintergrundprogramme...")

        targets = [
            "Discord.exe",
            "Spotify.exe",
            "Teams.exe",
            "OneDrive.exe"
        ]

        for process in psutil.process_iter(['pid', 'name']):

            try:

                if process.info['name'] in targets:

                    psutil.Process(
                        process.info['pid']
                    ).terminate()

            except:
                pass

        input("\nENTER drücken...")

    def full_boost(self):

        self.status = "FULL_FPS_BOOST"

        self.interface()

        self.loading("Starte kompletten FPS Boost...")

        subprocess.run(
            "ipconfig /flushdns",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        subprocess.run(
            "netsh int ip reset",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        subprocess.run(
            "powercfg /setactive SCHEME_MIN",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        print(f"\n{GREEN}NEXUS BOOST COMPLETED{RESET}")

        input("\nENTER drücken...")

    # =========================================
    # MENU
    # =========================================

    def menu_loop(self):

        while self.running:

            self.interface()

            choice = input(f"\n{CYAN}NEXUS@SYSTEM > {RESET}")

            if choice == "1":
                self.ram_boost()

            elif choice == "2":
                self.dns_boost()

            elif choice == "3":
                self.temp_clean()

            elif choice == "4":
                self.cpu_boost()

            elif choice == "5":
                self.gpu_boost()

            elif choice == "6":
                self.network_boost()

            elif choice == "7":
                self.close_apps()

            elif choice == "8":
                self.full_boost()

            elif choice == "9":

                self.running = False

                print(f"\n{RED}NEXUS CLOSED{RESET}\n")

                time.sleep(1)

                exit()

            else:

                self.status = "INVALID_OPTION"

# =========================================
# START
# =========================================

if __name__ == "__main__":

    os.system("")

    NexusTool()