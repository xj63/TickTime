function wakelock() {
  navigator.wakeLock.request("screen").catch(error => {
    console.error(error.name, error.message);
  })
}

document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "visible")
    wakelock();
});

wakelock();
