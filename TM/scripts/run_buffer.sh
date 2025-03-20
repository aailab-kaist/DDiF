cd ..
cuda_id=0
dst="ImageNet"
subset="nette"
res=128
model="ConvNetD5"
data_path="../data"
buffer_path="../buffers"

train_epochs=50
num_experts=100

CUDA_VISIBLE_DEVICES=${cuda_id} python buffer.py \
--dataset ${dst} --subset ${subset} --res ${res} \
--model ${model} \
--data_path ${data_path} --buffer_path ${buffer_path} \
--train_epochs ${train_epochs} \
--num_experts ${num_experts}
# --zca