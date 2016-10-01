import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

while True:
    msg = raw_input('Yo, say what? ')
    print execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, msg) 