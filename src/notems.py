from alphageometry import *


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    FLAGS = parse_args()

    start_time = time.perf_counter()
    if FLAGS.problem_name != '':
        main(FLAGS)
    else:
        out_file = FLAGS.out_file
        for name in pr.Problem.from_txt_file(FLAGS.problems_file, to_dict=True).keys():
            if name.startswith('#'): continue
            FLAGS.problem_name = name
            FLAGS.out_file = f"{out_file}/{name}.txt" if out_file != '' else ''
            try:
                main(FLAGS)
            except Exception as e:
                print(f"exception occurred on {name}:\n{e}")

    elapsed_time = time.perf_counter() - start_time
    logging.info(f"Total time = {elapsed_time:.4f} seconds")