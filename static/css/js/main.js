// KATACHI Studio - Main JavaScript
// Vanilla JS implementation for animations and interactions

;(() => {
  // ============================================
  // UTILITY FUNCTIONS
  // ============================================

  function debounce(func, wait) {
    let timeout
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout)
        func(...args)
      }
      clearTimeout(timeout)
      timeout = setTimeout(later, wait)
    }
  }

  // ============================================
  // HEADER SCROLL EFFECT
  // ============================================

  function initHeaderScroll() {
    const header = document.getElementById("main-header")
    const logo = header.querySelector(".header-logo a")

    let isScrolled = false

    const handleScroll = () => {
      const scrollY = window.scrollY
      const shouldBeScrolled = scrollY > 20

      if (shouldBeScrolled !== isScrolled) {
        isScrolled = shouldBeScrolled

        if (isScrolled) {
          logo.classList.remove("text-white", "hover:text-white/80")
          logo.classList.add("text-neutral-900", "hover:text-neutral-700")
        } else {
          logo.classList.remove("text-neutral-900", "hover:text-neutral-700")
          logo.classList.add("text-white", "hover:text-white/80")
        }
      }
    }

    window.addEventListener("scroll", debounce(handleScroll, 10))
    handleScroll() // Initial check
  }

  // ============================================
  // HERO SECTION PARALLAX
  // ============================================

  function initHeroParallax() {
    const heroSection = document.getElementById("hero-section")
    if (!heroSection) return

    const heroImage = heroSection.querySelector(".hero-image")
    const heroContent = heroSection.querySelector(".hero-content")
    const infoStrip = heroSection.querySelector(".info-strip")

    const handleScroll = () => {
      const scrollY = window.scrollY
      const heroHeight = heroSection.offsetHeight
      const scrollProgress = Math.min(scrollY / heroHeight, 1)

      // Parallax effects
      if (heroImage) {
        const imageScale = 1.05 - scrollProgress * 0.1
        const imageY = scrollProgress * -50
        heroImage.style.transform = `scale(${imageScale}) translateY(${imageY}px)`
      }

      if (heroContent) {
        const contentY = scrollProgress * 100
        const contentOpacity = 1 - scrollProgress * 2
        heroContent.style.transform = `translateY(${contentY}px)`
        heroContent.style.opacity = Math.max(contentOpacity, 0)
      }

      if (infoStrip) {
        const stripOpacity = 1 - scrollProgress * 3
        infoStrip.style.opacity = Math.max(stripOpacity, 0)
      }
    }

    window.addEventListener("scroll", debounce(handleScroll, 10))
    handleScroll() // Initial check
  }

  // ============================================
  // FADE IN ANIMATIONS
  // ============================================

  function initFadeInAnimations() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px",
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible")
          observer.unobserve(entry.target)
        }
      })
    }, observerOptions)

    // Observe all fade-in elements
    document.querySelectorAll(".fade-in-up").forEach((el) => {
      observer.observe(el)
    })

    // Observe product cards
    document.querySelectorAll(".product-card").forEach((el) => {
      observer.observe(el)
    })
  }

  // ============================================
  // HERO TEXT ANIMATION
  // ============================================

  function initHeroTextAnimation() {
    const heroText = document.querySelector(".hero-text")
    const heroTextItalic = document.querySelector(".hero-text-italic")
    const heroSubtitle = document.querySelector(".hero-subtitle")

    if (heroText) {
      setTimeout(() => {
        heroText.style.opacity = "1"
        heroText.style.transform = "translateY(0)"
      }, 500)
    }

    if (heroTextItalic) {
      setTimeout(() => {
        heroTextItalic.style.opacity = "1"
        heroTextItalic.style.transform = "translateY(0)"
      }, 1100)
    }

    if (heroSubtitle) {
      setTimeout(() => {
        heroSubtitle.style.opacity = "1"
        heroSubtitle.style.transform = "translateY(0)"
      }, 700)
    }
  }

  // ============================================
  // QUICK LOOK MODAL
  // ============================================

  function initQuickLookModal() {
    const modal = document.getElementById("quick-look-modal")
    if (!modal) return

    const modalBackdrop = modal.querySelector(".modal-backdrop")
    const modalContent = modal.querySelector(".modal-content")
    const closeBtn = document.getElementById("modal-close-btn")
    const mainImage = document.getElementById("modal-main-image")
    const prevBtn = document.getElementById("modal-prev-btn")
    const nextBtn = document.getElementById("modal-next-btn")
    const thumbnailsContainer = document.getElementById("modal-thumbnails")

    let currentProduct = null
    let currentImageIndex = 0
    let productImages = []

    // Open modal
    function openModal(productData) {
      currentProduct = productData
      currentImageIndex = 0
      productImages = productData.images || [productData.image]

      // Populate modal content
      document.getElementById("modal-product-name").textContent = productData.name
      document.getElementById("modal-product-materials").textContent = productData.materials
      document.getElementById("modal-product-price").textContent = productData.price
      document.getElementById("modal-product-dimensions").textContent = productData.dimensions

      // Set main image
      updateMainImage()

      // Create thumbnails
      createThumbnails()

      // Create swatches
      createSwatches(productData.swatches)

      // Show modal
      modal.classList.remove("hidden")
      modal.classList.add("flex")
      document.body.style.overflow = "hidden"

      // Animate in
      setTimeout(() => {
        modalBackdrop.style.opacity = "1"
        modalContent.style.transform = "scale(1)"
        modalContent.style.opacity = "1"
      }, 10)
    }

    // Close modal
    function closeModal() {
      modalBackdrop.style.opacity = "0"
      modalContent.style.transform = "scale(0.9)"
      modalContent.style.opacity = "0"

      setTimeout(() => {
        modal.classList.add("hidden")
        modal.classList.remove("flex")
        document.body.style.overflow = ""
      }, 300)
    }

    // Update main image
    function updateMainImage() {
      mainImage.src = productImages[currentImageIndex]
      mainImage.alt = `${currentProduct.name} - Image ${currentImageIndex + 1}`

      // Update thumbnail active state
      const thumbnails = thumbnailsContainer.querySelectorAll("button")
      thumbnails.forEach((thumb, index) => {
        if (index === currentImageIndex) {
          thumb.classList.add("border-neutral-900")
          thumb.classList.remove("border-neutral-200")
        } else {
          thumb.classList.remove("border-neutral-900")
          thumb.classList.add("border-neutral-200")
        }
      })
    }

    // Create thumbnails
    function createThumbnails() {
      thumbnailsContainer.innerHTML = ""

      productImages.forEach((image, index) => {
        const button = document.createElement("button")
        button.className = `relative w-16 h-16 rounded-lg overflow-hidden border-2 transition-all duration-200 ${
          index === 0 ? "border-neutral-900" : "border-neutral-200"
        }`
        button.innerHTML = `<img src="${image}" alt="${currentProduct.name} thumbnail ${index + 1}" class="w-full h-full object-cover">`
        button.addEventListener("click", () => {
          currentImageIndex = index
          updateMainImage()
        })
        thumbnailsContainer.appendChild(button)
      })

      // Show/hide navigation buttons
      if (productImages.length <= 1) {
        prevBtn.style.display = "none"
        nextBtn.style.display = "none"
      } else {
        prevBtn.style.display = "block"
        nextBtn.style.display = "block"
      }
    }

    // Create swatches
    function createSwatches(swatches) {
      const swatchesContainer = document.getElementById("modal-swatches")
      swatchesContainer.innerHTML = ""

      if (!swatches || swatches.length === 0) {
        swatchesContainer.parentElement.style.display = "none"
        return
      }

      swatchesContainer.parentElement.style.display = "block"

      swatches.forEach((swatch, index) => {
        const button = document.createElement("button")
        button.className = `w-8 h-8 rounded-full border-2 transition-all duration-200 relative group ${
          index === 0 ? "border-neutral-900 scale-110" : "border-neutral-300"
        }`
        button.style.backgroundColor = swatch.color
        button.innerHTML = `
                    <div class="absolute bottom-10 left-1/2 transform -translate-x-1/2 bg-neutral-900 text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap pointer-events-none">
                        ${swatch.name}
                    </div>
                `
        swatchesContainer.appendChild(button)
      })
    }

    // Navigation
    function nextImage() {
      currentImageIndex = (currentImageIndex + 1) % productImages.length
      updateMainImage()
    }

    function prevImage() {
      currentImageIndex = (currentImageIndex - 1 + productImages.length) % productImages.length
      updateMainImage()
    }

    // Event listeners
    closeBtn.addEventListener("click", closeModal)
    modalBackdrop.addEventListener("click", closeModal)
    nextBtn.addEventListener("click", nextImage)
    prevBtn.addEventListener("click", prevImage)

    // Keyboard navigation
    document.addEventListener("keydown", (e) => {
      if (!modal.classList.contains("hidden")) {
        if (e.key === "Escape") closeModal()
        if (e.key === "ArrowRight") nextImage()
        if (e.key === "ArrowLeft") prevImage()
      }
    })

    // Attach to product cards
    document.querySelectorAll(".product-card-item").forEach((card) => {
      const quickLookBtn = card.querySelector(".quick-look-btn")

      if (quickLookBtn) {
        quickLookBtn.addEventListener("click", (e) => {
          e.preventDefault()

          const productData = {
            name: card.dataset.productName,
            price: card.dataset.productPrice,
            materials: card.dataset.productMaterials,
            dimensions: card.dataset.productDimensions,
            image: card.querySelector(".product-image").src,
            images: [card.querySelector(".product-image").src],
            swatches: [], // Can be populated from data attributes if needed
          }

          openModal(productData)
        })
      }
    })
  }

  // ============================================
  // SMOOTH SCROLL
  // ============================================

  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        const href = this.getAttribute("href")
        if (href === "#") return

        e.preventDefault()
        const target = document.querySelector(href)

        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          })
        }
      })
    })
  }

  // ============================================
  // SOCIAL LINK HOVER EFFECTS
  // ============================================

  function initSocialLinks() {
    document.querySelectorAll(".social-link").forEach((link) => {
      link.addEventListener("mouseenter", function () {
        this.style.transform = "scale(1.1)"
      })

      link.addEventListener("mouseleave", function () {
        this.style.transform = "scale(1)"
      })
    })
  }

  // ============================================
  // FOOTER LINK HOVER EFFECTS
  // ============================================

  function initFooterLinks() {
    document.querySelectorAll(".footer-link").forEach((link) => {
      const arrow = document.createElement("span")
      arrow.innerHTML = "↗"
      arrow.className = "ml-1 opacity-0 transition-opacity duration-200 inline-block"
      arrow.style.fontSize = "0.875rem"

      link.appendChild(arrow)

      link.addEventListener("mouseenter", () => {
        arrow.style.opacity = "1"
      })

      link.addEventListener("mouseleave", () => {
        arrow.style.opacity = "0"
      })
    })
  }

  // ============================================
  // INITIALIZE ALL
  // ============================================

  function init() {
    // Wait for DOM to be ready
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", init)
      return
    }

    console.log("[v0] KATACHI Studio initialized")

    // Initialize all features
    initHeaderScroll()
    initHeroParallax()
    initFadeInAnimations()
    initHeroTextAnimation()
    initQuickLookModal()
    initSmoothScroll()
    initSocialLinks()
    initFooterLinks()
  }

  // Start initialization
  init()
})()
