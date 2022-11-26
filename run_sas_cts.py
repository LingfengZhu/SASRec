from recbole.quick_start import run_recbole


# 参数文件
parameter_dict = {
   'neg_sampling': None,
}

# 配置文件
config_file_list = ['sas_cts_2.yaml']

# 训练代码
run_recbole(model='SASCTS', dataset='ml-1m', config_file_list=config_file_list, config_dict=parameter_dict)
