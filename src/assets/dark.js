const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

function updateTheme() {
  if (prefersDarkScheme.matches)
    document.documentElement.classList.add("dark");
  else
    document.documentElement.classList.remove("dark");
};

updateTheme();
prefersDarkScheme.addEventListener("change", updateTheme);
