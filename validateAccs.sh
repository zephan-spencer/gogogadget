benchmarks=$(head -n 1 validation_benchmarks)
declare -a benchmarkList=($benchmarks)

for i in "${benchmarkList[@]}"
do
    timeout --foreground 30m  ./systemValidation.sh -b $i &> $M5_PATH/BM_ARM_OUT/sys_validation/$i/${i}_validation
    valResult=$( tail -n 1 BM_ARM_OUT/sys_validation/$i/system.terminal )
    if [ "Check Passed" = "$valResult" ]; then
        echo $valResult
    else
        echo "Check Failed, software made it to: $valResult"
    fi
done