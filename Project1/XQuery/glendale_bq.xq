let $glendale_businesses := /root/business[city eq "Glendale"]
return fn:count($glendale_businesses)