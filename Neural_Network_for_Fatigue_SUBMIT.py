from __future__ import division
from math import *
import jmp_score as jmp

def getModelMetadata():
	return {"creator": u"Neural", "modelName": u"", "predicted": u"Fatigue", "table": u"FullPanel", "version": u"14.0.0", "timestamp": u"2019-09-09T06:58:01Z"}


def getInputMetadata():
    return {
        u"BestOutofSelfTotal": "float",
        u"Skills_Y": "float",
        u"SleepQuality": "float",
        u"PlayerID-1": "float",
        u"Duration": "float",
        u"AcuteLoad": "float",
        u"TournamentGame": "float",
        u"SessionLoad": "float",
        u"DailyLoad": "float"
	}


def getOutputMetadata():
    return {
        u"Predicted Fatigue": "float"
	}


def score(indata, outdata):
    # H1_1
    # H1_2
    # H1_3
    # H1_4
    # H1_5
    # H1_6
    # H1_7
    # H1_8
    # H1_9
    # H1_10
    # H1_11
    # H1_12
    # H1_13
    # H1_14
    # H1_15
    # H1_16
    # H1_17
    # H1_18
    # H1_19
    # H1_20
    # H1_21
    # H1_22
    # H1_23
    # H1_24
    # H1_25
    # H1_26
    # H1_27
    # H1_28
    # H1_29
    # H1_30
    # H1_31
    # H1_32
    # H1_33
    # H1_34
    # H1_35
    # H1_36
    # H1_37
    # H1_38
    # H1_39
    # H1_40
    # H1_41
    # H1_42
    # H1_43
    # H1_44
    # H1_45
    # H1_46
    # H1_47
    # H1_48
    # H1_49
    # H1_50
    # H1_51
    # H1_52
    # H1_53
    # H1_54
    # H1_55
    # H1_56
    # H1_57
    # H1_58
    # H1_59
    # H1_60
    # H1_61
    # H1_62
    # H1_63
    # H1_64
    # H1_65
    # H1_66
    # H1_67
    # H1_68
    # H1_69
    # H1_70
    # H1_71
    # H1_72
    # H1_73
    # H1_74
    # H1_75
    # H1_76
    # H1_77
    # H1_78
    # H1_79
    # H1_80
    # H1_81
    # H1_82
    # H1_83
    # H1_84
    # H1_85
    # H1_86
    # H1_87
    # H1_88
    # H1_89
    # H1_90
    # H1_91
    # H1_92
    # H1_93
    # H1_94
    # H1_95
    # H1_96
    # H1_97
    # H1_98
    # H1_99
    # H1_100
    # H1_101
    # H1_102
    # H1_103
    # H1_104
    # H1_105
    # H1_106
    # H1_107
    # H1_108
    # H1_109
    # H1_110
    # H1_111
    # H1_112
    # H1_113
    # H1_114
    # H1_115
    # H1_116
    # H1_117
    # H1_118
    # H1_119
    # H1_120
    # H1_121
    # H1_122
    # H1_123
    # H1_124
    # H1_125
    # H1_126
    # H1_127
    # H1_128
    # H1_129
    # H1_130
    # H1_131
    # H1_132
    # H1_133
    # H1_134
    # H1_135
    # H1_136
    # H1_137
    # H1_138
    # H1_139
    # H1_140
    # H1_141
    # H1_142
    # H1_143
    # H1_144
    # H1_145
    # H1_146
    # H1_147
    # H1_148
    # H1_149
    # H1_150
    # H1_151
    # H1_152
    # H1_153
    # H1_154
    # H1_155
    # H1_156
    # H1_157
    # H1_158
    # H1_159
    # H1_160
    # H1_161
    # H1_162
    # H1_163
    # H1_164
    # H1_165
    # H1_166
    # H1_167
    # H1_168
    # H1_169
    # H1_170
    # H1_171
    # H1_172
    # H1_173
    # H1_174
    # H1_175
    # H1_176
    # H1_177
    # H1_178
    # H1_179
    # H1_180
    # H1_181
    # H1_182
    # H1_183
    # H1_184
    # H1_185
    # H1_186
    # H1_187
    # H1_188
    # H1_189
    # H1_190
    # H1_191
    # H1_192
    # H1_193
    # H1_194
    # H1_195
    # H1_196
    # H1_197
    # H1_198
    # H1_199
    # H1_200
    # H1_201
    # H1_202
    # H1_203
    # H1_204
    # H1_205
    # H1_206
    # H1_207
    # H1_208
    # H1_209
    # H1_210
    # H1_211
    # H1_212
    # H1_213
    _temp_0 = 165.457258253717
    _temp_1 = 276.359562097094
    _temp_2 = 60.1944861065038
    _temp_3 = -31.5292464008683
    _temp_4 = 25.5227463542567
    _temp_5 = -127.199545559663
    _temp_6 = -19.502327554209
    _temp_7 = -621.185880313701
    _temp_8 = -76.9108804142658
    _temp_9 = 421.534168971839
    _temp_10 = 77.8422812341789
    _temp_11 = 29.9449093197622
    _temp_12 = -22.5302304105098
    _temp_13 = -306.271923916924
    _temp_14 = 21.0743393756025
    _temp_15 = -290.113530665672
    _temp_16 = 151.679261048317
    _temp_17 = -26.0118181875363
    _temp_18 = -1.47940597707063
    _temp_19 = 5.37627652543962
    _temp_20 = 0.868597453713464
    _temp_21 = 9.70264882858312
    _temp_22 = -179.300806148543
    _temp_23 = 110.66855817209
    _temp_24 = 16.390961751826
    _temp_25 = 19.5573622638652
    _temp_26 = -10.4898150447069
    _temp_27 = 179.521970916068
    _temp_28 = -109.473673176047
    _temp_29 = 63.8791057734263
    _temp_30 = -85.1943084190581
    _temp_31 = -33.8886903368233
    _temp_32 = -8.5464262839495
    _temp_33 = 19.6651962454814
    _temp_34 = 74.8943581124891
    _temp_35 = -64.6878372462143
    _temp_36 = 41.866483589376
    _temp_37 = 3.00922890717947
    _temp_38 = 12.631032562821
    _temp_39 = -15.617984932123
    _temp_40 = -35.0296637727237
    _temp_41 = -29.3694482045528
    _temp_42 = -21.1422739609482
    _temp_43 = -18.3128322644193
    _temp_44 = -1.01154271644243
    _temp_45 = 23.5932988341615
    _temp_46 = 7.88077387034148
    _temp_47 = 66.7172474455795
    _temp_48 = 31.4803002892262
    _temp_49 = -243.161733465237
    _temp_50 = -65.2087419759485
    _temp_51 = -140.512404026946
    _temp_52 = -252.41169661647
    _temp_53 = -44.7376959343932
    _temp_54 = 69.3065219421853
    _temp_55 = 3.44387599824256
    _temp_56 = -69.722401732233
    _temp_57 = -133.883888979285
    _temp_58 = -63.6884255101074
    _temp_59 = -45.8665662031976
    _temp_60 = -22.3655491288733
    _temp_61 = -55.0290029548017
    _temp_62 = -21.3043441033647
    _temp_63 = 17.2194793002477
    _temp_64 = 15.580414212195
    _temp_65 = -0.170713424487596
    _temp_66 = -149.940682661175
    _temp_67 = 12.3249359493102
    _temp_68 = 211.270227661076
    _temp_69 = -51.799728742474
    _temp_70 = 12.065831947574
    _temp_71 = 140.905749116177
    _temp_72 = -181.912182396136
    _temp_73 = 42.5841339142755
    _temp_74 = 241.065484343466
    _temp_75 = 186.206250135106
    _temp_76 = -0.00643636925356628
    _temp_77 = -85.7197576465036
    _temp_78 = -23.7873404188627
    _temp_79 = 19.0257314344378
    _temp_80 = 25.0220013676658
    _temp_81 = 11.3736578267723
    _temp_82 = -116.406861919603
    _temp_83 = 97.6991088462623
    _temp_84 = -166.773649873666
    _temp_85 = 130.408694729012
    _temp_86 = -206.284633724103
    _temp_87 = 93.9910674114924
    _temp_88 = 100.193443746278
    _temp_89 = -62.8170753592769
    _temp_90 = 2.55302009475118
    _temp_91 = -42.9599486026964
    _temp_92 = -9.41185387913965
    _temp_93 = 11.6464058890251
    _temp_94 = 0.194912157394336
    _temp_95 = 18.3925868755078
    _temp_96 = 67.1474579582369
    _temp_97 = 55.2736216141312
    _temp_98 = -27.6057673787891
    _temp_99 = -3.33028925091375
    _temp_100 = 14.6586388115038
    _temp_101 = -7.04948499927892
    _temp_102 = -196.198980005795
    _temp_103 = 253.424821393084
    _temp_104 = 105.359474287732
    _temp_105 = -4.42398604391544
    _temp_106 = -9.31432502564133
    _temp_107 = 2.07506468394092
    _temp_108 = -4.540848711062
    _temp_109 = 6.24469940340222
    _temp_110 = 4.60105208359093
    _temp_111 = -8.32208392806949
    _temp_112 = -14.5321773686619
    _temp_113 = 7.40197646672975
    _temp_114 = -45.9812285827875
    _temp_115 = 6.61023974076788
    _temp_116 = -7.66695041280378
    _temp_117 = 2.9645843185016
    _temp_118 = 1.60881043632438
    _temp_119 = 11.0357759561899
    _temp_120 = -2.8187120757919
    _temp_121 = -10.3872025113633
    _temp_122 = -14.3951969522469
    _temp_123 = 17.7678015167647
    _temp_124 = 14.0009618318628
    _temp_125 = -29.0666495401949
    _temp_126 = -8.84579100271618
    _temp_127 = 21.723753732028
    _temp_128 = 8.32058758843077
    _temp_129 = 55.0452386943122
    _temp_130 = 3.66465772089312
    _temp_131 = 34.2907329217286
    _temp_132 = -6.79370412421557
    _temp_133 = -16.6862175589724
    _temp_134 = 29.7348974594074
    _temp_135 = 38.2110421075204
    _temp_136 = 18.347342151039
    _temp_137 = 32.1283733543
    _temp_138 = 1.03803522794397
    _temp_139 = -18.2368429818202
    _temp_140 = 25.4954085002973
    _temp_141 = 31.2738906202712
    _temp_142 = -30.234301026128
    _temp_143 = -32.7752498983915
    _temp_144 = 408.161243170639
    _temp_145 = -45.3811842284785
    _temp_146 = 242.225952813814
    _temp_147 = -36.9273150613427
    _temp_148 = -32.1442446371761
    _temp_149 = 44.8599517631383
    _temp_150 = -46.6352981098403
    _temp_151 = -31.1490775126797
    _temp_152 = 0.622372847409909
    _temp_153 = -34.0199749147997
    _temp_154 = 4.45788433312526
    _temp_155 = -19.6790167385795
    _temp_156 = 102.727613217327
    _temp_157 = -48.7917557098983
    _temp_158 = -20.3105303635175
    _temp_159 = 42.9204433318938
    _temp_160 = 25.092655266067
    _temp_161 = -15.8141592362961
    _temp_162 = 4.89947949808036
    _temp_163 = -26.7636446020529
    _temp_164 = -9.50503731518844
    _temp_165 = -23.5463634067707
    _temp_166 = -22.0572035535871
    _temp_167 = -52.5205633577331
    _temp_168 = -10.4906025177025
    _temp_169 = 42.9972661425186
    _temp_170 = 5.92819169532722
    _temp_171 = -13.6324734436937
    _temp_172 = -57.2724987327886
    _temp_173 = -17.0239634947127
    _temp_174 = 24.9406241423969
    _temp_175 = 5.16051522763883
    _temp_176 = 6.246983569906
    _temp_177 = 20.1458542621035
    _temp_178 = 33.935084080828
    _temp_179 = 3.62534147563799
    _temp_180 = -37.4241581096508
    _temp_181 = -9.28336643110562
    _temp_182 = -14.8883579653166
    _temp_183 = 40.6837290366489
    _temp_184 = 37.0867588778941
    _temp_185 = -47.9949157250003
    _temp_186 = 36.289557320393
    _temp_187 = -2.48594646059872
    _temp_188 = 14.3131137885724
    _temp_189 = 14.4701679669039
    _temp_190 = 17.7519248260423
    _temp_191 = -47.9844592998282
    _temp_192 = -4.23030065546895
    _temp_193 = 22.0572893490762
    _temp_194 = -56.3558848969997
    _temp_195 = 2.08717463111406
    _temp_196 = -20.7656381356955
    _temp_197 = 4.29090810385082
    _temp_198 = 10.1394678979224
    _temp_199 = 74.3809366165842
    _temp_200 = 50.1220704486095
    _temp_201 = 17.0764414739472
    _temp_202 = -13.5409326605749
    _temp_203 = 66.2641474377867
    _temp_204 = -83.7188622604945
    _temp_205 = -9.60152962594178
    _temp_206 = -62.0865450114838
    _temp_207 = -26.4880223535628
    _temp_208 = -30.5686394780022
    _temp_209 = 10.8134102427591
    _temp_210 = -1.23367634592404
    _temp_211 = -0.349930219284191
    _temp_212 = 28.147777763152
    _temp_213 = 3.89366113023881

    _temp_0 += 0.914801970409657 * indata[u"BestOutofSelfTotal"]
    _temp_0 += -7.06578195557337 * indata[u"Skills_Y"]
    _temp_0 += -13.4020178106094 * indata[u"SleepQuality"]
    _temp_0 += -338.777117132792 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_0 += -0.752134688815608 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_0 += 8.48298574789167 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_0 += 0.151057122472173 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_0 += 1.19136190441513 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_0 += 4.91978374374234 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_1 = tanh(_temp_0)

    _temp_1 += -1.22890473070897 * indata[u"BestOutofSelfTotal"]
    _temp_1 += -6.4791134410283 * indata[u"Skills_Y"]
    _temp_1 += 2.16815088579209 * indata[u"SleepQuality"]
    _temp_1 += -772.930393825031 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_1 += -3.54663010876778 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_1 += 3.78771153731488 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_1 += -0.0402861415386581 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_1 += 0.111547054006793 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_1 += -4.18463460146889 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_2 = tanh(_temp_1)

    _temp_2 += 2.81054892739491 * indata[u"BestOutofSelfTotal"]
    _temp_2 += 7.5146546888376 * indata[u"Skills_Y"]
    _temp_2 += 1.21352021334999 * indata[u"SleepQuality"]
    _temp_2 += -138.266288008422 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_2 += 34.0011812618413 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_2 += -31.6690417584183 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_2 += -0.102358638033018 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_2 += -2.98121110604573 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_2 += 4.83963156164112 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_3 = tanh(_temp_2)

    _temp_3 += -0.385369602346419 * indata[u"BestOutofSelfTotal"]
    _temp_3 += -0.847601876156751 * indata[u"Skills_Y"]
    _temp_3 += 1.21113048161586 * indata[u"SleepQuality"]
    _temp_3 += 129.701469435249 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_3 += 2.85487424984701 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_3 += -15.1877243364317 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_3 += 0.000140610423792553 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_3 += -0.673995509061369 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_3 += -0.702232822002232 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_4 = tanh(_temp_3)

    _temp_4 += 0.885624538971398 * indata[u"BestOutofSelfTotal"]
    _temp_4 += 2.15280401864784 * indata[u"Skills_Y"]
    _temp_4 += -1.01448406144689 * indata[u"SleepQuality"]
    _temp_4 += -136.238252740688 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_4 += 15.2298974493379 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_4 += 6.47740353552748 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_4 += 0.000147067799153192 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_4 += -2.15111566540403 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_4 += 1.12710550838125 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_5 = tanh(_temp_4)

    _temp_5 += -0.118404602727154 * indata[u"BestOutofSelfTotal"]
    _temp_5 += 0.443250468705249 * indata[u"Skills_Y"]
    _temp_5 += -2.68903714107467 * indata[u"SleepQuality"]
    _temp_5 += 447.738968164061 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_5 += 5.03958771536779 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_5 += -19.2914879840919 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_5 += 0.000857754261813725 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_5 += -2.43084562533282 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_5 += 1.66404809217391 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_6 = tanh(_temp_5)

    _temp_6 += -0.195762923188991 * indata[u"BestOutofSelfTotal"]
    _temp_6 += 10.7875201156818 * indata[u"Skills_Y"]
    _temp_6 += 3.85081150684221 * indata[u"SleepQuality"]
    _temp_6 += -92.8270128950247 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_6 += 18.1551573348496 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_6 += 12.4835290881546 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_6 += -1.77240987922024 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_6 += -4.69109493892851 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_6 += 9.35845423080194 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_7 = tanh(_temp_6)

    _temp_7 += 1.48521232498627 * indata[u"BestOutofSelfTotal"]
    _temp_7 += -0.857467841854234 * indata[u"Skills_Y"]
    _temp_7 += -2.58973572897251 * indata[u"SleepQuality"]
    _temp_7 += 1345.55274135416 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_7 += 3.88759768340521 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_7 += 84.7725223707831 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_7 += 0.919761006167769 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_7 += 0.142591331957406 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_7 += 2.88919135957497 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_8 = tanh(_temp_7)

    _temp_8 += -2.34723967012974 * indata[u"BestOutofSelfTotal"]
    _temp_8 += 3.71338714606804 * indata[u"Skills_Y"]
    _temp_8 += -5.90727881697588 * indata[u"SleepQuality"]
    _temp_8 += 401.295681363871 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_8 += -22.0200634978306 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_8 += -11.2101691095014 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_8 += -0.213340438386114 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_8 += 2.4139376985793 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_8 += 11.4763718635463 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_9 = tanh(_temp_8)

    _temp_9 += -0.11649266584927 * indata[u"BestOutofSelfTotal"]
    _temp_9 += -4.76335423282266 * indata[u"Skills_Y"]
    _temp_9 += 3.074005690283 * indata[u"SleepQuality"]
    _temp_9 += -912.553866306177 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_9 += 44.2310433760161 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_9 += -81.355345884746 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_9 += 0.0625907876362119 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_9 += 1.84411263348253 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_9 += -2.62218873160959 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_10 = tanh(_temp_9)

    _temp_10 += 1.62264815083503 * indata[u"BestOutofSelfTotal"]
    _temp_10 += 0.52994746685306 * indata[u"Skills_Y"]
    _temp_10 += 3.340251032917 * indata[u"SleepQuality"]
    _temp_10 += -104.642730931844 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_10 += 11.0552909016011 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_10 += -37.6124404566207 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_10 += -0.350875006199012 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_10 += 0.0167940493610358 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_10 += 2.27799979619404 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_11 = tanh(_temp_10)

    _temp_11 += 1.42699356956132 * indata[u"BestOutofSelfTotal"]
    _temp_11 += -9.0847536689104 * indata[u"Skills_Y"]
    _temp_11 += -0.987664946608412 * indata[u"SleepQuality"]
    _temp_11 += -49.9519348599941 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_11 += 39.5947931168677 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_11 += -22.2587808424306 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_11 += 0.937406034530566 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_11 += 2.59629198924331 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_11 += -0.612926182490682 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_12 = tanh(_temp_11)

    _temp_12 += 1.65447783546982 * indata[u"BestOutofSelfTotal"]
    _temp_12 += 2.14982308456406 * indata[u"Skills_Y"]
    _temp_12 += 2.27944281245232 * indata[u"SleepQuality"]
    _temp_12 += -158.585164739754 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_12 += 17.5250818319782 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_12 += 27.7518778881833 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_12 += 0.527161550410633 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_12 += -2.32603075420606 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_12 += -6.35507166556166 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_13 = tanh(_temp_12)

    _temp_13 += 1.60110711620003 * indata[u"BestOutofSelfTotal"]
    _temp_13 += -0.449899209777352 * indata[u"Skills_Y"]
    _temp_13 += -1.77706601047058 * indata[u"SleepQuality"]
    _temp_13 += 684.269478223828 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_13 += -0.0274586050824831 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_13 += 38.8177559572223 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_13 += 0.262343815435124 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_13 += 0.289868510257863 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_13 += 2.1408490966992 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_14 = tanh(_temp_13)

    _temp_14 += -0.00519828768859541 * indata[u"BestOutofSelfTotal"]
    _temp_14 += 0.67258791261913 * indata[u"Skills_Y"]
    _temp_14 += 5.21733011524785 * indata[u"SleepQuality"]
    _temp_14 += -124.319728115561 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_14 += -6.74013411879819 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_14 += 10.6775258363489 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_14 += -0.278424503906096 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_14 += -3.16625449249644 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_14 += 7.37597972236213 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_15 = tanh(_temp_14)

    _temp_15 += 0.605569263336524 * indata[u"BestOutofSelfTotal"]
    _temp_15 += 3.2629079970277 * indata[u"Skills_Y"]
    _temp_15 += -1.35821266900354 * indata[u"SleepQuality"]
    _temp_15 += 568.362971572795 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_15 += 7.97702276156941 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_15 += 46.816015021027 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_15 += -0.0101652939649845 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_15 += 0.381947326495506 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_15 += -2.00032913501904 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_16 = tanh(_temp_15)

    _temp_16 += -1.19303595502847 * indata[u"BestOutofSelfTotal"]
    _temp_16 += -6.24984749081532 * indata[u"Skills_Y"]
    _temp_16 += -0.235985684414945 * indata[u"SleepQuality"]
    _temp_16 += -242.78606806256 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_16 += -25.2508402847542 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_16 += -20.3634914790304 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_16 += -0.00178277456454895 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_16 += 2.05302615694161 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_16 += -1.0958750097887 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_17 = tanh(_temp_16)

    _temp_17 += 0.202112261308501 * indata[u"BestOutofSelfTotal"]
    _temp_17 += -5.56172803330821 * indata[u"Skills_Y"]
    _temp_17 += 1.42172423110776 * indata[u"SleepQuality"]
    _temp_17 += 183.708102991023 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_17 += 12.4178346320167 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_17 += -33.6791659307109 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_17 += -0.00241725755682678 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_17 += -1.4485535457036 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_17 += 2.01113886102835 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_18 = tanh(_temp_17)

    _temp_18 += -0.039708382690761 * indata[u"BestOutofSelfTotal"]
    _temp_18 += -0.0449219916097058 * indata[u"Skills_Y"]
    _temp_18 += -0.0900947907674176 * indata[u"SleepQuality"]
    _temp_18 += 9.37658289316447 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_18 += -0.389322626948166 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_18 += -0.300912428721528 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_18 += 0.00925839176055882 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_18 += 0.230505172915638 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_18 += 0.17279395480121 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_19 = tanh(_temp_18)

    _temp_19 += -0.102720548806294 * indata[u"BestOutofSelfTotal"]
    _temp_19 += 0.466924518712276 * indata[u"Skills_Y"]
    _temp_19 += 0.0645834103634683 * indata[u"SleepQuality"]
    _temp_19 += -16.9107584803065 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_19 += 0.124900562498873 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_19 += 0.314670771415273 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_19 += -0.00881043385598638 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_19 += 0.155814634637703 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_19 += 0.0185874062612018 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_20 = tanh(_temp_19)

    _temp_20 += -0.178276449273539 * indata[u"BestOutofSelfTotal"]
    _temp_20 += 0.558682002629501 * indata[u"Skills_Y"]
    _temp_20 += -0.13421823952081 * indata[u"SleepQuality"]
    _temp_20 += 0.7417986541666 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_20 += -1.33966000806412 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_20 += 1.05107475532203 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_20 += 0.0231052300398932 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_20 += 0.677715256637351 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_20 += 0.115623606942634 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_21 = tanh(_temp_20)

    _temp_21 += -0.558031140974794 * indata[u"BestOutofSelfTotal"]
    _temp_21 += -3.09853138208857 * indata[u"Skills_Y"]
    _temp_21 += -1.02599552981786 * indata[u"SleepQuality"]
    _temp_21 += -19.356792336075 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_21 += -1.89199222445092 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_21 += -0.219669978659795 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_21 += -0.0592573103211379 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_21 += 0.206045094301043 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_21 += -3.82733254315824 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_22 = tanh(_temp_21)

    _temp_22 += 0.362686947728043 * indata[u"BestOutofSelfTotal"]
    _temp_22 += 3.27278567121415 * indata[u"Skills_Y"]
    _temp_22 += 0.0692023671684737 * indata[u"SleepQuality"]
    _temp_22 += 367.473107112209 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_22 += -1.85414129199564 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_22 += 28.624090480729 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_22 += 0.382768171917181 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_22 += 0.0585760568097851 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_22 += 2.16703874137422 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_23 = tanh(_temp_22)

    _temp_23 += 0.563975019412972 * indata[u"BestOutofSelfTotal"]
    _temp_23 += -3.92012689937117 * indata[u"Skills_Y"]
    _temp_23 += -4.5114036089304 * indata[u"SleepQuality"]
    _temp_23 += -182.628285062779 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_23 += -3.83805506113691 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_23 += -11.4378701922708 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_23 += -0.400985565321443 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_23 += 1.91747154244566 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_23 += 2.24065192693457 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_24 = tanh(_temp_23)

    _temp_24 += 0.15695963750464 * indata[u"BestOutofSelfTotal"]
    _temp_24 += 0.430989225019745 * indata[u"Skills_Y"]
    _temp_24 += -0.136440723808202 * indata[u"SleepQuality"]
    _temp_24 += -57.2282808810157 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_24 += -1.67347617214097 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_24 += 4.31627196902862 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_24 += -0.0811475452372707 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_24 += 0.281941930407699 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_24 += 0.143413953988888 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_25 = tanh(_temp_24)

    _temp_25 += -0.179182231884586 * indata[u"BestOutofSelfTotal"]
    _temp_25 += -0.160112887262703 * indata[u"Skills_Y"]
    _temp_25 += -0.12635200605808 * indata[u"SleepQuality"]
    _temp_25 += -63.6556919970857 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_25 += -4.45845999536277 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_25 += 5.0161950442352 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_25 += 0.0413807749885167 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_25 += 0.399775392535165 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_25 += -0.534765247043911 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_26 = tanh(_temp_25)

    _temp_26 += -0.220295803041233 * indata[u"BestOutofSelfTotal"]
    _temp_26 += -0.409558065655232 * indata[u"Skills_Y"]
    _temp_26 += -0.11900660724509 * indata[u"SleepQuality"]
    _temp_26 += 27.1286607399071 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_26 += -2.1789489605405 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_26 += 1.82667915216971 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_26 += 0.0820383060548833 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_26 += 0.166730382209621 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_26 += -0.49085987473746 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_27 = tanh(_temp_26)

    _temp_27 += 2.1039836780617 * indata[u"BestOutofSelfTotal"]
    _temp_27 += 1.95231067792228 * indata[u"Skills_Y"]
    _temp_27 += -8.7532954023108 * indata[u"SleepQuality"]
    _temp_27 += -260.524701487059 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_27 += 30.4325799554665 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_27 += -50.1122196030257 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_27 += -0.116951789277343 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_27 += 4.68449916415111 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_27 += 1.93087173057318 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_28 = tanh(_temp_27)

    _temp_28 += -1.16806838304961 * indata[u"BestOutofSelfTotal"]
    _temp_28 += -9.61994275312303 * indata[u"Skills_Y"]
    _temp_28 += -0.9624863919504 * indata[u"SleepQuality"]
    _temp_28 += 66.6802199782023 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_28 += 43.4290913821901 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_28 += 35.7559726231668 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_28 += 0.0372982792162504 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_28 += 0.0189558408714997 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_28 += -2.84053214481105 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_29 = tanh(_temp_28)

    _temp_29 += 0.394348537871841 * indata[u"BestOutofSelfTotal"]
    _temp_29 += 1.01970359275331 * indata[u"Skills_Y"]
    _temp_29 += 0.315100852007454 * indata[u"SleepQuality"]
    _temp_29 += -119.169862224686 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_29 += 4.58456255810114 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_29 += -15.8339402863518 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_29 += -0.0328411083647833 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_29 += -1.04181367501739 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_29 += 1.45454846045003 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_30 = tanh(_temp_29)

    _temp_30 += -0.845142246835226 * indata[u"BestOutofSelfTotal"]
    _temp_30 += 8.35293131056506 * indata[u"Skills_Y"]
    _temp_30 += 1.04448971285898 * indata[u"SleepQuality"]
    _temp_30 += 232.465927608991 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_30 += 6.35238109568132 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_30 += -6.29967152745728 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_30 += -0.0946260694425276 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_30 += 1.16981657609047 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_30 += 0.675013145465499 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_31 = tanh(_temp_30)

    _temp_31 += -0.289809178536421 * indata[u"BestOutofSelfTotal"]
    _temp_31 += -0.560054650361159 * indata[u"Skills_Y"]
    _temp_31 += 0.179588102835457 * indata[u"SleepQuality"]
    _temp_31 += 93.174039632051 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_31 += 5.73874172243248 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_31 += -2.61980630075302 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_31 += -0.0198171512857492 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_31 += -0.204776015535727 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_31 += 0.394018962643836 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_32 = tanh(_temp_31)

    _temp_32 += 0.104811804772338 * indata[u"BestOutofSelfTotal"]
    _temp_32 += 2.7375203819497 * indata[u"Skills_Y"]
    _temp_32 += -0.611487267978753 * indata[u"SleepQuality"]
    _temp_32 += 10.3578199710661 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_32 += -8.36039792025261 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_32 += 8.51675309607174 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_32 += 0.0233362761955763 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_32 += 1.08645435065138 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_32 += -0.510749544474681 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_33 = tanh(_temp_32)

    _temp_33 += 0.406247291484285 * indata[u"BestOutofSelfTotal"]
    _temp_33 += 5.00535377475333 * indata[u"Skills_Y"]
    _temp_33 += -1.79033541120309 * indata[u"SleepQuality"]
    _temp_33 += -168.96250700474 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_33 += 0.900184619535077 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_33 += 26.547698620529 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_33 += -0.032399462646248 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_33 += 1.34395707411732 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_33 += -1.44706959345473 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_34 = tanh(_temp_33)

    _temp_34 += 1.25889492260915 * indata[u"BestOutofSelfTotal"]
    _temp_34 += 6.38025361648169 * indata[u"Skills_Y"]
    _temp_34 += -1.80226665862974 * indata[u"SleepQuality"]
    _temp_34 += -540.481470314192 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_34 += 37.8255456661873 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_34 += 52.7599796462851 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_34 += 0.00336365953409783 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_34 += 0.0643120853494944 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_34 += -2.15743839368456 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_35 = tanh(_temp_34)

    _temp_35 += 1.03413528552237 * indata[u"BestOutofSelfTotal"]
    _temp_35 += -4.04008481689581 * indata[u"Skills_Y"]
    _temp_35 += -2.97555974089224 * indata[u"SleepQuality"]
    _temp_35 += 103.229331358333 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_35 += 7.45801937517693 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_35 += 19.8411718000146 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_35 += 0.00393462086998913 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_35 += 2.86448933073278 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_35 += -1.34192499481294 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_36 = tanh(_temp_35)

    _temp_36 += -0.527709705443537 * indata[u"BestOutofSelfTotal"]
    _temp_36 += -3.78899412844934 * indata[u"Skills_Y"]
    _temp_36 += -1.85942160926504 * indata[u"SleepQuality"]
    _temp_36 += -84.5843500177094 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_36 += -0.766630356142965 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_36 += 0.938340186951271 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_36 += -0.0354697118854909 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_36 += -0.480210967232723 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_36 += 3.03194167109652 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_37 = tanh(_temp_36)

    _temp_37 += 0.790636307196535 * indata[u"BestOutofSelfTotal"]
    _temp_37 += -9.19791743812352 * indata[u"Skills_Y"]
    _temp_37 += -1.2536178858929 * indata[u"SleepQuality"]
    _temp_37 += -37.5304947439165 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_37 += -7.57545914390355 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_37 += 13.9812148745721 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_37 += -0.13195478592893 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_37 += -0.838469228662719 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_37 += -0.690686969213826 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_38 = tanh(_temp_37)

    _temp_38 += -0.827177509324798 * indata[u"BestOutofSelfTotal"]
    _temp_38 += -7.65003157995908 * indata[u"Skills_Y"]
    _temp_38 += -0.652040378154468 * indata[u"SleepQuality"]
    _temp_38 += -95.4150111634735 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_38 += 2.70942828693187 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_38 += 17.8317151188634 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_38 += 0.0155299654808335 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_38 += -2.19622334761812 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_38 += 4.11784067550652 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_39 = tanh(_temp_38)

    _temp_39 += 0.169601381553888 * indata[u"BestOutofSelfTotal"]
    _temp_39 += -1.40174489188149 * indata[u"Skills_Y"]
    _temp_39 += -0.146303870958639 * indata[u"SleepQuality"]
    _temp_39 += 34.2937521559575 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_39 += -0.592209048963115 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_39 += 2.79990003884853 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_39 += -0.00983624564012424 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_39 += 0.112795459807768 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_39 += -0.123687496756868 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_40 = tanh(_temp_39)

    _temp_40 += 0.327567684762623 * indata[u"BestOutofSelfTotal"]
    _temp_40 += 3.54673853066574 * indata[u"Skills_Y"]
    _temp_40 += -0.231290133265714 * indata[u"SleepQuality"]
    _temp_40 += 113.308275002621 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_40 += 3.78587127414669 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_40 += -8.7581530003448 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_40 += 0.179591663008524 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_40 += -0.524270789776044 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_40 += -2.22294308357601 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_41 = tanh(_temp_40)

    _temp_41 += 0.474653913229101 * indata[u"BestOutofSelfTotal"]
    _temp_41 += 1.26769477903849 * indata[u"Skills_Y"]
    _temp_41 += 0.995959736183647 * indata[u"SleepQuality"]
    _temp_41 += 60.0840159835399 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_41 += 4.89686529742373 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_41 += -3.11072815899906 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_41 += 0.189367399137403 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_41 += -0.505909959511624 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_41 += -2.43464401500511 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_42 = tanh(_temp_41)

    _temp_42 += 0.101285417420003 * indata[u"BestOutofSelfTotal"]
    _temp_42 += -0.208360049906505 * indata[u"Skills_Y"]
    _temp_42 += 0.172976214407725 * indata[u"SleepQuality"]
    _temp_42 += 43.5453304019762 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_42 += 0.780930499453815 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_42 += 1.74277793706296 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_42 += 0.0244339461831138 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_42 += -0.488427500678782 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_42 += -0.454807617291009 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_43 = tanh(_temp_42)

    _temp_43 += -0.143097573400776 * indata[u"BestOutofSelfTotal"]
    _temp_43 += -0.125004341443289 * indata[u"Skills_Y"]
    _temp_43 += 0.458543385680998 * indata[u"SleepQuality"]
    _temp_43 += 65.502151047449 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_43 += 1.73827974894508 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_43 += -4.64364278248571 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_43 += -0.00141904244611658 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_43 += 0.533246755439833 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_43 += 0.279458733011273 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_44 = tanh(_temp_43)

    _temp_44 += 0.0543833855259598 * indata[u"BestOutofSelfTotal"]
    _temp_44 += -0.00908865091699213 * indata[u"Skills_Y"]
    _temp_44 += -0.156646394631143 * indata[u"SleepQuality"]
    _temp_44 += -3.34374812217411 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_44 += -0.606359662768713 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_44 += 1.82520722904474 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_44 += 0.00272850287215204 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_44 += -0.188696899635465 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_44 += -0.1788364516164 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_45 = tanh(_temp_44)

    _temp_45 += 0.416233704261052 * indata[u"BestOutofSelfTotal"]
    _temp_45 += 2.41837229057997 * indata[u"Skills_Y"]
    _temp_45 += 0.1041968925047 * indata[u"SleepQuality"]
    _temp_45 += -162.741019270628 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_45 += -8.23295495198354 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_45 += 23.4737902136261 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_45 += -0.00655469624284617 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_45 += -0.524262090831244 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_45 += -1.81760112085843 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_46 = tanh(_temp_45)

    _temp_46 += 0.0996386576531866 * indata[u"BestOutofSelfTotal"]
    _temp_46 += -1.13910524602315 * indata[u"Skills_Y"]
    _temp_46 += -0.635972902245977 * indata[u"SleepQuality"]
    _temp_46 += -35.7547350550571 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_46 += -2.4210944103734 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_46 += 6.4230184555246 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_46 += -0.01756180496126 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_46 += -0.151295388890759 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_46 += -1.27594309563181 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_47 = tanh(_temp_46)

    _temp_47 += -0.338576685365585 * indata[u"BestOutofSelfTotal"]
    _temp_47 += -4.32052998537469 * indata[u"Skills_Y"]
    _temp_47 += 1.16600160120261 * indata[u"SleepQuality"]
    _temp_47 += -45.896454436066 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_47 += 1.36173036973796 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_47 += -32.0133550487833 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_47 += -0.0950013668853379 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_47 += -0.245504397261544 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_47 += -0.311999782740745 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_48 = tanh(_temp_47)

    _temp_48 += 1.62166109780278 * indata[u"BestOutofSelfTotal"]
    _temp_48 += -36.9248067330114 * indata[u"Skills_Y"]
    _temp_48 += -30.2590470943053 * indata[u"SleepQuality"]
    _temp_48 += 59.0090332808616 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_48 += 7.53708043074562 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_48 += 52.0039313818768 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_48 += -1.69860550982998 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_48 += 8.89004614484522 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_48 += 13.5103181656406 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_49 = tanh(_temp_48)

    _temp_49 += 1.01164506441394 * indata[u"BestOutofSelfTotal"]
    _temp_49 += -0.395669056380264 * indata[u"Skills_Y"]
    _temp_49 += 1.67705188762912 * indata[u"SleepQuality"]
    _temp_49 += 472.485608545859 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_49 += 36.9441769493784 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_49 += 7.16108606807902 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_49 += 0.0394984916351361 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_49 += -0.943109004425092 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_49 += -16.8893386578104 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_50 = tanh(_temp_49)

    _temp_50 += -0.319471198685938 * indata[u"BestOutofSelfTotal"]
    _temp_50 += 14.8964026786426 * indata[u"Skills_Y"]
    _temp_50 += -0.150021499018375 * indata[u"SleepQuality"]
    _temp_50 += -298.425763809764 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_50 += 47.491187757813 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_50 += 53.7882778829818 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_50 += -0.022645108056578 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_50 += -10.0746235706983 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_50 += -26.7918130520654 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_51 = tanh(_temp_50)

    _temp_51 += 1.12862259893993 * indata[u"BestOutofSelfTotal"]
    _temp_51 += 9.61054536273958 * indata[u"Skills_Y"]
    _temp_51 += -4.56809941445943 * indata[u"SleepQuality"]
    _temp_51 += 477.725174942943 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_51 += -42.9362681932471 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_51 += 11.0889142410292 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_51 += -0.0340985660670773 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_51 += 5.23061371346451 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_51 += -1.81977984305919 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_52 = tanh(_temp_51)

    _temp_52 += -2.06308480818392 * indata[u"BestOutofSelfTotal"]
    _temp_52 += 5.15939508854181 * indata[u"Skills_Y"]
    _temp_52 += -1.4633877992159 * indata[u"SleepQuality"]
    _temp_52 += 875.291127819209 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_52 += -7.49748679204876 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_52 += -42.85605133244 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_52 += -0.528696838246011 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_52 += -0.745951384206055 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_52 += -5.60546297236784 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_53 = tanh(_temp_52)

    _temp_53 += -2.24915407264006 * indata[u"BestOutofSelfTotal"]
    _temp_53 += -2.76945483376078 * indata[u"Skills_Y"]
    _temp_53 += -1.15261495823066 * indata[u"SleepQuality"]
    _temp_53 += 98.1704662556354 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_53 += -14.4598800796132 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_53 += 17.0221960031355 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_53 += 0.090968896533582 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_53 += 1.75212740572173 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_53 += -3.45764875009314 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_54 = tanh(_temp_53)

    _temp_54 += -0.263281453547186 * indata[u"BestOutofSelfTotal"]
    _temp_54 += -6.09005359352739 * indata[u"Skills_Y"]
    _temp_54 += 1.09210303586997 * indata[u"SleepQuality"]
    _temp_54 += -13.8675289619528 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_54 += -28.6475604057443 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_54 += -23.0921853621669 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_54 += -0.102122367539691 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_54 += -2.50148638215624 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_54 += 2.42087604685763 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_55 = tanh(_temp_54)

    _temp_55 += 0.16758326650277 * indata[u"BestOutofSelfTotal"]
    _temp_55 += -5.45863019691561 * indata[u"Skills_Y"]
    _temp_55 += -0.643188822571489 * indata[u"SleepQuality"]
    _temp_55 += 161.727618639872 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_55 += -18.6794203005379 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_55 += -26.002439632527 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_55 += -0.0784049400585958 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_55 += -1.18515016494507 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_55 += 2.0665861991383 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_56 = tanh(_temp_55)

    _temp_56 += 0.15215056033716 * indata[u"BestOutofSelfTotal"]
    _temp_56 += 1.83165436755306 * indata[u"Skills_Y"]
    _temp_56 += -1.47978433915885 * indata[u"SleepQuality"]
    _temp_56 += 117.20516322906 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_56 += 3.43495386718421 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_56 += 16.7538181984665 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_56 += 0.0575813439968382 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_56 += 2.13327055131794 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_56 += -1.97527689561967 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_57 = tanh(_temp_56)

    _temp_57 += -0.290779135693905 * indata[u"BestOutofSelfTotal"]
    _temp_57 += -0.816693119763523 * indata[u"Skills_Y"]
    _temp_57 += -0.865928031446514 * indata[u"SleepQuality"]
    _temp_57 += 383.531040250185 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_57 += 1.62463238711455 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_57 += -0.718229658082367 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_57 += -0.0104900102943972 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_57 += -0.308848439926174 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_57 += 4.74321162480692 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_58 = tanh(_temp_57)

    _temp_58 += -0.119430312089288 * indata[u"BestOutofSelfTotal"]
    _temp_58 += -0.558341078808852 * indata[u"Skills_Y"]
    _temp_58 += -0.0171538182919654 * indata[u"SleepQuality"]
    _temp_58 += 209.455831892983 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_58 += -0.811886801670691 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_58 += -5.15963096399498 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_58 += -0.0220918155250327 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_58 += 0.126953986847453 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_58 += 3.52824365377615 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_59 = tanh(_temp_58)

    _temp_59 += 0.0995037946121231 * indata[u"BestOutofSelfTotal"]
    _temp_59 += -2.13585882105751 * indata[u"Skills_Y"]
    _temp_59 += 1.28844058149482 * indata[u"SleepQuality"]
    _temp_59 += 41.4160064469447 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_59 += 1.16948551950234 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_59 += 17.8383314424595 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_59 += -0.310816557110742 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_59 += 1.0224569933864 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_59 += 0.880386058241769 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_60 = tanh(_temp_59)

    _temp_60 += -0.25863048419162 * indata[u"BestOutofSelfTotal"]
    _temp_60 += 1.36855172670352 * indata[u"Skills_Y"]
    _temp_60 += 0.287829357189998 * indata[u"SleepQuality"]
    _temp_60 += -12.0189448164339 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_60 += 10.6034626386419 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_60 += 8.45949943318311 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_60 += 0.0245291979615872 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_60 += -0.47245018986935 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_60 += -0.265126933599575 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_61 = tanh(_temp_60)

    _temp_61 += -0.847338596803575 * indata[u"BestOutofSelfTotal"]
    _temp_61 += 2.79707606614827 * indata[u"Skills_Y"]
    _temp_61 += -0.383051719994528 * indata[u"SleepQuality"]
    _temp_61 += 98.0395841539994 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_61 += -8.06431316844482 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_61 += 22.2525027484631 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_61 += -0.00330600716535635 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_61 += 4.86743130520201 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_61 += 1.20184729129358 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_62 = tanh(_temp_61)

    _temp_62 += -0.246701012143071 * indata[u"BestOutofSelfTotal"]
    _temp_62 += -5.92313661655909 * indata[u"Skills_Y"]
    _temp_62 += 1.21727064917393 * indata[u"SleepQuality"]
    _temp_62 += 45.0426943647909 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_62 += -9.69433460624112 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_62 += 14.1167435313536 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_62 += -0.0139412250029145 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_62 += 1.83925673220965 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_62 += 9.05669739157398 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_63 = tanh(_temp_62)

    _temp_63 += 0.167401610705803 * indata[u"BestOutofSelfTotal"]
    _temp_63 += -0.235667848087261 * indata[u"Skills_Y"]
    _temp_63 += -0.141286766956737 * indata[u"SleepQuality"]
    _temp_63 += -48.5280019738981 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_63 += 2.17818435653781 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_63 += -0.841031820387038 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_63 += -0.0189911234750348 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_63 += -0.278409583433281 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_63 += -0.0153709881577541 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_64 = tanh(_temp_63)

    _temp_64 += 0.0259694567224302 * indata[u"BestOutofSelfTotal"]
    _temp_64 += 0.531511050414298 * indata[u"Skills_Y"]
    _temp_64 += -0.364708488302888 * indata[u"SleepQuality"]
    _temp_64 += -36.1638941554991 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_64 += -0.255312812774167 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_64 += -0.371751191817924 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_64 += -0.0035412121417647 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_64 += -0.457595120181379 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_64 += 0.0127951004465965 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_65 = tanh(_temp_64)

    _temp_65 += -0.312876036714396 * indata[u"BestOutofSelfTotal"]
    _temp_65 += 1.99288726640248 * indata[u"Skills_Y"]
    _temp_65 += 0.0928287965154657 * indata[u"SleepQuality"]
    _temp_65 += 22.667579978904 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_65 += -3.47873369895808 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_65 += -3.54339196276765 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_65 += 0.0203870867829901 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_65 += -0.590457242075717 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_65 += 0.393379275686259 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_66 = tanh(_temp_65)

    _temp_66 += 0.0125472316356667 * indata[u"BestOutofSelfTotal"]
    _temp_66 += -0.665851128696802 * indata[u"Skills_Y"]
    _temp_66 += -0.686754521994259 * indata[u"SleepQuality"]
    _temp_66 += 391.872320409336 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_66 += 4.63823565693689 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_66 += 5.5044365912155 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_66 += 0.195892445923053 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_66 += -1.09224135492227 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_66 += 4.24320816843997 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_67 = tanh(_temp_66)

    _temp_67 += 0.281857890170441 * indata[u"BestOutofSelfTotal"]
    _temp_67 += -0.67660322704532 * indata[u"Skills_Y"]
    _temp_67 += 0.919747228824938 * indata[u"SleepQuality"]
    _temp_67 += -25.0381113608772 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_67 += 4.65648480615548 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_67 += -6.60317138497671 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_67 += -0.0421733214397784 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_67 += -0.769348538695078 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_67 += 0.312179155184147 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_68 = tanh(_temp_67)

    _temp_68 += -0.624975459214985 * indata[u"BestOutofSelfTotal"]
    _temp_68 += 1.20533386116596 * indata[u"Skills_Y"]
    _temp_68 += 0.979575489541098 * indata[u"SleepQuality"]
    _temp_68 += -523.908383578208 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_68 += -6.92195601783722 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_68 += -12.3420709732694 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_68 += -0.530641351507957 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_68 += 1.2598170566872 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_68 += -4.15239675514525 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_69 = tanh(_temp_68)

    _temp_69 += -0.195997228094048 * indata[u"BestOutofSelfTotal"]
    _temp_69 += -1.68633770378786 * indata[u"Skills_Y"]
    _temp_69 += -0.575082432536811 * indata[u"SleepQuality"]
    _temp_69 += 105.42701061934 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_69 += -14.337530012087 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_69 += 16.8738004584398 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_69 += -0.135445663971765 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_69 += 0.947039497085708 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_69 += 0.0770208666626685 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_70 = tanh(_temp_69)

    _temp_70 += -0.640146243677839 * indata[u"BestOutofSelfTotal"]
    _temp_70 += -5.51116347704832 * indata[u"Skills_Y"]
    _temp_70 += 1.03477846327239 * indata[u"SleepQuality"]
    _temp_70 += -198.005133113668 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_70 += -2.85679327318925 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_70 += 40.6796874121595 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_70 += -0.139339669685857 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_70 += -0.488667666778763 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_70 += 5.10905212251839 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_71 = tanh(_temp_70)

    _temp_71 += -0.805614982128295 * indata[u"BestOutofSelfTotal"]
    _temp_71 += -1.43496851372562 * indata[u"Skills_Y"]
    _temp_71 += -0.177436795663357 * indata[u"SleepQuality"]
    _temp_71 += -385.309678112788 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_71 += -9.33559611233998 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_71 += 11.6780490020501 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_71 += 0.0442999849074863 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_71 += -0.541246673855394 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_71 += 7.7986307969673 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_72 = tanh(_temp_71)

    _temp_72 += 1.12043046279663 * indata[u"BestOutofSelfTotal"]
    _temp_72 += 3.17574088616725 * indata[u"Skills_Y"]
    _temp_72 += -2.34133645604449 * indata[u"SleepQuality"]
    _temp_72 += 639.495793075675 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_72 += 17.1521724015731 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_72 += -40.3829939676418 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_72 += 1.79281885829411 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_72 += -3.64786171721325 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_72 += -0.782902886800295 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_73 = tanh(_temp_72)

    _temp_73 += 0.875057692220826 * indata[u"BestOutofSelfTotal"]
    _temp_73 += 6.68128064094439 * indata[u"Skills_Y"]
    _temp_73 += 0.0497956259331022 * indata[u"SleepQuality"]
    _temp_73 += 98.6070302528722 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_73 += -5.46982560597552 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_73 += -45.0297591181745 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_73 += 0.825087380743855 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_73 += 1.1725917024701 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_73 += 1.07207713172529 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_74 = tanh(_temp_73)

    _temp_74 += -0.488052220385165 * indata[u"BestOutofSelfTotal"]
    _temp_74 += 4.96482132403067 * indata[u"Skills_Y"]
    _temp_74 += -1.48227414276292 * indata[u"SleepQuality"]
    _temp_74 += -547.568335898783 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_74 += -16.097818810618 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_74 += -7.91125065721885 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_74 += -0.140319940627206 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_74 += 0.365103923510451 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_74 += 8.06357668333262 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_75 = tanh(_temp_74)

    _temp_75 += 0.139787858233682 * indata[u"BestOutofSelfTotal"]
    _temp_75 += -2.9915691970306 * indata[u"Skills_Y"]
    _temp_75 += 1.18468550442013 * indata[u"SleepQuality"]
    _temp_75 += -374.375000423975 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_75 += 27.9287972053519 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_75 += -47.722421274062 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_75 += -0.0298820858298992 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_75 += -0.449125488693825 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_75 += -1.69244256941679 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_76 = tanh(_temp_75)

    _temp_76 += 0.59814117793195 * indata[u"BestOutofSelfTotal"]
    _temp_76 += 2.37306129625705 * indata[u"Skills_Y"]
    _temp_76 += 0.0279494081831232 * indata[u"SleepQuality"]
    _temp_76 += -41.2031091212105 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_76 += 5.35113027958331 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_76 += 4.98117474327283 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_76 += 0.164279979464045 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_76 += -0.114838473790372 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_76 += -0.0521917572742939 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_77 = tanh(_temp_76)

    _temp_77 += -0.093721268569042 * indata[u"BestOutofSelfTotal"]
    _temp_77 += 2.41347503461577 * indata[u"Skills_Y"]
    _temp_77 += -0.111559034491211 * indata[u"SleepQuality"]
    _temp_77 += 162.563663566948 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_77 += -20.8933412505296 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_77 += 28.2261706994541 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_77 += 0.0345253409126831 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_77 += -0.0368096481607442 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_77 += 1.78256074976967 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_78 = tanh(_temp_77)

    _temp_78 += 0.022355140040325 * indata[u"BestOutofSelfTotal"]
    _temp_78 += -0.96220941549716 * indata[u"Skills_Y"]
    _temp_78 += 0.376856829256324 * indata[u"SleepQuality"]
    _temp_78 += 27.58170848192 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_78 += 2.30748752815049 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_78 += 6.60078273128049 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_78 += 0.103670830763977 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_78 += 0.660871234179373 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_78 += -0.40807596932209 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_79 = tanh(_temp_78)

    _temp_79 += 0.100462690811633 * indata[u"BestOutofSelfTotal"]
    _temp_79 += -0.127208410379559 * indata[u"Skills_Y"]
    _temp_79 += -0.149382493627757 * indata[u"SleepQuality"]
    _temp_79 += -28.2156372926797 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_79 += 1.32317107582711 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_79 += -5.55330193624548 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_79 += -0.258862909700279 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_79 += 0.112526052091376 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_79 += -0.052279734797401 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_80 = tanh(_temp_79)

    _temp_80 += -0.138540587284453 * indata[u"BestOutofSelfTotal"]
    _temp_80 += 1.58929276199344 * indata[u"Skills_Y"]
    _temp_80 += 0.185802892849834 * indata[u"SleepQuality"]
    _temp_80 += -29.2412220589953 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_80 += -4.83069866496439 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_80 += -7.00004321355969 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_80 += 0.0939175966093432 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_80 += -1.3213103522029 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_80 += 1.05168806263627 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_81 = tanh(_temp_80)

    _temp_81 += -0.922495602031549 * indata[u"BestOutofSelfTotal"]
    _temp_81 += 4.1336482094506 * indata[u"Skills_Y"]
    _temp_81 += 0.464890215254241 * indata[u"SleepQuality"]
    _temp_81 += 4.54132595459806 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_81 += 2.74583277456294 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_81 += -10.9234892216959 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_81 += 0.0175622200789891 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_81 += -2.5413789295751 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_81 += 2.08129115209751 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_82 = tanh(_temp_81)

    _temp_82 += -0.594538755184971 * indata[u"BestOutofSelfTotal"]
    _temp_82 += 0.865621942688758 * indata[u"Skills_Y"]
    _temp_82 += -0.449348952925793 * indata[u"SleepQuality"]
    _temp_82 += 231.773343819644 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_82 += 5.4430685417198 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_82 += 14.4288522417944 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_82 += -0.000161036391556096 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_82 += -0.346216700844409 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_82 += -3.80746573541925 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_83 = tanh(_temp_82)

    _temp_83 += -0.277087979121715 * indata[u"BestOutofSelfTotal"]
    _temp_83 += 5.25172606393921 * indata[u"Skills_Y"]
    _temp_83 += -1.01018997814758 * indata[u"SleepQuality"]
    _temp_83 += -223.077245974318 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_83 += -3.00312519164257 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_83 += -6.63852273342335 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_83 += -0.175879427024578 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_83 += -1.35264887035796 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_83 += 5.24401993824096 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_84 = tanh(_temp_83)

    _temp_84 += -1.5792408511231 * indata[u"BestOutofSelfTotal"]
    _temp_84 += 2.5965621753764 * indata[u"Skills_Y"]
    _temp_84 += -2.65382953462883 * indata[u"SleepQuality"]
    _temp_84 += 678.742137956624 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_84 += -6.15502190699666 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_84 += -46.4208343340986 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_84 += 0.196837476899461 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_84 += -5.01175796645065 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_84 += 0.0107228611694193 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_85 = tanh(_temp_84)

    _temp_85 += 1.24906111168418 * indata[u"BestOutofSelfTotal"]
    _temp_85 += 6.30294685922044 * indata[u"Skills_Y"]
    _temp_85 += 4.80665790804765 * indata[u"SleepQuality"]
    _temp_85 += -527.546263242397 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_85 += 10.7694526622491 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_85 += 12.3518453349705 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_85 += 1.241528155935 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_85 += -1.92622359727567 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_85 += -11.19780700861 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_86 = tanh(_temp_85)

    _temp_86 += 0.240032280903974 * indata[u"BestOutofSelfTotal"]
    _temp_86 += 5.94331578588398 * indata[u"Skills_Y"]
    _temp_86 += -4.48892875047718 * indata[u"SleepQuality"]
    _temp_86 += 643.362009348781 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_86 += 16.2150764398644 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_86 += -29.0805662072788 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_86 += -0.0359436524719931 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_86 += -4.48035842355853 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_86 += -5.90264499944161 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_87 = tanh(_temp_86)

    _temp_87 += 1.11038535044049 * indata[u"BestOutofSelfTotal"]
    _temp_87 += -0.328204000617261 * indata[u"Skills_Y"]
    _temp_87 += -2.51470861371126 * indata[u"SleepQuality"]
    _temp_87 += -201.161682912632 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_87 += -13.5561499019328 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_87 += -2.93456213482751 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_87 += 0.488728387790213 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_87 += -2.58545001414601 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_87 += -0.192995196217538 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_88 = tanh(_temp_87)

    _temp_88 += 0.463359219720382 * indata[u"BestOutofSelfTotal"]
    _temp_88 += -7.10349644396564 * indata[u"Skills_Y"]
    _temp_88 += 0.220635304777957 * indata[u"SleepQuality"]
    _temp_88 += -7.89109595632906 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_88 += -36.1532553391438 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_88 += -36.7845660035739 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_88 += -0.074073570283676 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_88 += -2.64961563772259 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_88 += 3.42926007980839 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_89 = tanh(_temp_88)

    _temp_89 += -0.334300042835839 * indata[u"BestOutofSelfTotal"]
    _temp_89 += 3.92565800118246 * indata[u"Skills_Y"]
    _temp_89 += -1.24238787876464 * indata[u"SleepQuality"]
    _temp_89 += 65.5461566519545 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_89 += 5.77301428340864 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_89 += 22.4628380763863 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_89 += 0.0532540130044577 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_89 += 3.3413736061654 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_89 += -3.30325996602033 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_90 = tanh(_temp_89)

    _temp_90 += 0.0164797135962847 * indata[u"BestOutofSelfTotal"]
    _temp_90 += -1.06058364435794 * indata[u"Skills_Y"]
    _temp_90 += 0.1815910792785 * indata[u"SleepQuality"]
    _temp_90 += -16.7256730240396 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_90 += 0.778725339975166 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_90 += 2.19805865911478 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_90 += -0.0629702152608605 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_90 += 0.228485795779701 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_90 += 0.621457762890412 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_91 = tanh(_temp_90)

    _temp_91 += 0.152951566298828 * indata[u"BestOutofSelfTotal"]
    _temp_91 += -0.196846676396323 * indata[u"Skills_Y"]
    _temp_91 += -0.275854701132476 * indata[u"SleepQuality"]
    _temp_91 += 85.9597237864411 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_91 += -0.20271846868518 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_91 += 8.08799392380656 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_91 += -0.0615506585487758 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_91 += 0.299469356196916 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_91 += 0.372294854555594 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_92 = tanh(_temp_91)

    _temp_92 += 0.124071257139076 * indata[u"BestOutofSelfTotal"]
    _temp_92 += 0.655126038563186 * indata[u"Skills_Y"]
    _temp_92 += 0.252172976770336 * indata[u"SleepQuality"]
    _temp_92 += 22.9434818764935 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_92 += -0.712398501539343 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_92 += 0.0171263141602979 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_92 += -0.193133829802365 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_92 += 0.00952444177076056 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_92 += -0.382605555479439 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_93 = tanh(_temp_92)

    _temp_93 += -0.0462614331618712 * indata[u"BestOutofSelfTotal"]
    _temp_93 += 0.125421742873546 * indata[u"Skills_Y"]
    _temp_93 += 0.107286748253137 * indata[u"SleepQuality"]
    _temp_93 += -44.4092102457934 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_93 += 0.307370121902455 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_93 += 2.59940190077377 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_93 += 0.0529924042244825 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_93 += 0.245654853825434 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_93 += 0.0932638851830216 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_94 = tanh(_temp_93)

    _temp_94 += 0.0651503540188423 * indata[u"BestOutofSelfTotal"]
    _temp_94 += -0.731765813039942 * indata[u"Skills_Y"]
    _temp_94 += -0.0484905804175881 * indata[u"SleepQuality"]
    _temp_94 += -10.9332561708957 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_94 += 1.43045984704414 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_94 += 1.86766095744149 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_94 += 0.0776542910458163 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_94 += 0.252744053039007 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_94 += -0.139485724333975 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_95 = tanh(_temp_94)

    _temp_95 += 0.186964780990841 * indata[u"BestOutofSelfTotal"]
    _temp_95 += 0.0229329996066645 * indata[u"Skills_Y"]
    _temp_95 += 0.211479209339576 * indata[u"SleepQuality"]
    _temp_95 += -41.3295436747444 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_95 += 1.70869784258821 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_95 += -3.7450053333319 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_95 += -0.0744573916085652 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_95 += -0.322996883321843 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_95 += -0.11505675108052 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_96 = tanh(_temp_95)

    _temp_96 += 0.265245935608862 * indata[u"BestOutofSelfTotal"]
    _temp_96 += 0.824843803571707 * indata[u"Skills_Y"]
    _temp_96 += 0.208822583002121 * indata[u"SleepQuality"]
    _temp_96 += -148.298211962123 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_96 += -1.86604638669064 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_96 += -9.09568287061239 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_96 += -0.311851097774346 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_96 += 0.372349719040608 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_96 += -1.39365324226611 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_97 = tanh(_temp_96)

    _temp_97 += -0.259846548198974 * indata[u"BestOutofSelfTotal"]
    _temp_97 += 0.0199686698972359 * indata[u"Skills_Y"]
    _temp_97 += 0.38846628678791 * indata[u"SleepQuality"]
    _temp_97 += -129.262737117034 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_97 += 0.472051303853183 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_97 += -6.16845169279182 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_97 += -0.0996281385422319 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_97 += -0.191827209380494 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_97 += 0.466103124585295 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_98 = tanh(_temp_97)

    _temp_98 += 0.451254489201996 * indata[u"BestOutofSelfTotal"]
    _temp_98 += 0.17084873376486 * indata[u"Skills_Y"]
    _temp_98 += 0.527204630863456 * indata[u"SleepQuality"]
    _temp_98 += 25.6896268314573 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_98 += 3.62292253277623 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_98 += 5.98431858375883 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_98 += 0.0696158083089175 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_98 += -0.847917543412518 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_98 += -1.5143413700291 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_99 = tanh(_temp_98)

    _temp_99 += -0.00755607494080502 * indata[u"BestOutofSelfTotal"]
    _temp_99 += 0.203154358784303 * indata[u"Skills_Y"]
    _temp_99 += -0.0292242135043929 * indata[u"SleepQuality"]
    _temp_99 += 8.40504891289611 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_99 += -0.329161734580197 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_99 += 0.0279822801495189 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_99 += -0.117448087311589 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_99 += -0.187580406666283 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_99 += -0.00870320642258041 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_100 = tanh(_temp_99)

    _temp_100 += -0.0298132848153214 * indata[u"BestOutofSelfTotal"]
    _temp_100 += -0.173278875334717 * indata[u"Skills_Y"]
    _temp_100 += -0.0116040621335169 * indata[u"SleepQuality"]
    _temp_100 += -36.092665189753 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_100 += 0.540609191694725 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_100 += -0.962192736707192 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_100 += -0.0228525774182452 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_100 += 0.122688295269596 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_100 += 0.128912068560462 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_101 = tanh(_temp_100)

    _temp_101 += -0.00839013133082643 * indata[u"BestOutofSelfTotal"]
    _temp_101 += -0.12641910835136 * indata[u"Skills_Y"]
    _temp_101 += -0.107754586942664 * indata[u"SleepQuality"]
    _temp_101 += 15.7423270816007 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_101 += -0.453191896646393 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_101 += 1.36277178525676 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_101 += 0.0185342012552576 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_101 += 0.0783550996129138 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_101 += -0.0753976996003673 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_102 = tanh(_temp_101)

    _temp_102 += -0.520055996675287 * indata[u"BestOutofSelfTotal"]
    _temp_102 += -6.75454278815065 * indata[u"Skills_Y"]
    _temp_102 += 0.9838256366562 * indata[u"SleepQuality"]
    _temp_102 += 619.885509892433 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_102 += 15.8002533287231 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_102 += -29.6826279812707 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_102 += 0.304639734021541 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_102 += -0.559958391855746 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_102 += -1.35463737410092 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_103 = tanh(_temp_102)

    _temp_103 += 0.990769892622507 * indata[u"BestOutofSelfTotal"]
    _temp_103 += 4.31237072620718 * indata[u"Skills_Y"]
    _temp_103 += 1.79960085266721 * indata[u"SleepQuality"]
    _temp_103 += -526.798253867144 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_103 += 5.78408848469608 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_103 += -41.6347816281674 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_103 += -0.455191666154532 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_103 += -1.73999518473577 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_103 += 7.77440002091582 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_104 = tanh(_temp_103)

    _temp_104 += 1.14280290951718 * indata[u"BestOutofSelfTotal"]
    _temp_104 += 0.906593251004345 * indata[u"Skills_Y"]
    _temp_104 += -2.80580333983357 * indata[u"SleepQuality"]
    _temp_104 += -304.822512178918 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_104 += -10.8339570072518 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_104 += 11.9932453060796 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_104 += 0.121945637344146 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_104 += -1.36406669242227 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_104 += -1.63297839333324 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_105 = tanh(_temp_104)

    _temp_105 += 0.0315062850942018 * indata[u"BestOutofSelfTotal"]
    _temp_105 += -0.343792962122222 * indata[u"Skills_Y"]
    _temp_105 += 0.121918034999122 * indata[u"SleepQuality"]
    _temp_105 += 21.9692361761148 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_105 += -1.72586422336534 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_105 += -1.55578569303231 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_105 += 0.0619968999103829 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_105 += -0.148616732607713 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_105 += -0.105739926147855 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_106 = tanh(_temp_105)

    _temp_106 += 0.0333580098672235 * indata[u"BestOutofSelfTotal"]
    _temp_106 += 0.0432317806917785 * indata[u"Skills_Y"]
    _temp_106 += -0.0467273933100468 * indata[u"SleepQuality"]
    _temp_106 += 14.7980874142051 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_106 += 0.389693238757912 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_106 += 2.34362772305352 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_106 += 0.22519733374381 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_106 += 0.0380964292029398 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_106 += 0.0412981996474777 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_107 = tanh(_temp_106)

    _temp_107 += -0.0434994939430197 * indata[u"BestOutofSelfTotal"]
    _temp_107 += 0.065659760921023 * indata[u"Skills_Y"]
    _temp_107 += -0.208682760563333 * indata[u"SleepQuality"]
    _temp_107 += -1.39289727110328 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_107 += 0.587330978605426 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_107 += -0.981187864770971 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_107 += 0.0472806811083474 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_107 += -0.129712404752006 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_107 += -0.0275993857357144 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_108 = tanh(_temp_107)

    _temp_108 += -0.0162871152803999 * indata[u"BestOutofSelfTotal"]
    _temp_108 += -0.152116067028133 * indata[u"Skills_Y"]
    _temp_108 += -0.0585652131155444 * indata[u"SleepQuality"]
    _temp_108 += 11.4620591554013 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_108 += -0.249588379369704 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_108 += 0.543431305643531 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_108 += -0.0254417597448637 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_108 += 0.038163170465949 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_108 += -0.0445795168823163 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_109 = tanh(_temp_108)

    _temp_109 += 0.00402376885986163 * indata[u"BestOutofSelfTotal"]
    _temp_109 += 0.115827631987851 * indata[u"Skills_Y"]
    _temp_109 += 0.0973986635820842 * indata[u"SleepQuality"]
    _temp_109 += -16.4285545175042 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_109 += 0.359127052224017 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_109 += -0.55207891390082 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_109 += -0.00535491200125645 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_109 += -0.0295548774874813 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_109 += 0.047023384395657 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_110 = tanh(_temp_109)

    _temp_110 += -0.00347482759488284 * indata[u"BestOutofSelfTotal"]
    _temp_110 += 0.164605117209341 * indata[u"Skills_Y"]
    _temp_110 += 0.0760314326798639 * indata[u"SleepQuality"]
    _temp_110 += -10.0747475654647 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_110 += 0.0641924409291583 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_110 += -0.790448003418988 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_110 += 0.0347841923434174 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_110 += -0.0207555058276372 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_110 += 0.0250191784268776 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_111 = tanh(_temp_110)

    _temp_111 += 0.247567330269288 * indata[u"BestOutofSelfTotal"]
    _temp_111 += -0.604035079775172 * indata[u"Skills_Y"]
    _temp_111 += 0.799852835894053 * indata[u"SleepQuality"]
    _temp_111 += 10.8902923220481 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_111 += -3.13948573658643 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_111 += 2.4109278479197 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_111 += 0.463891803706421 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_111 += -0.59161817722469 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_111 += -0.218227539658329 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_112 = tanh(_temp_111)

    _temp_112 += 0.0816862032002998 * indata[u"BestOutofSelfTotal"]
    _temp_112 += -0.313965910416133 * indata[u"Skills_Y"]
    _temp_112 += -0.0535819449392271 * indata[u"SleepQuality"]
    _temp_112 += 64.483206094652 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_112 += -5.6661706749035 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_112 += -1.77387837181186 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_112 += 0.418826697231595 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_112 += -0.0321453944329901 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_112 += -0.0469196921847813 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_113 = tanh(_temp_112)

    _temp_113 += -0.147556468248431 * indata[u"BestOutofSelfTotal"]
    _temp_113 += -0.0466321561626496 * indata[u"Skills_Y"]
    _temp_113 += 0.0507225693586694 * indata[u"SleepQuality"]
    _temp_113 += 1.49418351084919 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_113 += -0.595418445790259 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_113 += -4.34517013598144 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_113 += -0.293573179965309 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_113 += -0.0870611606265937 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_113 += 0.373089693443389 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_114 = tanh(_temp_113)

    _temp_114 += 0.150557947873996 * indata[u"BestOutofSelfTotal"]
    _temp_114 += 0.403848616401085 * indata[u"Skills_Y"]
    _temp_114 += -0.333712142968522 * indata[u"SleepQuality"]
    _temp_114 += 94.8521829078755 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_114 += 1.51926609154092 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_114 += 6.47166346435801 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_114 += 0.223170924364694 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_114 += 0.167683522604135 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_114 += -1.06913768646088 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_115 = tanh(_temp_114)

    _temp_115 += -0.254235494326135 * indata[u"BestOutofSelfTotal"]
    _temp_115 += -1.01004239706088 * indata[u"Skills_Y"]
    _temp_115 += -1.26813940789228 * indata[u"SleepQuality"]
    _temp_115 += -28.2101356238673 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_115 += -2.17635430067894 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_115 += 6.93399624966071 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_115 += -0.0592052355449187 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_115 += 0.195321119280072 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_115 += 0.617487041350718 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_116 = tanh(_temp_115)

    _temp_116 += -0.0430133628141337 * indata[u"BestOutofSelfTotal"]
    _temp_116 += -1.41028486607203 * indata[u"Skills_Y"]
    _temp_116 += -0.111573147815102 * indata[u"SleepQuality"]
    _temp_116 += 33.6642225133255 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_116 += -0.77303465820365 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_116 += -2.03351719985286 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_116 += -0.0886777091607903 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_116 += -0.155401138902055 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_116 += -0.467724583052261 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_117 = tanh(_temp_116)

    _temp_117 += 0.175994546802185 * indata[u"BestOutofSelfTotal"]
    _temp_117 += -0.992372345690281 * indata[u"Skills_Y"]
    _temp_117 += -0.105476922509081 * indata[u"SleepQuality"]
    _temp_117 += -21.980883325284 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_117 += 1.23213223804334 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_117 += 1.76464818017267 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_117 += -0.263946132754013 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_117 += -0.383866017480305 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_117 += -0.789094527952588 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_118 = tanh(_temp_117)

    _temp_118 += -0.299803437454863 * indata[u"BestOutofSelfTotal"]
    _temp_118 += 0.537451046212404 * indata[u"Skills_Y"]
    _temp_118 += -0.228834542730441 * indata[u"SleepQuality"]
    _temp_118 += -4.73364320131354 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_118 += 4.22793946371013 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_118 += -0.857860481156395 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_118 += -0.139039005032545 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_118 += 0.573901995677622 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_118 += 0.124505609073336 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_119 = tanh(_temp_118)

    _temp_119 += -0.121637486877645 * indata[u"BestOutofSelfTotal"]
    _temp_119 += -0.15525820038406 * indata[u"Skills_Y"]
    _temp_119 += 0.0634309207925928 * indata[u"SleepQuality"]
    _temp_119 += -28.7792128938282 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_119 += 2.4317933595648 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_119 += -1.28099586163246 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_119 += -0.276516163749108 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_119 += 0.672248501600906 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_119 += -0.590161956024007 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_120 = tanh(_temp_119)

    _temp_120 += -0.119717911378245 * indata[u"BestOutofSelfTotal"]
    _temp_120 += -0.649165718409682 * indata[u"Skills_Y"]
    _temp_120 += 0.627060728539622 * indata[u"SleepQuality"]
    _temp_120 += 7.21194530261995 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_120 += 5.87959296775371 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_120 += -3.4585618142375 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_120 += -0.464819193252586 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_120 += -0.191608633836743 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_120 += 0.933014091069595 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_121 = tanh(_temp_120)

    _temp_121 += -0.215423844644706 * indata[u"BestOutofSelfTotal"]
    _temp_121 += -0.224960667091616 * indata[u"Skills_Y"]
    _temp_121 += -0.572341369142283 * indata[u"SleepQuality"]
    _temp_121 += 33.3737734011482 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_121 += 3.34870884629693 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_121 += -1.08616227179667 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_121 += -0.214036378141748 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_121 += 0.577334119741548 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_121 += 0.243431330144201 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_122 = tanh(_temp_121)

    _temp_122 += 0.173801220634778 * indata[u"BestOutofSelfTotal"]
    _temp_122 += 0.353805692038193 * indata[u"Skills_Y"]
    _temp_122 += 0.177566017851427 * indata[u"SleepQuality"]
    _temp_122 += -21.9643172317356 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_122 += 0.621385801680035 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_122 += 12.4747007413475 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_122 += 1.15264051001998 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_122 += -0.536264216520508 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_122 += -0.179251689839442 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_123 = tanh(_temp_122)

    _temp_123 += -0.0106449795072264 * indata[u"BestOutofSelfTotal"]
    _temp_123 += 0.651439629805562 * indata[u"Skills_Y"]
    _temp_123 += 0.500668010141028 * indata[u"SleepQuality"]
    _temp_123 += -35.9657527132842 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_123 += 0.365656693040523 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_123 += -3.76159279007658 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_123 += -0.322604295840564 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_123 += 0.723337607589131 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_123 += 0.28600522776785 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_124 = tanh(_temp_123)

    _temp_124 += 0.308608032544163 * indata[u"BestOutofSelfTotal"]
    _temp_124 += 0.749165583830827 * indata[u"Skills_Y"]
    _temp_124 += 0.392425605184681 * indata[u"SleepQuality"]
    _temp_124 += -42.1709426693789 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_124 += -1.24940553636331 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_124 += -0.73716242269323 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_124 += 0.106116324341108 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_124 += 0.225150143953677 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_124 += -0.884323629145549 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_125 = tanh(_temp_124)

    _temp_125 += -0.315078209253751 * indata[u"BestOutofSelfTotal"]
    _temp_125 += -0.0236471660695919 * indata[u"Skills_Y"]
    _temp_125 += -0.594904098839331 * indata[u"SleepQuality"]
    _temp_125 += 63.7095387789329 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_125 += 3.78275116976569 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_125 += 3.31213594868836 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_125 += -0.171073012858291 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_125 += 0.691907512501631 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_125 += -0.0364014573619699 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_126 = tanh(_temp_125)

    _temp_126 += -0.0524812378682808 * indata[u"BestOutofSelfTotal"]
    _temp_126 += 0.454050313119356 * indata[u"Skills_Y"]
    _temp_126 += -0.109347337322545 * indata[u"SleepQuality"]
    _temp_126 += 5.66598129109235 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_126 += 1.28985490876517 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_126 += 3.42309081128597 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_126 += 0.508270483724359 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_126 += -0.485745306487461 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_126 += -0.65288829368254 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_127 = tanh(_temp_126)

    _temp_127 += 0.390854802082161 * indata[u"BestOutofSelfTotal"]
    _temp_127 += 0.680117333004843 * indata[u"Skills_Y"]
    _temp_127 += 0.262680644766514 * indata[u"SleepQuality"]
    _temp_127 += -36.9274556185707 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_127 += -0.915916885678404 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_127 += -5.38662078593322 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_127 += 0.410694431927189 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_127 += 0.0380366050958803 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_127 += 0.00125145016422082 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_128 = tanh(_temp_127)

    _temp_128 += 0.0210165883987107 * indata[u"BestOutofSelfTotal"]
    _temp_128 += 1.33100880538189 * indata[u"Skills_Y"]
    _temp_128 += -0.0131861082492614 * indata[u"SleepQuality"]
    _temp_128 += 9.31476881860392 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_128 += -6.8487295729105 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_128 += -3.99029387658245 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_128 += 0.209565424243728 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_128 += -0.29759587624434 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_128 += -0.0628939505561852 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_129 = tanh(_temp_128)

    _temp_129 += -0.149206090078722 * indata[u"BestOutofSelfTotal"]
    _temp_129 += 0.267075246047315 * indata[u"Skills_Y"]
    _temp_129 += 0.454168480691203 * indata[u"SleepQuality"]
    _temp_129 += -83.1848369243134 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_129 += -7.07559896618962 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_129 += -11.3342714660188 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_129 += -0.170950339894425 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_129 += 0.646494064237003 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_129 += 0.328644961964718 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_130 = tanh(_temp_129)

    _temp_130 += 0.0970020269847006 * indata[u"BestOutofSelfTotal"]
    _temp_130 += 1.15247142066016 * indata[u"Skills_Y"]
    _temp_130 += -0.341721528984121 * indata[u"SleepQuality"]
    _temp_130 += -53.9210003799272 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_130 += 7.07181403338666 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_130 += 6.07865652052444 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_130 += -0.126206036891062 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_130 += 0.433843563376776 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_130 += 0.311296560128364 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_131 = tanh(_temp_130)

    _temp_131 += -0.183083883361602 * indata[u"BestOutofSelfTotal"]
    _temp_131 += 0.014669754248076 * indata[u"Skills_Y"]
    _temp_131 += -0.136735186683 * indata[u"SleepQuality"]
    _temp_131 += -109.542631411525 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_131 += -3.22125437685821 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_131 += 5.92531529875632 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_131 += -0.202881861923735 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_131 += 0.182781963687412 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_131 += -1.25492681371812 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_132 = tanh(_temp_131)

    _temp_132 += -0.0741513662071521 * indata[u"BestOutofSelfTotal"]
    _temp_132 += -0.074333991853895 * indata[u"Skills_Y"]
    _temp_132 += 0.145327290919081 * indata[u"SleepQuality"]
    _temp_132 += 27.2085192461646 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_132 += 4.82678075779312 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_132 += -4.14310714519353 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_132 += -0.075422297454662 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_132 += 0.636224869735734 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_132 += -0.133708626867567 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_133 = tanh(_temp_132)

    _temp_133 += 0.351328152487995 * indata[u"BestOutofSelfTotal"]
    _temp_133 += 0.291228393352498 * indata[u"Skills_Y"]
    _temp_133 += -0.615022810006217 * indata[u"SleepQuality"]
    _temp_133 += 92.3851772761665 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_133 += 0.0738438403010731 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_133 += -8.37096334828055 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_133 += 0.483859485533547 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_133 += 0.130995868157187 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_133 += 0.325449288397148 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_134 = tanh(_temp_133)

    _temp_134 += 0.0570978543905721 * indata[u"BestOutofSelfTotal"]
    _temp_134 += 0.485688953644521 * indata[u"Skills_Y"]
    _temp_134 += -0.171455888267611 * indata[u"SleepQuality"]
    _temp_134 += -114.078911721721 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_134 += -2.79739785255153 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_134 += 8.42114711819615 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_134 += 0.445943461453412 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_134 += -0.827566088727704 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_134 += -0.323657403361896 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_135 = tanh(_temp_134)

    _temp_135 += 0.0484821392610127 * indata[u"BestOutofSelfTotal"]
    _temp_135 += -1.09955366062446 * indata[u"Skills_Y"]
    _temp_135 += -0.617672607420213 * indata[u"SleepQuality"]
    _temp_135 += 18.0444614766625 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_135 += -7.02674362385545 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_135 += -21.1903416509692 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_135 += 0.125926385667823 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_135 += 0.39184489186144 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_135 += 0.303341821460087 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_136 = tanh(_temp_135)

    _temp_136 += 0.183603740047719 * indata[u"BestOutofSelfTotal"]
    _temp_136 += 1.48880152253358 * indata[u"Skills_Y"]
    _temp_136 += 0.27186702681044 * indata[u"SleepQuality"]
    _temp_136 += -95.1551530656203 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_136 += 8.16170018756994 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_136 += 3.59677534925142 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_136 += -0.0562954928476804 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_136 += -0.903417033920721 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_136 += -0.0367425743970269 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_137 = tanh(_temp_136)

    _temp_137 += -0.0780888297482146 * indata[u"BestOutofSelfTotal"]
    _temp_137 += -0.193264151053731 * indata[u"Skills_Y"]
    _temp_137 += -0.259834809582369 * indata[u"SleepQuality"]
    _temp_137 += -125.434488245796 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_137 += -0.490667525589127 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_137 += 8.84701882349016 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_137 += 0.430514931331666 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_137 += -0.84229766869282 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_137 += -0.437548683293289 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_138 = tanh(_temp_137)

    _temp_138 += 0.005000623036799 * indata[u"BestOutofSelfTotal"]
    _temp_138 += 0.00778462492964238 * indata[u"Skills_Y"]
    _temp_138 += 0.157394823393606 * indata[u"SleepQuality"]
    _temp_138 += -2.6475523840259 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_138 += 0.086591707887637 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_138 += -0.383528378330123 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_138 += -0.0388035217168457 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_138 += 0.0205438686801501 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_138 += 0.000305397858346016 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_139 = tanh(_temp_138)

    _temp_139 += 0.11707893371711 * indata[u"BestOutofSelfTotal"]
    _temp_139 += 0.866607413880766 * indata[u"Skills_Y"]
    _temp_139 += 0.206018964558589 * indata[u"SleepQuality"]
    _temp_139 += 36.9745697641783 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_139 += 3.76837136218231 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_139 += 0.554849992112953 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_139 += 0.259061217069378 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_139 += 0.510592871260753 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_139 += 0.052270677518574 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_140 = tanh(_temp_139)

    _temp_140 += -0.140703276213613 * indata[u"BestOutofSelfTotal"]
    _temp_140 += 0.0289715977153574 * indata[u"Skills_Y"]
    _temp_140 += 0.195435113013031 * indata[u"SleepQuality"]
    _temp_140 += -42.7282568701224 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_140 += -1.82523612774713 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_140 += -5.71240742107178 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_140 += -0.0739760740158843 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_140 += -0.459316410331525 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_140 += 0.148216802940541 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_141 = tanh(_temp_140)

    _temp_141 += 0.218573308939088 * indata[u"BestOutofSelfTotal"]
    _temp_141 += 0.63326720500846 * indata[u"Skills_Y"]
    _temp_141 += 0.580204405803166 * indata[u"SleepQuality"]
    _temp_141 += -105.385129886987 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_141 += 2.96191887242097 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_141 += 1.40465995559699 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_141 += -0.0661020958879961 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_141 += -0.746901806094954 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_141 += 0.300963621254015 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_142 = tanh(_temp_141)

    _temp_142 += 0.101545076566689 * indata[u"BestOutofSelfTotal"]
    _temp_142 += 0.578204030019424 * indata[u"Skills_Y"]
    _temp_142 += -0.334802423138949 * indata[u"SleepQuality"]
    _temp_142 += 26.7403770736372 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_142 += 1.74127867649065 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_142 += 11.4242774309913 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_142 += -0.142486208037997 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_142 += -0.454200289998388 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_142 += 0.156581339498659 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_143 = tanh(_temp_142)

    _temp_143 += 0.0780401059048476 * indata[u"BestOutofSelfTotal"]
    _temp_143 += -0.690855804506942 * indata[u"Skills_Y"]
    _temp_143 += -0.42093186082421 * indata[u"SleepQuality"]
    _temp_143 += 72.6108188646215 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_143 += -2.21296768828347 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_143 += 4.84957035879676 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_143 += -0.151604385365544 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_143 += -0.724509639336392 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_143 += -0.113475630084405 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_144 = tanh(_temp_143)

    _temp_144 += -0.0187108606587466 * indata[u"BestOutofSelfTotal"]
    _temp_144 += 8.98129487858175 * indata[u"Skills_Y"]
    _temp_144 += 1.86509919079118 * indata[u"SleepQuality"]
    _temp_144 += -1039.82564111636 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_144 += -7.47516045990541 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_144 += -11.236008993456 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_144 += -0.121357913648208 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_144 += -1.16145090966697 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_144 += 13.3121063547607 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_145 = tanh(_temp_144)

    _temp_145 += -0.426816861220106 * indata[u"BestOutofSelfTotal"]
    _temp_145 += 10.5164590673356 * indata[u"Skills_Y"]
    _temp_145 += 0.538663939411584 * indata[u"SleepQuality"]
    _temp_145 += -67.4561366898891 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_145 += 54.4215124231021 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_145 += 5.19568324444648 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_145 += 0.774589590991298 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_145 += 0.158666581752034 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_145 += -1.539821352066 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_146 = tanh(_temp_145)

    _temp_146 += -0.238649425771361 * indata[u"BestOutofSelfTotal"]
    _temp_146 += 2.97689865559208 * indata[u"Skills_Y"]
    _temp_146 += 0.995253750390724 * indata[u"SleepQuality"]
    _temp_146 += -537.10245623704 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_146 += -22.7855760499497 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_146 += -14.2831247104417 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_146 += -0.283386395390553 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_146 += 0.134110305223645 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_146 += 5.83371497808948 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_147 = tanh(_temp_146)

    _temp_147 += 0.0219216079538265 * indata[u"BestOutofSelfTotal"]
    _temp_147 += -1.24256913753449 * indata[u"Skills_Y"]
    _temp_147 += 0.273274039774017 * indata[u"SleepQuality"]
    _temp_147 += 110.02693990703 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_147 += 1.18763159344697 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_147 += -3.58528540685592 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_147 += -0.13200921982115 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_147 += -0.115009342688548 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_147 += -0.391901135382428 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_148 = tanh(_temp_147)

    _temp_148 += -0.177572832221788 * indata[u"BestOutofSelfTotal"]
    _temp_148 += 0.390830660457329 * indata[u"Skills_Y"]
    _temp_148 += -0.784079156248003 * indata[u"SleepQuality"]
    _temp_148 += 65.8962445272104 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_148 += 4.11758150184694 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_148 += 2.49554304506071 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_148 += 0.195282177896715 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_148 += -1.22489671332115 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_148 += -0.935304269576388 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_149 = tanh(_temp_148)

    _temp_149 += 0.0160773697879688 * indata[u"BestOutofSelfTotal"]
    _temp_149 += 0.797187204134955 * indata[u"Skills_Y"]
    _temp_149 += 0.220461558209625 * indata[u"SleepQuality"]
    _temp_149 += -128.566801693603 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_149 += 1.11308828756897 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_149 += -1.39415178818855 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_149 += 0.76689332612074 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_149 += -0.243067056034604 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_149 += -1.61140605107345 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_150 = tanh(_temp_149)

    _temp_150 += -0.0549232210167851 * indata[u"BestOutofSelfTotal"]
    _temp_150 += 0.711534141164857 * indata[u"Skills_Y"]
    _temp_150 += 0.149721627694484 * indata[u"SleepQuality"]
    _temp_150 += 103.537254443739 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_150 += 1.90017132116641 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_150 += 2.79942038922419 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_150 += 0.30650851036269 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_150 += -0.569193291298269 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_150 += -0.0399298309186703 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_151 = tanh(_temp_150)

    _temp_151 += 0.260643441698156 * indata[u"BestOutofSelfTotal"]
    _temp_151 += -0.0863389263624546 * indata[u"Skills_Y"]
    _temp_151 += -0.121062530490018 * indata[u"SleepQuality"]
    _temp_151 += 82.9480526290301 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_151 += -0.448915061725845 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_151 += 0.933469578013028 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_151 += 0.317398408020562 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_151 += 0.303156752504203 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_151 += -0.698159545643185 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_152 = tanh(_temp_151)

    _temp_152 += -0.273577301470545 * indata[u"BestOutofSelfTotal"]
    _temp_152 += -0.0507250130735664 * indata[u"Skills_Y"]
    _temp_152 += -0.383485986207389 * indata[u"SleepQuality"]
    _temp_152 += -49.6505851698018 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_152 += 2.28856166779628 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_152 += 10.0745690873326 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_152 += -0.390773922750561 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_152 += -0.0917357265050768 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_152 += -0.28591572849333 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_153 = tanh(_temp_152)

    _temp_153 += 0.0835609216954072 * indata[u"BestOutofSelfTotal"]
    _temp_153 += -0.268645686056271 * indata[u"Skills_Y"]
    _temp_153 += -0.154973987338199 * indata[u"SleepQuality"]
    _temp_153 += 105.756711599458 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_153 += 2.12701450151535 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_153 += -2.43723331957417 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_153 += -0.0289083082541192 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_153 += 0.576921220917567 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_153 += 1.26521787347422 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_154 = tanh(_temp_153)

    _temp_154 += -0.0368430476753698 * indata[u"BestOutofSelfTotal"]
    _temp_154 += -1.20022676859815 * indata[u"Skills_Y"]
    _temp_154 += 0.356426898680773 * indata[u"SleepQuality"]
    _temp_154 += -46.5416491719233 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_154 += -4.06610983053978 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_154 += 9.24671020287509 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_154 += 0.353713950834348 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_154 += -0.827954868936677 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_154 += 0.217377993859449 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_155 = tanh(_temp_154)

    _temp_155 += -0.226264771266854 * indata[u"BestOutofSelfTotal"]
    _temp_155 += 0.143440182243238 * indata[u"Skills_Y"]
    _temp_155 += 0.0919481587355901 * indata[u"SleepQuality"]
    _temp_155 += 21.7503366600654 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_155 += -2.205632000727 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_155 += 8.20526119591592 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_155 += 0.632218090722803 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_155 += -0.362612096225191 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_155 += 0.211423330122835 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_156 = tanh(_temp_155)

    _temp_156 += -0.0274834382081024 * indata[u"BestOutofSelfTotal"]
    _temp_156 += 0.839848688748954 * indata[u"Skills_Y"]
    _temp_156 += -1.45929306196499 * indata[u"SleepQuality"]
    _temp_156 += -244.634425878092 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_156 += -0.721370279674245 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_156 += -3.25847108271501 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_156 += -0.487090925975165 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_156 += 0.466514030811438 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_156 += 2.2919102661053 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_157 = tanh(_temp_156)

    _temp_157 += 0.258637844761535 * indata[u"BestOutofSelfTotal"]
    _temp_157 += 0.458024368915096 * indata[u"Skills_Y"]
    _temp_157 += 0.463568437068075 * indata[u"SleepQuality"]
    _temp_157 += 131.86765845272 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_157 += 1.1675138218731 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_157 += -3.1647247983116 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_157 += -0.56640560099156 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_157 += -0.435171411659197 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_157 += -0.277902045942438 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_158 = tanh(_temp_157)

    _temp_158 += -0.184970965340122 * indata[u"BestOutofSelfTotal"]
    _temp_158 += 0.0927110544189674 * indata[u"Skills_Y"]
    _temp_158 += 0.200880545340855 * indata[u"SleepQuality"]
    _temp_158 += 52.769676540214 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_158 += 0.593761189098747 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_158 += -0.54632895762573 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_158 += 0.907033376426886 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_158 += 0.0879552580851037 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_158 += -1.34585622435714 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_159 = tanh(_temp_158)

    _temp_159 += 0.225553791770405 * indata[u"BestOutofSelfTotal"]
    _temp_159 += 0.930397973263119 * indata[u"Skills_Y"]
    _temp_159 += 0.466325982065765 * indata[u"SleepQuality"]
    _temp_159 += -74.83822976968 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_159 += -0.895303507004636 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_159 += -9.6323586878705 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_159 += 0.509350325914576 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_159 += -0.0056480422822628 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_159 += 0.554680652742566 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_160 = tanh(_temp_159)

    _temp_160 += -0.169523395397537 * indata[u"BestOutofSelfTotal"]
    _temp_160 += -0.80253763072818 * indata[u"Skills_Y"]
    _temp_160 += -0.0609943027622861 * indata[u"SleepQuality"]
    _temp_160 += -39.6931734346306 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_160 += -3.06687563534103 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_160 += -3.94296418655165 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_160 += -1.05692895599828 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_160 += -0.13516674620317 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_160 += -0.0134648595232675 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_161 = tanh(_temp_160)

    _temp_161 += 0.102572782658409 * indata[u"BestOutofSelfTotal"]
    _temp_161 += 1.41708502687177 * indata[u"Skills_Y"]
    _temp_161 += -0.159747260147024 * indata[u"SleepQuality"]
    _temp_161 += 37.5216709712319 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_161 += -7.08914230889803 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_161 += 5.77720815579685 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_161 += -0.222938038609632 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_161 += 0.212742554646496 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_161 += 0.841316560474817 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_162 = tanh(_temp_161)

    _temp_162 += 0.0362665639236348 * indata[u"BestOutofSelfTotal"]
    _temp_162 += -0.122829823626009 * indata[u"Skills_Y"]
    _temp_162 += -0.166675632998742 * indata[u"SleepQuality"]
    _temp_162 += -7.91535678155307 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_162 += -1.91654631295431 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_162 += -0.693284949311018 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_162 += -0.0815002052455335 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_162 += 0.150855340663781 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_162 += -0.722622704196334 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_163 = tanh(_temp_162)

    _temp_163 += -0.158713302662216 * indata[u"BestOutofSelfTotal"]
    _temp_163 += 1.99929916377983 * indata[u"Skills_Y"]
    _temp_163 += 0.0324862637059822 * indata[u"SleepQuality"]
    _temp_163 += 115.758507597842 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_163 += -1.22893913686015 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_163 += -10.2111374754082 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_163 += -0.477150769746639 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_163 += -0.760636147353158 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_163 += 0.755042763976544 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_164 = tanh(_temp_163)

    _temp_164 += 0.238538430740906 * indata[u"BestOutofSelfTotal"]
    _temp_164 += -0.98919984971525 * indata[u"Skills_Y"]
    _temp_164 += -0.0599754870322245 * indata[u"SleepQuality"]
    _temp_164 += -24.6316014437589 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_164 += 1.56033029849726 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_164 += 10.9388318616824 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_164 += 0.672611451913103 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_164 += 0.989564896505841 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_164 += -0.606388350747578 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_165 = tanh(_temp_164)

    _temp_165 += -0.28709483381012 * indata[u"BestOutofSelfTotal"]
    _temp_165 += -0.136741585256627 * indata[u"Skills_Y"]
    _temp_165 += -0.346453982597579 * indata[u"SleepQuality"]
    _temp_165 += 21.5697554692039 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_165 += 1.61886849893919 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_165 += 9.00493137429183 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_165 += -0.237985240430748 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_165 += -0.825846799707925 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_165 += 0.285369930810614 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_166 = tanh(_temp_165)

    _temp_166 += -0.0176286644278609 * indata[u"BestOutofSelfTotal"]
    _temp_166 += -0.978893932405949 * indata[u"Skills_Y"]
    _temp_166 += 0.376759612809641 * indata[u"SleepQuality"]
    _temp_166 += 46.5849300890112 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_166 += 4.96285450117301 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_166 += 0.93324196867894 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_166 += 0.635693800408008 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_166 += 0.943850794539664 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_166 += -0.306980187846236 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_167 = tanh(_temp_166)

    _temp_167 += -0.227215101454324 * indata[u"BestOutofSelfTotal"]
    _temp_167 += -1.44218002760685 * indata[u"Skills_Y"]
    _temp_167 += -0.3241908788231 * indata[u"SleepQuality"]
    _temp_167 += 119.292490799696 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_167 += 2.05539653523719 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_167 += 7.23849191777762 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_167 += 0.238936678145435 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_167 += -0.188833199814472 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_167 += 1.68016917262887 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_168 = tanh(_temp_167)

    _temp_168 += 0.17278149400386 * indata[u"BestOutofSelfTotal"]
    _temp_168 += -0.0930896960640712 * indata[u"Skills_Y"]
    _temp_168 += -0.148937813235614 * indata[u"SleepQuality"]
    _temp_168 += 30.6453059064239 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_168 += -4.17732868388086 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_168 += 1.58812336107006 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_168 += -0.151442062841826 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_168 += 0.234591531570322 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_168 += -0.657552311872501 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_169 = tanh(_temp_168)

    _temp_169 += -0.0593026155679277 * indata[u"BestOutofSelfTotal"]
    _temp_169 += -0.619588763639407 * indata[u"Skills_Y"]
    _temp_169 += 0.0174365042431883 * indata[u"SleepQuality"]
    _temp_169 += -85.4383087879967 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_169 += 2.06135851719803 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_169 += -8.07123029330368 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_169 += -0.156812105635755 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_169 += -0.0600157772436235 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_169 += -0.321766476865466 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_170 = tanh(_temp_169)

    _temp_170 += 0.197092857280727 * indata[u"BestOutofSelfTotal"]
    _temp_170 += 0.7784529797859 * indata[u"Skills_Y"]
    _temp_170 += 0.718290152433658 * indata[u"SleepQuality"]
    _temp_170 += -37.9215365064415 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_170 += -0.846937887496809 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_170 += 3.66140174980038 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_170 += -0.539726863603129 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_170 += 0.00502582278523044 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_170 += 1.09031018558672 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_171 = tanh(_temp_170)

    _temp_171 += -0.0978557431104099 * indata[u"BestOutofSelfTotal"]
    _temp_171 += -0.260653743888093 * indata[u"Skills_Y"]
    _temp_171 += -0.225729738284207 * indata[u"SleepQuality"]
    _temp_171 += 21.0053716621212 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_171 += 2.12985844967249 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_171 += 3.14511705585826 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_171 += -0.325965712414951 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_171 += 1.12882734057283 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_171 += -0.32013326788936 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_172 = tanh(_temp_171)

    _temp_172 += 0.13637335866915 * indata[u"BestOutofSelfTotal"]
    _temp_172 += 1.8942398693751 * indata[u"Skills_Y"]
    _temp_172 += 0.175749087716005 * indata[u"SleepQuality"]
    _temp_172 += 105.805482849746 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_172 += 1.49675718934578 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_172 += 8.82999371186403 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_172 += 0.133711633938028 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_172 += -0.479350052820744 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_172 += -0.280806053221139 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_173 = tanh(_temp_172)

    _temp_173 += -0.597885968966208 * indata[u"BestOutofSelfTotal"]
    _temp_173 += 0.704869874702452 * indata[u"Skills_Y"]
    _temp_173 += -0.278112279571889 * indata[u"SleepQuality"]
    _temp_173 += 42.0699233394693 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_173 += 1.66102790516218 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_173 += 1.56476522857172 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_173 += 0.0853437169095328 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_173 += 0.184006141592967 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_173 += 0.0832383180252924 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_174 = tanh(_temp_173)

    _temp_174 += -0.0602071268553959 * indata[u"BestOutofSelfTotal"]
    _temp_174 += 1.14987169523946 * indata[u"Skills_Y"]
    _temp_174 += -0.00563811220142432 * indata[u"SleepQuality"]
    _temp_174 += -49.8605678233015 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_174 += 2.78695886113995 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_174 += -5.93311218079647 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_174 += -0.339026745568074 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_174 += -0.347849777124024 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_174 += 1.40958954148608 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_175 = tanh(_temp_174)

    _temp_175 += -0.230518162200465 * indata[u"BestOutofSelfTotal"]
    _temp_175 += 0.639935886686476 * indata[u"Skills_Y"]
    _temp_175 += -0.0249217636306083 * indata[u"SleepQuality"]
    _temp_175 += -1.47480948447478 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_175 += -0.252311723494788 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_175 += -2.07289546951436 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_175 += 0.438633935373424 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_175 += -0.320399665187142 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_175 += -0.19337402843444 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_176 = tanh(_temp_175)

    _temp_176 += -0.201963653572407 * indata[u"BestOutofSelfTotal"]
    _temp_176 += -0.0305594713111743 * indata[u"Skills_Y"]
    _temp_176 += -0.451828431094105 * indata[u"SleepQuality"]
    _temp_176 += -39.6762591343343 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_176 += 3.15430803021454 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_176 += 5.32125252692483 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_176 += -0.649018814183574 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_176 += 0.641935043704924 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_176 += 1.16732805959293 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_177 = tanh(_temp_176)

    _temp_177 += -0.131245567518915 * indata[u"BestOutofSelfTotal"]
    _temp_177 += 1.02652047809851 * indata[u"Skills_Y"]
    _temp_177 += -0.129552178133687 * indata[u"SleepQuality"]
    _temp_177 += -92.0558683813822 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_177 += -3.69401359047912 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_177 += 10.7584567048403 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_177 += -0.480059865663378 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_177 += 0.216359863007687 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_177 += 0.283563412487677 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_178 = tanh(_temp_177)

    _temp_178 += 0.269103024890612 * indata[u"BestOutofSelfTotal"]
    _temp_178 += -0.116302229486339 * indata[u"Skills_Y"]
    _temp_178 += 0.455552261887153 * indata[u"SleepQuality"]
    _temp_178 += -85.9907294516332 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_178 += 2.63675578991441 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_178 += -3.93224053298686 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_178 += -0.154108593765609 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_178 += -0.303569312350832 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_178 += 0.998401967920062 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_179 = tanh(_temp_178)

    _temp_179 += -0.0833250129667671 * indata[u"BestOutofSelfTotal"]
    _temp_179 += 0.289396737402091 * indata[u"Skills_Y"]
    _temp_179 += -0.777812919995176 * indata[u"SleepQuality"]
    _temp_179 += 4.11898479788288 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_179 += -3.94565706733834 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_179 += 0.596077727198645 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_179 += 0.272508689804823 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_179 += -0.272076368765567 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_179 += 0.49305958681885 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_180 = tanh(_temp_179)

    _temp_180 += 0.0427021293007135 * indata[u"BestOutofSelfTotal"]
    _temp_180 += -0.962055481796232 * indata[u"Skills_Y"]
    _temp_180 += -0.843517087487085 * indata[u"SleepQuality"]
    _temp_180 += 72.7053367744113 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_180 += -0.605348992829355 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_180 += 7.88695599432646 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_180 += -0.991759293460303 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_180 += -0.205634092034465 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_180 += -1.06454605722474 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_181 = tanh(_temp_180)

    _temp_181 += 0.083588097817327 * indata[u"BestOutofSelfTotal"]
    _temp_181 += -0.571686380130057 * indata[u"Skills_Y"]
    _temp_181 += 0.484464699426255 * indata[u"SleepQuality"]
    _temp_181 += -29.137294311639 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_181 += 7.48250142628483 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_181 += 8.54631551639073 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_181 += -0.389202235612438 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_181 += 0.664627584293801 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_181 += 0.967429804372768 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_182 = tanh(_temp_181)

    _temp_182 += -0.248587345591126 * indata[u"BestOutofSelfTotal"]
    _temp_182 += 0.0940501816922304 * indata[u"Skills_Y"]
    _temp_182 += 0.0168059650005725 * indata[u"SleepQuality"]
    _temp_182 += 37.1162051984714 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_182 += -2.83362695243287 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_182 += 3.07640595830609 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_182 += 0.652367048324283 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_182 += 0.454970867530846 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_182 += 0.954485442973567 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_183 = tanh(_temp_182)

    _temp_183 += 0.384526414795799 * indata[u"BestOutofSelfTotal"]
    _temp_183 += -1.0803672228364 * indata[u"Skills_Y"]
    _temp_183 += 0.282146935361661 * indata[u"SleepQuality"]
    _temp_183 += -29.3865026677243 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_183 += -20.7289869698949 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_183 += -7.82586010304159 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_183 += 0.139060043145363 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_183 += -0.844208388552508 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_183 += -0.48991715359405 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_184 = tanh(_temp_183)

    _temp_184 += 0.077931938038779 * indata[u"BestOutofSelfTotal"]
    _temp_184 += 1.6241827992334 * indata[u"Skills_Y"]
    _temp_184 += -0.174458545257843 * indata[u"SleepQuality"]
    _temp_184 += -83.5176343349685 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_184 += -1.67792360374608 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_184 += -4.00302849615828 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_184 += -0.145816962508593 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_184 += -0.418243208445285 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_184 += -1.09718343903912 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_185 = tanh(_temp_184)

    _temp_185 += -0.368645714394785 * indata[u"BestOutofSelfTotal"]
    _temp_185 += -0.382161227462268 * indata[u"Skills_Y"]
    _temp_185 += -0.00776139534517747 * indata[u"SleepQuality"]
    _temp_185 += 65.3799179526161 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_185 += 18.6638665000398 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_185 += 6.12279933324676 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_185 += -0.140634890987941 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_185 += 1.22207286929217 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_185 += 1.31443626064892 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_186 = tanh(_temp_185)

    _temp_186 += 0.0605621691583839 * indata[u"BestOutofSelfTotal"]
    _temp_186 += 0.754612527894187 * indata[u"Skills_Y"]
    _temp_186 += 0.138566221286669 * indata[u"SleepQuality"]
    _temp_186 += -76.5304401684475 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_186 += -1.00939685764025 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_186 += -6.53077247220559 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_186 += 0.0210181450258091 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_186 += -0.346312379627999 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_186 += -1.31895757984711 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_187 = tanh(_temp_186)

    _temp_187 += -0.122681267366352 * indata[u"BestOutofSelfTotal"]
    _temp_187 += -1.84711766074116 * indata[u"Skills_Y"]
    _temp_187 += 0.643441538333938 * indata[u"SleepQuality"]
    _temp_187 += 13.4682496946874 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_187 += -0.999895190502017 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_187 += -0.896710784665071 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_187 += 0.0574247351679262 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_187 += 1.08637837170127 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_187 += -0.463617681097235 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_188 = tanh(_temp_187)

    _temp_188 += -0.0799878860467647 * indata[u"BestOutofSelfTotal"]
    _temp_188 += -0.297594641223523 * indata[u"Skills_Y"]
    _temp_188 += 0.836335840965763 * indata[u"SleepQuality"]
    _temp_188 += -24.3649591678074 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_188 += -0.317876357199625 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_188 += -4.31967471392171 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_188 += 0.152747453400022 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_188 += 0.487434183758744 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_188 += -0.536358458389722 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_189 = tanh(_temp_188)

    _temp_189 += 0.0595159979345755 * indata[u"BestOutofSelfTotal"]
    _temp_189 += 1.28226364735837 * indata[u"Skills_Y"]
    _temp_189 += -0.0986610952202975 * indata[u"SleepQuality"]
    _temp_189 += -44.8063273189258 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_189 += 0.659047668364095 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_189 += -0.0437295161934269 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_189 += 0.141825423664774 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_189 += 0.0230214908433872 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_189 += -1.33663451800475 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_190 = tanh(_temp_189)

    _temp_190 += 0.0312508238255555 * indata[u"BestOutofSelfTotal"]
    _temp_190 += -0.40147143388175 * indata[u"Skills_Y"]
    _temp_190 += 0.0322552589078944 * indata[u"SleepQuality"]
    _temp_190 += -39.6375133573998 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_190 += -0.67898022814627 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_190 += -2.55874765174679 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_190 += -0.0294885042436436 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_190 += -0.697380987010307 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_190 += -1.19784330180016 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_191 = tanh(_temp_190)

    _temp_191 += -0.245116449666934 * indata[u"BestOutofSelfTotal"]
    _temp_191 += 1.14654827522189 * indata[u"Skills_Y"]
    _temp_191 += -0.186925807288966 * indata[u"SleepQuality"]
    _temp_191 += 131.620396366502 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_191 += -5.52799511669417 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_191 += 3.65071850895461 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_191 += -0.464310794089706 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_191 += -0.197733501433148 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_191 += 1.4907767276162 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_192 = tanh(_temp_191)

    _temp_192 += -0.434492099930684 * indata[u"BestOutofSelfTotal"]
    _temp_192 += 0.282280642078642 * indata[u"Skills_Y"]
    _temp_192 += 0.676910265161339 * indata[u"SleepQuality"]
    _temp_192 += 20.843840271121 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_192 += -2.69741621748997 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_192 += -1.74992809209779 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_192 += -0.0895435672792773 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_192 += -0.580172419246866 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_192 += 0.355755661431732 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_193 = tanh(_temp_192)

    _temp_193 += 0.185132772704996 * indata[u"BestOutofSelfTotal"]
    _temp_193 += 1.47459159192634 * indata[u"Skills_Y"]
    _temp_193 += 0.0403476440230851 * indata[u"SleepQuality"]
    _temp_193 += -60.0912026050285 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_193 += 1.74624699114012 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_193 += -1.49467228450245 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_193 += 0.0707746319290969 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_193 += 0.170539021435771 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_193 += 0.134431490398034 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_194 = tanh(_temp_193)

    _temp_194 += 0.230353512223714 * indata[u"BestOutofSelfTotal"]
    _temp_194 += -0.123954689471295 * indata[u"Skills_Y"]
    _temp_194 += -0.0346242415713303 * indata[u"SleepQuality"]
    _temp_194 += 106.825228327433 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_194 += 4.82147213987191 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_194 += 7.29310893889595 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_194 += 0.511402574007797 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_194 += 0.460835453967203 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_194 += -0.964995002698532 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_195 = tanh(_temp_194)

    _temp_195 += 0.150917885597866 * indata[u"BestOutofSelfTotal"]
    _temp_195 += 0.513517167728339 * indata[u"Skills_Y"]
    _temp_195 += -0.168189652696217 * indata[u"SleepQuality"]
    _temp_195 += -3.86744020163636 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_195 += -5.90342166504541 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_195 += 2.24290169406961 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_195 += -0.503632385128223 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_195 += -0.688819942755286 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_195 += -0.35885970589024 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_196 = tanh(_temp_195)

    _temp_196 += -0.102101427535037 * indata[u"BestOutofSelfTotal"]
    _temp_196 += -1.21699823550279 * indata[u"Skills_Y"]
    _temp_196 += 0.653656978111593 * indata[u"SleepQuality"]
    _temp_196 += 45.6106805993516 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_196 += 5.3737100594734 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_196 += -2.05389755260671 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_196 += 0.447369424618728 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_196 += 0.457688524127371 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_196 += -1.04525038128183 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_197 = tanh(_temp_196)

    _temp_197 += -0.195270044173057 * indata[u"BestOutofSelfTotal"]
    _temp_197 += 1.15578175455447 * indata[u"Skills_Y"]
    _temp_197 += 0.178367307204482 * indata[u"SleepQuality"]
    _temp_197 += 4.07779927021084 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_197 += -2.97647275000439 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_197 += -1.79537404672551 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_197 += -0.601281394632984 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_197 += -0.0329635110069627 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_197 += 0.914720935348465 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_198 = tanh(_temp_197)

    _temp_198 += 0.0098449928338082 * indata[u"BestOutofSelfTotal"]
    _temp_198 += -0.533811619716805 * indata[u"Skills_Y"]
    _temp_198 += -0.250795721979246 * indata[u"SleepQuality"]
    _temp_198 += 31.7032948956336 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_198 += 2.11295297812188 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_198 += -13.7359653279887 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_198 += 0.466457471488243 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_198 += -0.0448531085774132 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_198 += 0.112836412225208 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_199 = tanh(_temp_198)

    _temp_199 += -0.129020961056879 * indata[u"BestOutofSelfTotal"]
    _temp_199 += -0.0382463700506304 * indata[u"Skills_Y"]
    _temp_199 += -0.867079963755845 * indata[u"SleepQuality"]
    _temp_199 += -184.809847572343 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_199 += -0.688167972195919 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_199 += -0.641050354043766 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_199 += -0.235151269148293 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_199 += -0.141161688925916 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_199 += 1.47599268730045 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_200 = tanh(_temp_199)

    _temp_200 += -0.0322194333029518 * indata[u"BestOutofSelfTotal"]
    _temp_200 += -1.03268193647352 * indata[u"Skills_Y"]
    _temp_200 += -0.113646815411797 * indata[u"SleepQuality"]
    _temp_200 += -107.620745746399 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_200 += -1.77031021907823 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_200 += -3.91403675514468 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_200 += 0.255361387573107 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_200 += 0.130254066783271 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_200 += 0.606043936414349 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_201 = tanh(_temp_200)

    _temp_201 += 0.0989017876765012 * indata[u"BestOutofSelfTotal"]
    _temp_201 += 0.0455384552606661 * indata[u"Skills_Y"]
    _temp_201 += -0.0498445661495363 * indata[u"SleepQuality"]
    _temp_201 += -53.0141900732957 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_201 += 0.0553079003416892 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_201 += 1.50754058761234 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_201 += 0.472788525529582 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_201 += 0.236858515774713 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_201 += 0.102676217936501 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_202 = tanh(_temp_201)

    _temp_202 += -0.090895504934659 * indata[u"BestOutofSelfTotal"]
    _temp_202 += 0.71505447510596 * indata[u"Skills_Y"]
    _temp_202 += 0.767010426994311 * indata[u"SleepQuality"]
    _temp_202 += 24.9492590289191 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_202 += 2.1967063902939 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_202 += -0.106004499487404 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_202 += 0.41540546176655 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_202 += 0.230477790294722 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_202 += -0.356439921454927 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_203 = tanh(_temp_202)

    _temp_203 += 0.0864251789934779 * indata[u"BestOutofSelfTotal"]
    _temp_203 += 0.659290049692932 * indata[u"Skills_Y"]
    _temp_203 += -0.875361283127739 * indata[u"SleepQuality"]
    _temp_203 += -119.486560098273 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_203 += -1.42010983288821 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_203 += -11.1614455294225 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_203 += -0.682995085080849 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_203 += 0.129737804704489 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_203 += 0.346726725844183 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_204 = tanh(_temp_203)

    _temp_204 += 0.0183175970835765 * indata[u"BestOutofSelfTotal"]
    _temp_204 += 0.215958467923918 * indata[u"Skills_Y"]
    _temp_204 += 0.402940167831214 * indata[u"SleepQuality"]
    _temp_204 += 158.186820577147 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_204 += 3.58503585874556 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_204 += 12.944261257471 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_204 += 0.0447658777394011 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_204 += -0.1330864992649 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_204 += -0.32221770297752 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_205 = tanh(_temp_204)

    _temp_205 += -0.0482960826129398 * indata[u"BestOutofSelfTotal"]
    _temp_205 += -0.420198797466696 * indata[u"Skills_Y"]
    _temp_205 += 0.52891209793782 * indata[u"SleepQuality"]
    _temp_205 += 40.4805923406969 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_205 += 2.35730121713612 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_205 += -5.65534936412908 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_205 += -0.358468765587378 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_205 += -0.0571783884541869 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_205 += -0.182316505365638 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_206 = tanh(_temp_205)

    _temp_206 += 0.0561194174492384 * indata[u"BestOutofSelfTotal"]
    _temp_206 += -0.30227931618774 * indata[u"Skills_Y"]
    _temp_206 += 1.03073159929537 * indata[u"SleepQuality"]
    _temp_206 += 133.877032273633 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_206 += -5.09691863598535 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_206 += 9.66242302520831 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_206 += 0.429711752289304 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_206 += 0.603725029459377 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_206 += 0.232389786522609 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_207 = tanh(_temp_206)

    _temp_207 += 0.166961466404309 * indata[u"BestOutofSelfTotal"]
    _temp_207 += 0.538013663523134 * indata[u"Skills_Y"]
    _temp_207 += 0.14432231792855 * indata[u"SleepQuality"]
    _temp_207 += 75.5607734103731 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_207 += 1.54828589016428 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_207 += -1.77279150093222 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_207 += 0.172255672168839 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_207 += 0.801328465235388 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_207 += -0.104912741786095 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_208 = tanh(_temp_207)

    _temp_208 += 0.0642425201229273 * indata[u"BestOutofSelfTotal"]
    _temp_208 += 1.68580905764012 * indata[u"Skills_Y"]
    _temp_208 += 0.0403944221998065 * indata[u"SleepQuality"]
    _temp_208 += 68.4640266653612 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_208 += -2.48600539627953 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_208 += 4.78675614572599 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_208 += 0.138210628616224 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_208 += 0.617956507910501 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_208 += 0.190545396942062 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_209 = tanh(_temp_208)

    _temp_209 += -0.046515199184083 * indata[u"BestOutofSelfTotal"]
    _temp_209 += -0.552531131244812 * indata[u"Skills_Y"]
    _temp_209 += -0.938043075906061 * indata[u"SleepQuality"]
    _temp_209 += -27.5940341657839 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_209 += 4.34875487244871 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_209 += -0.442836435327548 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_209 += -0.820628826532797 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_209 += 0.21265719711982 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_209 += 0.4598672395191 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_210 = tanh(_temp_209)

    _temp_210 += 0.0955872928145319 * indata[u"BestOutofSelfTotal"]
    _temp_210 += -0.685558551798466 * indata[u"Skills_Y"]
    _temp_210 += -0.0644660363959862 * indata[u"SleepQuality"]
    _temp_210 += 38.0705653249971 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_210 += -2.70273634385505 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_210 += -6.6691924305136 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_210 += -0.230288302926201 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_210 += 0.0521857015835232 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_210 += -0.801208837677518 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_211 = tanh(_temp_210)

    _temp_211 += -0.189009835451723 * indata[u"BestOutofSelfTotal"]
    _temp_211 += 1.67794724997226 * indata[u"Skills_Y"]
    _temp_211 += 0.355600450034766 * indata[u"SleepQuality"]
    _temp_211 += -13.3778031330363 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_211 += 3.23173298538644 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_211 += 0.163464971814482 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_211 += -0.097643529174808 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_211 += 0.168920242243757 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_211 += -0.365972854447812 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_212 = tanh(_temp_211)

    _temp_212 += -0.225049877996228 * indata[u"BestOutofSelfTotal"]
    _temp_212 += 0.10729375698278 * indata[u"Skills_Y"]
    _temp_212 += -0.534894347368447 * indata[u"SleepQuality"]
    _temp_212 += -47.4617817973146 * asinh((0.357728608883482 + 0.00172481629073379 * indata[u"PlayerID-1"]))
    _temp_212 += 5.25984868341809 * asinh((0.715093233703259 + 0.00839637199166007 * indata[u"Duration"]))
    _temp_212 += -5.63637526768171 * asinh((2.07686960948435 + 0.00166514481610497 * indata[u"AcuteLoad"]))
    _temp_212 += -0.0773321892516481 * log(((-0.535898384862246 + indata[u"TournamentGame"]) / (7.46410161513776 + -1 * indata[u"TournamentGame"])))
    _temp_212 += 1.2148574625213 * log(((22.7996686935525 + indata[u"SessionLoad"]) / (1134.06491833222 + -1 * indata[u"SessionLoad"])))
    _temp_212 += 1.917474377265 * log(((132.416511495654 + indata[u"DailyLoad"]) / (2309.70762658227 + -1 * indata[u"DailyLoad"])))
    H1_213 = tanh(_temp_212)

    _temp_213 += -0.0500000608376952 * H1_1
    _temp_213 += 0.040294662063484 * H1_10
    _temp_213 += -0.00324258545218751 * H1_100
    _temp_213 += -0.00256757957834319 * H1_101
    _temp_213 += -0.0204481488670085 * H1_102
    _temp_213 += 0.0124082676606119 * H1_103
    _temp_213 += 0.00978666409715658 * H1_104
    _temp_213 += 0.00624406245194532 * H1_105
    _temp_213 += -0.000336741224587228 * H1_106
    _temp_213 += -0.00425975147114274 * H1_107
    _temp_213 += -0.00656090512659058 * H1_108
    _temp_213 += -0.00667380629398836 * H1_109
    _temp_213 += 0.0400869970021441 * H1_11
    _temp_213 += 0.00567878586444664 * H1_110
    _temp_213 += 0.00666379607237069 * H1_111
    _temp_213 += 0.00657413157331303 * H1_112
    _temp_213 += -0.00622953124918847 * H1_113
    _temp_213 += 0.00183946019114553 * H1_114
    _temp_213 += -0.00294781441763965 * H1_115
    _temp_213 += -0.00234423762128296 * H1_116
    _temp_213 += -0.000736580892806772 * H1_117
    _temp_213 += -0.00776031514021071 * H1_118
    _temp_213 += -0.0143838745314084 * H1_119
    _temp_213 += -0.0372519549866262 * H1_12
    _temp_213 += 0.0134472438694552 * H1_120
    _temp_213 += 0.00265819115799562 * H1_121
    _temp_213 += -0.00366577379970821 * H1_122
    _temp_213 += -0.00133445619530264 * H1_123
    _temp_213 += 0.00233273832700161 * H1_124
    _temp_213 += -0.00134888369701171 * H1_125
    _temp_213 += -0.00282371646751848 * H1_126
    _temp_213 += -0.00189049872288839 * H1_127
    _temp_213 += 0.00128046626872873 * H1_128
    _temp_213 += 0.000413940073244395 * H1_129
    _temp_213 += 0.0340315042552589 * H1_13
    _temp_213 += 0.00229200466617316 * H1_130
    _temp_213 += 0.000750941364129888 * H1_131
    _temp_213 += -0.00242379416252864 * H1_132
    _temp_213 += 0.00116738976398132 * H1_133
    _temp_213 += -0.00181566152792756 * H1_134
    _temp_213 += 0.00176708076448472 * H1_135
    _temp_213 += 0.00126782290006795 * H1_136
    _temp_213 += 0.00254905520151094 * H1_137
    _temp_213 += 0.000407259366130393 * H1_138
    _temp_213 += -0.00103077287952224 * H1_139
    _temp_213 += -0.0393771379934114 * H1_14
    _temp_213 += 0.00487554775561477 * H1_140
    _temp_213 += 0.00525795251382824 * H1_141
    _temp_213 += 0.0021822598937483 * H1_142
    _temp_213 += -0.00118505622504529 * H1_143
    _temp_213 += 0.000136260833191601 * H1_144
    _temp_213 += -0.0175897373020622 * H1_145
    _temp_213 += 0.0140057493058186 * H1_146
    _temp_213 += 0.0170830163763105 * H1_147
    _temp_213 += 0.00166660748606271 * H1_148
    _temp_213 += -0.00184669486924871 * H1_149
    _temp_213 += 0.0379693630996575 * H1_15
    _temp_213 += -0.000429912987531771 * H1_150
    _temp_213 += -0.000288223441289242 * H1_151
    _temp_213 += -0.00170943111217624 * H1_152
    _temp_213 += -0.00197064305661457 * H1_153
    _temp_213 += 0.000119647230348343 * H1_154
    _temp_213 += 0.00124509704515678 * H1_155
    _temp_213 += -0.00198725370718227 * H1_156
    _temp_213 += -0.00822264613165953 * H1_157
    _temp_213 += -0.00749373053955737 * H1_158
    _temp_213 += -0.00670225181690336 * H1_159
    _temp_213 += -0.0802356020613988 * H1_16
    _temp_213 += 0.00147086008939086 * H1_160
    _temp_213 += 0.000492268876048275 * H1_161
    _temp_213 += -0.000274762563319738 * H1_162
    _temp_213 += -0.00227606754441466 * H1_163
    _temp_213 += -0.0013110587708376 * H1_164
    _temp_213 += -0.00175204927676965 * H1_165
    _temp_213 += -0.00179918430153938 * H1_166
    _temp_213 += -0.00156019794965339 * H1_167
    _temp_213 += 0.00196186925669741 * H1_168
    _temp_213 += 0.000633171084880774 * H1_169
    _temp_213 += -0.109431719200248 * H1_17
    _temp_213 += 0.000728264680859394 * H1_170
    _temp_213 += 0.000781185023228064 * H1_171
    _temp_213 += 0.000261365785211276 * H1_172
    _temp_213 += -0.000537980717677248 * H1_173
    _temp_213 += -0.00088996208115138 * H1_174
    _temp_213 += 0.00138995352173048 * H1_175
    _temp_213 += -0.000978095634699595 * H1_176
    _temp_213 += -0.00110500021345628 * H1_177
    _temp_213 += -0.00101110736108573 * H1_178
    _temp_213 += 0.00148768328035125 * H1_179
    _temp_213 += 0.0588184394434951 * H1_18
    _temp_213 += 0.000270863493949549 * H1_180
    _temp_213 += -0.000371546229815933 * H1_181
    _temp_213 += 0.0000965882812334638 * H1_182
    _temp_213 += -0.00126806587088594 * H1_183
    _temp_213 += -0.111518562749332 * H1_184
    _temp_213 += -0.011131794468886 * H1_185
    _temp_213 += -0.117459476379389 * H1_186
    _temp_213 += -0.00103961381520993 * H1_187
    _temp_213 += -0.00064296943272404 * H1_188
    _temp_213 += 0.00154494681546383 * H1_189
    _temp_213 += 0.265515831813933 * H1_19
    _temp_213 += -0.000725909424277391 * H1_190
    _temp_213 += 0.000820868256882588 * H1_191
    _temp_213 += 0.000180838233301807 * H1_192
    _temp_213 += 0.00102517465310023 * H1_193
    _temp_213 += 0.000436530355718666 * H1_194
    _temp_213 += 0.000894464372527959 * H1_195
    _temp_213 += 0.00044899160131243 * H1_196
    _temp_213 += 0.00135509477115252 * H1_197
    _temp_213 += 0.000197728808187993 * H1_198
    _temp_213 += -0.00124373242230926 * H1_199
    _temp_213 += 0.0522548179699876 * H1_2
    _temp_213 += 0.377814180946745 * H1_20
    _temp_213 += -0.001679319965862 * H1_200
    _temp_213 += 0.00207056785132387 * H1_201
    _temp_213 += -0.000389525067249958 * H1_202
    _temp_213 += 0.000313964363797329 * H1_203
    _temp_213 += -0.000620153913929632 * H1_204
    _temp_213 += -0.00129285654335051 * H1_205
    _temp_213 += 0.000565450899393256 * H1_206
    _temp_213 += 0.00151730523229455 * H1_207
    _temp_213 += 0.000433259601644089 * H1_208
    _temp_213 += -0.000637399807626356 * H1_209
    _temp_213 += -0.325159620417336 * H1_21
    _temp_213 += -0.00072997379252354 * H1_210
    _temp_213 += -0.0118966520945103 * H1_211
    _temp_213 += 0.00135268530249946 * H1_212
    _temp_213 += -0.00841117102194339 * H1_213
    _temp_213 += -0.0501896111746093 * H1_22
    _temp_213 += -0.0486084699386681 * H1_23
    _temp_213 += -0.025589741172086 * H1_24
    _temp_213 += -0.166171710968317 * H1_25
    _temp_213 += 0.106142410448239 * H1_26
    _temp_213 += -0.205756146259834 * H1_27
    _temp_213 += -0.0317419006627844 * H1_28
    _temp_213 += 0.0328263908390094 * H1_29
    _temp_213 += 0.0522548172944193 * H1_3
    _temp_213 += 0.0687048345199471 * H1_30
    _temp_213 += 0.0672760287229047 * H1_31
    _temp_213 += -0.0938366254755145 * H1_32
    _temp_213 += -0.0993881506591264 * H1_33
    _temp_213 += -0.101571425367827 * H1_34
    _temp_213 += 0.117913993260522 * H1_35
    _temp_213 += -0.0321281422196293 * H1_36
    _temp_213 += -0.0667169201075019 * H1_37
    _temp_213 += -0.0211040730336903 * H1_38
    _temp_213 += 0.0676043957555525 * H1_39
    _temp_213 += 0.145373578713644 * H1_4
    _temp_213 += -0.0380838874331549 * H1_40
    _temp_213 += -0.0558079066834176 * H1_41
    _temp_213 += 0.0613431537933523 * H1_42
    _temp_213 += 0.0786969750467628 * H1_43
    _temp_213 += -0.130258393393175 * H1_44
    _temp_213 += -0.330938048681517 * H1_45
    _temp_213 += 0.0499640263365957 * H1_46
    _temp_213 += -0.127640846265484 * H1_47
    _temp_213 += 0.0486448472748922 * H1_48
    _temp_213 += -0.020139854673435 * H1_49
    _temp_213 += 0.100254411462967 * H1_5
    _temp_213 += 0.0298818441577998 * H1_50
    _temp_213 += -0.0401140372109778 * H1_51
    _temp_213 += -0.0202947918996133 * H1_52
    _temp_213 += 0.0100678544922822 * H1_53
    _temp_213 += -0.0221702766489806 * H1_54
    _temp_213 += -0.0321948981722693 * H1_55
    _temp_213 += 0.00841421422231574 * H1_56
    _temp_213 += -0.0310597830302715 * H1_57
    _temp_213 += -0.0517447100667899 * H1_58
    _temp_213 += 0.0550050843180667 * H1_59
    _temp_213 += -0.0901263793222712 * H1_6
    _temp_213 += -0.0119167649901243 * H1_60
    _temp_213 += 0.0406746018932996 * H1_61
    _temp_213 += -0.0374219320878362 * H1_62
    _temp_213 += 0.0227205384984647 * H1_63
    _temp_213 += 0.0454172830174114 * H1_64
    _temp_213 += -0.0698600333471854 * H1_65
    _temp_213 += 0.0282862706356347 * H1_66
    _temp_213 += 0.0291185830870761 * H1_67
    _temp_213 += 0.0181067754997714 * H1_68
    _temp_213 += 0.0272998549193936 * H1_69
    _temp_213 += 0.0417224183755969 * H1_7
    _temp_213 += -0.0475192839712109 * H1_70
    _temp_213 += 0.0309462644606555 * H1_71
    _temp_213 += -0.0267477963403416 * H1_72
    _temp_213 += -0.0217374510784372 * H1_73
    _temp_213 += 0.0101651396618982 * H1_74
    _temp_213 += -0.0172251598963889 * H1_75
    _temp_213 += 0.0561502243678587 * H1_76
    _temp_213 += 0.00542724828028995 * H1_77
    _temp_213 += 0.0523001248587109 * H1_78
    _temp_213 += 0.0301062902198613 * H1_79
    _temp_213 += -0.0417917784303073 * H1_8
    _temp_213 += 0.0211355573764481 * H1_80
    _temp_213 += 0.0276000208931951 * H1_81
    _temp_213 += 0.0232431159913422 * H1_82
    _temp_213 += -0.0224658956051976 * H1_83
    _temp_213 += -0.0192704127469676 * H1_84
    _temp_213 += 0.011763261498119 * H1_85
    _temp_213 += 0.00674616783981962 * H1_86
    _temp_213 += -0.0145316179897011 * H1_87
    _temp_213 += 0.00400780679960821 * H1_88
    _temp_213 += -0.0165768258277152 * H1_89
    _temp_213 += -0.041113184069728 * H1_9
    _temp_213 += -0.0130831145002281 * H1_90
    _temp_213 += 0.00804902652203691 * H1_91
    _temp_213 += -0.0069049603749143 * H1_92
    _temp_213 += 0.00986520528474367 * H1_93
    _temp_213 += 0.00506001625426634 * H1_94
    _temp_213 += -0.00350633353900465 * H1_95
    _temp_213 += 0.00716722707352678 * H1_96
    _temp_213 += -0.010425402556421 * H1_97
    _temp_213 += 0.019187758373917 * H1_98
    _temp_213 += 0.0117766517509108 * H1_99
    outdata[u"Predicted Fatigue"] = _temp_213

    return outdata[u"Predicted Fatigue"]


