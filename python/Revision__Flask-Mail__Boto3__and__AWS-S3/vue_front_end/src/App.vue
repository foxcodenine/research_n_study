<template>
  <div id="app">
    <div class="container">
      <form action="#" class="form" @submit.prevent="uploadImage()">
        <h2 class="form__title">Vue / Flask AWS file upload</h2>

        <input 
          class="form__input form__input--txt " 
          type="text" 
          placeholder="Enter image name"
          v-model="imageName">
        
        <input 
          class="form__input form__input--file" 
          type="file"
          @change="onFileChange($event)">
        
        <button class="form__btn" type="submit">Upload</button>
      </form>
      <div class="image">
        <img :src="imageURL" alt="Upload Profile Picture">
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
      backEndBaseURL: 'http://127.0.0.1:5000',
      imageName: '',
      imageCover: null,
      imageURL: 'https://flask-uploads-acfbfed9-5fae-490c-9d35-291c9af697b3.s3.eu-central-1.amazonaws.com/my_fox.jpeg'
    }
  },
  methods: {

    uploadImage() {
      if (!this.imageCover || this.imageName.trim() === '') {
        return
      }
      const path = `${this.backEndBaseURL}/upload_from_vue_to_s3/`
      const payload = this.createImagePayload();
    
      axios.post(path, payload)
      .then(res => {
        console.log(res);
        this.imageURL = res.data.image_url
      })
      .catch(err => {
        console.log(err);
      })
    },
    
    createImagePayload() {
      
      let filename_extension = this.imageCover.name.split('.')
      filename_extension = filename_extension[filename_extension.length - 1]
      
      const payload = new FormData();

      

      payload.append('imageName', `${this.imageName}.${filename_extension}`);
      payload.append('imageCover', this.imageCover);
     
      return payload;
    }
    ,onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if(!files.length) {
        return
      }
      this.imageCover = files[0];
      console.log(this.imageCover);
    }
  }
}
</script>



<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif; 
  padding-top: 5rem;
}

.container {
  border: 1px #000 solid;
  border: 1px #000 solid;
  padding: 2rem 0;
  border-radius: 1rem;
  justify-content: space-evenly;
  max-width: 75rem;


  margin: 0 auto;
  display: flex;
}

.form {
  border: 1px #000 solid;
  padding: 2rem;
  border-radius: 1rem;




  display: flex;
  flex-direction: column;
  align-items: center;

  &__title {
    margin-bottom: 2rem;
  }

  &__input { 
      align-self: stretch;
      margin: 0 2rem 2rem 2rem ;
    &--txt {
      border: 1px solid #000;
      padding: .5rem 1rem;
      font-size: 1.6;
    }   
    &--file { 

      &::-webkit-file-upload-button {
          border: 1px solid #000;
          padding: .5rem 1rem;
          border-radius: .5rem;
          background-color:#fff;

      }
      &::file-selector-button {
          border: 1px solid #000;
          padding: .5rem 1rem;
          border-radius: .5rem;
          background-color:#fff;

      }
    }
  }
  &__btn {
        border: 1px solid #000;
        padding: .5rem 2rem;
        border-radius: .5rem;
        background-color: #fff;

        transition: .2s all;

        &:active {
          transform: scale(.95);
        }
  }
}

.image {
    border: 1px #000 solid;
  border-radius: 1rem;
  overflow: hidden;
  width: 23rem;
  height: 23rem;

  img {
    object-fit: cover;
    height: 100%;
    width: 100%;
  }

}

</style>
