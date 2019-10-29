(:
Are there some attributes that affect on business rating? (if time allows) GRAPH
ex: businesses with garage have higher rating than those with no garage
attribute = noise
Noise type = [
	u'loud'
	'loud'
	u'average'
	'average'
	'quiet'
	u'quiet'
	u'very_loud'
	'very_loud'
]
:)
let  $business := /root/business
let $busAll :=(
for $x in $business
where $x/attributes/NoiseLevel!="qqqqqqq"
return $x)
let $busNoAtt :=(
for $x in $business
where $x/attributes/NoiseLevel="u'very_loud'"
return $x)
let $busWithAtt :=(
for $x in $business
where $x/attributes/NoiseLevel="'very_loud'"
return $x)

let $rAll := avg($busAll/stars)
let $cAll := count($busAll)
let $rNo := avg($busNoAtt/stars)
let $cNo := count($busNoAtt)
let $rWi := avg($busWithAtt/stars)
let $cWi := count($busWithAtt)
return 
	<data>
	<rating name="all" cnt="{$cAll}"> {$rAll} </rating>
	<rating name="with" cnt="{$cWi}"> {$rWi} </rating>
	<rating name="no" cnt="{$cNo}" > {$rNo} </rating>
	<rating> {$cWi+$cNo} </rating>
	<rating> {(($rWi*$cWi)+($rNo*$cNo))div($cWi+$cNo)} </rating>
	</data>
