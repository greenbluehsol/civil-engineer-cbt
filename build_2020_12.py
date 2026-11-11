# -*- coding: utf-8 -*-
"""
Generate complete explanations for 2020_12
Questions 1~20 (응용역학) and Questions 61~80 (철근콘크리트 및 강구조)
"""
import json
import os

raw_path = "c:/sol/기사문제 답지 만들기/data/sessions_raw/2020_12.json"
out_path = "c:/sol/기사문제 답지 만들기/data/explanations/2020_12.json"

with open(raw_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

data_2020_12 = {
    1: {
        "topic": "내민보의 지점반력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
단순 지지 구간(경간 $a$)과 내민 구간(길이 $b$)을 갖는 내민보(Overhanging Beam)의 모멘트 평형식:
- 지점 A 기준 모멘트의 합은 0입니다:
  $$\\sum M_A = 0 \\implies R_B \\cdot a - P(a + b) = 0$$
- 지점 B의 반력 공식:
  $$R_B = P \\frac{a + b}{a} = P \\left(1 + \\frac{b}{a}\\right)$$

**단계별 풀이**
1. **문제 조건**:
   - B 지점의 반력 $R_B = 2P$가 되기 위한 $b/a$ 산정
2. **방정식 수립 및 풀이**:
   $$P \\left(1 + \\frac{b}{a}\\right) = 2P$$
   $$1 + \\frac{b}{a} = 2 \\implies \\frac{b}{a} = 1.00$$

따라서 정답은 **2**입니다."""
    },
    2: {
        "topic": "트러스 절점법에 의한 수직재 부재력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
트러스의 절점법(Method of Joints):
- 임의의 절점에 작용하는 외력과 부재력은 힘의 평형을 만족해야 합니다:
  $$\\sum F_y = 0$$
- 수평 상현재 2개와 수직재 1개가 만나는 T자형 상부 절점에 수직 외력 $P$가 작용할 때, 수직 방향의 평형은 수직재 혼자 외력을 전부 부담합니다.

**단계별 풀이**
1. **수직재 V가 연결된 상현재 절점 분석**:
   - 절점에 연결된 부재: 좌측 수평 상현재, 우측 수평 상현재, 수직재 V
   - 하중: 하향 연직 집중하중 $100\\text{ kN}$ 작용
2. **절점의 연직방향 힘의 평형방정식 $\\sum F_y = 0$**:
   - 수평 부재들은 연직 방향 분력이 0입니다.
   - 수직재 V의 부재력을 $V$(인장을 양수로 가정)라 하면:
     $$-V - 100\\text{ kN} = 0 \\implies V = -100\\text{ kN}$$
   - 음(-)의 부호는 절점을 밀어붙이는 **압축력($100\\text{ kN}$ 압축)**을 의미합니다.

따라서 정답은 **2**입니다."""
    },
    3: {
        "topic": "케이블 및 도르래 구조물의 평형",
        "choices": [
            "$P = \\frac{W}{2\\cos\\frac{\\alpha}{2}}$",
            "$P = \\frac{W}{2\\cos\\alpha}$",
            "$P = \\frac{W}{\\cos\\frac{\\alpha}{2}}$",
            "$P = \\frac{2W}{\\cos\\frac{\\alpha}{2}}$"
        ],
        "explanation": """**핵심 개념 / 공식**
1. **연속 케이블의 장력 균일성**:
   - 마찰이 없는 도르래를 지나는 케이블 전체의 장력 $T$는 일정합니다 ($T = P$).
2. **하중 $W$ 작용 절점의 평형**:
   - 하향 연직 하중 $W$에 대해 대칭 배치된 두 케이블의 장력 $T$가 위쪽으로 지지합니다.
   - 두 케이블 사이의 벌어진 각도가 $\\alpha$이므로, 연직선과 각 케이블이 이루는 각도는 각각 $\\frac{\\alpha}{2}$입니다.
   - 연직방향 힘의 평형방정식:
     $$\\sum F_y = 0 \\implies 2 T \\cos\\frac{\\alpha}{2} = W$$

**단계별 풀이**
1. **케이블 장력 $T$ 산정**:
   $$2 T \\cos\\frac{\\alpha}{2} = W \\implies T = \\frac{W}{2\\cos\\frac{\\alpha}{2}}$$
2. **도르래를 거쳐 당기는 힘 $P$**:
   - 도르래의 마찰을 무시하므로 $P = T$:
     $$P = \\frac{W}{2\\cos\\frac{\\alpha}{2}}$$

따라서 정답은 **1**입니다."""
    },
    4: {
        "topic": "탄성계수와 전단탄성계수의 관계",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
등방성 탄성재료의 탄성계수(Young's Modulus, $E$), 전단탄성계수(Shear Modulus, $G$), 푸아송 비(Poisson's Ratio, $\\nu$)의 관계식:
$$G = \\frac{E}{2(1 + \\nu)}$$

**단계별 풀이**
1. **주어진 조건**:
   - 탄성계수 $E = 2.1 \\times 10^5\\text{ MPa}$
   - 푸아송 비 $\\nu = 0.25$
2. **전단탄성계수 $G$ 계산**:
   $$G = \\frac{2.1 \\times 10^5\\text{ MPa}}{2(1 + 0.25)} = \\frac{2.1 \\times 10^5}{2 \\times 1.25} = \\frac{2.1 \\times 10^5}{2.5} = 0.84 \\times 10^5\\text{ MPa} = 8.4 \\times 10^4\\text{ MPa}$$

따라서 정답은 **1**입니다."""
    },
    5: {
        "topic": "T형 단면 단순보의 최대 전단응력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
보 단면의 전단응력 공식:
$$\\tau = \\frac{V Q}{I b_w}$$
- $V_{\\max}$: 단순보 지점부에서의 최대 전단력 ($V_{\\max} = \\frac{wL}{2}$)
- $I$: 단면 전체의 도심축(중립축)에 대한 단면 2차 모멘트
- $Q$: 도심축 상부(또는 하부) 단면의 도심축에 대한 단면 1차 모멘트
- $b_w$: 최대 전단응력이 발생하는 도심축에서의 폭

**단계별 풀이**
1. **보의 최대 전단력 $V$ 계산**:
   - $w = 4\\text{ kN/m}$, $L = 5\\text{ m}$
   $$V = \\frac{4\\text{ kN/m} \\times 5\\text{ m}}{2} = 10\\text{ kN} = 10,000\\text{ N}$$
2. **단면 도심축(중립축) 위치 $\\bar{y}$ 산정 (하단 기준)**:
   - 복부(Web): $30\\text{ mm} \\times 70\\text{ mm}$, $A_1 = 2100\\text{ mm}^2$, $y_1 = 35\\text{ mm}$
   - 플랜지(Flange): $70\\text{ mm} \\times 30\\text{ mm}$, $A_2 = 2100\\text{ mm}^2$, $y_2 = 70 + 15 = 85\\text{ mm}$
   $$\\bar{y} = \\frac{2100 \\times 35 + 2100 \\times 85}{2100 + 2100} = \\frac{35 + 85}{2} = 60\\text{ mm}$$
   - 도심축은 하단에서 $60\\text{ mm}$ 위치(복부 내)에 존재하므로, 최대 전단응력 발생 단면의 폭은 $b_w = 30\\text{ mm}$입니다.
3. **단면 2차 모멘트 $I$ 계산**:
   - 복부: $I_1 = \\frac{30 \\times 70^3}{12} + 2100 \\times (60 - 35)^2 = 857,500 + 1,312,500 = 2,170,000\\text{ mm}^4$
   - 플랜지: $I_2 = \\frac{70 \\times 30^3}{12} + 2100 \\times (85 - 60)^2 = 157,500 + 1,312,500 = 1,470,000\\text{ mm}^4$
   $$I = I_1 + I_2 = 2,170,000 + 1,470,000 = 3,640,000\\text{ mm}^4 = 3.64 \\times 10^6\\text{ mm}^4$$
4. **도심축 하부 단면의 단면 1차 모멘트 $Q$ 계산**:
   - 도심축 하부 단면 크기: $30\\text{ mm} \\times 60\\text{ mm}$, 도심거리: $60/2 = 30\\text{ mm}$
   $$Q = (30 \\times 60) \\times 30 = 54,000\\text{ mm}^3$$
5. **최대 전단응력 $\\tau_{\\max}$ 계산**:
   $$\\tau_{\\max} = \\frac{10,000\\text{ N} \\times 54,000\\text{ mm}^3}{3.64 \\times 10^6\\text{ mm}^4 \\times 30\\text{ mm}} = \\frac{540,000,000}{109,200,000} \\approx 4.945\\text{ MPa} \\approx 4.95\\text{ MPa}$$

따라서 정답은 **4**입니다."""
    },
    6: {
        "topic": "훅의 법칙과 탄성계수 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
1. 인장변형률(Strain) 공식:
   $$\\varepsilon = \\frac{\\Delta L}{L}$$
2. 훅의 법칙(Hooke's Law)에 의한 탄성계수(Modulus of Elasticity, $E$):
   $$E = \\frac{\\sigma}{\\varepsilon}$$

**단계별 풀이**
1. **주어진 조건**:
   - 원래 길이 $L = 5\\text{ m} = 5000\\text{ mm}$
   - 늘어난 길이 $\\Delta L = 5\\text{ mm}$
   - 인장응력 $\\sigma = 200\\text{ MPa}$
2. **변형률 $\\varepsilon$ 계산**:
   $$\\varepsilon = \\frac{5\\text{ mm}}{5000\\text{ mm}} = 0.001$$
3. **탄성계수 $E$ 계산**:
   $$E = \\frac{\\sigma}{\\varepsilon} = \\frac{200\\text{ MPa}}{0.001} = 200,000\\text{ MPa} = 2 \\times 10^5\\text{ MPa}$$

따라서 정답은 **2**입니다."""
    },
    7: {
        "topic": "일단고정 타단지지보의 고정단 휨모멘트",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
A단이 고정이고 B단이 롤러(지점)인 일단고정 타단지지보에서 집중하중 $P$가 고정단으로부터 $a$, 롤러 지점으로부터 $b$ 위치에 작용할 때:
- 고정단 A의 휨모멘트 공식:
  $$M_A = -\\frac{P \\cdot a \\cdot b(2L - a)}{2L^2} = -\\frac{P \\cdot b(L^2 - b^2)}{2L^2}$$
  (음의 부호는 상부 인장 모멘트를 의미)

**단계별 풀이**
1. **주어진 조건**:
   - 하중 $P = 50\\text{ kN}$
   - $a = 3\\text{ m}$, $b = 2\\text{ m}$
   - 전체 경간 $L = a + b = 3 + 2 = 5\\text{ m}$
2. **A점의 휨모멘트 $M_A$ 계산**:
   $$M_A = -\\frac{P \\cdot b (L^2 - b^2)}{2 L^2} = -\\frac{50 \\times 2 \\times (5^2 - 2^2)}{2 \\times 5^2}$$
   $$M_A = -\\frac{100 \\times (25 - 4)}{2 \\times 25} = -\\frac{100 \\times 21}{50} = -42\\text{ kN}\\cdot\\text{m}$$

따라서 정답은 **3**입니다."""
    },
    8: {
        "topic": "휨과 축압축을 동시에 받는 보의 단면응력",
        "choices": [
            "$\\frac{P}{bh^2}\\left(1 + \\frac{6a}{h}\\right)$",
            "$\\frac{P}{bh}\\left(1 - \\frac{6a}{h}\\right)$",
            "$\\frac{P}{b^2h^2}\\left(1 - \\frac{6a}{h}\\right)$",
            "$\\frac{P}{b^2h}\\left(1 - \\frac{a}{h}\\right)$"
        ],
        "explanation": """**핵심 개념 / 공식**
축하중과 휨모멘트를 동시에 받는 부재 단면의 조합응력 공식 (압축을 양수로 정의):
$$\\sigma = \\frac{N}{A} \\pm \\frac{M}{Z}$$
- 단면적: $A = b \\cdot h$
- 단면계수: $Z = \\frac{b h^2}{6}$
- 축압축력: $N = P$
- 양측 대칭 수직하중 $P$에 의한 중앙점 휨모멘트: $M = P \\cdot a$ (하연 인장(-), 상연 압축(+))

**단계별 풀이**
1. **축압축력에 의한 응력 (전 단면 균등 압축)**:
   $$\\sigma_{\\text{axial}} = +\\frac{P}{A} = +\\frac{P}{bh}$$
2. **휨모멘트에 의한 단면 하단 응력 (인장 응력)**:
   $$\\sigma_{\\text{bending}} = -\\frac{M}{Z} = -\\frac{Pa}{\\frac{1}{6}bh^2} = -\\frac{6Pa}{bh^2}$$
3. **단면 하단의 수직응력 합성**:
   $$\\sigma = \\sigma_{\\text{axial}} + \\sigma_{\\text{bending}} = \\frac{P}{bh} - \\frac{6Pa}{bh^2} = \\frac{P}{bh}\\left(1 - \\frac{6a}{h}\\right)$$

따라서 정답은 **2**입니다."""
    },
    9: {
        "topic": "게르버보의 휨모멘트 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
**게르버보(Gerber Beam)**의 해석:
- 내부 힌지(B)를 기준으로 부구조(지지보)와 주구조(내민보)로 분리합니다.
- 지지보 AB의 힌지 B 반력을 먼저 구한 뒤, 내민보 BCD의 하중으로 전달시켜 평형방정식을 세웁니다.

**단계별 풀이**
1. **보 AB (단순보 구간) 해석**:
   - 경간 $L_{AB} = 6\\text{ m}$, 등분포하중 $w_1 = 10\\text{ kN/m}$
   - 힌지 B로 전달되는 전단력(반력):
     $$V_B = \\frac{w_1 \\cdot L_{AB}}{2} = \\frac{10\\text{ kN/m} \\times 6\\text{ m}}{2} = 30\\text{ kN}$$
2. **보 BCD (내민보 구간) 해석**:
   - 힌지 B에서 하향 집중하중 $V_B = 30\\text{ kN}$ 작용
   - 내민 구간 $BC = 4\\text{ m}$ (하중 없음)
   - 지지 구간 $CD = 10\\text{ m}$에 등분포하중 $w_2 = 20\\text{ kN/m}$ 작용
   - C점 기준 모멘트 평형식 $\\sum M_C = 0$을 통해 지점 D 반력 $R_D$ 산정:
     $$-V_B \\times 4\\text{ m} + (w_2 \\times 10\\text{ m}) \\times 5\\text{ m} - R_D \\times 10\\text{ m} = 0$$
     $$-(30 \\times 4) + (200 \\times 5) - 10 R_D = 0$$
     $$-120 + 1000 - 10 R_D = 0 \\implies 10 R_D = 880 \\implies R_D = 88\\text{ kN}\\;(\\uparrow)$$
3. **E점(D점으로부터 $5\\text{ m}$ 좌측)의 휨모멘트 $M_E$ 계산**:
   - E점 우측(ED 구간)의 자유물체도 고려:
     $$M_E = R_D \\times 5\\text{ m} - (20\\text{ kN/m} \\times 5\\text{ m}) \\times 2.5\\text{ m}$$
     $$M_E = (88 \\times 5) - (100 \\times 2.5) = 440 - 250 = 190\\text{ kN}\\cdot\\text{m}$$

따라서 정답은 **1**입니다."""
    },
    10: {
        "topic": "양단고정 원형 장주의 오일러 좌굴응력",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
오일러 좌굴응력(Euler Buckling Stress) 공식:
$$\\sigma_{cr} = \\frac{\\pi^2 E}{\\lambda^2}$$
여기서,
- 세장비 $\\lambda = \\frac{L_e}{r} = \\frac{K \\cdot L}{r}$
- $K$: 유효좌굴길이계수 (양단 고정이므로 $K = 0.5$)
- $L$: 기둥의 길이 ($8\\text{ m} = 8000\\text{ mm}$, 문제 그림 참조)
- $r$: 원형 단면의 단면 2차 반지름 ($r = \\frac{d}{4}$)

**단계별 풀이**
1. **단면 특성 및 세장비 계산**:
   - 지름 $d = 4\\text{ cm} = 40\\text{ mm}$
   $$r = \\frac{d}{4} = \\frac{40\\text{ mm}}{4} = 10\\text{ mm}$$
   - 유효좌굴길이:
     $$L_e = K \\cdot L = 0.5 \\times 8000\\text{ mm} = 4000\\text{ mm}$$
   - 세장비:
     $$\\lambda = \\frac{L_e}{r} = \\frac{4000}{10} = 400$$
2. **좌굴응력 $\\sigma_{cr}$ 계산**:
   - 탄성계수 $E = 2.1 \\times 10^5\\text{ MPa}$
   $$\\sigma_{cr} = \\frac{\\pi^2 E}{\\lambda^2} = \\frac{\\pi^2 \\times 2.1 \\times 10^5}{400^2} = \\frac{9.8696 \\times 210,000}{160,000} \\approx \\frac{2,072,617}{160,000} \\approx 12.95\\text{ MPa}$$

따라서 정답은 **3**입니다."""
    },
    11: {
        "topic": "보의 휨 탄성변형에너지 공식",
        "choices": [
            "$U = \\int_0^L \\frac{M^2}{2EI}\\, dx$",
            "$U = \\int_0^L \\frac{2EI}{M^2}\\, dx$",
            "$U = \\int_0^L \\frac{EI}{2M^2}\\, dx$",
            "$U = \\int_0^L \\frac{M^2}{EI}\\, dx$"
        ],
        "explanation": """**핵심 개념 / 공식**
보의 휨 탄성변형에너지(Strain Energy due to Flexure):
- 미소 길이 $dx$의 보 요소에 휨모멘트 $M$이 작용할 때 요소의 회전각은 $d\\theta = \\frac{M}{EI}dx$입니다.
- 이 미소 요소에 축적되는 탄성변형에너지는 외력 모멘트가 한 일과 같으므로:
  $$dU = \\frac{1}{2} M\\, d\\theta = \\frac{M^2}{2EI}\\, dx$$
- 보 전체 길이($L$)에 걸쳐 적분하면 총 휨 탄성 에너지는 다음과 같습니다:
  $$U = \\int_0^L \\frac{M^2}{2EI}\\, dx$$

**단계별 풀이**
- ① $U = \\int_0^L \\frac{M^2}{2EI}\\, dx$ 가 정확한 공식입니다.

따라서 정답은 **1**입니다."""
    },
    12: {
        "topic": "단부 모멘트를 받는 단순보의 최대 처짐 위치",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
단순보 AB(경간 $L$)의 B단에 외력 모멘트 $M$이 작용할 때의 탄성곡선 미분방정식 풀이:
- A 지점으로부터 거리 $x$인 단면의 처짐식:
  $$y(x) = \\frac{M x}{6 E I L} (L^2 - x^2)$$
- 처짐이 최대가 되는 위치에서는 처짐각(탄성곡선의 기울기)이 0이 됩니다:
  $$\\frac{dy}{dx} = 0$$

**단계별 풀이**
1. **처짐식을 $x$에 대해 미분**:
   $$\\frac{dy}{dx} = \\frac{M}{6 E I L} (L^2 - 3x^2) = 0$$
2. **최대 처짐 위치 $x$ 산정**:
   $$L^2 - 3x^2 = 0 \\implies x^2 = \\frac{L^2}{3}$$
   $$x = \\frac{L}{\\sqrt{3}} \\approx 0.577 L$$
3. 따라서 A점으로부터 약 $0.577L$ 떨어진 위치에서 최대 수직 처짐이 발생합니다.

따라서 정답은 **2**입니다."""
    },
    13: {
        "topic": "캔틸레버보 부분등분포하중의 처짐비",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
캔틸레버보 고정단(A)에서 중간점(C, $L/2$)까지만 등분포하중 $w$가 작용할 때:
1. C점의 처짐 $\\delta_C$:
   길이가 $L/2$인 캔틸레버보 자유단 처짐과 동일:
   $$\\delta_C = \\frac{w (L/2)^4}{8EI} = \\frac{w L^4}{128 EI}$$
2. C점의 처짐각 $\\theta_C$:
   $$\\theta_C = \\frac{w (L/2)^3}{6EI} = \\frac{w L^3}{48 EI}$$
3. 자유단 B점의 처짐 $\\delta_B$:
   CB 구간에는 하중이 없으므로 직선으로 기울어지며 변형합니다:
   $$\\delta_B = \\delta_C + \\theta_C \\cdot \\left(\\frac{L}{2}\\right)$$

**단계별 풀이**
1. **B점 처짐 계산**:
   $$\\delta_B = \\frac{w L^4}{128 EI} + \\frac{w L^3}{48 EI} \\left(\\frac{L}{2}\\right) = \\frac{w L^4}{128 EI} + \\frac{w L^4}{96 EI}$$
   - 공통 분모 384로 통분 ($128 \\times 3 = 384$, $96 \\times 4 = 384$):
     $$\\delta_C = \\frac{3 w L^4}{384 EI}$$
     $$\\delta_B = \\frac{(3 + 4) w L^4}{384 EI} = \\frac{7 w L^4}{384 EI}$$
2. **처짐비 $\\delta_C : \\delta_B$ 계산**:
   $$\\delta_C : \\delta_B = 3 : 7$$

따라서 정답은 **2**입니다."""
    },
    14: {
        "topic": "단면 2차 모멘트 및 휨강성 비교",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
1. **휨강성(Flexural Rigidity)**:
   - 보의 처짐에 저항하는 강성으로 $E \\cdot I$ (단면 2차 모멘트 $I$에 비례)로 정의됩니다.
   - 직사각형 단면: $I = \\frac{b h^3}{12}$
2. **단면계수(Section Modulus, 휨저항강도)**:
   - 휨응력 및 최대 휨모멘트 저항력에 관련된 값으로 $Z = \\frac{b h^2}{6}$입니다.

**단계별 풀이**
1. **두 단면의 특성치 계산**:
   - **보 (A)**: 폭 $b = 10\\text{ cm}$, 높이 $h = 30\\text{ cm}$
     $$I_A = \\frac{10 \\times 30^3}{12} = 22,500\\text{ cm}^4, \\quad Z_A = \\frac{10 \\times 30^2}{6} = 1500\\text{ cm}^3$$
   - **보 (B)**: 폭 $b = 15\\text{ cm}$, 높이 $h = 20\\text{ cm}$
     $$I_B = \\frac{15 \\times 20^3}{12} = 10,000\\text{ cm}^4, \\quad Z_B = \\frac{15 \\times 20^2}{6} = 1000\\text{ cm}^3$$
2. **비교 분석 및 출제 오류 해설**:
   - 엄밀한 **휨강성(EI)**의 비는:
     $$\\frac{I_A}{I_B} = \\frac{22,500}{10,000} = 2.25\\text{배}$$
   - 단면계수(휨강도)의 비는:
     $$\\frac{Z_A}{Z_B} = \\frac{1500}{1000} = 1.5\\text{배}$$
   - 출제자가 휨강성(EI)을 단면계수의 비(1.5배)로 혼동하여 가답안 발표 시 ③번으로 발표하였으나, 최종 확정답안 발표 시 용어 오류로 인정되어 **전항 정답(모두 정답)** 처리되었습니다. 문제 시스템에서는 가답안인 ③번이 정답 처리됩니다.

따라서 정답은 **3**입니다."""
    },
    15: {
        "topic": "3힌지 아치의 지점반력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
**3힌지 아치(Three-hinged Arch)**의 지점반력 산정:
1. 지점 A와 B가 동일 높이에 위치하므로 전체 구조물에 대한 모멘트 평형식 $\\sum M_B = 0$으로부터 수직반력 $V_A$를 산정합니다.
2. 힌지점 C의 모멘트가 0이므로, 좌측 부재 AC에 대한 모멘트 평형식 $\\sum M_C^{\\text{left}} = 0$으로부터 수평반력 $H_A$를 구합니다.

**단계별 풀이**
1. **수직반력 $V_A$ 계산**:
   - 총 경간 $L = 6\\text{ m} + 9\\text{ m} = 15\\text{ m}$
   - 전체 경간에 등분포하중 $w = 1\\text{ kN/m}$ 재하 (총 하중 $15\\text{ kN}$, 중앙 $7.5\\text{ m}$에 재하)
   - B점 기준 모멘트 평형:
     $$V_A \\times 15\\text{ m} - (1\\text{ kN/m} \\times 15\\text{ m}) \\times 7.5\\text{ m} = 0$$
     $$15 V_A = 112.5 \\implies V_A = 7.5\\text{ kN}\\;(\\uparrow)$$
2. **수평반력 $H_A$ 계산**:
   - 좌측 부재 AC의 수평길이 $6\\text{ m}$, 아치 높이 $h = 3\\text{ m}$
   - 힌지 C 기준 좌측 부분 모멘트 평형 $\\sum M_C = 0$:
     $$V_A \\times 6\\text{ m} - H_A \\times 3\\text{ m} - (1\\text{ kN/m} \\times 6\\text{ m}) \\times 3\\text{ m} = 0$$
     $$(7.5 \\times 6) - 3 H_A - 18 = 0$$
     $$45 - 18 - 3 H_A = 0 \\implies 27 = 3 H_A \\implies H_A = 9.0\\text{ kN}\\;(\\rightarrow)$$

따라서 정답은 **3**입니다."""
    },
    16: {
        "topic": "양단고정보 지점회전에 의한 단부 반력 및 모멘트",
        "choices": [
            "$R_A = \\frac{6EI\\theta}{L^2},\\; M_A = \\frac{4EI\\theta}{L}$",
            "$R_A = \\frac{12EI\\theta}{L^3},\\; M_A = \\frac{6EI\\theta}{L^2}$",
            "$R_A = \\frac{4EI\\theta}{L^2},\\; M_A = \\frac{6EI\\theta}{L}$",
            "$R_A = \\frac{2EI\\theta}{L},\\; M_A = \\frac{4EI\\theta}{L^2}$"
        ],
        "explanation": """**핵심 개념 / 공식**
처짐각법(Slope-Deflection Method) 기본 공식:
$$M_{AB} = 2E K (2\\theta_A + \\theta_B - 3R) + C_{AB}$$
여기서 보 AB에 외력 하중이 없고($C_{AB}=0$), B단은 고정($\\theta_B = 0$), 지점침하 없음($R=0$), A단이 회전각 $\\theta$만큼 회전($\\theta_A = \\theta$)할 때:
- A단 모멘트: $M_A = M_{AB} = \\frac{4EI\\theta}{L}$
- B단 전달모멘트: $M_B = M_{BA} = \\frac{2EI\\theta}{L}$
- 양단 모멘트 평형에 의한 전단반력:
  $$R_A = \\frac{M_A + M_B}{L} = \\frac{\\frac{4EI\\theta}{L} + \\frac{2EI\\theta}{L}}{L} = \\frac{6EI\\theta}{L^2}$$

**단계별 풀이**
1. A단의 고정단 모멘트:
   $$M_A = \\frac{4EI\\theta}{L}$$
2. 보의 수직반력 평형 $\\sum M_B = 0$:
   $$R_A \\cdot L - M_A - M_B = 0 \\implies R_A = \\frac{M_A + M_B}{L} = \\frac{6EI\\theta}{L^2}$$

따라서 정답은 **1**입니다."""
    },
    17: {
        "topic": "원형 단면의 핵(Kern) 면적 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
원형 단면(반지름 $r$)을 갖는 단주의 핵(Kern):
- 단면에 편심하중이 작용할 때 전 단면에 압축응력만 발생(인장응력 무발생)하도록 하는 편심 한계 거리(핵 반지름 $k$):
  $$k = \\frac{Z}{A} = \\frac{\\frac{\\pi r^3}{4}}{\\pi r^2} = \\frac{r}{4}$$
- 원형 단면의 핵은 단면 중심과 동심인 **반지름 $k = r/4$의 원**입니다.
- 핵의 면적 공식:
  $$A_{\\text{kern}} = \\pi k^2 = \\pi \\left(\\frac{r}{4}\\right)^2$$

**단계별 풀이**
1. **주어진 조건**:
   - 원형 단면의 반지름 $r = 30\\text{ cm}$
2. **핵의 반지름 $k$ 계산**:
   $$k = \\frac{30\\text{ cm}}{4} = 7.5\\text{ cm}$$
3. **핵의 면적 $A_{\\text{kern}}$ 계산**:
   $$A_{\\text{kern}} = \\pi \\times (7.5\\text{ cm})^2 = 56.25\\pi\\text{ cm}^2 \\approx 56.25 \\times 3.14159 \\approx 176.71\\text{ cm}^2 \\approx 176.7\\text{ cm}^2$$

따라서 정답은 **3**입니다."""
    },
    18: {
        "topic": "단면의 기하학적 성질과 부호 특성",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
**단면의 기하학적 특성치와 부호**:
1. **단면 2차 모멘트 ($I = \\int y^2 dA$)**:
   - 거리의 제곱을 적분하므로 항상 양수($I > 0$)입니다.
2. **단면계수 ($Z = I / y_{\\max}$)**:
   - 양수인 $I$와 최외단 거리의 비이므로 항상 양수($Z > 0$)입니다.
3. **단면 2차 반지름 ($r = \\sqrt{I/A}$)**:
   - 제곱근 값이므로 항상 양수($r > 0$)입니다.
4. **단면 상승 모멘트 ($I_{xy} = \\int x y\\, dA$)**:
   - 좌표 $x$와 $y$의 곱을 적분하므로, 기준 좌표축에 대한 단면의 위치(사분면)에 따라 **정(+), 부(-), 또는 0**의 값을 모두 가질 수 있습니다.

**단계별 풀이**
- 문제에서 "정(+)의 값뿐만 아니라 부(-)의 값도 갖는 것"은 **단면 상승 모멘트**입니다.

따라서 정답은 **4**입니다."""
    },
    19: {
        "topic": "경사면에 수직인 분력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
힘의 벡터 합성 및 경사면에 수직인 분력 계산:
- 직각삼각형 ABC에서 각 C가 $60^\\circ$, 각 B가 $90^\\circ$이므로 경사면 AC는 수평선 BC와 $60^\\circ$의 각을 이룹니다.
- 경사면 AC의 법선(수직 방향 단위벡터, 안쪽을 향하는 방향)은 수평축으로부터 아래로 $30^\\circ$ 기울어져 있습니다.
- 작용하는 두 힘 $P_1$과 $P_2$의 법선 방향 정사영(내적)을 통해 수직 분력 $p$를 구합니다:
  $$p = P_1 \\cos 30^\\circ + P_2 \\sin 30^\\circ$$

**단계별 풀이**
1. **주어진 힘**:
   - $P_1 = 600\\sqrt{3}\\text{ kN}$ (우측 수평 방향)
   - $P_2 = 600\\text{ kN}$ (하향 연직 방향)
2. **AC면에 수직인 방향으로의 성분 분해**:
   - 수평력 $P_1$의 수직 기여분: $P_1 \\cos 30^\\circ = 600\\sqrt{3} \\times \\frac{\\sqrt{3}}{2} = 600 \\times \\frac{3}{2} = 900\\text{ kN}$
   - 수직력 $P_2$의 수직 기여분: $P_2 \\sin 30^\\circ = 600 \\times \\frac{1}{2} = 300\\text{ kN}$
3. **합성 분력 $p$ 계산**:
   $$p = 900\\text{ kN} + 300\\text{ kN} = 1200\\text{ kN}$$

따라서 정답은 **2**입니다."""
    },
    20: {
        "topic": "단순보 통과 이동 집중하중의 최대 단면력",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
지간 $L$인 단순보 위를 단일 집중하중 $P$가 통과할 때:
1. **최대 전단력 ($S_{\\max}$)**:
   - 하중 $P$가 지점 바로 안쪽($x \\to 0$ 또는 $x \\to L$)에 위치할 때 발생:
     $$S_{\\max} = P$$
2. **최대 휨모멘트 ($M_{\\max}$)**:
   - 하중 $P$가 단순보의 정중앙($x = L/2$)에 위치할 때 발생:
     $$M_{\\max} = \\frac{P L}{4}$$

**단계별 풀이**
1. **주어진 조건**:
   - 지간 $L = 10\\text{ m}$
   - 집중하중 $P = 200\\text{ kN}$
2. **최대 전단력 $S$ 산정**:
   $$S = P = 200\\text{ kN}$$
3. **최대 휨모멘트 $M$ 산정**:
   $$M = \\frac{P L}{4} = \\frac{200\\text{ kN} \\times 10\\text{ m}}{4} = 500\\text{ kN}\\cdot\\text{m}$$

따라서 정답은 **3**입니다."""
    },
    61: {
        "topic": "콘크리트 탄성계수 계산 시 평균압축강도(fcu)",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 콘크리트구조기준에서 콘크리트 탄성계수 및 크리프 계산에 적용하는 **콘크리트의 평균 압축강도($f_{cu}$)** 산정 기준:
$$f_{cu} = f_{ck} + \\Delta f$$
- $f_{ck} \\le 40\\text{ MPa}$인 경우: $\\Delta f = 4.0\\text{ MPa}$
- $f_{ck} \\ge 60\\text{ MPa}$인 경우: $\\Delta f = 6.0\\text{ MPa}$
- $40\\text{ MPa} < f_{ck} < 60\\text{ MPa}$인 경우: 직선보간하여 산정
  $$\\Delta f = 4.0 + \\frac{6.0 - 4.0}{60 - 40} \\times (f_{ck} - 40) = 4.0 + 0.1 \\times (f_{ck} - 40)$$

**단계별 풀이**
1. **주어진 강도**:
   - 설계기준압축강도 $f_{ck} = 50\\text{ MPa}$
2. **$\\Delta f$ 산정 (직선보간)**:
   $$\\Delta f = 4.0 + 0.1 \\times (50 - 40) = 4.0 + 1.0 = 5.0\\text{ MPa}$$
3. **평균 압축강도 $f_{cu}$ 계산**:
   $$f_{cu} = 50\\text{ MPa} + 5.0\\text{ MPa} = 55\\text{ MPa}$$

따라서 정답은 **2**입니다."""
    },
    62: {
        "topic": "프리스트레스트 콘크리트 부재의 최소 피복두께",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 50(철근 배근 및 세목) 규정에 따른 **콘크리트의 최소 피복두께**:
- **흙에 접하여 콘크리트를 친 후 영구히 흙에 묻혀 있는 콘크리트**:
  - 부재 종류(일반 철근콘크리트 또는 프리스트레스트 콘크리트)에 관계없이 **$75\\text{ mm}$**

**단계별 풀이**
- 지반과 직접 접촉하여 타설되고 영구히 매립되는 기초 및 지하 구조물 부재의 최소 피복두께는 내부 강재의 부식을 방지하기 위해 엄격하게 **$75\\text{ mm}$**로 규정되어 있습니다.

따라서 정답은 **3**입니다."""
    },
    63: {
        "topic": "2방향 슬래브 직접설계법(Direct Design Method) 제한사항",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 70에 따른 **2방향 슬래브 직접설계법 적용 제한사항**:
1. 각 방향으로 **3경간 이상** 연속되어야 한다.
2. 슬래브 판들은 단변 경간에 대한 장변 경간의 비가 **2 이하**인 직사각형이어야 한다.
3. 각 방향으로 연속한 받침부 중심간 경간 차이는 긴 경간의 **1/3 이하**이어야 한다.
4. 기둥 중심선으로부터 기둥의 어긋남(편심)은 그 방향 경간의 **최대 10% 이하**이어야 한다.
5. 활하중은 고정하중의 2배 이하이어야 한다.

**단계별 풀이**
- ④ "기둥의 어긋남은 그 방향 경간의 최대 20%까지 벗어날 수 있다"는 설명은 틀렸습니다. 기준에서는 **최대 10%**까지로 엄격히 제한하고 있습니다.

따라서 정답은 **4**입니다."""
    },
    64: {
        "topic": "PSC 보의 하연응력 0 조건과 프리스트레스 힘 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
PSC 보 중앙 단면의 하연 콘크리트 응력 공식 (압축을 양수로 정의):
$$\\sigma_{\\text{bot}} = \\frac{P}{A} + \\frac{P \\cdot e}{Z} - \\frac{M}{Z}$$
- 긴장재가 도심에 배치되었으므로 편심거리 $e = 0$입니다:
  $$\\sigma_{\\text{bot}} = \\frac{P}{A} - \\frac{M}{Z}$$
- 하연 응력이 0이 되기 위한 조건:
  $$\\sigma_{\\text{bot}} = 0 \\implies \\frac{P}{A} = \\frac{M}{Z} \\implies P = \\frac{M \\cdot A}{Z}$$

**단계별 풀이**
1. **외력에 의한 중앙 휨모멘트 $M$ 계산**:
   - 경간 $L = 8\\text{ m}$, 등분포하중 $w = 20\\text{ kN/m}$
   $$M = \\frac{w L^2}{8} = \\frac{20\\text{ kN/m} \\times 8^2\\text{ m}^2}{8} = 160\\text{ kN}\\cdot\\text{m} = 160 \\times 10^6\\text{ N}\\cdot\\text{mm}$$
2. **단면 특성치 계산**:
   - 폭 $b = 250\\text{ mm}$, 높이 $h = 400\\text{ mm}$ (그림 참조)
   $$A = b \\cdot h = 250 \\times 400 = 100,000\\text{ mm}^2$$
   $$Z = \\frac{b h^2}{6} = \\frac{250 \\times 400^2}{6} = \\frac{40,000,000}{6} = \\frac{20}{3} \\times 10^6\\text{ mm}^3$$
3. **프리스트레스 힘 $P$ 계산**:
   $$P = \\frac{M \\cdot A}{Z} = \\frac{160 \\times 10^6\\text{ N}\\cdot\\text{mm} \\times 100,000\\text{ mm}^2}{\\frac{20}{3} \\times 10^6\\text{ mm}^3} = \\frac{16,000,000}{\\frac{20}{3}} = 2,400,000\\text{ N} = 2400\\text{ kN}$$

따라서 정답은 **3**입니다."""
    },
    65: {
        "topic": "연속 휨부재의 모멘트 재분배 규정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 20에 따른 **연속 휨부재의 모멘트 재분배(Moment Redistribution)**:
1. 탄성이론에 의해 산정된 연속 휨부재 받침부의 부모멘트는 최외단 인장철근의 순인장변형률 $\\varepsilon_t \\ge 0.0075$인 경우에 한하여 **$1000\\varepsilon_t \\%$ (최대 20%)만큼 감소**시킬 수 있습니다.
2. 부모멘트를 조정한 경우, 정적 평형조건을 만족하도록 경간 내의 정모멘트를 반드시 수정하여야 합니다.
3. 근사해법(모멘트 계수법 등)에 의해 산정된 모멘트는 재분배할 수 없습니다.

**단계별 풀이**
- ②번 "10% 이내에서 800 εt% 만큼 증가 또는 감소시킬 수 있다"는 설명은 틀렸습니다. 재분배 한도는 **20% 이내**이며, 재분배율 공식은 **$1000\\varepsilon_t \\%$**이고 오직 **감소**시킬 때만 적용됩니다.

따라서 정답은 **2**입니다."""
    },
    66: {
        "topic": "고장력 볼트 복전단 마찰이음 소요 볼트 수 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
고장력 볼트 마찰이음부의 전단내력 및 소요 볼트 수:
- 볼트 1개당 허용 전단내력:
  $$R_v = m \\cdot A_b \\cdot \\tau_a$$
  여기서,
  - $m$: 전단면 수 (복전단이므로 $m = 2$)
  - $A_b$: 볼트 1개의 공칭 단면적 ($A_b = \\frac{\\pi d^2}{4}$)
  - $\\tau_a$: 볼트의 허용전단응력
- 소요 볼트 수:
  $$n = \\frac{P}{R_v}$$

**단계별 풀이**
1. **주어진 조건**:
   - 작용 인장력 $P = 350\\text{ kN} = 350,000\\text{ N}$
   - 볼트 지름 $d = 20\\text{ mm}$
   - 허용전단응력 $\\tau_a = 120\\text{ MPa}$
   - 복전단 ($m = 2$)
2. **볼트 1개의 단면적 $A_b$ 계산**:
   $$A_b = \\frac{\\pi \\times 20^2}{4} = 100\\pi \\approx 314.16\\text{ mm}^2$$
3. **볼트 1개의 허용 전단내력 $R_v$ 계산**:
   $$R_v = 2 \\times 314.16\\text{ mm}^2 \\times 120\\text{ N/mm}^2 = 75,398\\text{ N} \\approx 75.40\\text{ kN}$$
4. **최소 소요 볼트 수 $n$ 계산**:
   $$n = \\frac{350\\text{ kN}}{75.40\\text{ kN}} \\approx 4.64\\text{개} \\implies 5\\text{개}$$

따라서 정답은 **2**입니다."""
    },
    67: {
        "topic": "강구조 리벳 구멍의 지름 규정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
강구조 연결 설계기준(허용응력설계법)에 따른 **구멍의 공칭 치수 규정**:
- **리벳 구멍의 지름**: 리벳의 공칭 지름에 **$1.5\\text{ mm}$**를 가산합니다.
  $$d_{\\text{hole}} = d + 1.5\\text{ mm}$$
- *(참고: 볼트의 경우 일반적으로 볼트 공칭지름이 $16\\text{ mm}$ 이상일 때 $+2.0\\text{ mm}$ 적용)*

**단계별 풀이**
1. **주어진 조건**:
   - 리벳의 지름 $d = 22\\text{ mm}$
2. **리벳 구멍의 지름 계산**:
   $$d_{\\text{hole}} = 22\\text{ mm} + 1.5\\text{ mm} = 23.5\\text{ mm}$$

따라서 정답은 **3**입니다."""
    },
    68: {
        "topic": "고강도 콘크리트의 등가응력블록 깊이계수(β1) 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 20 (2021/2022 개정) 표 4.1-2에 따른 **등가 직사각형 응력블록 계수 $\\beta_1$**:
- $f_{ck} \\le 50\\text{ MPa}$ : $\\beta_1 = 0.80$
- $f_{ck} = 60\\text{ MPa}$ : $\\beta_1 = 0.76$
- $50\\text{ MPa} < f_{ck} < 60\\text{ MPa}$ 사이의 강도는 **직선보간**하여 산정합니다:
  $$\\beta_1 = 0.80 - \\frac{0.80 - 0.76}{60 - 50} \\times (f_{ck} - 50) = 0.80 - 0.004 \\times (f_{ck} - 50)$$

**단계별 풀이**
1. **주어진 강도**:
   - $f_{ck} = 58\\text{ MPa}$
2. **계수 $\\beta_1$ 계산**:
   $$\\beta_1 = 0.80 - 0.004 \\times (58 - 50) = 0.80 - 0.004 \\times 8 = 0.80 - 0.032 = 0.768$$

따라서 정답은 **3**입니다."""
    },
    69: {
        "topic": "인장철근 겹침이음의 규정 및 등급 분류",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 52(철근의 정착 및 이음)에 따른 **인장 겹침이음 규정**:
1. 다발철근의 겹침이음은 다발 내의 개개 철근에 대한 겹침이음길이를 기본으로 결정하며, 겹침이음이 한 군데에 집중되지 않도록 합니다.
2. 어떤 경우이든 인장 겹침이음길이는 **최소 $300\\text{ mm}$ 이상**이어야 합니다.
3. 인장 겹침이음은 **A급 이음($1.0 l_d$)**과 **B급 이음($1.3 l_d$)**으로 분류됩니다.
4. **이음 등급 판정**:
   - 배근량이 소요량의 2배 이상이고, 겹침이음된 철근량이 전체 철근량의 **1/2 이하**이면 **A급 이음**입니다.
   - 위의 조건을 만족하지 못하는 경우는 모두 B급 이음입니다.

**단계별 풀이**
- ④ "겹침이음된 철근량이 전체 철근량의 1/2 이하인 경우는 B급이음이다"는 틀린 설명입니다. 겹침이음량이 1/2 이하이면서 배근량이 소요량의 2배 이상이면 **A급 이음**에 해당합니다.

따라서 정답은 **4**입니다."""
    },
    70: {
        "topic": "습윤환경 노출 보의 표피철근 최대 간격 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 20에 따른 **표피철근(Skin Reinforcement)의 최대 배근 간격($s$)**:
부재 전체 깊이 $h > 900\\text{ mm}$인 휨부재의 복부 양 측면에는 표피철근을 배치해야 하며, 그 간격 $s$는 다음 두 식 중 작은 값 이하이어야 합니다:
1. $s \\le 375 \\left(\\frac{k_{cr}}{f_s}\\right) - 2.5 c_c$
2. $s \\le 300 \\left(\\frac{k_{cr}}{f_s}\\right)$
여기서,
- 사용하중 시 철근 응력: $f_s = \\frac{2}{3} f_y$
- 습윤환경 균열제어계수: $k_{cr} = 210$ (건조환경은 280)
- $c_c$: 표피철근 표면에서 부재 측면까지의 최단 피복두께

**단계별 풀이**
1. **주어진 조건**:
   - $f_y = 400\\text{ MPa} \\implies f_s = \\frac{2}{3} \\times 400 = 266.67\\text{ MPa}$
   - 습윤환경이므로 $k_{cr} = 210$
   - 피복두께 $c_c = 50\\text{ mm}$
2. **식 (1)에 의한 간격 계산**:
   $$s_1 = 375 \\times \\left(\\frac{210}{266.67}\\right) - 2.5(50) = 375 \\times 0.7875 - 125 = 295.31 - 125 = 170.31\\text{ mm}$$
3. **식 (2)에 의한 간격 계산**:
   $$s_2 = 300 \\times \\left(\\frac{210}{266.67}\\right) = 300 \\times 0.7875 = 236.25\\text{ mm}$$
4. **최대 간격 결정**:
   $$s = \\min(s_1, s_2) = 170.31\\text{ mm} \\approx 170\\text{ mm}$$

따라서 정답은 **1**입니다."""
    },
    71: {
        "topic": "경사 맞대기 용접부의 인장응력 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
강구조설계기준에 따른 **맞대기 용접(Groove Weld)**의 인장응력:
- 완전용입 맞대기 용접부는 모재와 동등 이상의 강도를 갖는 용접재를 사용합니다.
- 축선과 $60^\\circ$ 이상 경사진 맞대기 이음부는 이음효율 100%로 보아 모재의 순단면적으로 응력을 산정합니다:
  $$\\sigma = \\frac{P}{A} = \\frac{P}{b \\cdot t}$$

**단계별 풀이**
1. **주어진 조건**:
   - 강판 폭 $b = 400\\text{ mm}$
   - 강판 두께 $t = 10\\text{ mm}$
   - 인장하중 $P = 500\\text{ kN} = 500,000\\text{ N}$
2. **용접부 응력 $\\sigma$ 계산**:
   $$\\sigma = \\frac{500,000\\text{ N}}{400\\text{ mm} \\times 10\\text{ mm}} = \\frac{500,000}{4000} = 125\\text{ MPa}$$

따라서 정답은 **2**입니다."""
    },
    72: {
        "topic": "비구조요소를 지지하는 부재의 최대 허용 처짐",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 30(사용성 설계기준) 표 4.2-1에 따른 **보 및 슬래브의 최대 허용 처짐**:
1. 평지붕 구조로서 비구조요소를 지지·부착하지 않은 경우: $\\ell / 180$
2. 바닥구조로서 비구조요소를 지지·부착하지 않은 경우: $\\ell / 240$
3. **과도한 처짐에 의해 손상되기 쉬운 비구조요소를 지지 또는 부착한 지붕 또는 바닥구조**: **$\\ell / 480$**
4. 과도한 처짐에 의해 손상되기 쉽지 않은 비구조요소를 지지 또는 부착한 지붕 또는 바닥구조: $\\ell / 240$

**단계별 풀이**
- 문제에서 설명한 "과도한 처짐에 의해 손상되기 쉬운 비구조 요소를 지지 또는 부착한 지붕 또는 바닥구조"의 허용 처짐 기준은 **$\\ell / 480$**입니다.

따라서 정답은 **4**입니다."""
    },
    73: {
        "topic": "단철근 직사각형 보의 등가응력블록 깊이(a) 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
휨부재 단면의 인장철근 인장력과 콘크리트 압축력의 평형방정식:
$$C = T \\implies 0.85 f_{ck} b a = A_s f_y$$
등가 직사각형 응력블록의 깊이 $a$:
$$a = \\frac{A_s f_y}{0.85 f_{ck} b}$$

**단계별 풀이**
1. **주어진 조건**:
   - 인장철근량 $A_s = 3400\\text{ mm}^2$
   - $f_y = 300\\text{ MPa}$
   - $f_{ck} = 21\\text{ MPa}$
   - 보 폭 $b = 300\\text{ mm}$
2. **등가사각형 깊이 $a$ 계산**:
   $$a = \\frac{3400\\text{ mm}^2 \\times 300\\text{ MPa}}{0.85 \\times 21\\text{ MPa} \\times 300\\text{ mm}} = \\frac{3400}{0.85 \\times 21} = \\frac{3400}{17.85} \\approx 190.476\\text{ mm} \\approx 190.5\\text{ mm}$$

따라서 정답은 **4**입니다."""
    },
    74: {
        "topic": "단철근 T형보의 설계휨강도(øMn) 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
1. **플랜지 유효폭 $b$ 결정**:
   대칭 T형보 유효폭은 다음 세 값 중 최솟값:
   - $b \\le L/4$
   - $b \\le b_w + 16t_f$
   - $b \\le$ 인접 보와의 중심 간격
2. **단면 거동 판정 (T형보 vs 직사각형보)**:
   - 플랜지 전체가 저항 가능한 압축력: $C_{f\\max} = 0.85 f_{ck} b t_f$
   - 철근의 인장력 $T = A_s f_y > C_{f\\max}$이면 응력블록이 복부까지 내려오는 **T형 단면 거동($a > t_f$)**을 합니다.
3. **T형 단면의 공칭 휨강도 $M_n$ 산정**:
   - 돌출 플랜지 압축력: $C_f = 0.85 f_{ck} (b - b_w) t_f$
   - 돌출 플랜지 저항 모멘트: $M_{nf} = C_f \\left(d - \\frac{t_f}{2}\\right)$
   - 복부 압축력 분담 철근량: $A_{sw} = A_s - A_{sf} = A_s - \\frac{C_f}{f_y}$
   - 복부 응력블록 깊이: $a = \\frac{A_{sw} f_y}{0.85 f_{ck} b_w}$
   - 복부 저항 모멘트: $M_{nw} = A_{sw} f_y \\left(d - \\frac{a}{2}\\right)$
   - 설계휨강도: $\\phi M_n = \\phi (M_{nf} + M_{nw})$

**단계별 풀이**
1. **유효폭 $b$ 산정**:
   - 경간 $L = 3040\\text{ mm}$, $b_w = 360\\text{ mm}$, $t_f = 180\\text{ mm}$, 보 중심간격 $= 360 + 1540 = 1900\\text{ mm}$
   - $L/4 = 3040 / 4 = 760\\text{ mm}$
   - $b_w + 16t_f = 360 + 16(180) = 3240\\text{ mm}$
   - 최솟값이므로 $b = 760\\text{ mm}$
2. **T형 단면 거동 판정**:
   - $T = A_s f_y = 7652\\text{ mm}^2 \\times 350\\text{ MPa} = 2,678,200\\text{ N} = 2678.2\\text{ kN}$
   - $C_{f\\max} = 0.85 \\times 21 \\times 760 \\times 180 = 2,442,420\\text{ N} = 2442.4\\text{ kN}$
   - $T > C_{f\\max}$ 이므로 $a > t_f$ (T형 단면 거동)
3. **돌출 플랜지 및 복부 내력 산정**:
   - 돌출 플랜지 압축력:
     $$C_f = 0.85 \\times 21 \\times (760 - 360) \\times 180 = 1,285,200\\text{ N} = 1285.2\\text{ kN}$$
   - $A_{sf} = \\frac{C_f}{f_y} = \\frac{1,285,200}{350} = 3672\\text{ mm}^2$
   - $A_{sw} = A_s - A_{sf} = 7652 - 3672 = 3980\\text{ mm}^2$
   - 복부 압축력: $C_w = A_{sw} f_y = 3980 \\times 350 = 1,393,000\\text{ N} = 1393.0\\text{ kN}$
   - 복부 응력블록 깊이 $a$:
     $$a = \\frac{1,393,000}{0.85 \\times 21 \\times 360} = \\frac{1,393,000}{6426} \\approx 216.78\\text{ mm}$$
4. **공칭 및 설계휨강도 계산**:
   - $d = 910\\text{ mm}$
   $$M_{nf} = 1285.2\\text{ kN} \\times \\left(910 - \\frac{180}{2}\\right)\\text{ mm} = 1285.2 \\times 820 = 1,053,864\\text{ kN}\\cdot\\text{mm}$$
   $$M_{nw} = 1393.0\\text{ kN} \\times \\left(910 - \\frac{216.78}{2}\\right)\\text{ mm} = 1393.0 \\times 801.61 = 1,116,643\\text{ kN}\\cdot\\text{mm}$$
   $$M_n = 1,053,864 + 1,116,643 = 2,170,507\\text{ kN}\\cdot\\text{mm} \\approx 2170.5\\text{ kN}\\cdot\\text{m}$$
   - $\\phi = 0.85$ (인장지배단면)
   $$\\phi M_n = 0.85 \\times 2170.5\\text{ kN}\\cdot\\text{m} \\approx 1845\\text{ kN}\\cdot\\text{m}$$

따라서 정답은 **1**입니다."""
    },
    75: {
        "topic": "옹벽의 전도에 대한 최소 안전율",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 74(옹벽 설계기준)에 따른 **옹벽의 안정 조건(안전율)**:
1. **전도(Overturning)에 대한 안정**:
   저항 모멘트 $M_r$은 토압에 의한 전도 모멘트 $M_o$의 **최소 2.0배 이상**이어야 합니다:
   $$F_s = \\frac{M_r}{M_o} \\ge 2.0$$
2. **활동(Sliding)에 대한 안정**:
   저항력은 수평토압의 **최소 1.5배 이상**이어야 합니다 ($F_s \\ge 1.5$).
3. **지반 지지력에 대한 안정**:
   지반에 발생하는 최대 압축응력이 지반의 허용지지력 이하여야 합니다 (극한지지력 대비 안전율 $F_s \\ge 3.0$).

**단계별 풀이**
- 옹벽의 전도에 대한 저항휨모멘트는 전도모멘트의 **최소 2.0배 이상**이어야 합니다.

따라서 정답은 **2**입니다."""
    },
    76: {
        "topic": "콘크리트 부재의 비틀림 설계 및 위험단면 위치",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 22(비틀림 설계기준)의 **위험단면(Critical Section) 규정**:
1. **보통 철근콘크리트(RC) 부재**:
   - 받침부 전면에서 **유효깊이 $d$ 이내**에 위치한 단면은 받침부에서 $d$ 거리에 있는 단면과 동일한 계수비틀림모멘트 $T_u$에 대하여 설계할 수 있습니다.
2. **프리스트레스트 콘크리트(PSC) 부재**:
   - 받침부 전면에서 **부재 전체 높이의 절반인 $h/2$ 이내**에 위치한 단면은 받침부에서 **$h/2$ 거리에 있는 단면의 $T_u$**에 대하여 설계할 수 있습니다.
3. 부정정 구조물에서 비틀림 균열 후 내력 재분배가 발생할 수 있는 경우(적합 비틀림)에는 최대 계수비틀림모멘트를 균열 비틀림 모멘트 한도로 감소시킬 수 있습니다.

**단계별 풀이**
- ③ "프리스트레스콘크리트 부재에서, 받침부에서 d 이내에 위치한 단면을 설계할 때 d에서 계산된 Tu보다 작지 않은 비틀림모멘트에 대하여 설계하여야 한다"는 설명은 틀렸습니다. PSC 부재의 위험단면 기준 거리는 $d$가 아니라 **$h/2$**입니다.

따라서 정답은 **3**입니다."""
    },
    77: {
        "topic": "기둥 띠철근의 최대 수직간격 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 50에 따른 **띠철근(Tie Reinforcement) 기둥의 최대 수직배근 간격($s_{\\max}$)**:
다음 세 값 중 **가장 작은 값** 이하로 배근하여야 합니다:
1. 축방향(종방향) 주철근 지름의 **16배**: $16 d_b$
2. 띠철근 지름의 **48배**: $48 d_t$
3. 기둥 단면의 **최소 치수**: $b_{\\min}$

**단계별 풀이**
1. **주어진 조건**:
   - 기둥 단면 치수: $500\\text{ mm} \\times 600\\text{ mm} \\implies b_{\\min} = 500\\text{ mm}$
   - 주철근: D32 (공칭직경 $d_b = 31.8\\text{ mm}$)
   - 띠철근: D10 (공칭직경 $d_t = 9.5\\text{ mm}$)
2. **세 기준값 계산**:
   - (1) $16 d_b = 16 \\times 31.8\\text{ mm} = 508.8\\text{ mm}$
   - (2) $48 d_t = 48 \\times 9.5\\text{ mm} = 456\\text{ mm}$
   - (3) 기둥 최소 치수 $= 500\\text{ mm}$
3. **최대 수직간격 결정**:
   $$s_{\\max} = \\min(508.8, 456, 500) = 456\\text{ mm}$$

따라서 정답은 **1**입니다."""
    },
    78: {
        "topic": "콘크리트 공칭전단강도(Vc) 정밀식 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
KDS 14 20 22에 따른 **전단력과 휨모멘트를 동시에 받는 부재 콘크리트의 공칭 전단강도 정밀식**:
$$V_c = \\left(0.16 \\lambda \\sqrt{f_{ck}} + 17 \\rho_w \\frac{V_u d}{M_u}\\right) b_w d$$
제한 조건:
- $\\frac{V_u d}{M_u} \\le 1.0$
- $V_c \\le 0.29 \\lambda \\sqrt{f_{ck}} b_w d$

**단계별 풀이**
1. **주어진 조건**:
   - $b_w = 350\\text{ mm}$, $d = 600\\text{ mm}$
   - 보통중량 콘크리트 ($\\lambda = 1.0$), $f_{ck} = 24\\text{ MPa}$
   - $\\rho_w = 0.016$
   - $V_u = 100\\text{ kN} = 100 \\times 10^3\\text{ N}$
   - $M_u = 300\\text{ kN}\\cdot\\text{m} = 300 \\times 10^6\\text{ N}\\cdot\\text{mm}$
2. **모멘트 대비 전단 계수 검토**:
   $$\\frac{V_u d}{M_u} = \\frac{(100 \\times 10^3\\text{ N}) \\times 600\\text{ mm}}{300 \\times 10^6\\text{ N}\\cdot\\text{mm}} = \\frac{60 \\times 10^6}{300 \\times 10^6} = 0.20 \\le 1.0\\;(\\text{적합})$$
3. **괄호 안 단위응력 계산**:
   - $0.16 \\sqrt{24} \\approx 0.16 \\times 4.89898 = 0.78384\\text{ MPa}$
   - $17 \\rho_w \\left(\\frac{V_u d}{M_u}\\right) = 17 \\times 0.016 \\times 0.20 = 0.0544\\text{ MPa}$
   - 단위응력 합계 $= 0.78384 + 0.0544 = 0.83824\\text{ MPa}$
   - 상한치 검토: $0.29 \\sqrt{24} \\approx 1.42\\text{ MPa} > 0.838\\text{ MPa}$ (적합)
4. **공칭전단강도 $V_c$ 계산**:
   $$V_c = 0.83824\\text{ N/mm}^2 \\times (350\\text{ mm} \\times 600\\text{ mm}) = 0.83824 \\times 210,000 = 176,030\\text{ N} \\approx 176.4\\text{ kN}$$

따라서 정답은 **3**입니다."""
    },
    79: {
        "topic": "복철근보의 지속하중에 의한 추가 장기처짐 산정",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
복철근 콘크리트 보의 지속하중에 의한 추가 장기처짐 공식:
$$\\Delta_{lt} = \\lambda_\\Delta \\cdot \\Delta_i$$
장기처짐 증폭계수:
$$\\lambda_\\Delta = \\frac{\\xi}{1 + 50\\rho'}$$
- $\\xi$: 5년 이상 지속하중 재하 시 시간경과계수 $\\xi = 2.0$
- $\\rho'$: 압축철근비 ($\\rho' = \\frac{A_s'}{b d}$)
- $\\Delta_i$: 탄성 순간처짐

**단계별 풀이**
1. **압축철근비 $\\rho'$ 계산**:
   - $A_s' = 1200\\text{ mm}^2$, $b = 200\\text{ mm}$, $d = 300\\text{ mm}$ (그림 참조)
   $$\\rho' = \\frac{1200}{200 \\times 300} = \\frac{1200}{60,000} = 0.02$$
2. **증폭계수 $\\lambda_\\Delta$ 계산**:
   $$\\lambda_\\Delta = \\frac{2.0}{1 + 50(0.02)} = \\frac{2.0}{1 + 1.0} = \\frac{2.0}{2.0} = 1.0$$
3. **추가 장기처짐 계산**:
   - 탄성처짐 $\\Delta_i = 12\\text{ mm}$
   $$\\Delta_{lt} = \\lambda_\\Delta \\times \\Delta_i = 1.0 \\times 12\\text{ mm} = 12\\text{ mm}$$

따라서 정답은 **2**입니다."""
    },
    80: {
        "topic": "2경간 연속 PSC 보의 마찰 손실률 산정 (근사법)",
        "choices": None,
        "explanation": """**핵심 개념 / 공식**
포스트텐션 PSC 긴장재의 마찰에 의한 프리스트레스 손실률 근사식:
$$\\frac{\\Delta P}{P_0} = \\mu \\alpha + k x$$
여기서,
- $\\mu$: 곡률마찰계수
- $\\alpha$: 긴장단(A)에서 검토 단면(B)까지의 총 각도 변화량 ($\\text{radian}$)
- $k$: 파상마찰계수
- $x$: 긴장단에서 검토 단면까지의 긴장재 길이 ($x = 20\\text{ m}$)

**단계별 풀이**
1. **주어진 조건**:
   - $\\mu = 0.4$, $k = 0.0027\\text{ m}^{-1}$
   - $x = 20\\text{ m}$
   - A단에서 중간 B단까지의 각도 변화량 $\\alpha$:
     변곡점/처짐 접선각 $0.16\\text{ rad}$ 및 B점 피크 접선각 $0.10\\text{ rad}$의 합:
     $$\\alpha = 0.16 + 0.10 = 0.26\\text{ rad}$$
2. **마찰에 의한 손실률 계산**:
   - 곡률 마찰 손실: $\\mu \\alpha = 0.4 \\times 0.26 = 0.104 = 10.4\\%$
   - 파상 마찰 손실: $k x = 0.0027 \\times 20 = 0.054 = 5.4\\%$
   - 총 마찰 손실률:
     $$\\frac{\\Delta P}{P_0} = 0.104 + 0.054 = 0.158 = 15.8\\%$$

따라서 정답은 **4**입니다."""
    }
}

# Update questions
questions_out = []
for q in raw_data['questions']:
    qnum = q['qnum']
    if qnum in data_2020_12:
        info = data_2020_12[qnum]
        q_new = dict(q)
        q_new['topic'] = info['topic']
        if info['choices'] is not None:
            q_new['choices'] = info['choices']
        q_new['explanation'] = info['explanation']
        questions_out.append(q_new)
    else:
        print(f"Warning: Q{qnum} missing in data_2020_12")

out_json = {
    "session": raw_data['session'],
    "questions": questions_out
}

os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out_json, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions_out)} questions to {out_path}")
