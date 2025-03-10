import { initMobileMenu } from "./navigation.js";
import { initLanguageSwitcher } from "./languageSwitcher.js";
import { initGallery } from "./gallery.js";

// Initialisation au chargement de la page
document.addEventListener("DOMContentLoaded", () => {
  try {
    initMobileMenu();
    initLanguageSwitcher();
    initGallery();
  } catch (error) {
    console.error("Une erreur est survenue :", error);
  }
});

// Gestion des transitions CSS
document.documentElement.classList.add("transitions-enabled");

// Prévention du FOUC (Flash of Unstyled Content)
document.documentElement.classList.remove("no-js");
