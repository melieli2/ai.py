const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
const synth = window.speechSynthesis;

const listenBtn = document.getElementById('listen-btn');
const responseText = document.getElementById('response-text');

recognition.lang = 'sq-AL';
recognition.continuous = false;

let isListening = false;

listenBtn.addEventListener('click', () => {
  if (isListening) {
    recognition.stop();
  } else {
    recognition.start();
  }
});

recognition.onstart = () => {
  isListening = true;
  listenBtn.textContent = 'Ndalo dëgjimin';
};

recognition.onend = () => {
  isListening = false;
  listenBtn.textContent = 'Fillo të dëgjosh';
};

recognition.onresult = (event) => {
  const command = event.results[0][0].transcript.toLowerCase();
  displayAndRespond(command);
};

function displayAndRespond(command) {
  responseText.textContent = `Ke thënë: "${command}"`;

  if (command.includes('përshëndetje')) {
    respond('Përshëndetje! Si mund të të ndihmoj sot?');
  } else if (command.includes('si je')) {
    respond('Jam këtu për të ndihmuar, faleminderit! Si je ti?');
  } else if (command.includes('çfarë bën')) {
    respond('Jam këtu, duke të pritur për ndonjë komandë.');
  } else if (command.includes('faleminderit')) {
    respond('Të lutem! Jam këtu për të ndihmuar.');
  } else if (command.includes('orën') || command.includes('sa është ora')) {
    const now = new Date();
    const time = now.toLocaleTimeString('sq-AL', { hour: '2-digit', minute: '2-digit' });
    respond(`Ora është ${time}.`);
  } else if (command.includes('moti')) {
    respond('Më fal, nuk mund të marr të dhëna të motit tani. Kontrollo një aplikacion të motit për informacionin më të fundit.');
  } else if (command.includes('fakt të rastësishëm')) {
    const facts = [
      'Delfinët flenë vetëm me një sy të hapur.',
      'Gjelat mund të fluturojnë për rreth 10 sekonda.',
      'Bletët mund të dallojnë fytyrat njerëzore.',
      'Zemra e një breshke rrah vetëm 6 herë në minutë në gjendje të qetë.',
      'Shkronja më e përdorur në botë është "e".'
    ];
    const randomFact = facts[Math.floor(Math.random() * facts.length)];
    respond(`Ja një fakt: ${randomFact}`);
  } else if (command.includes('shaka')) {
    const jokes = [
      'Pse nuk mund të hajnë akullore pinguinët? Sepse gjithmonë e hedhin në det!',
      'Çfarë bëri kompjuteri kur u mërzit? Ai u bë me humor byte!',
      'Pse kalon rruga pulën? Për të dalë në anën tjetër!'
    ];
    const randomJoke = jokes[Math.floor(Math.random() * jokes.length)];
    respond(randomJoke);
  } else if (command.includes('motivim') || command.includes('motivues')) {
    const quotes = [
      'Mos ndaloni kurrë së ëndërruari, sepse ëndrrat janë fillimi i suksesit.',
      'Nëse sot nuk është dita jote, mos u shqetëso. Nesër mund të jetë.',
      'E vetmja gjë që qëndron midis jush dhe suksesit është përpjekja e vazhdueshme.',
      'Fillimi është hapi më i vështirë, por ai është më i rëndësishmi.'
    ];
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    respond(randomQuote);
  } else if (command.includes('stop')) {
    respond('Po ndalem tani. Mirupafshim!');
    recognition.stop();
  } else {
    respond('Nuk e kuptova komandën. Mund të provosh përsëri?');
  }
}

function respond(text) {
  responseText.textContent = text;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'sq-AL';
  synth.speak(utterance);
}