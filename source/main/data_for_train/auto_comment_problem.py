import pandas as pd

from tensor2tensor.utils import registry
from tensor2tensor.data_generators import text_problems, problem
from tensor2tensor.models import transformer


@registry.register_problem
class AutoCommentProblem(text_problems.Text2TextProblem):
    @property
    def approx_vocab_size(self):
        return 2 ** 15  # 32768

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        df = pd.read_csv(data_dir + '/QA.csv', lineterminator='\n')
        df.dropna(how='any', inplace=True)
        for i in range(df.shape[0]):
            q = df['q'].iloc[i]
            a = df['a'].iloc[i]
            if len(q) > 0 and len(a) > 0:
                yield {'inputs': q, 'targets': a}

    @property
    def is_generate_per_split(self):
        # generate_data will NOT shard the data into TRAIN and EVAL
        return False

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        # 10% evaluation data
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 90,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 10,
        }]


# Smaller than the typical translate model, and with more regularization
@registry.register_hparams
def transformer_poetry():
    hparams = transformer.transformer_base()
    hparams.num_hidden_layers = 2
    hparams.hidden_size = 128
    hparams.filter_size = 512
    hparams.num_heads = 4
    hparams.attention_dropout = 0.6
    hparams.layer_prepostprocess_dropout = 0.6
    hparams.learning_rate = 0.05
    hparams.batch_size = 2048
    return hparams


# hyperparameter tuning ranges
@registry.register_ranged_hparams
def transformer_poetry_range(rhp):
    rhp.set_float("learning_rate", 0.05, 0.25, scale=rhp.LOG_SCALE)
    rhp.set_int("num_hidden_layers", 2, 4)
    rhp.set_discrete("hidden_size", [128, 256, 512])
    rhp.set_float("attention_dropout", 0.4, 0.7)