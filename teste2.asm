.data
RES_1: .double 0.0
NUM_10_0: .double 10.0
NUM_5_0: .double 5.0
NUM_2_0: .double 2.0
RES_2: .double 0.0
A: .double 0.0
RES_3: .double 0.0
NUM_3_0: .double 3.0
B: .double 0.0
RES_4: .double 0.0
RES_5: .double 0.0
NUM_100_0: .double 100.0
RES_6: .double 0.0
RES_7: .double 0.0
RES_8: .double 0.0
NUM_50_0: .double 50.0
RES_9: .double 0.0
NUM_3_14: .double 3.14
PI: .double 0.0
RES_10: .double 0.0
NUM_20: .double 20
NUM_10: .double 10

.text
.global _start
_start:
    LDR SP, =0x20000

// --- Linha 1 ---
    LDR R0, =NUM_10_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_5_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VADD.F64 D2, D1, D0
    VPUSH {D2}
    LDR R0, =NUM_2_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VMUL.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_1
    VSTR D0, [R0]

// --- Linha 2 ---
    LDR R0, =NUM_5_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =A
    VSTR D0, [R0]
    VLDR D0, [SP]
    LDR R0, =RES_2
    VSTR D0, [R0]

// --- Linha 3 ---
    LDR R0, =NUM_3_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =B
    VSTR D0, [R0]
    VLDR D0, [SP]
    LDR R0, =RES_3
    VSTR D0, [R0]

// --- Linha 4 ---
    LDR R0, =A
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =B
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RES_4
    VSTR D0, [R0]

// --- Linha 5 ---
    LDR R0, =NUM_100_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_3_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RES_5
    VSTR D0, [R0]

// --- Linha 6 ---
    LDR R0, =NUM_100_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_3_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RES_6
    VSTR D0, [R0]

// --- Linha 7 ---
    LDR R0, =RES_3
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =A
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VADD.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_7
    VSTR D0, [R0]

// --- Linha 8 ---
    LDR R0, =NUM_50_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_2_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VDIV.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_8
    VSTR D0, [R0]

// --- Linha 9 ---
    LDR R0, =NUM_3_14
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =PI
    VSTR D0, [R0]
    VLDR D0, [SP]
    LDR R0, =RES_9
    VSTR D0, [R0]

// --- Linha 10 ---
    LDR R0, =NUM_20
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_10
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VADD.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_10
    VSTR D0, [R0]

// --- MOSTRANDO NOS LEDS (CPulator) ---
    VLDR D0, [SP]
    VCVT.S32.F64 S0, D0
    VMOV R0, S0
    LDR R1, =0xFF200000
    STR R0, [R1]
FIM: B FIM
