import datetime
import os
import torch
import argparse


from utils import *

ADV_NUM = 1000
BATCH = 20
if not os.path.isdir('adv'):
    os.mkdir('adv')


def main(task_id, attack_type, attack_norm):
    device = torch.device('cuda')
    model_file = MODEL_FILE_LIST[task_id]
    task_name = model_file.split('.')[0]
    attack_class = ATTACK_METHOD[attack_type]
    encoder, decoder, test_loader, _, word_map = load_dataset_model(model_file, batch_size=BATCH * CAP_PER_IMG)
    print('load model %s successful' % MODEL_FILE_LIST[task_id])

    if attack_norm == 0:
        attack_name = 'L2'
    elif attack_norm == 1:
        attack_name = 'Linf'
    else:
        raise NotImplementedError
    config = {
        'lr': 0.001,
        'beams': 1,
        'coeff': 100,
        'max_len': 60,
        'max_iter': 1000,
        'max_per': MAX_PER_DICT[attack_name]
    }
    attack = attack_class(encoder, decoder, word_map, attack_norm, device, config)
    results = []
    t1 = datetime.datetime.now()
    for i, data in enumerate(test_loader):
        (imgs, caption, caplen, all_captions) = data
        imgs = [imgs[jjj * CAP_PER_IMG:jjj * CAP_PER_IMG + 1] for jjj in range(BATCH)]
        imgs = torch.cat(imgs)
        imgs = imgs.to(attack.device)
        is_success, ori_img, adv_img = attack.run_attack(imgs)
        results.append([ori_img, adv_img])
        torch.save(results, 'adv/' + str(attack_type) + '_' + attack_name + '_' + task_name + '.adv')
        if i >= 10:
            break
    t2 = datetime.datetime.now()
    print(t2 - t1)
    torch.save(results, 'adv/' + str(attack_type) + '_' + attack_name + '_' + task_name + '.adv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transformer')
    parser.add_argument('--task', default=2, type=int, help='experiment subjects')
    parser.add_argument('--attack', default=3, type=int, help='attack method')
    parser.add_argument('--norm', default=1, type=int, help='attack type')
    args = parser.parse_args()
    main(args.task, args.attack, args.norm)

    # 3 4 5 6
