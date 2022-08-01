import tensorflow as tf

import matplotlib.pyplot as plt
import pandas as pd
import os
from keras.utils import img_to_array
from keras.utils import load_img
from keras.models import load_model
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

def carregar_imagens_dataframe(folder: str, categories, filenames, name_folder):
    
    filename = os.listdir(folder)

    qtd_img_train = 0
    for fn in filename:
        old_name_img = folder + '\\'+ fn
        new_name_img = folder + '\\_'+str(qtd_img_train) +'.png'
        os.rename(old_name_img, new_name_img)
        qtd_img_train = qtd_img_train + 1

    filename = os.listdir(folder)

    qtd_img_train = 0
    for fn in filename:
        print(fn)
        #category = filename.split('.')[0]
        old_name_img = folder + '\\'+ fn

        if name_folder == 'up_forest':
            
            new_name_img = folder +'\\img_up_forest_'+str(qtd_img_train) + '.png'
            if('img_up_forest_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(0)
        elif(name_folder == 'down_forest'):
            
            new_name_img = folder +'\\img_down_forest_'+str(qtd_img_train) + '.png'
            if('img_down_forest_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(1)
        elif(name_folder == 'others'):
            
            new_name_img = folder +'\\img_others_'+str(qtd_img_train) + '.png'
            if('img_others_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(2)
        elif(name_folder == 'ground'):
            
            new_name_img = folder +'\\img_ground_'+str(qtd_img_train) + '.png'
            if('img_ground_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(3)
        elif(name_folder == 'water'):
            
            new_name_img = folder +'\\img_water_'+str(qtd_img_train) + '.png'
            if('img_water_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(4)
        elif(name_folder == 'soy'):
            
            new_name_img = folder +'\\img_soy_'+str(qtd_img_train) + '.png'
            if('img_soy_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(5)
        elif(name_folder == 'pasture'):
            
            new_name_img = folder +'\\img_pasture_'+str(qtd_img_train) + '.png'
            if('img_pasture_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(6)
        else:
            
            new_name_img = folder +'\\img_transition_'+str(qtd_img_train) + '.png'
            if('img_transition_'+str(qtd_img_train) + '.png' != filename):
                os.rename(old_name_img, new_name_img)
            qtd_img_train = qtd_img_train + 1
            categories.append(7)
        
        print("Aquiiii")
        filenames.append(new_name_img)

#qtd_retorno = 0 - Retorna tudo
#qtd_retorno = 1 - Retorna diretório  Train and Validation 
#qtd_retorno = 2 - Retorna diretório Train 
#qtd_retorno = 3 - Retorna diretório Validation 
#qtd_retorno = 4 - Retorna diretório test
#qtd_retorno = 5 - Retorna dataframe
def local_do_dataset(qtd_retorno):
    #Dataset Local
    base_dir = 'dataset'
    

    # 1 - loading data
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')
    test_dir = os.path.join(base_dir, 'test')
    test_fnames = os.listdir(test_dir)

    if qtd_retorno   == 4:
        return test_dir

    # Directory with our training forest/noforest pictures
    train_up_forest_dir = os.path.join(train_dir, 'up_forest')
    train_down_forest_dir = os.path.join(train_dir, 'down_forest')
    train_soy_dir = os.path.join(train_dir, 'soy')
    train_pasture_dir = os.path.join(train_dir, 'pasture')
    train_ground_dir = os.path.join(train_dir, 'ground')
    train_water_dir = os.path.join(train_dir, 'water')
    train_others_dir = os.path.join(train_dir, 'others')
    train_transition_dir = os.path.join(train_dir, 'transition')



    # Directory with our validation forest/noforest pictures
    validation_up_forest_dir = os.path.join(validation_dir, 'up_forest')
    validation_down_forest_dir = os.path.join(validation_dir, 'down_forest')
    validation_soy_dir = os.path.join(validation_dir, 'soy')
    validation_pasture_dir = os.path.join(validation_dir, 'pasture')
    validation_ground_dir= os.path.join(validation_dir, 'ground')
    validation_water_dir = os.path.join(validation_dir, 'water')
    validation_others_dir = os.path.join(validation_dir, 'others')
    validation_transition_dir = os.path.join(validation_dir, 'transition')


    train_up_forest_fnames = os.listdir(validation_up_forest_dir)
    train_down_forest_fnames = os.listdir(validation_down_forest_dir)
    train_soy_fnames = os.listdir(validation_soy_dir)
    train_pasture_fnames = os.listdir(validation_pasture_dir)
    train_ground_fnames = os.listdir(validation_ground_dir)
    train_water_fnames = os.listdir(validation_water_dir)
    train_others_dfnames = os.listdir(validation_others_dir)
    train_transition_fnames = os.listdir(validation_transition_dir)


     # show the images quantity
    categories = []
    filenames = []
    carregar_imagens_dataframe(train_up_forest_dir, categories, filenames, "up_forest")
    carregar_imagens_dataframe(train_down_forest_dir, categories, filenames, "down_forest")
    carregar_imagens_dataframe(train_soy_dir, categories, filenames, "soy")
    carregar_imagens_dataframe(train_pasture_dir, categories, filenames, "pasture")
    carregar_imagens_dataframe(train_ground_dir, categories, filenames, "ground")
    carregar_imagens_dataframe(train_water_dir, categories, filenames, "water")
    carregar_imagens_dataframe(train_others_dir, categories, filenames, "others")
    carregar_imagens_dataframe(train_transition_dir, categories, filenames, "transition")


    
    df = pd.DataFrame({
        'filename': filenames,
        'category': categories
    })

    

    if qtd_retorno == 0:
        return df, train_dir, validation_dir, test_dir
    elif qtd_retorno == 1:
        return train_dir, validation_dir
    elif qtd_retorno == 2:
        return train_dir
    elif qtd_retorno == 3:
        return validation_dir
    elif qtd_retorno   == 5:
        return df

def preparar_dados(image_width, image_height, opc_return):
    # 3 - Preprocessing the data (preparing)
    train_dir, validation_dir = local_do_dataset(1)
    print(train_dir)

    # All images will be rescaled by 1./255.
    train_datagen = ImageDataGenerator(rescale=1.0 / 255.,
                                       rotation_range=45,
                                       horizontal_flip=True)
    validation_datagen = ImageDataGenerator(rescale=1.0 / 255.,
                                        rotation_range=45,
                                        horizontal_flip=True)
    # --------------------
    # Flow training images in batches of 20 using train_datagen generator
    # --------------------
    train_generator = train_datagen.flow_from_directory(train_dir,
                                                        batch_size=20,
                                                        class_mode='categorical',
                                                        target_size=(image_width, image_height))
    # --------------------
    # Flow validation images in batches of 20 using test_datagen generator
    # --------------------
    validation_generator = validation_datagen.flow_from_directory(validation_dir,
                                                            batch_size=20,                                                       
                                                            class_mode='categorical',
                                                            target_size=(image_width, image_height))
    if opc_return == 0:
        return train_generator, validation_generator
    elif opc_return == 1:
        return validation_generator

def rede_neural_convolucinal(show_sumary, image_width, image_height, img_color):
    # 2 - building the model (neural network)
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D( 16, (3, 3), activation='relu', input_shape=(image_width, image_height, img_color)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(1, 1), padding='same'),

        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),

        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),


        tf.keras.layers.Dropout(0.15),
        tf.keras.layers.Flatten(),

        # 512 neuron hidden layer
        
        
        tf.keras.layers.Dense(512, activation='relu'),
        # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('cats')
        # and 1 for the other ('dogs')
        tf.keras.layers.Dense(8, activation='softmax')
    ])

    if(show_sumary == 1):
        model.summary()

    model.compile(optimizer=RMSprop(learning_rate=0.0001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

   

    return model

def treinar_rede_neural(altura, largura):
    model = rede_neural_convolucinal(1, largura, altura, 3)

    
    #Desligar Callback no model.fit ainda não compreendo bem o funcionamento
    # my_callbacks = [
    #     tf.keras.callbacks.EarlyStopping(patience=2),
    #     tf.keras.callbacks.ModelCheckpoint(
    #         filepath='model.{epoch:02d}-{val_loss:.2f}.h5',
    #         save_weights_only=True,
    #         monitor='val_acc', 
    #         verbose=1,
    #         mode='max',
    #         save_best_only=True),
    #         tf.keras.callbacks.TensorBoard(log_dir='./logs')
    # ]

    train_generator, validation_generator = preparar_dados(largura, altura, 0)
    history = model.fit(
        train_generator,
        steps_per_epoch=20,
        epochs=5,
        validation_data=validation_generator,
        validation_steps=8,
        verbose=2,
        #callbacks=my_callbacks
        )

    # save the model
    model.save("model.h5")

    return model

