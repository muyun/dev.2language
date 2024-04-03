import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const postsDirectory = path.join(process.cwd(), 'posts');

export function getSortedPostsData() {
    // get file names
    const fileNames = fs.readdirSync(postsDirectory);
    const allPostsData = fileNames.map(
        (fileName) => {
            // remove ".md"
            //console.log(fileName);
            const id = fileName.replace(/\.md$/, '');
            //console.log(id);

            // read markdown
            const fullPath = path.join(postsDirectory, fileName);
            const fileContents = fs.readFileSync(fullPath, 'utf8');

            // parse
            const matterResult = matter(fileContents);

            //combine the data with id
            return { id, ...matterResult.data };

        }
    );

   

    // sort post by date
    return allPostsData.sort((a, b) => {
        if (a.date < b.date) {
            return 1;
        } else {
            return -1;
        }
    });
}

export function getAllPostsIds() {
    const fileNames = fs.readdirSync(postsDirectory);

    return fileNames.map((fileName) => {
        return {
            params: {
                id: fileName.replace(/\.md$/, ''),
            },
        };
    });
}

export async function getPostData(id) {
    const fullPath = path.join(postsDirectory, `${id}.md`);
    const fileContents = fs.readFileSync(fullPath, 'utf8');

    // parse the post metadata
    const matterResult = matter(fileContents);

    // use remark to convert markdown into HTML string
    const processedContent = await remark().use(html).process(matterResult.content);
    const contentHtml = processedContent.toString();

    // combine the data with the id
    return {
        id,
        contentHtml,
        ...matterResult.data,
    };


}

