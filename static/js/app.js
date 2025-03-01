// Fetch articles from News API endpoint
async function fetchArticles() {
  try {
    console.log("Fetching articles...") // Debug log
    const response = await fetch("/api/news/")

    console.log("Response status:", response.status) // Debug log

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    const data = await response.json()
    console.log("Received data:", data) // Debug log

    if (data.status === "ok" && data.articles && data.articles.length > 0) {
      console.log("Processing articles...") // Debug log

      // Get the first article as featured
      const featuredArticle = data.articles[0]
      updateFeaturedArticle(featuredArticle)

      // Get the next 4 articles for sidebar
      const sidebarArticles = data.articles.slice(1, 5)
      updateSidebarArticles(sidebarArticles)

      // Get the next 4 articles for bottom section
      const bottomArticles = data.articles.slice(5, 9)
      updateBottomArticles(bottomArticles)
    } else {
      console.error("No articles found in the response:", data)
      showError("No articles found")
    }
  } catch (error) {
    console.error("Error fetching articles:", error)
    showError("Failed to load articles")
  }
}

// Format date to readable format
function formatDate(dateString) {
  const date = new Date(dateString)
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}

// Calculate read time based on content length
function calculateReadTime(content) {
  if (!content) return 3
  const wordCount = content.split(/\s+/).length
  const readTime = Math.ceil(wordCount / 200)
  return readTime < 1 ? 1 : readTime
}

// Show error message to user
function showError(message) {
  const featuredSection = document.getElementById("featured-article")
  if (featuredSection) {
    const titleElement = featuredSection.querySelector("h1")
    const descriptionElement = featuredSection.querySelector("p")

    if (titleElement) titleElement.textContent = "Error Loading News"
    if (descriptionElement) descriptionElement.textContent = message
  }
}

// Update featured article with data from API
function updateFeaturedArticle(article) {
  console.log("Updating featured article:", article) // Debug log
  const featuredSection = document.getElementById("featured-article")
  if (!featuredSection) return

  const titleElement = featuredSection.querySelector("h1")
  const descriptionElement = featuredSection.querySelector("p")
  const sourceElement = featuredSection.querySelector(".text-gray-400 span:first-child")
  const authorElement = featuredSection.querySelector(".text-gray-400 span:nth-child(3)")
  const dateElement = featuredSection.querySelector(".text-gray-400 span:nth-child(5)")
  const imageContainer = featuredSection.querySelector(".md\\:w-1\\/2:last-child")

  if (titleElement) titleElement.textContent = article.title
  if (descriptionElement) descriptionElement.textContent = article.description
  if (sourceElement) sourceElement.textContent = article.source.name
  if (authorElement) authorElement.textContent = article.author || "Unknown Author"
  if (dateElement) dateElement.textContent = formatDate(article.publishedAt)

  if (imageContainer) {
    imageContainer.innerHTML = `
            <img src="${article.urlToImage || "/static/images/placeholder.jpg"}" 
                 alt="${article.title}"
                 class="w-full h-64 object-cover rounded-lg"
                 onerror="this.src='/static/images/placeholder.jpg'"
            >
        `
  }
}

// Update sidebar articles with data from API
function updateSidebarArticles(articles) {
  console.log("Updating sidebar articles:", articles) // Debug log
  const sidebarSection = document.getElementById("sidebar-articles")
  if (!sidebarSection) return

  sidebarSection.innerHTML = articles
    .map((article) => {
      const readTime = calculateReadTime(article.content)
      return `
            <div class="flex gap-4">
                <img src="${article.urlToImage || "/static/images/placeholder.jpg"}" 
                     alt="${article.title}" 
                     class="w-24 h-24 object-cover rounded-lg"
                     onerror="this.src='/static/images/placeholder.jpg'"
                >
                <div>
                    <div class="text-sm text-gray-400 mb-1">${article.author || "Unknown Author"} | ${formatDate(article.publishedAt)}</div>
                    <h3 class="text-lg font-bold mb-1">${article.title}</h3>
                    <div class="flex items-center text-sm text-gray-400 space-x-4">
                        <span>${article.source.name}</span>
                        <span>|</span>
                        <span>${readTime} mins read</span>
                    </div>
                </div>
            </div>
        `
    })
    .join("")
}

// Update bottom articles with data from API
function updateBottomArticles(articles) {
  console.log("Updating bottom articles:", articles) // Debug log
  const bottomSection = document.getElementById("bottom-articles")
  if (!bottomSection) return

  bottomSection.innerHTML = articles
    .map((article) => {
      const readTime = calculateReadTime(article.content)
      return `
            <div>
                <div class="text-sm text-gray-400 mb-2">${article.author || "Unknown Author"} | ${formatDate(article.publishedAt)}</div>
                <h3 class="text-xl font-bold mb-2">${article.title}</h3>
                <div class="flex items-center text-sm text-gray-400 space-x-4 mb-2">
                    <span>${article.source.name}</span>
                    <span>|</span>
                    <span>${readTime} mins read</span>
                </div>
            </div>
        `
    })
    .join("")
}

// Initialize when the DOM is loaded
document.addEventListener("DOMContentLoaded", fetchArticles)

