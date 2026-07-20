const courseGrid = document.querySelector("#course-grid");

const escapeHtml = (value) => String(value ?? "")
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

const renderCourses = (courses) => {
  courseGrid.innerHTML = courses.map((course, index) => {
    const tags = (course.tags ?? []).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("");
    const number = String(index + 1).padStart(2, "0");
    return `
      <article class="course-card">
        <div class="course-index"><span>COURSE ${number}</span><span class="course-status">${escapeHtml(course.statusLabel ?? "课程入口")}</span></div>
        <h3>${escapeHtml(course.title)}</h3>
        <p>${escapeHtml(course.description)}</p>
        <div class="tag-list">${tags}</div>
        <a class="course-link" href="${escapeHtml(course.path)}">打开云端课件 <span>↗</span></a>
      </article>`;
  }).join("");
};

fetch("./courses/catalog.json")
  .then((response) => {
    if (!response.ok) throw new Error(`catalog request failed: ${response.status}`);
    return response.json();
  })
  .then((data) => renderCourses(data.courses ?? []))
  .catch(() => {
    courseGrid.innerHTML = `<div class="loading-card">课程目录暂时无法展开，请直接查看 <a class="text-link" href="./courses/catalog.json">catalog.json</a>。</div>`;
  });
