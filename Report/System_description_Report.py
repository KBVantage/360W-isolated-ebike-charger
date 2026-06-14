# Dependencies: none beyond Python standard library


#!/usr/bin/env python3
"""
Company: Vantage Power
Author: Kaone Bogopa
Email: k.bogopa@vantagepower.co.bw
Location: Hamburg, Germany

Generates a professional two-column system description report in PDF using LaTeX.
Company logo: vantage-power.png (at top-left corner in header, 2x larger)
Author: Kaone Bogopa
Uses: article class with twocolumn option (flexible, professional, 2-column)
Margins: 1.27cm on left, right, top; 5cm bottom for footer
Includes: extra test/template content to ensure at least 2 pages
Colors:
  - Main title (section): #0F5B31
  - Subtitle 1 (subsection): #5C8C74
  - Title 3 (subsubsection): #94CD94
  - Body text: 10pt, #545455
  - Table header row: #5C8C74 with white text
Uses: pdfLaTeX, no titlesec, uses sectsty for section colors
Tables and images:
  - Tables: width = columnwidth, header row colored
  - Images: width = columnwidth to fit column
"""

import os
import subprocess


# ----------------------------
# MiKTeX path and pdflatex executable
# ----------------------------
MIKTEX_BIN = r"C:\Users\kbogo\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
PDFFLATEX_EXE = MIKTEX_BIN + r"\pdflatex.exe"

# Optionally add MiKTeX to PATH as well
current_path = os.environ.get("PATH", "")
os.environ["PATH"] = MIKTEX_BIN + os.pathsep + current_path


# ----------------------------
# Paths
# ----------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(PROJECT_ROOT, "assets")

# Adjust these filenames to match your actual files:
LOGO_FILENAME = "vantage-power.png"
WEABLE_FILENAME = "wearable.png"  # or "weable.png" if that's the real name

LOGO_PATH = os.path.join(IMAGES_DIR, LOGO_FILENAME)
WEABLE_PATH = os.path.join(IMAGES_DIR, WEABLE_FILENAME)

OUTPUT_TEX = os.path.join(PROJECT_ROOT, "system_description_report.tex")
OUTPUT_PDF = os.path.join(PROJECT_ROOT, "system_description_report.pdf")


# ----------------------------
# Author info
# ----------------------------
AUTHOR_NAME = "Kaone Bogopa"
AUTHOR_EMAIL = "k.bogopa@vantagepower.co.bw"

COMPANY_NAME = "Vantage Power"
REPORT_TITLE = "System Description Report"


# ----------------------------
# LaTeX template (raw string with single backslashes)
# ----------------------------
latex_content = r"""
\documentclass[twocolumn]{article}
\usepackage{geometry}          % page margins
\usepackage{graphicx}          % images
\usepackage{xcolor}            % colors
\usepackage{colortbl}          % colored tables
\usepackage{hyperref}          % links
\usepackage{fancyhdr}          % custom headers/footers
\usepackage{helvet}            % Helvetica font (Arial-like)
\usepackage{sectsty}           % for section styling
\renewcommand{\familydefault}{\sfdefault} % Use sans-serif by default

% Define custom colors
\definecolor{mainTitle}{HTML}{0F5B31}
\definecolor{subTitle1}{HTML}{5C8C74}
\definecolor{title3}{HTML}{94CD94}
\definecolor{bodyText}{HTML}{545455}
\definecolor{tableHeader}{HTML}{5C8C74}

% Set body font size to 10pt
\renewcommand{\normalsize}{\fontsize{10pt}{12pt}\selectfont}
\normalsize

% Apply body text color globally
\color{bodyText}

% Set section title colors
\sectionfont{\color{mainTitle}\large\bfseries}
\subsectionfont{\color{subTitle1}\bfseries}
\subsubsectionfont{\color{title3}\bfseries}

% Margins: 1.27cm on left, right, top; 5cm bottom for footer
\geometry{a4paper, left=1.27cm, right=1.27cm, top=1.27cm, bottom=5cm}

% Clear all header and footer elements first
\fancyhead{}
\fancyfoot{}

% Header: logo at top-left, 2cm height
\setlength{\headheight}{2.5cm}
\fancyhead[L]{\includegraphics[height=2cm]{assets/vantage-power.png}}

% Footer: 
% Left: report title (italic) on first line, name and email on same line (italic, small)
% Center: empty (no page number)
% Right: page number only
\fancyfoot[L]{\itshape\small System Description Report \\ \itshape\small Kaone Bogopa \quad Email: k.bogopa@vantagepower.co.bw}
\fancyfoot[C]{}
\fancyfoot[R]{\thepage}

% Remove horizontal line above header
\renewcommand{\headrulewidth}{0pt}

% Remove line above footer
\renewcommand{\footrulewidth}{0pt}

% Ensure fancy style is active globally
\pagestyle{fancy}

% Table template: rowcolor for header row and white text
\arrayrulecolor{black}

% Title and author
\title{\textbf{System Description Report}}
\author{Kaone Bogopa \\ \textit{Email: k.bogopa@vantagepower.co.bw}}

\begin{document}

% Force fancy style on title page
\pagestyle{fancy}
\thispagestyle{fancy}
\maketitle

% Force fancy style again after title
\pagestyle{fancy}
\thispagestyle{fancy}

% Abstract (one column, then rest in two columns)
\begin{abstract}
This report provides a professional system description for Vantage Power's 
solar and power electronics solutions. It is designed as a template for future 
technical reports, with professional formatting, company branding, and structured sections.
\end{abstract}

% Force fancy style again after abstract
\pagestyle{fancy}
\thispagestyle{fancy}

\section{Introduction}
Vantage Power is focused on solar street lighting systems and power electronics solutions, 
including MPPT chargers, LED drivers, and buck converters. This document serves as a 
template for system description reports, with consistent branding and professional formatting.

\section{System Overview}
The system described in this report is part of Vantage Power's solar energy and power 
electronics portfolio. It integrates embedded systems, PCB design, and solar energy 
conversion technologies.

\subsection{Key Components}
% Table template: fits column width, header row with color #5C8C74 and white text
\begin{tabular}{|p{0.5\columnwidth}|p{0.5\columnwidth}|}
\hline
\rowcolor{tableHeader}
\color{white}\bfseries Component & \color{white}\bfseries Description \\
\hline
MPPT Charger & High-efficiency solar battery charger \\
\hline
LED Driver & Constant-current driver for street lighting \\
\hline
Buck Converter & DC-DC voltage regulation \\
\hline
STM32 Controller & Embedded control and monitoring \\
\hline
\end{tabular}

% Example image: wearable.png, fits column width
\begin{figure}[ht]
    \centering
    \includegraphics[width=\columnwidth]{assets/wearable.png}
    \caption{Wearable monitor device}
    \label{fig:wearable}
\end{figure}

\section{Test Section 1: Template Placeholder for Page Filling}
This is a placeholder section for testing the template layout. 
It contains random text to fill space and ensure the document spans at least two pages.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

\subsection{Subsection A: Sample Technical Content}
Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
cupidatat non proident, sunt in culpa qui officia deserunt mollit.
Nam libero tempore, cum soluta nobis est eligendi optio cumque 
nihil impedit quo minus id quod maxime placeat facere possimus.

\subsection{Subsection B: Additional Sample Content}
Temporibus autem quibusdam et aut officiis debitis aut rerum 
necessitatibus saepe eveniet ut et voluptates repudiandae sint 
et molestiae non recusandae. Itaque earum rerum hic tenetur a 
sapiente delectus, ut aut reiciendis voluptatibus maiores alias.

\section{Test Section 2: Additional Placeholder for Page Filling}
This is another placeholder section to further extend the document 
and ensure it has at least two full pages of content.

\subsubsection{Subsection C: Design and Implementation Notes}
At vero eos et accusamus et iusto odio dignissimos ducimus qui 
blanditiis praesentium voluptatum deleniti atque corrupti quos 
dolores et quas molestias excepturi sint occaecati cupiditate non provident.

\subsubsection{Subsection D: System Integration Considerations}
Et harum quidem rerum facilis est et expedita distinctio. 
Nam libero tempore, cum soluta nobis est eligendi optio cumque 
nihil impedit quo minus id quod maxime placeat facere possimus.

\section{Test Section 3: More Placeholder Content}
This section adds even more content to guarantee at least two pages.

\subsubsection{Subsection E: Performance Metrics}
Voluptatibus maiores alias consequatur aut perferendis dignissimos 
ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti.

\subsubsection{Subsection F: Future Work}
Ut enim ad minima veniam, quis nostrum exercitationem ullamco laboris 
nisi ut aliquid ex ea commodi consequatur quis autem vel eum iure 
reprehenderit qui in ea voluptate velit esse quam nihil molestiae.

\section{Template Usage for Future Reports}
This document is structured as a reusable template for future Vantage Power reports. 
To use it for new projects:

\begin{enumerate}
    \item Update the report title and abstract.
    \item Replace section content with new system details.
    \item Add images later when needed.
    \item All images are sized to fit within the column width using \textbackslash includegraphics[width=\textbackslash columnwidth]{...}.
    \item Tables use the provided template: width = columnwidth, header row colored with \#5C8C74 and white text.
    \item The footer includes the report title, your name, and your email (all italic and small), and the page number on the right.
\end{enumerate}

% Force fancy style at the end as well
\pagestyle{fancy}
\thispagestyle{fancy}

\end{document}
"""


# ----------------------------
# Write .tex file
# ----------------------------
with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
    f.write(latex_content)

print(f"LaTeX file created: {OUTPUT_TEX}")


# ----------------------------
# Compile to PDF using pdflatex (full path)
# ----------------------------
if not os.path.exists(PDFFLATEX_EXE):
    print("ERROR: pdflatex.exe not found at:", PDFFLATEX_EXE)
    print("Check your MiKTeX installation path and update MIKTEX_BIN in the script.")
    exit(1)

compiler_args = [
    PDFFLATEX_EXE,
    "-interaction=nonstopmode",
    OUTPUT_TEX,
]

print(f"Compiling LaTeX to PDF with: {PDFFLATEX_EXE}")
result = subprocess.run(
    compiler_args,
    cwd=PROJECT_ROOT,
    capture_output=True,
    text=True,
)

if result.returncode == 0:
    print(f"PDF created successfully: {OUTPUT_PDF}")
else:
    print("LaTeX compilation failed. Check the log for errors.")
    print(result.stdout)
    print(result.stderr)