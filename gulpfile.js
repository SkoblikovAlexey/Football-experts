import gulp from 'gulp';
const { src, dest, watch, parallel, series } = gulp;
import autoprefixer from 'gulp-autoprefixer';
import browser from 'browser-sync';
import concat from 'gulp-concat';
import cheerio from 'gulp-cheerio';
// import csso from 'gulp-csso';
// import del from 'del';
// import fs from 'fs';
import notify from 'gulp-notify';
import plumber from 'gulp-plumber';
import rename from 'gulp-rename';
import sass from 'gulp-dart-sass';
import sourcemaps from 'gulp-sourcemaps';
import svgmin from 'gulp-svgmin';
import svgstore from 'gulp-svgstore';

/**
 *  Основные директории
 */
const Dirs = {
  APP: 'app',
  STATIC: 'app/static'
};

/**
 * Пути к файлам
 */
const path = {
  styles: {
    root: `${Dirs.APP}/sass/`,
    all: `${Dirs.APP}/sass/**/*.scss`,
    compile: `${Dirs.APP}/sass/styles.scss`,
    save: `${Dirs.STATIC}/css/`
  },
  templates: {
    root: `${Dirs.APP}/templates/`,
    pages: `${Dirs.APP}/templates/pages/`
  },
  scripts: {
    root: `${Dirs.STATIC}/mjs/`,
    save: `${Dirs.STATIC}/js/`
  },
  svg: {
    icons: `${Dirs.STATIC}/img/icons/`,
    sprite: `${Dirs.STATIC}/img/`
  },
  img: {
    root: `${Dirs.STATIC}/img/`,
  },
  images: {
    root: `${Dirs.STATIC}/images/`,
  },
  vendor: {
    styles: `${Dirs.APP}/vendor/css/`,
    scripts: `${Dirs.APP}/vendor/js/`
  }
};

/**
 * Основные задачи
 */
export const styles = () => src(path.styles.compile)
  .pipe(sourcemaps.init())
  .pipe(sass.sync().on('error', sass.logError))
  // .pipe(dest(path.styles.save))
  .pipe(autoprefixer())
  // .pipe(csso())
  .pipe(rename({
    suffix: `.min`
  }))
  .pipe(sourcemaps.write('.'))
  .pipe(dest(path.styles.save));

export const scripts = () => src(`${path.scripts.root}main.mjs`)
  .pipe(concat('script.js'))
  .pipe(dest(path.scripts.save)) // TODO: babel?
  // TODO: minify
  .pipe(rename({
    suffix: '.min'
  }))
  .pipe(dest(path.scripts.save));

// export const clean = () => del([dirs.dest]);

export const server = () => {
  const bs = browser.init({
    proxy: '127.0.0.1:5000',
    cors: true,
    notify: false,
    ui: false,
    open: false,
    scrollThrottle: 100,
  });
  watch(`${path.styles.root}**/*.scss`, styles).on('change', bs.reload);
  watch(`${path.templates.root}**/*.j2`).on('change', bs.reload);
  watch(`${path.scripts.root}**/*.js`, scripts).on('change', bs.reload);
  watch(`${path.svg.icons}**/*.svg`, sprite).on('change', bs.reload);
};

export const sprite = () => src(`${path.svg.icons}**/*.svg`)
  .pipe(plumber({errorHandler: notify.onError("Error: <%= error.message %>")}))
  .pipe(svgmin({
    plugins: [{
      removeDoctype: true
    }, {
      removeXMLNS: true
    }, {
      removeXMLProcInst: true
    }, {
      removeComments: true
    }, {
      removeMetadata: true
    }, {
      removeEditorNSData: true
    }, {
      removeViewBox: false
    }]
  }))
  .pipe(cheerio({
    run: function ($) {
      // $('[fill]').removeAttr('fill');
      // $('[stroke]').removeAttr('stroke');
      $('[style]').removeAttr('style');
    },
    parserOptions: {xmlMode: true}
  }))
  .pipe(svgstore({
    inlineSvg: true
  }))
  .pipe(rename('sprite.svg'))
  .pipe(dest(path.svg.sprite))

const vendorStyles = () => src(`${path.vendor.styles}*.css`)
  .pipe(dest(`${path.styles.save}`))

const vendorScripts = () => src(`${path.vendor.scripts}*.js`)
  .pipe(dest(`${path.scripts.save}`))

export const vendor = parallel(vendorStyles, vendorScripts);

/**
 * Задачи для разработки
 */
export const start = series(parallel(styles, scripts, vendor, sprite), server);

/**
 * Для билда
 */
// TODO: добавить images+
export const build = series(styles, scripts, vendor, sprite);

export default start;
