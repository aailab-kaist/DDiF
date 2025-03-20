### DDiF ###
DIM_IN = {"CIFAR10_32": {1: 2, 10: 2, 50: 2}, "CIFAR100_32": {1: 2, 10: 2, 50: 2}, "ImageNet_128": {1: 2, 10: 2, 50: 2}, "ImageNet_256": {1: 2}}

NUM_LAYERS = {"CIFAR10_32": {1: 2, 10: 2, 50: 2}, "CIFAR100_32": {1: 2, 10: 2, 50: 2}, "ImageNet_128": {1: 3, 10: 3, 50: 3}, "ImageNet_256": {1: 3}}

LAYER_SIZE = {"CIFAR10_32": {1: 6, 10: 6, 50: 20}, "CIFAR100_32": {1: 10, 10: 15, 50: 30}, "ImageNet_128": {1: 20, 10: 20, 50: 40}, "ImageNet_256": {1: 40}}

DIM_OUT = {"CIFAR10_32": {1: 3, 10: 3, 50: 3}, "CIFAR100_32": {1: 3, 10: 3, 50: 3}, "ImageNet_128": {1: 3, 10: 3, 50: 3}, "ImageNet_256": {1: 3}}

W0_INITIAL = {"CIFAR10_32": {1: 30, 10: 30, 50: 30}, "CIFAR100_32": {1: 30, 10: 30, 50: 30}, "ImageNet_128": {1: 30, 10: 30, 50: 30}, "ImageNet_256": {1: 30}}

W0 = {"CIFAR10_32": {1: 10, 10: 10, 50: 10}, "CIFAR100_32": {1: 10, 10: 10, 50: 10}, "ImageNet_128": {1: 40, 10: 40, 50: 40}, "ImageNet_256": {1: 40}}


def load_default(args):

    if args.dim_in == None:
        args.dim_in = DIM_IN[f"{args.dataset}_{args.res}"][args.ipc]

    if args.num_layers == None:
        args.num_layers = NUM_LAYERS[f"{args.dataset}_{args.res}"][args.ipc]

    if args.layer_size == None:
        args.layer_size = LAYER_SIZE[f"{args.dataset}_{args.res}"][args.ipc]

    if args.dim_out == None:
        args.dim_out = DIM_OUT[f"{args.dataset}_{args.res}"][args.ipc]

    if args.w0_initial == None:
        args.w0_initial = W0_INITIAL[f"{args.dataset}_{args.res}"][args.ipc]

    if args.w0 == None:
        args.w0 = W0[f"{args.dataset}_{args.res}"][args.ipc]

    return args