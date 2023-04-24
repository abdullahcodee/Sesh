Vue.component('video-to-text', {
  template: `
    <div class="pl-7 pt-32">
      <h1 class="text-6xl pl-3 md:text-8xl lg:text-9xl font-bold text-red-600 animate-title"> SESH </h1>
      <h2 class="text-2xl pl-3 lg:text-6xl md:text-4xl animate-title"> TRANSCRIBE </h2>
      <h2 class="text-2xl pl-3 lg:text-6xl md:text-4xl animate-title"> VIDEO TO TEXT</h2>
      <p class="pt-4 pl-3 text-xs md:text-base animate-title">Convert any video to a text transcription online</p>

      <form action="/convert" method="post" enctype="multipart/form-data">
        <!-- Existing file input field -->
        <input
          class=" mb-3 rounded-sm py-2 px-3 uppercase text-xs font-bold cursor-pointer tracking-wider border-none  lg:border-black border-2"
          type="file" name="file">

        <select name="language" id="language"
          class="mt-4 rounded-md py-2 px-3 uppercase text-xs font-bold text-white cursor-pointer tracking-wider ml-3 border-black border-2 bg-red-500 hover:bg-red-300">
          <option value="en">English</option>

        </select>

        <!-- Existing submit button -->
        <input
          class="mt-4 rounded-md py-2 px-3 uppercase text-xs font-bold text-white cursor-pointer tracking-wider ml-3 border-black border-2 bg-blue-400 hover:bg-green-400"
          type="submit" value="Convert" :disabled="loading">
        <span v-if="loading" class="loading-spinner ml-2">&#9696;</span>
      </form>
    </div>
  `,
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    convertVideo() {
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
      }, 3000);
    }
  }
});

new Vue({
  el: '#app'
});


  function copyText() {
    /* Get the text element */
    var textElement = document.querySelector(".ml-3.mr-48.mt-2");
    /* Create a textarea element to hold the text */
    var textareaElement = document.createElement("textarea");
    /* Set the value of the textarea to the text content of the text element */
    textareaElement.value = textElement.textContent;
    /* Append the textarea element to the DOM */
    document.body.appendChild(textareaElement);
    /* Select the text in the textarea */
    textareaElement.select();
    textareaElement.setSelectionRange(0, 99999); /* For mobile devices */
    /* Copy the text to the clipboard */
    document.execCommand("copy");
    /* Remove the textarea element from the DOM */
    document.body.removeChild(textareaElement);
    /* Show a notification or any other indication that the text has been copied */
    // alert("Text copied to clipboard!");
  }


  
