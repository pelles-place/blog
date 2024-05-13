<script setup>
import AuthorLink from "../components/AuthorLink.vue";
import { useRoute } from "vue-router";
import { useQuery } from "@vue/apollo-composable";
import { gql } from "graphql-tag";

// ***** This doesnt work... 
// PostView.vue:14 Uncaught (in promise) RangeError: Invalid time value
//     at Proxy.displayableDate (PostView.vue:14:49)
//     at Proxy._sfc_render (PostView.vue:52:23) 


const dateFormatter = new Intl.DateTimeFormat("en-GB", { dateStyle: "full" });
const displayableDate = (date) => dateFormatter.format(new Date(date));
const route = useRoute();
const slug = route.params.slug;
const { result, loading, error } = useQuery (gql`
  query {
    postBySlug(
      slug: "${slug}"
  ) {
      title
      subtitle
      published
      publishDate
      metaDescription
      slug
      body
      author {
        user {
          username
          firstName
          lastName
      
        }
      } 
      tags {
        name
      }
    }
  }
`);
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error" class="warn">{{ error.message }}</div>
  <section v-else :set="post = result.postBySlug">
    <h2>{{ post.title }}</h2>
    <h3>{{ post.subtitle }}</h3>
    <p>{{ post.metaDescription }}</p>
    <aside>
      Published on {{ displayableDate(post.publishDate) }}<br /> 
      <!-- Published on {{ post.publishDate }}<br />  -->
      Written by <AuthorLink :author="post.author" />
      <h4>Tags</h4>
      <ul>
        <li v-for="tag in post.tags" :key="tag.name">
          <RouterLink :to="{ name: 'tag', params: { tag: tag.name } }">
            {{ tag.name }}
          </RouterLink>
        </li>
      </ul>
    </aside>
    <article>{{ post.body }}</article>
  </section>
</template>