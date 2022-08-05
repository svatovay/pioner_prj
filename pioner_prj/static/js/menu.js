window.addEventListener("load", function () {
  const menuEls = document.querySelector("#menu").querySelectorAll("a");
  const titleEl = document.querySelector("title");
  makeRequest("/auth/rights_checking", menuEls);
  markMenuEl(menuEls, titleEl);
});

function markMenuEl(inputMenuEls, inputTitleEl) {
  inputMenuEls.forEach(inputMenuEl => {
    if (inputMenuEl.innerText.toLowerCase() === inputTitleEl.innerText.toLowerCase()) {
      elClasses = inputMenuEl.classList;
      elClasses.toggle("link-dark");
      elClasses.toggle("link-secondary");
    };
  });
};

function makeRequest(url, inputMenuEls) {
  httpRequest = new XMLHttpRequest();
  httpRequest.overrideMimeType('text/xml');
  httpRequest.open('GET', url, true);
  httpRequest.responseType = 'json';
  httpRequest.send(null);
  httpRequest.onreadystatechange = function() {
      hideMenuEl(httpRequest.response, inputMenuEls);
  };
};

function hideMenuEl(inputResponse, inputMenuEls) {
  if (httpRequest.readyState === 4 && httpRequest.status === 200){
    inputMenuEls.forEach(inputMenuEl => {
      dataRights = inputMenuEl.dataset.rights;
      if (dataRights === "" || inputResponse[dataRights]) {
        inputMenuEl.parentElement.hidden = false;
      };
    });
  };
};
