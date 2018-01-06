# 将 https://github.com/tensorflow/tensorflow 的 master 下载下来
# 解压后得到 tensorflow-master 文件夹
# 将此代码保存为 py 文件，放在 tensorflow-master/tensorflow 下
# 为防止网路错误，可以先将 http://yann.lecun.com/exdb/mnist/ 的四个文件下载到 tensorflow-master/tensorflow/MNIST_data

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 查看这个数据集的情况
print(mnist.train.images.shape, mnist.train.labels.shape)
print(mnist.test.images.shape, mnist.test.labels.shape)
print(mnist.validation.images.shape, mnist.validation.labels.shape)

import tensorflow as tf

sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, [None,784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) +b)
y_ = tf.placeholder(tf.float32, [None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
tf.global_variables_initializer().run()

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	train_step.run({x:batch_xs, y_:batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval({x:mnist.test.images, y_:mnist.test.labels}))