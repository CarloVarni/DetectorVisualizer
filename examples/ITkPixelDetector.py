from core.Range1D import Range1D
from core.Point import Point
from core.Grid import Grid
from core.DetectorElement import DetectorElement
from core.Detector import Detector

from ROOT import TCanvas, TGraph, TLine, TH1D, TLatex

def ITkPixelDetector(rangeR: Range1D,
                     rangeZ: Range1D,
                     rangeInclusive: Range1D) -> Detector:
    InclusiveBoundaries = DetectorElement(Point(rangeZ.minimum(), rangeR.minimum()),
                                          Point(rangeZ.maximum(), rangeR.minimum()),
                                          Point(rangeZ.maximum(), rangeR.maximum()),
                                          Point(rangeZ.minimum(), rangeR.maximum()))
    InclusiveBoundaries.graph.GetXaxis().SetRangeUser(rangeInclusive.minimum(),
                                                      rangeInclusive.maximum())
    InclusiveBoundaries.graph.GetYaxis().SetRangeUser(rangeR.minimum(),
                                                      rangeR.maximum())
    pixelDetector = Detector(boundaries=InclusiveBoundaries)

    # underflow
    underflowArea = DetectorElement(Point(rangeInclusive.minimum(), rangeR.minimum()),
                                    Point(rangeZ.minimum(), rangeR.minimum()),
                                    Point(rangeZ.minimum(), rangeR.maximum()),
                                    Point(rangeInclusive.minimum(), rangeR.maximum()))
    underflowArea.graph.SetFillColorAlpha(18, 0.6)
    pixelDetector.addElement(underflowArea)

    # overflow
    overflowArea = DetectorElement(Point(rangeZ.maximum(), rangeR.minimum()),
                                   Point(rangeInclusive.maximum(), rangeR.minimum()),
                                   Point(rangeInclusive.maximum(), rangeR.maximum()),
                                   Point(rangeZ.maximum(), rangeR.maximum()))
    overflowArea.graph.SetFillColorAlpha(18, 0.6)
    pixelDetector.addElement(overflowArea)

    # Barrel
    barrel_layers = []
    barrel_layers.append(DetectorElement(Point(-243, 33),
                                         Point(243, 33),
                                         Point(243, 37.6),
                                         Point(-243, 37.6)))

    barrel_layers.append(DetectorElement(Point(-245.3, 96.16),
                                         Point(245.3, 96.16),
                                         Point(245.3, 105.5),
                                         Point(-245.3, 105.5)))
    
    barrel_layers.append(DetectorElement(Point(-374.4, 156.4),
                                         Point(374.4, 156.4),
                                         Point(374.4, 165.9),
                                         Point(-374.4, 165.9)))

    barrel_layers.append(DetectorElement(Point(-374.45, 224),
                                         Point(374.45, 224),
                                         Point(374.45, 233.6),
                                         Point(-374.45, 233.6)))

    barrel_layers.append(DetectorElement(Point(-374.45, 286.9),
                                         Point(374.45, 286.9),
                                         Point(374.45, 296.4),
                                         Point(-374.45, 296.4)))


    for layer in barrel_layers:
        layer.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(layer)
    
    # End caps
    endcap_layers = []
    endcap_layers.append( DetectorElement(Point(-2861, 273.9),
                                          Point(-2839, 273.9),
                                          Point(-2839, 315.3),
                                          Point(-2861, 315.3)))

    endcap_layers.append(DetectorElement(Point(-2544, 273.9),
                                         Point(-2522, 273.9),
                                         Point(-2522, 315.3),
                                         Point(-2544, 315.3)))

    endcap_layers.append(DetectorElement(Point(-2264.0, 273.9),
                                         Point(-2242.0, 273.9),
                                         Point(-2242.0, 315.4),
                                         Point(-2264.0, 315.4)))

    endcap_layers.append(DetectorElement(Point(-2018.0, 273.9),
                                         Point(-1996.0, 273.9),
                                         Point(-1996.0, 315.4),
                                         Point(-2018.0, 315.4)))

    endcap_layers.append(DetectorElement(Point(-1800.0, 273.9),
                                         Point(-1778.0, 273.9),
                                         Point(-1778.0, 315.4),
                                         Point(-1800.0, 315.4)))

    endcap_layers.append(DetectorElement(Point(-1608.0, 273.9),
                                         Point(-1586.0, 273.9),
                                         Point(-1586.0, 315.5),
                                         Point(-1608.0, 315.5)))

    endcap_layers.append(DetectorElement(Point(-1438.0, 273.9),
                                         Point(-1416.0, 273.9),
                                         Point(-1416.0, 315.3),
                                         Point(-1438.0, 315.3)))

    endcap_layers.append(DetectorElement(Point(-1288.0, 273.9),
                                         Point(-1266.0, 273.9),
                                         Point(-1266.0, 315.4),
                                         Point(-1288.0, 315.4)))

    endcap_layers.append(DetectorElement(Point(-1156.5, 273.9),
                                         Point(-1134.5, 273.9),
                                         Point(-1134.5, 315.4),
                                         Point(-1156.5, 315.4)))

    endcap_layers.append(DetectorElement(Point(-2861.0, 213.85105541203203),
                                         Point(-2839.0, 213.85105541203203),
                                         Point(-2839.0, 255.3143855034416),
                                         Point(-2861.0, 255.3143855034416)))

    endcap_layers.append(DetectorElement(Point(-2502.0, 213.80797945888267),
                                         Point(-2480.0, 213.80797945888267),
                                         Point(-2480.0, 255.48735019025892),
                                         Point(-2502.0, 255.48735019025892)))

    endcap_layers.append(DetectorElement(Point(-2191.0, 213.7902150847882),
                                         Point(-2169.0, 213.7902150847882),
                                         Point(-2169.0, 255.38379924537108),
                                         Point(-2191.0, 255.38379924537108)))
    
    endcap_layers.append(DetectorElement(Point(-1922.0, 213.76242921264253),
                                         Point(-1900.0, 213.76242921264253),
                                         Point(-1900.0, 255.48866324946786),
                                         Point(-1922.0, 255.48866324946786)))

    endcap_layers.append(DetectorElement(Point(-1687.0, 213.7607831394945),
                                         Point(-1665.0, 213.7607831394945),
                                         Point(-1665.0, 255.45526221716395),
                                         Point(-1687.0, 255.45526221716395)))

    endcap_layers.append(DetectorElement(Point(-1484.0, 213.7708618766599),
                                         Point(-1462.0, 213.7708618766599),
                                         Point(-1462.0, 255.51881924038392),
                                         Point(-1484.0, 255.51881924038392)))

    endcap_layers.append(DetectorElement(Point(-1308.0, 213.81697553758445),
                                         Point(-1286.0, 213.81697553758445),
                                         Point(-1286.0, 255.57228711462437),
                                         Point(-1308.0, 255.57228711462437)))

    endcap_layers.append(DetectorElement(Point(-1156.5, 213.78685251766535),
                                         Point(-1134.5, 213.78685251766535),
                                         Point(-1134.5, 255.43340676779144),
                                         Point(-1156.5, 255.43340676779144)) )

    endcap_layers.append(DetectorElement(Point(-2861.0, 153.82247123083155),
                                         Point(-2839.0, 153.82247123083155),
                                         Point(-2839.0, 195.5411504126722),
                                         Point(-2861.0, 195.5411504126722)))
    
    endcap_layers.append(DetectorElement(Point(-2604.0, 153.73527473189097),
                                         Point(-2582.0, 153.73527473189097),
                                         Point(-2582.0, 195.50407292663368),
                                         Point(-2604.0, 195.50407292663368)))

    endcap_layers.append(DetectorElement(Point(-2372.0, 153.74850868011697),
                                         Point(-2350.0, 153.74850868011697),
                                         Point(-2350.0, 195.5234369127139),
                                         Point(-2372.0, 195.5234369127139)))
    
    endcap_layers.append(DetectorElement(Point(-2162.0, 153.71926007485206),
                                         Point(-2140.0, 153.71926007485206),
                                         Point(-2140.0, 195.6023012773623),
                                         Point(-2162.0, 195.6023012773623)))
    
    endcap_layers.append(DetectorElement(Point(-1972.0, 153.72171697727032),
                                         Point(-1950.0, 153.72171697727032),
                                         Point(-1950.0, 195.5971895503614),
                                         Point(-1972.0, 195.5971895503614)))
    
    endcap_layers.append(DetectorElement(Point(-1800.0, 153.69865735275633),
                                         Point(-1778.0, 153.69865735275633),
                                         Point(-1778.0, 195.3796717016384),
                                         Point(-1800.0, 195.3796717016384)))

    endcap_layers.append(DetectorElement(Point(-1644.0, 153.74556179743857),
                                         Point(-1622.0, 153.74556179743857),
                                         Point(-1622.0, 195.77681272816756),
                                         Point(-1644.0, 195.77681272816756)))
    
    endcap_layers.append(DetectorElement(Point(-1503.0, 153.78833412326827),
                                         Point(-1481.0, 153.78833412326827),
                                         Point(-1481.0, 195.66672587080308),
                                         Point(-1503.0, 195.66672587080308)))
    
    endcap_layers.append(DetectorElement(Point(-1376.0, 153.74535774588446),
                                         Point(-1354.0, 153.74535774588446),
                                         Point(-1354.0, 195.64619145952386),
                                         Point(-1376.0, 195.64619145952386))) 

    endcap_layers.append(DetectorElement(Point(-1260.0, 153.71073376313055),
                                         Point(-1238.0, 153.71073376313055),
                                         Point(-1238.0, 195.80028064139745),
                                         Point(-1260.0, 195.80028064139745)))
    
    endcap_layers.append(DetectorElement(Point(-1156.5, 153.78204438568244),
                                         Point(-1134.5, 153.78204438568244),
                                         Point(-1134.5, 195.55094395006125),
                                         Point(-1156.5, 195.55094395006125)))

    ###
    endcap_layers.append( DetectorElement(Point(-2623.83, 95.91542405359004), Point(-2618.17, 95.91542405359004), Point(-2618.17, 121.75829882800598), Point(-2623.83, 121.75829882800598)) )
    endcap_layers.append( DetectorElement(Point(-2359.83, 86.2561448142102), Point(-2354.17, 86.2561448142102), Point(-2354.17, 121.88749744518509), Point(-2359.83, 121.88749744518509)) )
    endcap_layers.append( DetectorElement(Point(-2122.83, 79.6631180104068), Point(-2117.17, 79.6631180104068), Point(-2117.17, 121.71052491054338), Point(-2122.83, 121.71052491054338)) )
    endcap_layers.append( DetectorElement(Point(-1911.83, 79.66945765103462), Point(-1906.17, 79.66945765103462), Point(-1906.17, 121.7952374627596), Point(-1911.83, 121.7952374627596)) )
    endcap_layers.append( DetectorElement(Point(-1850.7, 67.45258324482465), Point(-1841.3, 67.45258324482465), Point(-1841.3, 78.83552141319292), Point(-1850.7, 78.83552141319292)) )
    endcap_layers.append( DetectorElement(Point(-1723.83, 79.67467365041416), Point(-1718.17, 79.67467365041416), Point(-1718.17, 121.86913819852013), Point(-1723.83, 121.86913819852013)) )
    endcap_layers.append( DetectorElement(Point(-1669.7, 60.81890516681471), Point(-1660.3, 60.81890516681471), Point(-1660.3, 78.89702050774795), Point(-1669.7, 78.89702050774795)) )
    endcap_layers.append( DetectorElement(Point(-1555.83, 79.68131257609905), Point(-1550.17, 79.68131257609905), Point(-1550.17, 121.86434787004934), Point(-1555.83, 121.86434787004934)) )
    endcap_layers.append( DetectorElement(Point(-1507.7, 59.11506905450504), Point(-1498.3, 59.11506905450504), Point(-1498.3, 78.86358445499165), Point(-1507.7, 78.86358445499165)) )
    endcap_layers.append( DetectorElement(Point(-1405.83, 79.70141403068078), Point(-1400.17, 79.70141403068078), Point(-1400.17, 121.6580877893862), Point(-1405.83, 121.6580877893862)) )
    endcap_layers.append( DetectorElement(Point(-1363.7, 59.08999276628827), Point(-1354.3, 59.08999276628827), Point(-1354.3, 78.78106330311873), Point(-1363.7, 78.78106330311873)) )
    endcap_layers.append( DetectorElement(Point(-1274.83, 79.66598236443207), Point(-1269.17, 79.66598236443207), Point(-1269.17, 121.87091226215549), Point(-1274.83, 121.87091226215549)) )
    endcap_layers.append( DetectorElement(Point(-1233.7, 59.11841966933825), Point(-1224.3, 59.11841966933825), Point(-1224.3, 78.91567525384295), Point(-1233.7, 78.91567525384295)) )
    endcap_layers.append( DetectorElement(Point(-1144.83, 79.67974733274447), Point(-1139.17, 79.67974733274447), Point(-1139.17, 121.76786885233724), Point(-1144.83, 121.76786885233724)) )
    endcap_layers.append( DetectorElement(Point(-1107.7, 59.133593162939114), Point(-1098.3, 59.133593162939114), Point(-1098.3, 78.83789341890105), Point(-1107.7, 78.83789341890105)) )
    endcap_layers.append( DetectorElement(Point(-1028.83, 79.69701367052595), Point(-1023.17, 79.69701367052595), Point(-1023.17, 121.7752433935568), Point(-1028.83, 121.7752433935568)) )
    endcap_layers.append( DetectorElement(Point(-927.826, 79.68354146026644), Point(-922.174, 79.68354146026644), Point(-922.174, 121.83542692538161), Point(-927.826, 121.83542692538161)) )
    endcap_layers.append( DetectorElement(Point(-837.826, 79.6529324600168), Point(-832.174, 79.6529324600168), Point(-832.174, 121.90458166433241), Point(-837.826, 121.90458166433241)) )
    endcap_layers.append( DetectorElement(Point(-751.826, 79.67219034424747), Point(-746.174, 79.67219034424747), Point(-746.174, 121.75262892438914), Point(-751.826, 121.75262892438914)) )
    endcap_layers.append( DetectorElement(Point(-677.826, 79.72805374396142), Point(-672.174, 79.72805374396142), Point(-672.174, 121.85404853383021), Point(-677.826, 121.85404853383021)) )
    endcap_layers.append( DetectorElement(Point(-606.826, 79.69273053233901), Point(-601.174, 79.69273053233901), Point(-601.174, 121.8830663019683), Point(-606.826, 121.8830663019683)) )
    endcap_layers.append( DetectorElement(Point(-545.826, 79.70901933664722), Point(-540.174, 79.70901933664722), Point(-540.174, 121.78211913499452), Point(-545.826, 121.78211913499452)) )
    endcap_layers.append( DetectorElement(Point(-488.826, 79.65295789140539), Point(-483.174, 79.65295789140539), Point(-483.174, 121.78827334764215), Point(-488.826, 121.78827334764215)) )
    endcap_layers.append( DetectorElement(Point(-439.826, 79.68083780765612), Point(-434.174, 79.68083780765612), Point(-434.174, 121.84403275815356), Point(-439.826, 121.84403275815356)) )
    endcap_layers.append( DetectorElement(Point(-398.826, 79.66843258455636), Point(-393.174, 79.66843258455636), Point(-393.174, 121.63057224402917), Point(-398.826, 121.63057224402917)) )
    endcap_layers.append( DetectorElement(Point(-359.826, 79.64216668982581), Point(-354.174, 79.64216668982581), Point(-354.174, 121.78835797776402), Point(-359.826, 121.78835797776402)) )
    endcap_layers.append( DetectorElement(Point(-324.826, 79.67758212320452), Point(-319.174, 79.67758212320452), Point(-319.174, 121.77402501617495), Point(-324.826, 121.77402501617495)) )
    endcap_layers.append( DetectorElement(Point(-293.826, 79.65126919829966), Point(-288.174, 79.65126919829966), Point(-288.174, 121.60797836116676), Point(-293.826, 121.60797836116676)) )
    endcap_layers.append( DetectorElement(Point(-265.826, 79.68669481161832), Point(-243.01, 79.68669481161832), Point(-243.01, 121.74991934802257), Point(-265.826, 121.74991934802257)) )
    
    ###
    endcap_layers.append( DetectorElement(Point(-1144.6, 41.73401401763794), Point(-1139.4, 41.73401401763794), Point(-1139.4, 53.287950850544064), Point(-1144.6, 53.287950850544064)) )
    endcap_layers.append( DetectorElement(Point(-1028.6, 37.47567379052844), Point(-1023.4, 37.47567379052844), Point(-1023.4, 53.304701121383275), Point(-1028.6, 53.304701121383275)) )
    endcap_layers.append( DetectorElement(Point(-927.6, 33.7906357236735), Point(-922.4, 33.7906357236735), Point(-922.4, 53.239777617867645), Point(-927.6, 53.239777617867645)) )
    endcap_layers.append( DetectorElement(Point(-837.6, 33.179017396904634), Point(-832.4, 33.179017396904634), Point(-832.4, 53.28701962002003), Point(-837.6, 53.28701962002003)) )
    endcap_layers.append( DetectorElement(Point(-751.6, 33.188457114635504), Point(-746.4, 33.188457114635504), Point(-746.4, 53.27762908360319), Point(-751.6, 53.27762908360319)) )
    endcap_layers.append( DetectorElement(Point(-677.6, 33.21364147846484), Point(-672.4, 33.21364147846484), Point(-672.4, 53.31098441245387), Point(-677.6, 53.31098441245387)) )
    endcap_layers.append( DetectorElement(Point(-606.6, 33.21555813801719), Point(-601.4, 33.21555813801719), Point(-601.4, 53.24894022682517), Point(-606.6, 53.24894022682517)) )
    endcap_layers.append( DetectorElement(Point(-545.6, 33.215891919381), Point(-540.4, 33.215891919381), Point(-540.4, 53.31840530792345), Point(-545.6, 53.31840530792345)) )
    endcap_layers.append( DetectorElement(Point(-488.6, 33.20041614031366), Point(-483.4, 33.20041614031366), Point(-483.4, 53.25440410929504), Point(-488.6, 53.25440410929504)) )
    endcap_layers.append( DetectorElement(Point(-439.6, 33.210194012832865), Point(-434.4, 33.210194012832865), Point(-434.4, 53.29310510347469), Point(-439.6, 53.29310510347469)) )
    endcap_layers.append( DetectorElement(Point(-398.6, 33.1948418217349), Point(-393.4, 33.1948418217349), Point(-393.4, 53.28221157581581), Point(-398.6, 53.28221157581581)) )
    endcap_layers.append( DetectorElement(Point(-359.6, 33.21529620600274), Point(-354.4, 33.21529620600274), Point(-354.4, 53.25538708140614), Point(-359.6, 53.25538708140614)) )
    endcap_layers.append( DetectorElement(Point(-324.6, 33.20014340157321), Point(-319.4, 33.20014340157321), Point(-319.4, 53.31502056863901), Point(-324.6, 53.31502056863901)) )
    endcap_layers.append( DetectorElement(Point(-293.6, 33.19941657292188), Point(-288.4, 33.19941657292188), Point(-288.4, 53.285328061296575), Point(-293.6, 53.285328061296575)) )
    endcap_layers.append( DetectorElement(Point(-265.6, 33.19872357184836), Point(-260.4, 33.19872357184836), Point(-260.4, 53.26246513080295), Point(-265.6, 53.26246513080295)) )
    endcap_layers.append( DetectorElement(Point(-243.47, 33.11989523502301), Point(-243.002, 33.11989523502301), Point(-243.002, 37.51788333715003), Point(-243.47, 37.51788333715003)) )

    ### inclined #3
    endcap_layers.append( DetectorElement(Point(-1148.5, 153.78204438568244), Point(-1134.5, 153.78204438568244), Point(-1134.5, 195.55094395006125), Point(-1148.5, 195.55094395006125)) )
    endcap_layers.append( DetectorElement(Point(-1050.74, 148.14419084581075), Point(-1027.55, 148.14419084581075), Point(-1027.55, 189.66950694827042), Point(-1050.74, 189.66950694827042)) )
    endcap_layers.append( DetectorElement(Point(-862.826, 148.1176183057235), Point(-839.644, 148.1176183057235), Point(-839.644, 189.79529572476238), Point(-862.826, 189.79529572476238)) )
    endcap_layers.append( DetectorElement(Point(-712.107, 148.1206481159531), Point(-688.921, 148.1206481159531), Point(-688.921, 189.76787178550538), Point(-712.107, 189.76787178550538)) )
    endcap_layers.append( DetectorElement(Point(-591.21, 148.1145415609487), Point(-568.025, 148.1145415609487), Point(-568.025, 189.8916590512864), Point(-591.21, 189.8916590512864)) )
    endcap_layers.append( DetectorElement(Point(-494.241, 148.08454026079158), Point(-471.069, 148.08454026079158), Point(-471.069, 189.83443920113652), Point(-494.241, 189.83443920113652)) )
    endcap_layers.append( DetectorElement(Point(-416.448, 148.06904919762943), Point(-393.271, 148.06904919762943), Point(-393.271, 189.5630608385769), Point(-416.448, 189.5630608385769)) )

    ### inclined #5
    endcap_layers.append( DetectorElement(Point(-1148.5, 213.78685251766535), Point(-1134.5, 213.78685251766535), Point(-1134.5, 255.43340676779144), Point(-1148.5, 255.43340676779144)) )
    endcap_layers.append( DetectorElement(Point(-1050.58, 215.58353007593135), Point(-1022.26, 215.58353007593135), Point(-1022.26, 254.96762976599598), Point(-1050.58, 254.96762976599598)) )
    endcap_layers.append( DetectorElement(Point(-915.897, 215.6199303079611), Point(-887.57, 215.6199303079611), Point(-887.57, 255.05398614138537), Point(-915.897, 255.05398614138537)) )
    endcap_layers.append( DetectorElement(Point(-799.434, 215.67242809364853), Point(-771.094, 215.67242809364853), Point(-771.094, 255.20305002095878), Point(-799.434, 255.20305002095878)) )
    endcap_layers.append( DetectorElement(Point(-698.7, 215.5783792902479), Point(-670.363, 215.5783792902479), Point(-670.363, 255.12042909929812), Point(-698.7, 255.12042909929812)) )
    endcap_layers.append( DetectorElement(Point(-611.613, 215.63090216341905), Point(-583.279, 215.63090216341905), Point(-583.279, 255.25070811986006), Point(-611.613, 255.25070811986006)) )
    endcap_layers.append( DetectorElement(Point(-536.3, 215.57687006958795), Point(-507.957, 215.57687006958795), Point(-507.957, 255.23111307722655), Point(-536.3, 255.23111307722655)) )
    endcap_layers.append( DetectorElement(Point(-471.154, 215.60735267842796), Point(-442.82, 215.60735267842796), Point(-442.82, 255.11994183520818), Point(-471.154, 255.11994183520818)) )
    endcap_layers.append( DetectorElement(Point(-414.807, 215.63400421410813), Point(-374.404, 215.63400421410813), Point(-374.404, 255.09000132502254), Point(-414.807, 255.09000132502254)) )

    ### inclined #8
    endcap_layers.append( DetectorElement(Point(-1148.5, 274.0132141772728), Point(-1134.5, 274.0132141772728), Point(-1134.5, 315.37806915827235), Point(-1148.5, 315.37806915827235)) )
    endcap_layers.append( DetectorElement(Point(-1050.38, 278.44322648656765), Point(-1020.52, 278.44322648656765), Point(-1020.52, 316.93070463588725), Point(-1050.38, 316.93070463588725)) )
    endcap_layers.append( DetectorElement(Point(-936.603, 278.45295218043566), Point(-906.671, 278.45295218043566), Point(-906.671, 316.69167623455155), Point(-936.603, 316.69167623455155)) )
    endcap_layers.append( DetectorElement(Point(-834.678, 278.4358089744385), Point(-804.814, 278.4358089744385), Point(-804.814, 317.03642351155804), Point(-834.678, 317.03642351155804)) )
    endcap_layers.append( DetectorElement(Point(-743.535, 278.4602758843889), Point(-713.63, 278.4602758843889), Point(-713.63, 316.778772672665), Point(-743.535, 316.778772672665)) )
    endcap_layers.append( DetectorElement(Point(-661.885, 278.4691376514819), Point(-632.04, 278.4691376514819), Point(-632.04, 316.6818179596201), Point(-661.885, 316.6818179596201)) )
    endcap_layers.append( DetectorElement(Point(-588.816, 278.4578594653058), Point(-558.938, 278.4578594653058), Point(-558.938, 316.93961157199965), Point(-588.816, 316.93961157199965)) )
    endcap_layers.append( DetectorElement(Point(-523.424, 278.4990753916429), Point(-493.531, 278.4990753916429), Point(-493.531, 316.8898760104052), Point(-523.424, 316.8898760104052)) )
    endcap_layers.append( DetectorElement(Point(-464.89, 278.46599511647736), Point(-434.988, 278.46599511647736), Point(-434.988, 317.0297445887373), Point(-464.89, 317.0297445887373)) )
    endcap_layers.append( DetectorElement(Point(-412.475, 278.4575072864978), Point(-374.434, 278.4575072864978), Point(-374.434, 316.91731858640986), Point(-412.475, 316.91731858640986)) )
    
    mirrowed_endcap_layers = []
    for el in endcap_layers:
        mirrowed_endcap_layers.append(DetectorElement(Point(-el.lowRight.x, el.lowRight.y),
                                                      Point(-el.lowLeft.x, el.lowLeft.y),
                                                      Point(-el.upLeft.x, el.upLeft.y),
                                                      Point(-el.upRight.x, el.upRight.y)))
    endcap_layers += mirrowed_endcap_layers
    
    for el in endcap_layers:
        el.graph.SetFillColorAlpha(38, 0.8)
        pixelDetector.addElement(el)

    return pixelDetector

