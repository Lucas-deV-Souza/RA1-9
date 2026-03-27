.data
RES_1: .double 0.0
NUM_7_0: .double 7.0
NUM_2_0: .double 2.0
RES_2: .double 0.0
NUM_15_0: .double 15.0
NUM_3_0: .double 3.0
RES_3: .double 0.0
NUM_100_0: .double 100.0
VALOR: .double 0.0
RES_4: .double 0.0
NUM_10_0: .double 10.0
RES_5: .double 0.0
NUM_5_0: .double 5.0
RES_6: .double 0.0
RES_7: .double 0.0
NUM_8_0: .double 8.0
RES_8: .double 0.0
NUM_9: .double 9
NUM_3: .double 3
RES_9: .double 0.0
RESULTADO: .double 0.0
RES_10: .double 0.0
NUM_15: .double 15
NUM_5: .double 5

.text
.global _start
_start:
    LDR SP, =0x20000

// --- Linha 1 ---
    LDR R0, =NUM_7_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_2_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RES_1
    VSTR D0, [R0]

// --- Linha 2 ---
    LDR R0, =NUM_15_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_3_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_2_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RES_2
    VSTR D0, [R0]

// --- Linha 3 ---
    LDR R0, =NUM_100_0
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =VALOR
    VSTR D0, [R0]
    VLDR D0, [SP]
    LDR R0, =RES_3
    VSTR D0, [R0]

// --- Linha 4 ---
    LDR R0, =VALOR
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_10_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VDIV.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_4
    VSTR D0, [R0]

// --- Linha 5 ---
    LDR R0, =RES_3
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_5_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VADD.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_5
    VSTR D0, [R0]

// --- Linha 6 ---
    LDR R0, =VALOR
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =RES_4
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VMUL.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_6
    VSTR D0, [R0]

// --- Linha 7 ---
    LDR R0, =NUM_8_0
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_2_0
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VSUB.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_7
    VSTR D0, [R0]

// --- Linha 8 ---
    LDR R0, =NUM_9
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_3
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VADD.F64 D2, D1, D0
    VPUSH {D2}
    VLDR D0, [SP]
    LDR R0, =RES_8
    VSTR D0, [R0]

// --- Linha 9 ---
    LDR R0, =RES_8
    VLDR D0, [R0]
    VPUSH {D0}
    VLDR D0, [SP]
    LDR R0, =RESULTADO
    VSTR D0, [R0]
    VLDR D0, [SP]
    LDR R0, =RES_9
    VSTR D0, [R0]

// --- Linha 10 ---
    LDR R0, =NUM_15
    VLDR D0, [R0]
    VPUSH {D0}
    LDR R0, =NUM_5
    VLDR D0, [R0]
    VPUSH {D0}
    VPOP {D0}
    VPOP {D1}
    VMUL.F64 D2, D1, D0
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
