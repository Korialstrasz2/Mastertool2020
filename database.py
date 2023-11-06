import sqlite3


connection = sqlite3.connect("databasegioco.db")
cursor = connection.cursor()
def crea_gioco():
    crea_personaggio = """CREATE TABLE IF NOT EXISTS
        personaggitry(nomepg TEXT,
livello INTEGER,
sesso TEXT,
razza TEXT,
eta INTEGER,
stanchezza INTEGER,
modificatore_generale INTEGER,
forza_base INTEGER,
forza_bonus_extra INTEGER,
resistenza_base INTEGER,
resistenza_bonus_extra INTEGER,
velocita_base INTEGER,
velocita_bonus_extra INTEGER,
agilita_base INTEGER,
agilita_bonus_extra INTEGER,
intelligenza_base INTEGER,
intelligenza_bonus_extra INTEGER,
concentrazione_base INTEGER,
concentrazione_bonus_extra INTEGER,
personalita_base INTEGER,
personalita_bonus_extra INTEGER,
fortuna_base INTEGER,
fortuna_bonus_extra INTEGER,
pf_item INTEGER,
pf_extra INTEGER,
mana_item INTEGER,
mana_extra INTEGER,
energia_item INTEGER,
energia_extra INTEGER,
energia_limite_item INTEGER,
energia_limite_extra INTEGER,
pa_item INTEGER,
pa_extra INTEGER,
attacco_arma INTEGER,
attacco_item INTEGER,
attacco_extra INTEGER,

difesa_armatura INTEGER,
difesa_item INTEGER,
difesa_extra INTEGER,
difesa_temp INTEGER,
volonta_item INTEGER,
volonta_extra INTEGER,
potere_item INTEGER,
potere_extra INTEGER,
barr_fis_item INTEGER,
barr_fis_extra INTEGER,
barr_mag_item INTEGER,
barr_mag_extra INTEGER,
rd_fis INTEGER,
res_fis INTEGER,
res_mag INTEGER,
rd_fuoco INTEGER,
rd_gelo INTEGER,
rd_elettro INTEGER,
compri_a_meno_extra INTEGER,
vendi_a_piu_extra INTEGER,
equip_anello_1 TEXT,
equip_anello_2 TEXT,
equip_anello_3 TEXT,
equip_anello_4 TEXT,
equip_anello_5 TEXT,
equip_anello_6 TEXT,
equip_anello_7 TEXT,
equip_anello_8 TEXT,
equip_anello_9 TEXT,
equip_anello_10 TEXT,
equip_orecchino_1 TEXT,
equip_orecchino_2 TEXT,
equip_orecchino_3 TEXT,
equip_orecchino_4 TEXT,
equip_orecchino_5 TEXT,
equip_orecchino_6 TEXT,
equip_spilla TEXT,
equip_fascia TEXT,
equip_mantello TEXT,
equip_amuleto TEXT,
equip_cintura TEXT,
zaino_slot_1 TEXT,
zaino_slot_2 TEXT,
zaino_slot_3 TEXT,
zaino_slot_4 TEXT,
zaino_slot_5 TEXT,
zaino_slot_6 TEXT,
zaino_slot_7 TEXT,
zaino_slot_8 TEXT,
zaino_slot_9 TEXT,
zaino_slot_10 TEXT,
zaino_slot_11 TEXT,
zaino_slot_12 TEXT,
zaino_slot_13 TEXT,
zaino_slot_14 TEXT,
zaino_slot_15 TEXT,
zaino_slot_16 TEXT,
zaino_slot_17 TEXT,
zaino_slot_18 TEXT,
zaino_slot_19 TEXT,
zaino_slot_20 TEXT,
arma_1 TEXT,
arma_2 TEXT,
armatura TEXT,
scudo TEXT,
oggetto_difensivo_1 TEXT,
oggetto_difensivo_2 TEXT,
oggetto_difensivo_3 TEXT,
oggetto_difensivo_4 TEXT,
magia_1 TEXT,
magia_2 TEXT,
magia_3 TEXT,
magia_4 TEXT,
magia_5 TEXT,
magia_6 TEXT,
magia_7 TEXT,
magia_8 TEXT,
magia_9 TEXT,
magia_10 TEXT,
magia_11 TEXT,
magia_12 TEXT,
magia_13 TEXT,
magia_14 TEXT,
magia_15 TEXT,
magia_16 TEXT,
magia_17 TEXT,
magia_18 TEXT,
magia_19 TEXT,
magia_20 TEXT,
en_per_mana_ordine INTEGER,
en_per_mana_caos INTEGER,
pa_per_mana_ordine INTEGER,
pa_per_mana_caos INTEGER,
sconto_mana_per_potere INTEGER,
sconto_pa_per_potere INTEGER,
monete INTEGER,
relazioni_skaal INTEGER,
relazioni_imperiali INTEGER,
relazioni_raven_rock INTEGER,
relazioni_east_emp_comp INTEGER,
relazioni_riekling INTEGER,
relazioni_miraak INTEGER,
relazioni_minatori INTEGER,
relazioni_elfi_oscuri INTEGER,
punti_exp_rossi INTEGER,
punti_exp_spesi_rossi INTEGER,
punti_exp_blu INTEGER,
punti_exp_spesi_blu INTEGER,
punti_exp_verdi INTEGER,
punti_exp_spesi_verdi INTEGER,
punti_exp_extra INTEGER,
punti_exp_spesi_extra INTEGER,
punti_abilita INTEGER,
punti_abilita_spesi INTEGER,
skill_igegneria TEXT,
skill_conoscenze_naturaegeografia TEXT,
skill_conoscenze_religioni TEXT,
skill_conoscenze_storiaenobilta TEXT,
skill_cammuffare TEXT,
skill_furtivita TEXT,
skill_intimidire TEXT,
skill_strategia_militare TEXT,
skill_sopravvivenza TEXT,
skill_intuizione TEXT,
skill_diplomazia TEXT,
skill_sapienza_magica TEXT,
skill_percezione TEXT,
skill_raggirare TEXT,
skill_gestione_risorse TEXT,
note1 TEXT,
note2 TEXT,
note3 TEXT,
note4 TEXT,
alchimia_note_1 TEXT,
alchimia_note_2 TEXT,
alchimia_note_3 TEXT,
alchimia_ingredienti_rossi_1 INTEGER,
alchimia_ingredienti_rossi_2 INTEGER,
alchimia_ingredienti_rossi_3 INTEGER,
alchimia_ingredienti_rossi_4 INTEGER,
alchimia_ingredienti_verdi_1 INTEGER,
alchimia_ingredienti_verdi_2 INTEGER,
alchimia_ingredienti_verdi_3 INTEGER,
alchimia_ingredienti_verdi_4 INTEGER,
alchimia_ingredienti_blu_1 INTEGER,
alchimia_ingredienti_blu_2 INTEGER,
alchimia_ingredienti_blu_3 INTEGER,
alchimia_ingredienti_blu_4 INTEGER,
alchimia_effetto_ingredienti_1 INTEGER,
alchimia_effetto_ingredienti_2 INTEGER,
alchimia_effetto_ingredienti_3 INTEGER,
alchimia_effetto_ingredienti_4 INTEGER,
alchimia_moltiplicatore_rossi INTEGER,
alchimia_moltiplicatore_verdi INTEGER,
alchimia_moltiplicatore_blu INTEGER,
magia_1_nome TEXT,
magia_1_formula TEXT,
magia_2_nome TEXT,
magia_2_formula TEXT,
magia_3_nome TEXT,
magia_3_formula TEXT,
magia_4_nome TEXT,
magia_4_formula TEXT,
magia_5_nome TEXT,
magia_5_formula TEXT,
magia_6_nome TEXT,
magia_6_formula TEXT,
magia_7_nome TEXT,
magia_7_formula TEXT,
magia_8_nome TEXT,
magia_8_formula TEXT,
magia_9_nome TEXT,
magia_9_formula TEXT,
magia_10_nome TEXT,
magia_10_formula TEXT,
magia_11_nome TEXT,
magia_11_formula TEXT,
magia_12_nome TEXT,
magia_12_formula TEXT,
magia_13_nome TEXT,
magia_13_formula TEXT,
magia_14_nome TEXT,
magia_14_formula TEXT,
magia_15_nome TEXT,
magia_15_formula TEXT,
magia_16_nome TEXT,
magia_16_formula TEXT,
magia_17_nome TEXT,
magia_17_formula TEXT,
magia_18_nome TEXT,
magia_18_formula TEXT,
magia_19_nome TEXT,
magia_19_formula TEXT,
magia_20_nome TEXT,
magia_20_formula TEXT,
attacco_arma_1 INTEGER,
attacco_arma_2 INTEGER,
pa_arma_1 INTEGER,
pa_arma_2 INTEGER,
note_arma_1 TEXT,
note_arma_2 TEXT,
dado_arma_1 TEXT,
dado_arma_2 TEXT,
tipo_arma_1 TEXT,
tipo_arma_2 TEXT,
buca_rd_arma_1 TEXT,
buca_rd_arma_2 TEXT,
bonus_danno_arma_1 INTEGER,
bonus_danno_arma_2 INTEGER,
crit_min_arma_1 TEXT,
crit_nor_arma_1 TEXT,
crit_mag_arma_1 TEXT,
crit_min_arma_2 TEXT,
crit_nor_arma_2 TEXT,
crit_mag_arma_2 TEXT,
slot_zaino_magici INTEGER,
slot_zaino_non_magici INTEGER,
note_armatura TEXT,
pe_rossi_sessione_1 INTEGER,
pe_rossi_sessione_2 INTEGER,
pe_rossi_sessione_3 INTEGER,
pe_rossi_sessione_4 INTEGER,
pe_rossi_sessione_5 INTEGER,
pe_rossi_sessione_6 INTEGER,
pe_rossi_sessione_7 INTEGER,
pe_rossi_sessione_8 INTEGER,
pe_rossi_sessione_9 INTEGER,
pe_rossi_sessione_10 INTEGER,
pe_rossi_sessione_11 INTEGER,
pe_rossi_sessione_12 INTEGER,
pe_rossi_sessione_13 INTEGER,
pe_rossi_sessione_14 INTEGER,
pe_rossi_sessione_15 INTEGER,
pe_rossi_sessione_16 INTEGER,
pe_rossi_sessione_17 INTEGER,
pe_rossi_sessione_18 INTEGER,
pe_rossi_sessione_19 INTEGER,
pe_rossi_sessione_20 INTEGER,
pe_rossi_sessione_21 INTEGER,
pe_rossi_sessione_22 INTEGER,
pe_rossi_sessione_23 INTEGER,
pe_rossi_sessione_24 INTEGER,
pe_rossi_sessione_25 INTEGER,
pe_rossi_sessione_26 INTEGER,
pe_rossi_sessione_27 INTEGER,
pe_rossi_sessione_28 INTEGER,
pe_rossi_sessione_29 INTEGER,
pe_rossi_sessione_30 INTEGER,
pe_rossi_sessione_31 INTEGER,
pe_rossi_sessione_32 INTEGER,
pe_rossi_sessione_33 INTEGER,
pe_rossi_sessione_34 INTEGER,
pe_rossi_sessione_35 INTEGER,
pe_rossi_sessione_36 INTEGER,
pe_rossi_sessione_37 INTEGER,
pe_rossi_sessione_38 INTEGER,
pe_rossi_sessione_39 INTEGER,
pe_rossi_sessione_40 INTEGER,
pe_verdi_sessione_1 INTEGER,
pe_verdi_sessione_2 INTEGER,
pe_verdi_sessione_3 INTEGER,
pe_verdi_sessione_4 INTEGER,
pe_verdi_sessione_5 INTEGER,
pe_verdi_sessione_6 INTEGER,
pe_verdi_sessione_7 INTEGER,
pe_verdi_sessione_8 INTEGER,
pe_verdi_sessione_9 INTEGER,
pe_verdi_sessione_10 INTEGER,
pe_verdi_sessione_11 INTEGER,
pe_verdi_sessione_12 INTEGER,
pe_verdi_sessione_13 INTEGER,
pe_verdi_sessione_14 INTEGER,
pe_verdi_sessione_15 INTEGER,
pe_verdi_sessione_16 INTEGER,
pe_verdi_sessione_17 INTEGER,
pe_verdi_sessione_18 INTEGER,
pe_verdi_sessione_19 INTEGER,
pe_verdi_sessione_20 INTEGER,
pe_verdi_sessione_21 INTEGER,
pe_verdi_sessione_22 INTEGER,
pe_verdi_sessione_23 INTEGER,
pe_verdi_sessione_24 INTEGER,
pe_verdi_sessione_25 INTEGER,
pe_verdi_sessione_26 INTEGER,
pe_verdi_sessione_27 INTEGER,
pe_verdi_sessione_28 INTEGER,
pe_verdi_sessione_29 INTEGER,
pe_verdi_sessione_30 INTEGER,
pe_verdi_sessione_31 INTEGER,
pe_verdi_sessione_32 INTEGER,
pe_verdi_sessione_33 INTEGER,
pe_verdi_sessione_34 INTEGER,
pe_verdi_sessione_35 INTEGER,
pe_verdi_sessione_36 INTEGER,
pe_verdi_sessione_37 INTEGER,
pe_verdi_sessione_38 INTEGER,
pe_verdi_sessione_39 INTEGER,
pe_verdi_sessione_40 INTEGER,
pe_blu_sessione_1 INTEGER,
pe_blu_sessione_2 INTEGER,
pe_blu_sessione_3 INTEGER,
pe_blu_sessione_4 INTEGER,
pe_blu_sessione_5 INTEGER,
pe_blu_sessione_6 INTEGER,
pe_blu_sessione_7 INTEGER,
pe_blu_sessione_8 INTEGER,
pe_blu_sessione_9 INTEGER,
pe_blu_sessione_10 INTEGER,
pe_blu_sessione_11 INTEGER,
pe_blu_sessione_12 INTEGER,
pe_blu_sessione_13 INTEGER,
pe_blu_sessione_14 INTEGER,
pe_blu_sessione_15 INTEGER,
pe_blu_sessione_16 INTEGER,
pe_blu_sessione_17 INTEGER,
pe_blu_sessione_18 INTEGER,
pe_blu_sessione_19 INTEGER,
pe_blu_sessione_20 INTEGER,
pe_blu_sessione_21 INTEGER,
pe_blu_sessione_22 INTEGER,
pe_blu_sessione_23 INTEGER,
pe_blu_sessione_24 INTEGER,
pe_blu_sessione_25 INTEGER,
pe_blu_sessione_26 INTEGER,
pe_blu_sessione_27 INTEGER,
pe_blu_sessione_28 INTEGER,
pe_blu_sessione_29 INTEGER,
pe_blu_sessione_30 INTEGER,
pe_blu_sessione_31 INTEGER,
pe_blu_sessione_32 INTEGER,
pe_blu_sessione_33 INTEGER,
pe_blu_sessione_34 INTEGER,
pe_blu_sessione_35 INTEGER,
pe_blu_sessione_36 INTEGER,
pe_blu_sessione_37 INTEGER,
pe_blu_sessione_38 INTEGER,
pe_blu_sessione_39 INTEGER,
pe_blu_sessione_40 INTEGER,
pe_extra_sessione_1 INTEGER,
pe_extra_sessione_2 INTEGER,
pe_extra_sessione_3 INTEGER,
pe_extra_sessione_4 INTEGER,
pe_extra_sessione_5 INTEGER,
pe_extra_sessione_6 INTEGER,
pe_extra_sessione_7 INTEGER,
pe_extra_sessione_8 INTEGER,
pe_extra_sessione_9 INTEGER,
pe_extra_sessione_10 INTEGER,
pe_extra_sessione_11 INTEGER,
pe_extra_sessione_12 INTEGER,
pe_extra_sessione_13 INTEGER,
pe_extra_sessione_14 INTEGER,
pe_extra_sessione_15 INTEGER,
pe_extra_sessione_16 INTEGER,
pe_extra_sessione_17 INTEGER,
pe_extra_sessione_18 INTEGER,
pe_extra_sessione_19 INTEGER,
pe_extra_sessione_20 INTEGER,
pe_extra_sessione_21 INTEGER,
pe_extra_sessione_22 INTEGER,
pe_extra_sessione_23 INTEGER,
pe_extra_sessione_24 INTEGER,
pe_extra_sessione_25 INTEGER,
pe_extra_sessione_26 INTEGER,
pe_extra_sessione_27 INTEGER,
pe_extra_sessione_28 INTEGER,
pe_extra_sessione_29 INTEGER,
pe_extra_sessione_30 INTEGER,
pe_extra_sessione_31 INTEGER,
pe_extra_sessione_32 INTEGER,
pe_extra_sessione_33 INTEGER,
pe_extra_sessione_34 INTEGER,
pe_extra_sessione_35 INTEGER,
pe_extra_sessione_36 INTEGER,
pe_extra_sessione_37 INTEGER,
pe_extra_sessione_38 INTEGER,
pe_extra_sessione_39 INTEGER,
pe_extra_sessione_40 INTEGER,
pe_skill_sessione_1 INTEGER,
pe_skill_sessione_2 INTEGER,
pe_skill_sessione_3 INTEGER,
pe_skill_sessione_4 INTEGER,
pe_skill_sessione_5 INTEGER,
pe_skill_sessione_6 INTEGER,
pe_skill_sessione_7 INTEGER,
pe_skill_sessione_8 INTEGER,
pe_skill_sessione_9 INTEGER,
pe_skill_sessione_10 INTEGER,
pe_skill_sessione_11 INTEGER,
pe_skill_sessione_12 INTEGER,
pe_skill_sessione_13 INTEGER,
pe_skill_sessione_14 INTEGER,
pe_skill_sessione_15 INTEGER,
pe_skill_sessione_16 INTEGER,
pe_skill_sessione_17 INTEGER,
pe_skill_sessione_18 INTEGER,
pe_skill_sessione_19 INTEGER,
pe_skill_sessione_20 INTEGER,
pe_skill_sessione_21 INTEGER,
pe_skill_sessione_22 INTEGER,
pe_skill_sessione_23 INTEGER,
pe_skill_sessione_24 INTEGER,
pe_skill_sessione_25 INTEGER,
pe_skill_sessione_26 INTEGER,
pe_skill_sessione_27 INTEGER,
pe_skill_sessione_28 INTEGER,
pe_skill_sessione_29 INTEGER,
pe_skill_sessione_30 INTEGER,
pe_skill_sessione_31 INTEGER,
pe_skill_sessione_32 INTEGER,
pe_skill_sessione_33 INTEGER,
pe_skill_sessione_34 INTEGER,
pe_skill_sessione_35 INTEGER,
pe_skill_sessione_36 INTEGER,
pe_skill_sessione_37 INTEGER,
pe_skill_sessione_38 INTEGER,
pe_skill_sessione_39 INTEGER,
pe_skill_sessione_40 INTEGER,
nome_skill_1_pg TEXT,
en_skill_1_pg TEXT,
pa_skill_1_pg TEXT,
atk_skill_1_pg TEXT,
def_skill_1_pg TEXT,
nome_skill_2_pg TEXT,
en_skill_2_pg TEXT,
pa_skill_2_pg TEXT,
atk_skill_2_pg TEXT,
def_skill_2_pg TEXT,
nome_skill_3_pg TEXT,
en_skill_3_pg TEXT,
pa_skill_3_pg TEXT,
atk_skill_3_pg TEXT,
def_skill_3_pg TEXT,
nome_skill_4_pg TEXT,
en_skill_4_pg TEXT,
pa_skill_4_pg TEXT,
atk_skill_4_pg TEXT,
def_skill_4_pg TEXT,
nome_skill_5_pg TEXT,
en_skill_5_pg TEXT,
pa_skill_5_pg TEXT,
atk_skill_5_pg TEXT,
def_skill_5_pg TEXT,
nome_skill_6_pg TEXT,
en_skill_6_pg TEXT,
pa_skill_6_pg TEXT,
atk_skill_6_pg TEXT,
def_skill_6_pg TEXT,
nome_skill_7_pg TEXT,
en_skill_7_pg TEXT,
pa_skill_7_pg TEXT,
atk_skill_7_pg TEXT,
def_skill_7_pg TEXT,
nome_skill_8_pg TEXT,
en_skill_8_pg TEXT,
pa_skill_8_pg TEXT,
atk_skill_8_pg TEXT,
def_skill_8_pg TEXT,
nome_skill_9_pg TEXT,
en_skill_9_pg TEXT,
pa_skill_9_pg TEXT,
atk_skill_9_pg TEXT,
def_skill_9_pg TEXT,
nome_skill_10_pg TEXT,
en_skill_10_pg TEXT,
pa_skill_10_pg TEXT,
atk_skill_10_pg TEXT,
def_skill_10_pg TEXT,
nome_skill_11_pg TEXT,
en_skill_11_pg TEXT,
pa_skill_11_pg TEXT,
atk_skill_11_pg TEXT,
def_skill_11_pg TEXT,
nome_skill_12_pg TEXT,
en_skill_12_pg TEXT,
pa_skill_12_pg TEXT,
atk_skill_12_pg TEXT,
def_skill_12_pg TEXT,
nome_skill_13_pg TEXT,
en_skill_13_pg TEXT,
pa_skill_13_pg TEXT,
atk_skill_13_pg TEXT,
def_skill_13_pg TEXT,
nome_skill_14_pg TEXT,
en_skill_14_pg TEXT,
pa_skill_14_pg TEXT,
atk_skill_14_pg TEXT,
def_skill_14_pg TEXT,
nome_skill_15_pg TEXT,
en_skill_15_pg TEXT,
pa_skill_15_pg TEXT,
atk_skill_15_pg TEXT,
def_skill_15_pg TEXT,
nome_skill_16_pg TEXT,
en_skill_16_pg TEXT,
pa_skill_16_pg TEXT,
atk_skill_16_pg TEXT,
def_skill_16_pg TEXT,
nome_skill_17_pg TEXT,
en_skill_17_pg TEXT,
pa_skill_17_pg TEXT,
atk_skill_17_pg TEXT,
def_skill_17_pg TEXT,
nome_skill_18_pg TEXT,
en_skill_18_pg TEXT,
pa_skill_18_pg TEXT,
atk_skill_18_pg TEXT,
def_skill_18_pg TEXT,
nome_skill_19_pg TEXT,
en_skill_19_pg TEXT,
pa_skill_19_pg TEXT,
atk_skill_19_pg TEXT,
def_skill_19_pg TEXT,
nome_skill_20_pg TEXT,
en_skill_20_pg TEXT,
pa_skill_20_pg TEXT,
atk_skill_20_pg TEXT,
def_skill_20_pg TEXT,
nome_skill_21_pg TEXT,
en_skill_21_pg TEXT,
pa_skill_21_pg TEXT,
atk_skill_21_pg TEXT,
def_skill_21_pg TEXT,
nome_skill_22_pg TEXT,
en_skill_22_pg TEXT,
pa_skill_22_pg TEXT,
atk_skill_22_pg TEXT,
def_skill_22_pg TEXT,
nome_skill_23_pg TEXT,
en_skill_23_pg TEXT,
pa_skill_23_pg TEXT,
atk_skill_23_pg TEXT,
def_skill_23_pg TEXT,
nome_skill_24_pg TEXT,
en_skill_24_pg TEXT,
pa_skill_24_pg TEXT,
atk_skill_24_pg TEXT,
def_skill_24_pg TEXT,
nome_skill_25_pg TEXT,
en_skill_25_pg TEXT,
pa_skill_25_pg TEXT,
atk_skill_25_pg TEXT,
def_skill_25_pg TEXT,
nome_skill_26_pg TEXT,
en_skill_26_pg TEXT,
pa_skill_26_pg TEXT,
atk_skill_26_pg TEXT,
def_skill_26_pg TEXT,
nome_skill_27_pg TEXT,
en_skill_27_pg TEXT,
pa_skill_27_pg TEXT,
atk_skill_27_pg TEXT,
def_skill_27_pg TEXT,
nome_skill_28_pg TEXT,
en_skill_28_pg TEXT,
pa_skill_28_pg TEXT,
atk_skill_28_pg TEXT,
def_skill_28_pg TEXT,
nome_skill_29_pg TEXT,
en_skill_29_pg TEXT,
pa_skill_29_pg TEXT,
atk_skill_29_pg TEXT,
def_skill_29_pg TEXT,
nome_skill_30_pg TEXT,
en_skill_30_pg TEXT,
pa_skill_30_pg TEXT,
atk_skill_30_pg TEXT,
def_skill_30_pg TEXT,
nome_skill_31_pg TEXT,
en_skill_31_pg TEXT,
pa_skill_31_pg TEXT,
atk_skill_31_pg TEXT,
def_skill_31_pg TEXT,
nome_skill_32_pg TEXT,
en_skill_32_pg TEXT,
pa_skill_32_pg TEXT,
atk_skill_32_pg TEXT,
def_skill_32_pg TEXT,
nome_skill_33_pg TEXT,
en_skill_33_pg TEXT,
pa_skill_33_pg TEXT,
atk_skill_33_pg TEXT,
def_skill_33_pg TEXT,
nome_skill_34_pg TEXT,
en_skill_34_pg TEXT,
pa_skill_34_pg TEXT,
atk_skill_34_pg TEXT,
def_skill_34_pg TEXT,
nome_skill_35_pg TEXT,
en_skill_35_pg TEXT,
pa_skill_35_pg TEXT,
atk_skill_35_pg TEXT,
def_skill_35_pg TEXT,
nome_skill_36_pg TEXT,
en_skill_36_pg TEXT,
pa_skill_36_pg TEXT,
atk_skill_36_pg TEXT,
def_skill_36_pg TEXT,
nome_skill_37_pg TEXT,
en_skill_37_pg TEXT,
pa_skill_37_pg TEXT,
atk_skill_37_pg TEXT,
def_skill_37_pg TEXT,
nome_skill_38_pg TEXT,
en_skill_38_pg TEXT,
pa_skill_38_pg TEXT,
atk_skill_38_pg TEXT,
def_skill_38_pg TEXT,
nome_skill_39_pg TEXT,
en_skill_39_pg TEXT,
pa_skill_39_pg TEXT,
atk_skill_39_pg TEXT,
def_skill_39_pg TEXT,
nome_skill_40_pg TEXT,
en_skill_40_pg TEXT,
pa_skill_40_pg TEXT,
atk_skill_40_pg TEXT,
def_skill_40_pg TEXT,
oggetti_difensivi_1 TEXT,
oggetti_difensivi_2 TEXT,
oggetti_difensivi_3 TEXT,
oggetti_difensivi_4 TEXT,
oggetti_difensivi_5 TEXT,
extra1 TEXT,
extra2 TEXT,
extra3 TEXT,
extra4 TEXT,
extra5 TEXT,
extra6 TEXT,
extra7 TEXT,
extra8 TEXT,
extra9 TEXT,
extra10 TEXT,
extra11 TEXT,
extra12 TEXT,
extra13 TEXT,
extra14 TEXT,
extra15 TEXT,
extra16 TEXT,
extra17 TEXT,
extra18 TEXT,
extra19 TEXT,
extra20 TEXT,
diario1 TEXT,
diario2 TEXT,
diario3 TEXT,
diario4 TEXT,
diario5 TEXT,
diario6 TEXT,
diario7 TEXT,
diario8 TEXT,
diario9 TEXT,
diario10 TEXT,
diario11 TEXT,
diario12 TEXT,
diario13 TEXT,
diario14 TEXT,
diario15 TEXT,
diario16 TEXT,
diario17 TEXT,
diario18 TEXT,
diario19 TEXT,
diario20 TEXT,
nome_skill_41_pg TEXT,
en_skill_41_pg TEXT,
pa_skill_41_pg TEXT,
atk_skill_41_pg TEXT,
def_skill_41_pg TEXT,
nome_skill_42_pg TEXT,
en_skill_42_pg TEXT,
pa_skill_42_pg TEXT,
atk_skill_42_pg TEXT,
def_skill_42_pg TEXT,
nome_skill_43_pg TEXT,
en_skill_43_pg TEXT,
pa_skill_43_pg TEXT,
atk_skill_43_pg TEXT,
def_skill_43_pg TEXT,
nome_skill_44_pg TEXT,
en_skill_44_pg TEXT,
pa_skill_44_pg TEXT,
atk_skill_44_pg TEXT,
def_skill_44_pg TEXT,
nome_skill_45_pg TEXT,
en_skill_45_pg TEXT,
pa_skill_45_pg TEXT,
atk_skill_45_pg TEXT,
def_skill_45_pg TEXT,
nome_skill_46_pg TEXT,
en_skill_46_pg TEXT,
pa_skill_46_pg TEXT,
atk_skill_46_pg TEXT,
def_skill_46_pg TEXT,
nome_skill_47_pg TEXT,
en_skill_47_pg TEXT,
pa_skill_47_pg TEXT,
atk_skill_47_pg TEXT,
def_skill_47_pg TEXT,
nome_skill_48_pg TEXT,
en_skill_48_pg TEXT,
pa_skill_48_pg TEXT,
atk_skill_48_pg TEXT,
def_skill_48_pg TEXT,
nome_skill_49_pg TEXT,
en_skill_49_pg TEXT,
pa_skill_49_pg TEXT,
atk_skill_49_pg TEXT,
def_skill_49_pg TEXT,
nome_skill_50_pg TEXT,
en_skill_50_pg TEXT,
pa_skill_50_pg TEXT,
atk_skill_50_pg TEXT,
def_skill_50_pg TEXT,
nome_skill_51_pg TEXT,
en_skill_51_pg TEXT,
pa_skill_51_pg TEXT,
atk_skill_51_pg TEXT,
def_skill_51_pg TEXT,
nome_skill_52_pg TEXT,
en_skill_52_pg TEXT,
pa_skill_52_pg TEXT,
atk_skill_52_pg TEXT,
def_skill_52_pg TEXT,
nome_skill_53_pg TEXT,
en_skill_53_pg TEXT,
pa_skill_53_pg TEXT,
atk_skill_53_pg TEXT,
def_skill_53_pg TEXT,
nome_skill_54_pg TEXT,
en_skill_54_pg TEXT,
pa_skill_54_pg TEXT,
atk_skill_54_pg TEXT,
def_skill_54_pg TEXT,
nome_skill_55_pg TEXT,
en_skill_55_pg TEXT,
pa_skill_55_pg TEXT,
atk_skill_55_pg TEXT,
def_skill_55_pg TEXT)"""
    cursor.execute(crea_personaggio)

def crea_pg(nomepg):
    cursor.execute(f"""INSERT INTO personaggitry VALUES ('{nomepg}', 
'1', 'Maschio', 'Bretone', '19', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0','0', '0', '0', '0', '0', '0', '0', '0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
'0', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')""")

#
# crea_gioco()
# crea_pg("Hugo")
try:
    cursor.execute("SELECT * FROM personaggitry")
    seleziona = tuple(cursor.fetchall())
    pgstat = list(seleziona[0])
except sqlite3.OperationalError:
    crea_gioco()
    crea_pg("Starter")
    cursor.execute("SELECT * FROM personaggitry")
    seleziona = tuple(cursor.fetchall())
    pgstat = list(seleziona[0])

def print_all():
    cursor.execute("SELECT * FROM personaggitry")
    results = cursor.fetchall()
    print(results)


nomepg = pgstat[0]
livello = pgstat[1]
sesso = pgstat[2]
razza = pgstat[3]
eta = pgstat[4]
stanchezza = pgstat[5]
modificatore_generale = pgstat[6]
forza_base = pgstat[7]
forza_bonus_extra = pgstat[8]
resistenza_base = pgstat[9]
resistenza_bonus_extra = pgstat[10]
velocita_base = pgstat[11]
velocita_bonus_extra = pgstat[12]
agilita_base = pgstat[13]
agilita_bonus_extra = pgstat[14]
intelligenza_base = pgstat[15]
intelligenza_bonus_extra = pgstat[16]
concentrazione_base = pgstat[17]
concentrazione_bonus_extra = pgstat[18]
personalita_base = pgstat[19]
personalita_bonus_extra = pgstat[20]
fortuna_base = pgstat[21]
fortuna_bonus_extra = pgstat[22]
pf_item = pgstat[23]
pf_extra = pgstat[24]
mana_item = pgstat[25]
mana_extra = pgstat[26]
energia_item = pgstat[27]
energia_extra = pgstat[28]
energia_limite_item = pgstat[29]
energia_limite_extra = pgstat[30]
pa_item = pgstat[31]
pa_extra = pgstat[32]
attacco_arma = pgstat[33]
attacco_item = pgstat[34]
attacco_extra = pgstat[35]
difesa_armatura = pgstat[36]
difesa_item = pgstat[37]
difesa_extra = pgstat[38]
difesa_temp = pgstat[39]
volonta_item = pgstat[40]
volonta_extra = pgstat[41]
potere_item = pgstat[42]
potere_extra = pgstat[43]
barr_fis_item = pgstat[44]
barr_fis_extra = pgstat[45]
barr_mag_item = pgstat[46]
barr_mag_extra = pgstat[47]
rd_fis = pgstat[48]
res_fis = pgstat[49]
res_mag = pgstat[50]
rd_fuoco = pgstat[51]
rd_gelo = pgstat[52]
rd_elettro = pgstat[53]
compri_a_meno_extra = pgstat[54]
vendi_a_piu_extra = pgstat[55]
equip_anello_1 = pgstat[56]
equip_anello_2 = pgstat[57]
equip_anello_3 = pgstat[58]
equip_anello_4 = pgstat[59]
equip_anello_5 = pgstat[60]
equip_anello_6 = pgstat[61]
equip_anello_7 = pgstat[62]
equip_anello_8 = pgstat[63]
equip_anello_9 = pgstat[64]
equip_anello_10 = pgstat[65]
equip_orecchino_1 = pgstat[66]
equip_orecchino_2 = pgstat[67]
equip_orecchino_3 = pgstat[68]
equip_orecchino_4 = pgstat[69]
equip_orecchino_5 = pgstat[70]
equip_orecchino_6 = pgstat[71]
equip_spilla = pgstat[72]
equip_fascia = pgstat[73]
equip_mantello = pgstat[74]
equip_amuleto = pgstat[75]
equip_cintura = pgstat[76]
zaino_slot_1 = pgstat[77]
zaino_slot_2 = pgstat[78]
zaino_slot_3 = pgstat[79]
zaino_slot_4 = pgstat[80]
zaino_slot_5 = pgstat[81]
zaino_slot_6 = pgstat[82]
zaino_slot_7 = pgstat[83]
zaino_slot_8 = pgstat[84]
zaino_slot_9 = pgstat[85]
zaino_slot_10 = pgstat[86]
zaino_slot_11 = pgstat[87]
zaino_slot_12 = pgstat[88]
zaino_slot_13 = pgstat[89]
zaino_slot_14 = pgstat[90]
zaino_slot_15 = pgstat[91]
zaino_slot_16 = pgstat[92]
zaino_slot_17 = pgstat[93]
zaino_slot_18 = pgstat[94]
zaino_slot_19 = pgstat[95]
zaino_slot_20 = pgstat[96]
arma_1 = pgstat[97]
arma_2 = pgstat[98]
armatura = pgstat[99]
scudo = pgstat[100]
oggetto_difensivo_1 = pgstat[101]
oggetto_difensivo_2 = pgstat[102]
oggetto_difensivo_3 = pgstat[103]
oggetto_difensivo_4 = pgstat[104]
magia_1 = pgstat[105]
magia_2 = pgstat[106]
magia_3 = pgstat[107]
magia_4 = pgstat[108]
magia_5 = pgstat[109]
magia_6 = pgstat[110]
magia_7 = pgstat[111]
magia_8 = pgstat[112]
magia_9 = pgstat[113]
magia_10 = pgstat[114]
magia_11 = pgstat[115]
magia_12 = pgstat[116]
magia_13 = pgstat[117]
magia_14 = pgstat[118]
magia_15 = pgstat[119]
magia_16 = pgstat[120]
magia_17 = pgstat[121]
magia_18 = pgstat[122]
magia_19 = pgstat[123]
magia_20 = pgstat[124]
en_per_mana_ordine = pgstat[125]
en_per_mana_caos = pgstat[126]
pa_per_mana_ordine = pgstat[127]
pa_per_mana_caos = pgstat[128]
sconto_mana_per_potere = pgstat[129]
sconto_pa_per_potere = pgstat[130]
monete = pgstat[131]
relazioni_skaal = pgstat[132]
relazioni_imperiali = pgstat[133]
relazioni_raven_rock = pgstat[134]
relazioni_east_emp_comp = pgstat[135]
relazioni_riekling = pgstat[136]
relazioni_miraak = pgstat[137]
relazioni_minatori = pgstat[138]
relazioni_elfi_oscuri = pgstat[139]
punti_exp_rossi = pgstat[140]
punti_exp_spesi_rossi = pgstat[141]
punti_exp_blu = pgstat[142]
punti_exp_spesi_blu = pgstat[143]
punti_exp_verdi = pgstat[144]
punti_exp_spesi_verdi = pgstat[145]
punti_exp_extra = pgstat[146]
punti_exp_spesi_extra = pgstat[147]
punti_abilita = pgstat[148]
punti_abilita_spesi = pgstat[149]
skill_igegneria = pgstat[150]
skill_conoscenze_naturaegeografia = pgstat[151]
skill_conoscenze_religioni = pgstat[152]
skill_conoscenze_storiaenobilta = pgstat[153]
skill_cammuffare = pgstat[154]
skill_furtivita = pgstat[155]
skill_intimidire = pgstat[156]
skill_strategia_militare = pgstat[157]
skill_sopravvivenza = pgstat[158]
skill_intuizione = pgstat[159]
skill_diplomazia = pgstat[160]
skill_sapienza_magica = pgstat[161]
skill_percezione = pgstat[162]
skill_raggirare = pgstat[163]
skill_gestione_risorse = pgstat[164]
note1 = pgstat[165]
note2 = pgstat[166]
note3 = pgstat[167]
note4 = pgstat[168]
alchimia_note_1 = pgstat[169]
alchimia_note_2 = pgstat[170]
alchimia_note_3 = pgstat[171]
alchimia_ingredienti_rossi_1 = pgstat[172]
alchimia_ingredienti_rossi_2 = pgstat[173]
alchimia_ingredienti_rossi_3 = pgstat[174]
alchimia_ingredienti_rossi_4 = pgstat[175]
alchimia_ingredienti_verdi_1 = pgstat[176]
alchimia_ingredienti_verdi_2 = pgstat[177]
alchimia_ingredienti_verdi_3 = pgstat[178]
alchimia_ingredienti_verdi_4 = pgstat[179]
alchimia_ingredienti_blu_1 = pgstat[180]
alchimia_ingredienti_blu_2 = pgstat[181]
alchimia_ingredienti_blu_3 = pgstat[182]
alchimia_ingredienti_blu_4 = pgstat[183]
alchimia_effetto_ingredienti_1 = pgstat[184]
alchimia_effetto_ingredienti_2 = pgstat[185]
alchimia_effetto_ingredienti_3 = pgstat[186]
alchimia_effetto_ingredienti_4 = pgstat[187]
alchimia_moltiplicatore_rossi = pgstat[188]
alchimia_moltiplicatore_verdi = pgstat[189]
alchimia_moltiplicatore_blu = pgstat[190]
magia_1_nome = pgstat[191]
magia_1_formula = pgstat[192]
magia_2_nome = pgstat[193]
magia_2_formula = pgstat[194]
magia_3_nome = pgstat[195]
magia_3_formula = pgstat[196]
magia_4_nome = pgstat[197]
magia_4_formula = pgstat[198]
magia_5_nome = pgstat[199]
magia_5_formula = pgstat[200]
magia_6_nome = pgstat[201]
magia_6_formula = pgstat[202]
magia_7_nome = pgstat[203]
magia_7_formula = pgstat[204]
magia_8_nome = pgstat[205]
magia_8_formula = pgstat[206]
magia_9_nome = pgstat[207]
magia_9_formula = pgstat[208]
magia_10_nome = pgstat[209]
magia_10_formula = pgstat[210]
magia_11_nome = pgstat[211]
magia_11_formula = pgstat[212]
magia_12_nome = pgstat[213]
magia_12_formula = pgstat[214]
magia_13_nome = pgstat[215]
magia_13_formula = pgstat[216]
magia_14_nome = pgstat[217]
magia_14_formula = pgstat[218]
magia_15_nome = pgstat[219]
magia_15_formula = pgstat[220]
magia_16_nome = pgstat[221]
magia_16_formula = pgstat[222]
magia_17_nome = pgstat[223]
magia_17_formula = pgstat[224]
magia_18_nome = pgstat[225]
magia_18_formula = pgstat[226]
magia_19_nome = pgstat[227]
magia_19_formula = pgstat[228]
magia_20_nome = pgstat[229]
magia_20_formula = pgstat[230]
attacco_arma_1 = pgstat[231]
attacco_arma_2 = pgstat[232]
pa_arma_1 = pgstat[233]
pa_arma_2 = pgstat[234]
note_arma_1 = pgstat[235]
note_arma_2 = pgstat[236]
dado_arma_1 = pgstat[237]
dado_arma_2 = pgstat[238]
tipo_arma_1 = pgstat[239]
tipo_arma_2 = pgstat[240]
buca_rd_arma_1 = pgstat[241]
buca_rd_arma_2 = pgstat[242]
bonus_danno_arma_1 = pgstat[243]
bonus_danno_arma_2 = pgstat[244]
crit_min_arma_1 = pgstat[245]
crit_nor_arma_1 = pgstat[246]
crit_mag_arma_1 = pgstat[247]
crit_min_arma_2 = pgstat[248]
crit_nor_arma_2 = pgstat[249]
crit_mag_arma_2 = pgstat[250]
slot_zaino_magici = pgstat[251]
slot_zaino_non_magici = pgstat[252]
note_armatura = pgstat[253]
pe_rossi_sessione_1 = pgstat[254]
pe_rossi_sessione_2 = pgstat[255]
pe_rossi_sessione_3 = pgstat[256]
pe_rossi_sessione_4 = pgstat[257]
pe_rossi_sessione_5 = pgstat[258]
pe_rossi_sessione_6 = pgstat[259]
pe_rossi_sessione_7 = pgstat[260]
pe_rossi_sessione_8 = pgstat[261]
pe_rossi_sessione_9 = pgstat[262]
pe_rossi_sessione_10 = pgstat[263]
pe_rossi_sessione_11 = pgstat[264]
pe_rossi_sessione_12 = pgstat[265]
pe_rossi_sessione_13 = pgstat[266]
pe_rossi_sessione_14 = pgstat[267]
pe_rossi_sessione_15 = pgstat[268]
pe_rossi_sessione_16 = pgstat[269]
pe_rossi_sessione_17 = pgstat[270]
pe_rossi_sessione_18 = pgstat[271]
pe_rossi_sessione_19 = pgstat[272]
pe_rossi_sessione_20 = pgstat[273]
pe_rossi_sessione_21 = pgstat[274]
pe_rossi_sessione_22 = pgstat[275]
pe_rossi_sessione_23 = pgstat[276]
pe_rossi_sessione_24 = pgstat[277]
pe_rossi_sessione_25 = pgstat[278]
pe_rossi_sessione_26 = pgstat[279]
pe_rossi_sessione_27 = pgstat[280]
pe_rossi_sessione_28 = pgstat[281]
pe_rossi_sessione_29 = pgstat[282]
pe_rossi_sessione_30 = pgstat[283]
pe_rossi_sessione_31 = pgstat[284]
pe_rossi_sessione_32 = pgstat[285]
pe_rossi_sessione_33 = pgstat[286]
pe_rossi_sessione_34 = pgstat[287]
pe_rossi_sessione_35 = pgstat[288]
pe_rossi_sessione_36 = pgstat[289]
pe_rossi_sessione_37 = pgstat[290]
pe_rossi_sessione_38 = pgstat[291]
pe_rossi_sessione_39 = pgstat[292]
pe_rossi_sessione_40 = pgstat[293]
pe_verdi_sessione_1 = pgstat[294]
pe_verdi_sessione_2 = pgstat[295]
pe_verdi_sessione_3 = pgstat[296]
pe_verdi_sessione_4 = pgstat[297]
pe_verdi_sessione_5 = pgstat[298]
pe_verdi_sessione_6 = pgstat[299]
pe_verdi_sessione_7 = pgstat[300]
pe_verdi_sessione_8 = pgstat[301]
pe_verdi_sessione_9 = pgstat[302]
pe_verdi_sessione_10 = pgstat[303]
pe_verdi_sessione_11 = pgstat[304]
pe_verdi_sessione_12 = pgstat[305]
pe_verdi_sessione_13 = pgstat[306]
pe_verdi_sessione_14 = pgstat[307]
pe_verdi_sessione_15 = pgstat[308]
pe_verdi_sessione_16 = pgstat[309]
pe_verdi_sessione_17 = pgstat[310]
pe_verdi_sessione_18 = pgstat[311]
pe_verdi_sessione_19 = pgstat[312]
pe_verdi_sessione_20 = pgstat[313]
pe_verdi_sessione_21 = pgstat[314]
pe_verdi_sessione_22 = pgstat[315]
pe_verdi_sessione_23 = pgstat[316]
pe_verdi_sessione_24 = pgstat[317]
pe_verdi_sessione_25 = pgstat[318]
pe_verdi_sessione_26 = pgstat[319]
pe_verdi_sessione_27 = pgstat[320]
pe_verdi_sessione_28 = pgstat[321]
pe_verdi_sessione_29 = pgstat[322]
pe_verdi_sessione_30 = pgstat[323]
pe_verdi_sessione_31 = pgstat[324]
pe_verdi_sessione_32 = pgstat[325]
pe_verdi_sessione_33 = pgstat[326]
pe_verdi_sessione_34 = pgstat[327]
pe_verdi_sessione_35 = pgstat[328]
pe_verdi_sessione_36 = pgstat[329]
pe_verdi_sessione_37 = pgstat[330]
pe_verdi_sessione_38 = pgstat[331]
pe_verdi_sessione_39 = pgstat[332]
pe_verdi_sessione_40 = pgstat[333]
pe_blu_sessione_1 = pgstat[334]
pe_blu_sessione_2 = pgstat[335]
pe_blu_sessione_3 = pgstat[336]
pe_blu_sessione_4 = pgstat[337]
pe_blu_sessione_5 = pgstat[338]
pe_blu_sessione_6 = pgstat[339]
pe_blu_sessione_7 = pgstat[340]
pe_blu_sessione_8 = pgstat[341]
pe_blu_sessione_9 = pgstat[342]
pe_blu_sessione_10 = pgstat[343]
pe_blu_sessione_11 = pgstat[344]
pe_blu_sessione_12 = pgstat[345]
pe_blu_sessione_13 = pgstat[346]
pe_blu_sessione_14 = pgstat[347]
pe_blu_sessione_15 = pgstat[348]
pe_blu_sessione_16 = pgstat[349]
pe_blu_sessione_17 = pgstat[350]
pe_blu_sessione_18 = pgstat[351]
pe_blu_sessione_19 = pgstat[352]
pe_blu_sessione_20 = pgstat[353]
pe_blu_sessione_21 = pgstat[354]
pe_blu_sessione_22 = pgstat[355]
pe_blu_sessione_23 = pgstat[356]
pe_blu_sessione_24 = pgstat[357]
pe_blu_sessione_25 = pgstat[358]
pe_blu_sessione_26 = pgstat[359]
pe_blu_sessione_27 = pgstat[360]
pe_blu_sessione_28 = pgstat[361]
pe_blu_sessione_29 = pgstat[362]
pe_blu_sessione_30 = pgstat[363]
pe_blu_sessione_31 = pgstat[364]
pe_blu_sessione_32 = pgstat[365]
pe_blu_sessione_33 = pgstat[366]
pe_blu_sessione_34 = pgstat[367]
pe_blu_sessione_35 = pgstat[368]
pe_blu_sessione_36 = pgstat[369]
pe_blu_sessione_37 = pgstat[370]
pe_blu_sessione_38 = pgstat[371]
pe_blu_sessione_39 = pgstat[372]
pe_blu_sessione_40 = pgstat[373]
pe_extra_sessione_1 = pgstat[374]
pe_extra_sessione_2 = pgstat[375]
pe_extra_sessione_3 = pgstat[376]
pe_extra_sessione_4 = pgstat[377]
pe_extra_sessione_5 = pgstat[378]
pe_extra_sessione_6 = pgstat[379]
pe_extra_sessione_7 = pgstat[380]
pe_extra_sessione_8 = pgstat[381]
pe_extra_sessione_9 = pgstat[382]
pe_extra_sessione_10 = pgstat[383]
pe_extra_sessione_11 = pgstat[384]
pe_extra_sessione_12 = pgstat[385]
pe_extra_sessione_13 = pgstat[386]
pe_extra_sessione_14 = pgstat[387]
pe_extra_sessione_15 = pgstat[388]
pe_extra_sessione_16 = pgstat[389]
pe_extra_sessione_17 = pgstat[390]
pe_extra_sessione_18 = pgstat[391]
pe_extra_sessione_19 = pgstat[392]
pe_extra_sessione_20 = pgstat[393]
pe_extra_sessione_21 = pgstat[394]
pe_extra_sessione_22 = pgstat[395]
pe_extra_sessione_23 = pgstat[396]
pe_extra_sessione_24 = pgstat[397]
pe_extra_sessione_25 = pgstat[398]
pe_extra_sessione_26 = pgstat[399]
pe_extra_sessione_27 = pgstat[400]
pe_extra_sessione_28 = pgstat[401]
pe_extra_sessione_29 = pgstat[402]
pe_extra_sessione_30 = pgstat[403]
pe_extra_sessione_31 = pgstat[404]
pe_extra_sessione_32 = pgstat[405]
pe_extra_sessione_33 = pgstat[406]
pe_extra_sessione_34 = pgstat[407]
pe_extra_sessione_35 = pgstat[408]
pe_extra_sessione_36 = pgstat[409]
pe_extra_sessione_37 = pgstat[410]
pe_extra_sessione_38 = pgstat[411]
pe_extra_sessione_39 = pgstat[412]
pe_extra_sessione_40 = pgstat[413]
pe_skill_sessione_1 = pgstat[414]
pe_skill_sessione_2 = pgstat[415]
pe_skill_sessione_3 = pgstat[416]
pe_skill_sessione_4 = pgstat[417]
pe_skill_sessione_5 = pgstat[418]
pe_skill_sessione_6 = pgstat[419]
pe_skill_sessione_7 = pgstat[420]
pe_skill_sessione_8 = pgstat[421]
pe_skill_sessione_9 = pgstat[422]
pe_skill_sessione_10 = pgstat[423]
pe_skill_sessione_11 = pgstat[424]
pe_skill_sessione_12 = pgstat[425]
pe_skill_sessione_13 = pgstat[426]
pe_skill_sessione_14 = pgstat[427]
pe_skill_sessione_15 = pgstat[428]
pe_skill_sessione_16 = pgstat[429]
pe_skill_sessione_17 = pgstat[430]
pe_skill_sessione_18 = pgstat[431]
pe_skill_sessione_19 = pgstat[432]
pe_skill_sessione_20 = pgstat[433]
pe_skill_sessione_21 = pgstat[434]
pe_skill_sessione_22 = pgstat[435]
pe_skill_sessione_23 = pgstat[436]
pe_skill_sessione_24 = pgstat[437]
pe_skill_sessione_25 = pgstat[438]
pe_skill_sessione_26 = pgstat[439]
pe_skill_sessione_27 = pgstat[440]
pe_skill_sessione_28 = pgstat[441]
pe_skill_sessione_29 = pgstat[442]
pe_skill_sessione_30 = pgstat[443]
pe_skill_sessione_31 = pgstat[444]
pe_skill_sessione_32 = pgstat[445]
pe_skill_sessione_33 = pgstat[446]
pe_skill_sessione_34 = pgstat[447]
pe_skill_sessione_35 = pgstat[448]
pe_skill_sessione_36 = pgstat[449]
pe_skill_sessione_37 = pgstat[450]
pe_skill_sessione_38 = pgstat[451]
pe_skill_sessione_39 = pgstat[452]
pe_skill_sessione_40 = pgstat[453]
nome_skill_1_pg = pgstat[454]
en_skill_1_pg = pgstat[455]
pa_skill_1_pg = pgstat[456]
atk_skill_1_pg = pgstat[457]
def_skill_1_pg = pgstat[458]
nome_skill_2_pg = pgstat[459]
en_skill_2_pg = pgstat[460]
pa_skill_2_pg = pgstat[461]
atk_skill_2_pg = pgstat[462]
def_skill_2_pg = pgstat[463]
nome_skill_3_pg = pgstat[464]
en_skill_3_pg = pgstat[465]
pa_skill_3_pg = pgstat[466]
atk_skill_3_pg = pgstat[467]
def_skill_3_pg = pgstat[468]
nome_skill_4_pg = pgstat[469]
en_skill_4_pg = pgstat[470]
pa_skill_4_pg = pgstat[471]
atk_skill_4_pg = pgstat[472]
def_skill_4_pg = pgstat[473]
nome_skill_5_pg = pgstat[474]
en_skill_5_pg = pgstat[475]
pa_skill_5_pg = pgstat[476]
atk_skill_5_pg = pgstat[477]
def_skill_5_pg = pgstat[478]
nome_skill_6_pg = pgstat[479]
en_skill_6_pg = pgstat[480]
pa_skill_6_pg = pgstat[481]
atk_skill_6_pg = pgstat[482]
def_skill_6_pg = pgstat[483]
nome_skill_7_pg = pgstat[484]
en_skill_7_pg = pgstat[485]
pa_skill_7_pg = pgstat[486]
atk_skill_7_pg = pgstat[487]
def_skill_7_pg = pgstat[488]
nome_skill_8_pg = pgstat[489]
en_skill_8_pg = pgstat[490]
pa_skill_8_pg = pgstat[491]
atk_skill_8_pg = pgstat[492]
def_skill_8_pg = pgstat[493]
nome_skill_9_pg = pgstat[494]
en_skill_9_pg = pgstat[495]
pa_skill_9_pg = pgstat[496]
atk_skill_9_pg = pgstat[497]
def_skill_9_pg = pgstat[498]
nome_skill_10_pg = pgstat[499]
en_skill_10_pg = pgstat[500]
pa_skill_10_pg = pgstat[501]
atk_skill_10_pg = pgstat[502]
def_skill_10_pg = pgstat[503]
nome_skill_11_pg = pgstat[504]
en_skill_11_pg = pgstat[505]
pa_skill_11_pg = pgstat[506]
atk_skill_11_pg = pgstat[507]
def_skill_11_pg = pgstat[508]
nome_skill_12_pg = pgstat[509]
en_skill_12_pg = pgstat[510]
pa_skill_12_pg = pgstat[511]
atk_skill_12_pg = pgstat[512]
def_skill_12_pg = pgstat[513]
nome_skill_13_pg = pgstat[514]
en_skill_13_pg = pgstat[515]
pa_skill_13_pg = pgstat[516]
atk_skill_13_pg = pgstat[517]
def_skill_13_pg = pgstat[518]
nome_skill_14_pg = pgstat[519]
en_skill_14_pg = pgstat[520]
pa_skill_14_pg = pgstat[521]
atk_skill_14_pg = pgstat[522]
def_skill_14_pg = pgstat[523]
nome_skill_15_pg = pgstat[524]
en_skill_15_pg = pgstat[525]
pa_skill_15_pg = pgstat[526]
atk_skill_15_pg = pgstat[527]
def_skill_15_pg = pgstat[528]
nome_skill_16_pg = pgstat[529]
en_skill_16_pg = pgstat[530]
pa_skill_16_pg = pgstat[531]
atk_skill_16_pg = pgstat[532]
def_skill_16_pg = pgstat[533]
nome_skill_17_pg = pgstat[534]
en_skill_17_pg = pgstat[535]
pa_skill_17_pg = pgstat[536]
atk_skill_17_pg = pgstat[537]
def_skill_17_pg = pgstat[538]
nome_skill_18_pg = pgstat[539]
en_skill_18_pg = pgstat[540]
pa_skill_18_pg = pgstat[541]
atk_skill_18_pg = pgstat[542]
def_skill_18_pg = pgstat[543]
nome_skill_19_pg = pgstat[544]
en_skill_19_pg = pgstat[545]
pa_skill_19_pg = pgstat[546]
atk_skill_19_pg = pgstat[547]
def_skill_19_pg = pgstat[548]
nome_skill_20_pg = pgstat[549]
en_skill_20_pg = pgstat[550]
pa_skill_20_pg = pgstat[551]
atk_skill_20_pg = pgstat[552]
def_skill_20_pg = pgstat[553]
nome_skill_21_pg = pgstat[554]
en_skill_21_pg = pgstat[555]
pa_skill_21_pg = pgstat[556]
atk_skill_21_pg = pgstat[557]
def_skill_21_pg = pgstat[558]
nome_skill_22_pg = pgstat[559]
en_skill_22_pg = pgstat[560]
pa_skill_22_pg = pgstat[561]
atk_skill_22_pg = pgstat[562]
def_skill_22_pg = pgstat[563]
nome_skill_23_pg = pgstat[564]
en_skill_23_pg = pgstat[565]
pa_skill_23_pg = pgstat[566]
atk_skill_23_pg = pgstat[567]
def_skill_23_pg = pgstat[568]
nome_skill_24_pg = pgstat[569]
en_skill_24_pg = pgstat[570]
pa_skill_24_pg = pgstat[571]
atk_skill_24_pg = pgstat[572]
def_skill_24_pg = pgstat[573]
nome_skill_25_pg = pgstat[574]
en_skill_25_pg = pgstat[575]
pa_skill_25_pg = pgstat[576]
atk_skill_25_pg = pgstat[577]
def_skill_25_pg = pgstat[578]
nome_skill_26_pg = pgstat[579]
en_skill_26_pg = pgstat[580]
pa_skill_26_pg = pgstat[581]
atk_skill_26_pg = pgstat[582]
def_skill_26_pg = pgstat[583]
nome_skill_27_pg = pgstat[584]
en_skill_27_pg = pgstat[585]
pa_skill_27_pg = pgstat[586]
atk_skill_27_pg = pgstat[587]
def_skill_27_pg = pgstat[588]
nome_skill_28_pg = pgstat[589]
en_skill_28_pg = pgstat[590]
pa_skill_28_pg = pgstat[591]
atk_skill_28_pg = pgstat[592]
def_skill_28_pg = pgstat[593]
nome_skill_29_pg = pgstat[594]
en_skill_29_pg = pgstat[595]
pa_skill_29_pg = pgstat[596]
atk_skill_29_pg = pgstat[597]
def_skill_29_pg = pgstat[598]
nome_skill_30_pg = pgstat[599]
en_skill_30_pg = pgstat[600]
pa_skill_30_pg = pgstat[601]
atk_skill_30_pg = pgstat[602]
def_skill_30_pg = pgstat[603]
nome_skill_31_pg = pgstat[604]
en_skill_31_pg = pgstat[605]
pa_skill_31_pg = pgstat[606]
atk_skill_31_pg = pgstat[607]
def_skill_31_pg = pgstat[608]
nome_skill_32_pg = pgstat[609]
en_skill_32_pg = pgstat[610]
pa_skill_32_pg = pgstat[611]
atk_skill_32_pg = pgstat[612]
def_skill_32_pg = pgstat[613]
nome_skill_33_pg = pgstat[614]
en_skill_33_pg = pgstat[615]
pa_skill_33_pg = pgstat[616]
atk_skill_33_pg = pgstat[617]
def_skill_33_pg = pgstat[618]
nome_skill_34_pg = pgstat[619]
en_skill_34_pg = pgstat[620]
pa_skill_34_pg = pgstat[621]
atk_skill_34_pg = pgstat[622]
def_skill_34_pg = pgstat[623]
nome_skill_35_pg = pgstat[624]
en_skill_35_pg = pgstat[625]
pa_skill_35_pg = pgstat[626]
atk_skill_35_pg = pgstat[627]
def_skill_35_pg = pgstat[628]
nome_skill_36_pg = pgstat[629]
en_skill_36_pg = pgstat[630]
pa_skill_36_pg = pgstat[631]
atk_skill_36_pg = pgstat[632]
def_skill_36_pg = pgstat[633]
nome_skill_37_pg = pgstat[634]
en_skill_37_pg = pgstat[635]
pa_skill_37_pg = pgstat[636]
atk_skill_37_pg = pgstat[637]
def_skill_37_pg = pgstat[638]
nome_skill_38_pg = pgstat[639]
en_skill_38_pg = pgstat[640]
pa_skill_38_pg = pgstat[641]
atk_skill_38_pg = pgstat[642]
def_skill_38_pg = pgstat[643]
nome_skill_39_pg = pgstat[644]
en_skill_39_pg = pgstat[645]
pa_skill_39_pg = pgstat[646]
atk_skill_39_pg = pgstat[647]
def_skill_39_pg = pgstat[648]
nome_skill_40_pg = pgstat[649]
en_skill_40_pg = pgstat[650]
pa_skill_40_pg = pgstat[651]
atk_skill_40_pg = pgstat[652]
def_skill_40_pg = pgstat[653]
oggetti_difensivi_1 = pgstat[654]
oggetti_difensivi_2 = pgstat[655]
oggetti_difensivi_3 = pgstat[656]
oggetti_difensivi_4 = pgstat[657]
oggetti_difensivi_5 = pgstat[658]
extra1 = pgstat[659]
extra2 = pgstat[660]
extra3 = pgstat[661]
extra4 = pgstat[662]
extra5 = pgstat[663]
extra6 = pgstat[664]
extra7 = pgstat[665]
extra8 = pgstat[666]
extra9 = pgstat[667]
extra10 = pgstat[668]
extra11 = pgstat[669]
extra12 = pgstat[670]
extra13 = pgstat[671]
extra14 = pgstat[672]
extra15 = pgstat[673]
extra16 = pgstat[674]
extra17 = pgstat[675]
extra18 = pgstat[676]
extra19 = pgstat[677]
extra20 = pgstat[678]
diario1 = pgstat[679]
diario2 = pgstat[680]
diario3 = pgstat[681]
diario4 = pgstat[682]
diario5 = pgstat[683]
diario6 = pgstat[684]
diario7 = pgstat[685]
diario8 = pgstat[686]
diario9 = pgstat[687]
diario10 = pgstat[688]
diario11 = pgstat[689]
diario12 = pgstat[690]
diario13 = pgstat[691]
diario14 = pgstat[692]
diario15 = pgstat[693]
diario16 = pgstat[694]
diario17 = pgstat[695]
diario18 = pgstat[696]
diario19 = pgstat[697]
diario20 = pgstat[698]
nome_skill_41_pg = pgstat[699]
en_skill_41_pg = pgstat[700]
pa_skill_41_pg = pgstat[701]
atk_skill_41_pg = pgstat[702]
def_skill_41_pg = pgstat[703]
nome_skill_42_pg = pgstat[704]
en_skill_42_pg = pgstat[705]
pa_skill_42_pg = pgstat[706]
atk_skill_42_pg = pgstat[707]
def_skill_42_pg = pgstat[708]
nome_skill_43_pg = pgstat[709]
en_skill_43_pg = pgstat[710]
pa_skill_43_pg = pgstat[711]
atk_skill_43_pg = pgstat[712]
def_skill_43_pg = pgstat[713]
nome_skill_44_pg = pgstat[714]
en_skill_44_pg = pgstat[715]
pa_skill_44_pg = pgstat[716]
atk_skill_44_pg = pgstat[717]
def_skill_44_pg = pgstat[718]
nome_skill_45_pg = pgstat[719]
en_skill_45_pg = pgstat[720]
pa_skill_45_pg = pgstat[721]
atk_skill_45_pg = pgstat[722]
def_skill_45_pg = pgstat[723]
nome_skill_46_pg = pgstat[724]
en_skill_46_pg = pgstat[725]
pa_skill_46_pg = pgstat[726]
atk_skill_46_pg = pgstat[727]
def_skill_46_pg = pgstat[728]
nome_skill_47_pg = pgstat[729]
en_skill_47_pg = pgstat[730]
pa_skill_47_pg = pgstat[731]
atk_skill_47_pg = pgstat[732]
def_skill_47_pg = pgstat[733]
nome_skill_48_pg = pgstat[734]
en_skill_48_pg = pgstat[735]
pa_skill_48_pg = pgstat[736]
atk_skill_48_pg = pgstat[737]
def_skill_48_pg = pgstat[738]
nome_skill_49_pg = pgstat[739]
en_skill_49_pg = pgstat[740]
pa_skill_49_pg = pgstat[741]
atk_skill_49_pg = pgstat[742]
def_skill_49_pg = pgstat[743]
nome_skill_50_pg = pgstat[744]
en_skill_50_pg = pgstat[745]
pa_skill_50_pg = pgstat[746]
atk_skill_50_pg = pgstat[747]
def_skill_50_pg = pgstat[748]
nome_skill_51_pg = pgstat[749]
en_skill_51_pg = pgstat[750]
pa_skill_51_pg = pgstat[751]
atk_skill_51_pg = pgstat[752]
def_skill_51_pg = pgstat[753]
nome_skill_52_pg = pgstat[754]
en_skill_52_pg = pgstat[755]
pa_skill_52_pg = pgstat[756]
atk_skill_52_pg = pgstat[757]
def_skill_52_pg = pgstat[758]
nome_skill_53_pg = pgstat[759]
en_skill_53_pg = pgstat[760]
pa_skill_53_pg = pgstat[761]
atk_skill_53_pg = pgstat[762]
def_skill_53_pg = pgstat[763]
nome_skill_54_pg = pgstat[764]
en_skill_54_pg = pgstat[765]
pa_skill_54_pg = pgstat[766]
atk_skill_54_pg = pgstat[767]
def_skill_54_pg = pgstat[768]
nome_skill_55_pg = pgstat[769]
en_skill_55_pg = pgstat[770]
pa_skill_55_pg = pgstat[771]
atk_skill_55_pg = pgstat[772]
def_skill_55_pg = pgstat[773]


connection.commit()


