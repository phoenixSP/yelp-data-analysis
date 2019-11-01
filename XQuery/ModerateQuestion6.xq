(:
Are there some attributes that affect on business rating? (if time allows) GRAPH
ex: businesses with garage have higher rating than those with no garage
:)
let  $business := /root/business

let $busAll :=(
for $x in $business
where $x/attributes/Wifi!="qqqqqqq"
return $x)
let $busNoAtt :=(
for $x in $business
where $x/attributes/Wifi="True"
return $x)
let $busWithAtt :=(
for $x in $business
where $x/attributes/Wifi!="False"
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
	</data>
