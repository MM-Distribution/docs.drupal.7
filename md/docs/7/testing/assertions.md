---
title: "Writing SimpleTest assertions"
source_url: "https://www.drupal.org/docs/7/testing/assertions"
page_type: page
last_updated: "Last updated on 26 July 2020"
published: "2008-06-02T22:14:43+00:00"
modified: "2020-07-26T18:02:42+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:12:08Z"
raw: "raw/docs/7/testing/assertions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing SimpleTest assertions

Up to date documentation or additions may be found at [the api.drupal.org reference site](http://api.drupal.org/api/drupal/modules--simpletest--drupal_web_test_case.php/7/source) (not necessarily formatted for browsing).

Note: Whenever you pass a message into a SimpleTest assertion, do NOT translate the message using [t()](http://api.drupal.org/api/function/t/7). (To format a string with variables, use [format_string()](http://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/format_string/7) instead.)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="header">
<th>Method</th>
<th>Description</th>
<th>Example usage</th>
</tr>
&#10;<tr class="odd">
<td><div class="sourceCode" id="cb1"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertTrue(<span class="va">$result</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="kw">FALSE</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$result</code> resolves to TRUE.</td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="va">$valid</span> <span class="op">=</span> is_valid(<span class="st">&#39;foo&#39;</span>)<span class="ot">;</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertTrue(<span class="va">$valid</span><span class="ot">,</span> <span class="st">&#39;foo is a valid variable.&#39;</span>)<span class="ot">;</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb3"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFalse(<span class="va">$result</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$result</code> resolves to FALSE.</td>
<td><div class="sourceCode" id="cb4"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="va">$valid</span> <span class="op">=</span> is_valid(<span class="st">&#39;bar&#39;</span>)<span class="ot">;</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFalse(<span class="va">$valid</span><span class="ot">,</span> <span class="st">&#39;bar is not a valid variable.&#39;</span>)<span class="ot">;</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb5"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNull(<span class="va">$value</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$value</code> resolves to NULL.</td>
<td><div class="sourceCode" id="cb6"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a><span class="va">$result</span> <span class="op">=</span> load_my_object(<span class="op">-</span><span class="dv">1</span>)<span class="ot">;</span></span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNull(<span class="va">$result</span><span class="ot">,</span> <span class="st">&#39;NULL is returned when trying to load an invalid object.&#39;</span>)<span class="ot">;</span></span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb7"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotNull(<span class="va">$value</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$value</code> does NOT resolve to NULL.</td>
<td><div class="sourceCode" id="cb8"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a><span class="va">$result</span> <span class="op">=</span> load_my_object(<span class="dv">1</span>)<span class="ot">;</span></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotNull(<span class="va">$result</span><span class="ot">,</span> <span class="st">&#39;A non-null result was returned when trying to load a valid object.&#39;</span>)<span class="ot">;</span></span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb9"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertEqual(<span class="va">$first</span><span class="ot">,</span> <span class="va">$second</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$first</code> is roughly equivalent (==) to <code class="language-php">$second</code>.</td>
<td><div class="sourceCode" id="cb10"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb10-2"><a href="#cb10-2" aria-hidden="true" tabindex="-1"></a>menu_set_active_item(<span class="st">&#39;node/3&#39;</span>)<span class="ot">;</span></span>
<span id="cb10-3"><a href="#cb10-3" aria-hidden="true" tabindex="-1"></a><span class="va">$arg</span> <span class="op">=</span> arg(<span class="dv">1</span>)<span class="ot">;</span></span>
<span id="cb10-4"><a href="#cb10-4" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertEqual(<span class="va">$arg</span><span class="ot">,</span> <span class="dv">3</span><span class="ot">,</span> <span class="st">&#39;arg(1) on page node/3 resolves to 3.&#39;</span>)<span class="ot">;</span></span>
<span id="cb10-5"><a href="#cb10-5" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb11"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb11-1"><a href="#cb11-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb11-2"><a href="#cb11-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotEqual(<span class="va">$first</span><span class="ot">,</span> <span class="va">$second</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb11-3"><a href="#cb11-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$first</code> is not roughly equivalent (!=) to <code class="language-php">$second</code>.</td>
<td><div class="sourceCode" id="cb12"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a>menu_set_active_item(<span class="st">&#39;node/3&#39;</span>)<span class="ot">;</span></span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a><span class="va">$arg</span> <span class="op">=</span> arg(<span class="dv">0</span>)<span class="ot">;</span></span>
<span id="cb12-4"><a href="#cb12-4" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotEqual(<span class="va">$arg</span><span class="ot">,</span> <span class="dv">3</span><span class="ot">,</span> <span class="st">&#39;arg(0) on page node/3 does not resolve to 3.&#39;</span>)<span class="ot">;</span></span>
<span id="cb12-5"><a href="#cb12-5" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb13"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb13-2"><a href="#cb13-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertIdentical(<span class="va">$first</span><span class="ot">,</span> <span class="va">$second</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb13-3"><a href="#cb13-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$first</code> is absolutely identical (===) to <code class="language-php">$second</code>.</td>
<td><div class="sourceCode" id="cb14"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a><span class="va">$awesome</span> <span class="op">=</span> get_awesome()<span class="ot">;</span></span>
<span id="cb14-3"><a href="#cb14-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertIdentical(<span class="va">$awesome</span><span class="ot">,</span> t(<span class="st">&#39;Drupal&#39;</span>)<span class="ot">,</span> <span class="st">&#39;Drupal is awesome.&#39;</span>)<span class="ot">;</span></span>
<span id="cb14-4"><a href="#cb14-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb15"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb15-2"><a href="#cb15-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotIdentical(<span class="va">$first</span><span class="ot">,</span> <span class="va">$second</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb15-3"><a href="#cb15-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the variable <code class="language-php">$first</code> is not absolutely identical (!==) to <code class="language-php">$second</code>.</td>
<td><div class="sourceCode" id="cb16"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a><span class="va">$awesome</span> <span class="op">=</span> get_awesome()<span class="ot">;</span></span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotIdentical(<span class="va">$awesome</span><span class="ot">,</span> t(<span class="st">&#39;Drupal</span><span class="sc">\&#39;</span><span class="st">s evil twin&#39;</span>)<span class="ot">,</span> <span class="st">&#39;Drupal</span><span class="sc">\&#39;</span><span class="st">s evil twin is NOT awesome.&#39;</span>)<span class="ot">;</span></span>
<span id="cb16-4"><a href="#cb16-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td colspan="3"><h3 id="return_values">Checking page results</h3></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb17"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb17-2"><a href="#cb17-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertPattern(<span class="va">$pattern</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb17-3"><a href="#cb17-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the raw html content of the current page matches the regular expression <code class="language-php">$pattern</code>.</td>
<td><div class="sourceCode" id="cb18"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb18-2"><a href="#cb18-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertPattern(<span class="st">&#39;|[Dd]rupal|&#39;</span><span class="ot">,</span> <span class="st">&#39;Drupal/drupal is on current page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb18-3"><a href="#cb18-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb19"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb19-1"><a href="#cb19-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb19-2"><a href="#cb19-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoPattern(<span class="va">$pattern</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;%s&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb19-3"><a href="#cb19-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the raw html content of the current page does not match the regular expression <code class="language-php">$pattern</code>.</td>
<td><div class="sourceCode" id="cb20"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb20-1"><a href="#cb20-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb20-2"><a href="#cb20-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoPattern(<span class="st">&#39;|[Ee]vil|&#39;</span><span class="ot">,</span> <span class="st">&#39;Evil/evil is not on current page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb20-3"><a href="#cb20-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb21"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb21-1"><a href="#cb21-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb21-2"><a href="#cb21-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertRaw(<span class="va">$raw</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&quot;%s&quot;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb21-3"><a href="#cb21-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the html <code class="language-php">$raw</code> appears in the raw html content of the current page in the SimpleTest browser.</td>
<td><div class="sourceCode" id="cb22"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb22-1"><a href="#cb22-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb22-2"><a href="#cb22-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb22-3"><a href="#cb22-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertRaw(<span class="st">&#39;&lt;a href=&quot;&#39;</span><span class="op">.</span> url(<span class="st">&#39;user/password&#39;</span>) <span class="op">.</span><span class="st">&#39;&quot;&gt;&#39;</span><span class="ot">,</span> <span class="st">&#39;A link to &quot;Request new password&quot; is on the user register page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb22-4"><a href="#cb22-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb23"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb23-1"><a href="#cb23-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb23-2"><a href="#cb23-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoRaw(<span class="va">$raw</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&quot;%s&quot;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb23-3"><a href="#cb23-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the html <code class="language-php">$raw</code> does NOT appear in the raw html content of the current page in the SimpleTest browser.</td>
<td><div class="sourceCode" id="cb24"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb24-1"><a href="#cb24-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb24-2"><a href="#cb24-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;node/1&#39;</span>)<span class="ot">;</span></span>
<span id="cb24-3"><a href="#cb24-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoRaw(<span class="st">&#39;&lt;a href=&quot;&#39;</span><span class="op">.</span> url(<span class="st">&#39;user/password&#39;</span>) <span class="op">.</span><span class="st">&#39;&quot;&gt;&#39;</span><span class="ot">,</span> <span class="st">&#39;A link to  &quot;Request new password&quot; does not appear on the page node/1.&#39;</span>)<span class="ot">;</span></span>
<span id="cb24-4"><a href="#cb24-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb25"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb25-1"><a href="#cb25-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb25-2"><a href="#cb25-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertText(<span class="va">$text</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&quot;%s&quot;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb25-3"><a href="#cb25-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the text in <code class="language-php">$text</code> appears in the content of the current page in the SimpleTest browser (html-stripped).</td>
<td><div class="sourceCode" id="cb26"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb26-1"><a href="#cb26-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb26-2"><a href="#cb26-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb26-3"><a href="#cb26-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertText(t(<span class="st">&#39;Request new password&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The text &quot;Request new password&quot; appears on the user register page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb26-4"><a href="#cb26-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb27"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb27-1"><a href="#cb27-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb27-2"><a href="#cb27-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoText(<span class="va">$text</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&quot;%s&quot;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb27-3"><a href="#cb27-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the text in <code class="language-php">$text</code> does NOT appear in the content of the current page in the SimpleTest browser (html-stripped).</td>
<td><div class="sourceCode" id="cb28"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb28-1"><a href="#cb28-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb28-2"><a href="#cb28-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;node/1&#39;</span>)<span class="ot">;</span></span>
<span id="cb28-3"><a href="#cb28-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoText(t(<span class="st">&#39;Request new password&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The text &quot;Request new password&quot; does NOT appear on the page node/1.&#39;</span>)<span class="ot">;</span></span>
<span id="cb28-4"><a href="#cb28-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb29"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb29-1"><a href="#cb29-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb29-2"><a href="#cb29-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertTitle(<span class="va">$title</span><span class="ot">,</span> <span class="va">$message</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb29-3"><a href="#cb29-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the title given in <code class="language-php">$title</code> is the title of the current page in the SimpleTest browser.</td>
<td><div class="sourceCode" id="cb30"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb30-1"><a href="#cb30-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb30-2"><a href="#cb30-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;tracker&#39;</span>)<span class="ot">;</span></span>
<span id="cb30-3"><a href="#cb30-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertTitle(t(<span class="st">&#39;Recent posts&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The title on the tracker page is &quot;Recent posts&quot;.&#39;</span>)<span class="ot">;</span></span>
<span id="cb30-4"><a href="#cb30-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb31"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb31-1"><a href="#cb31-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb31-2"><a href="#cb31-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoTitle(<span class="va">$title</span><span class="ot">,</span> <span class="va">$message</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb31-3"><a href="#cb31-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the title given in <code class="language-php">$title</code> is NOT the title of the current page in the SimpleTest browser.</td>
<td><div class="sourceCode" id="cb32"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb32-1"><a href="#cb32-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb32-2"><a href="#cb32-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;tracker&#39;</span>)<span class="ot">;</span></span>
<span id="cb32-3"><a href="#cb32-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNotTitle(t(<span class="st">&#39;Wrong Title&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The title on the tracker page is not &quot;Wrong Title&quot;.&#39;</span>)<span class="ot">;</span></span>
<span id="cb32-4"><a href="#cb32-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb33"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb33-1"><a href="#cb33-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb33-2"><a href="#cb33-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertUniqueText(<span class="va">$text</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb33-3"><a href="#cb33-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the text in <code class="language-php">$text</code> appears exactly once in the content of the current page in the SimpleTest browser (html-stripped).</td>
<td><div class="sourceCode" id="cb34"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb34-1"><a href="#cb34-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb34-2"><a href="#cb34-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb34-3"><a href="#cb34-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertUniqueText(t(<span class="st">&#39;Request new password&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The text &quot;Request new password&quot; appears exactly once on the user register page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb34-4"><a href="#cb34-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb35"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb35-1"><a href="#cb35-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb35-2"><a href="#cb35-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoUniqueText(<span class="va">$text</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb35-3"><a href="#cb35-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the text in <code class="language-php">$text</code> appears more than once in the content of the current page in the SimpleTest browser (html-stripped).</td>
<td><div class="sourceCode" id="cb36"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb36-1"><a href="#cb36-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb36-2"><a href="#cb36-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb36-3"><a href="#cb36-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoUniqueText(t(<span class="st">&#39;password&#39;</span>)<span class="ot">,</span> <span class="st">&#39;The text &quot;password&quot; appears more than once on the user register page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb36-4"><a href="#cb36-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb37"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb37-1"><a href="#cb37-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb37-2"><a href="#cb37-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertLink(<span class="va">$label</span><span class="ot">,</span> <span class="va">$index</span> <span class="op">=</span> <span class="dv">0</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb37-3"><a href="#cb37-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that a link with the specified $label (the text between the anchor tags) is in the page. If more than one link will match, you may use the $index to specify which to look for.</td>
<td><div class="sourceCode" id="cb38"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb38-1"><a href="#cb38-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb38-2"><a href="#cb38-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb38-3"><a href="#cb38-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertLink(<span class="st">&#39;Register&#39;</span><span class="ot">,</span> <span class="dv">0</span><span class="ot">,</span> <span class="st">&#39;The register link appears on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb38-4"><a href="#cb38-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb39"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb39-1"><a href="#cb39-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb39-2"><a href="#cb39-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoLink(<span class="va">$label</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb39-3"><a href="#cb39-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that no link with the specified $label (the text between the anchor tags) is on the page.</td>
<td><div class="sourceCode" id="cb40"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb40-1"><a href="#cb40-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb40-2"><a href="#cb40-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb40-3"><a href="#cb40-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoLink(<span class="st">&#39;Delete&#39;</span><span class="ot">,</span> <span class="st">&#39;There is no Delete link on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb40-4"><a href="#cb40-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb41"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb41-1"><a href="#cb41-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb41-2"><a href="#cb41-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertLinkByHref(<span class="va">$href</span><span class="ot">,</span> <span class="va">$index</span> <span class="op">=</span> <span class="dv">0</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb41-3"><a href="#cb41-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that a link with the given $href or partial HREF is on the page.</td>
<td><div class="sourceCode" id="cb42"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb42-1"><a href="#cb42-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb42-2"><a href="#cb42-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb42-3"><a href="#cb42-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertLinkByHref(<span class="st">&#39;node/1&#39;</span><span class="ot">,</span> <span class="dv">0</span><span class="ot">,</span> <span class="st">&#39;A link to node 1 appears on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb42-4"><a href="#cb42-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb43"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb43-1"><a href="#cb43-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb43-2"><a href="#cb43-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoLinkByHref(<span class="va">$href</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span><span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span><span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb43-3"><a href="#cb43-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that no link with the specified $href or partial HREF is on the page.</td>
<td><div class="sourceCode" id="cb44"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb44-1"><a href="#cb44-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb44-2"><a href="#cb44-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;user/register&#39;</span>)<span class="ot">;</span></span>
<span id="cb44-3"><a href="#cb44-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoLinkByHref(<span class="st">&#39;node/&#39;</span><span class="ot">,</span> <span class="st">&#39;There are no node/ links on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb44-4"><a href="#cb44-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb45"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb45-1"><a href="#cb45-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb45-2"><a href="#cb45-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertResponse(<span class="va">$code</span><span class="ot">,</span> <span class="va">$message</span><span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb45-3"><a href="#cb45-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Asserts that the http response code for the current page in the simpletest browser matches <code class="language-php">$code</code>.</td>
<td><div class="sourceCode" id="cb46"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb46-1"><a href="#cb46-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb46-2"><a href="#cb46-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;drupalGet(<span class="st">&#39;admin&#39;</span>)<span class="ot">;</span></span>
<span id="cb46-3"><a href="#cb46-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertResponse(<span class="dv">403</span><span class="ot">,</span> <span class="st">&#39;Access is denied on the administration page.&#39;</span>)<span class="ot">;</span></span>
<span id="cb46-4"><a href="#cb46-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td colspan="3"><h3 id="returned_form">Checking form elements</h3></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb47"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb47-1"><a href="#cb47-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb47-2"><a href="#cb47-2" aria-hidden="true" tabindex="-1"></a>assertFieldById(<span class="va">$id</span><span class="ot">,</span> <span class="va">$value</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb47-3"><a href="#cb47-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field exists in the current page with the given id. If <code class="language-php">$value</code> is not an empty string, also checks that the field contains that value.</td>
<td><div class="sourceCode" id="cb48"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb48-1"><a href="#cb48-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb48-2"><a href="#cb48-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldById(<span class="st">&#39;edit-path-alias&#39;</span><span class="ot">,</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="st">&#39;The edit-path-alias exists on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb48-3"><a href="#cb48-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldById(<span class="st">&#39;edit-path-alias&#39;</span><span class="ot">,</span> <span class="st">&#39;home&#39;</span><span class="ot">,</span> <span class="st">&#39;The edit-path-alias field is set correctly&#39;</span>)<span class="ot">;</span></span>
<span id="cb48-4"><a href="#cb48-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb49"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb49-1"><a href="#cb49-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb49-2"><a href="#cb49-2" aria-hidden="true" tabindex="-1"></a>assertNoFieldById(<span class="va">$id</span><span class="ot">,</span> <span class="va">$value</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb49-3"><a href="#cb49-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field does not exists in the current page with the given id. If <code class="language-php">$value</code> is not an empty string, also checks that the field does NOT contain that value.</td>
<td><div class="sourceCode" id="cb50"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb50-1"><a href="#cb50-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb50-2"><a href="#cb50-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldById(<span class="st">&#39;edit-path-alias-wrong&#39;</span><span class="ot">,</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="st">&#39;The edit-path-alias-wrong is not on the page&#39;</span>)<span class="ot">;</span></span>
<span id="cb50-3"><a href="#cb50-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldById(<span class="st">&#39;edit-path-alias&#39;</span><span class="ot">,</span> <span class="st">&#39;wrong-name&#39;</span><span class="ot">,</span> <span class="st">&#39;The edit-path-alias field is incorrect&#39;</span>)<span class="ot">;</span></span>
<span id="cb50-4"><a href="#cb50-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb51"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb51-1"><a href="#cb51-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb51-2"><a href="#cb51-2" aria-hidden="true" tabindex="-1"></a>assertFieldByName(<span class="va">$name</span><span class="ot">,</span> <span class="va">$value</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb51-3"><a href="#cb51-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field exists in the current page with the given name and value.</td>
<td><div class="sourceCode" id="cb52"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb52-1"><a href="#cb52-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb52-2"><a href="#cb52-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldByName(<span class="st">&#39;path[alias]&#39;</span><span class="ot">,</span> <span class="st">&quot;home&quot;</span><span class="ot">,</span> <span class="st">&quot;The alias field is correctly set to &#39;home&#39;&quot;</span>)<span class="ot">;</span></span>
<span id="cb52-3"><a href="#cb52-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb53"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb53-1"><a href="#cb53-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb53-2"><a href="#cb53-2" aria-hidden="true" tabindex="-1"></a>assertNoFieldByName(<span class="va">$name</span><span class="ot">,</span> <span class="va">$value</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb53-3"><a href="#cb53-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field does NOT exist in the current page with the given name and value.</td>
<td><div class="sourceCode" id="cb54"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb54-1"><a href="#cb54-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb54-2"><a href="#cb54-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldByName(<span class="st">&#39;path[alias]&#39;</span><span class="ot">,</span> <span class="st">&quot;wrong-name&quot;</span><span class="ot">,</span> <span class="st">&quot;The alias field is not set to &#39;wrong-name&#39;&quot;</span>)<span class="ot">;</span></span>
<span id="cb54-3"><a href="#cb54-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb55"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb55-1"><a href="#cb55-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb55-2"><a href="#cb55-2" aria-hidden="true" tabindex="-1"></a>assertFieldChecked(<span class="va">$id</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb55-3"><a href="#cb55-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that the checkbox field with the given $id exists and is checked.</td>
<td><div class="sourceCode" id="cb56"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb56-1"><a href="#cb56-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb56-2"><a href="#cb56-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldChecked(<span class="st">&#39;send-me-spam&#39;</span><span class="ot">,</span> <span class="st">&quot;The user has opted in to receive spam&quot;</span>)<span class="ot">;</span></span>
<span id="cb56-3"><a href="#cb56-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb57"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb57-1"><a href="#cb57-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb57-2"><a href="#cb57-2" aria-hidden="true" tabindex="-1"></a>assertNoFieldChecked(<span class="va">$id</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb57-3"><a href="#cb57-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that the checkbox field with the given $id exists but is NOT checked.</td>
<td><div class="sourceCode" id="cb58"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb58-1"><a href="#cb58-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb58-2"><a href="#cb58-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldChecked(<span class="st">&#39;send-me-spam&#39;</span><span class="ot">,</span> <span class="st">&quot;The user has not checked the Spam checkbox.&quot;</span>)<span class="ot">;</span></span>
<span id="cb58-3"><a href="#cb58-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb59"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb59-1"><a href="#cb59-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb59-2"><a href="#cb59-2" aria-hidden="true" tabindex="-1"></a>assertOptionSelected(<span class="va">$id</span><span class="ot">,</span> <span class="va">$option</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb59-3"><a href="#cb59-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a select option in the current page is checked.</td>
<td><div class="sourceCode" id="cb60"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb60-1"><a href="#cb60-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb60-2"><a href="#cb60-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertOptionSelected(<span class="st">&#39;ice-cream-flavor&#39;</span><span class="ot">,</span> <span class="dv">2</span><span class="ot">,</span> <span class="st">&quot;The user has selected flavor 2.&quot;</span>)<span class="ot">;</span></span>
<span id="cb60-3"><a href="#cb60-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb61"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb61-1"><a href="#cb61-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb61-2"><a href="#cb61-2" aria-hidden="true" tabindex="-1"></a>assertNoOptionSelected(<span class="va">$id</span><span class="ot">,</span> <span class="va">$option</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb61-3"><a href="#cb61-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that the specified select option in the current page is NOT checked.</td>
<td><div class="sourceCode" id="cb62"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb62-1"><a href="#cb62-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb62-2"><a href="#cb62-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoOptionSelected(<span class="st">&#39;ice-cream-flavor&#39;</span><span class="ot">,</span> <span class="dv">7</span><span class="ot">,</span> <span class="st">&quot;The user has not selected flavor 7.&quot;</span>)<span class="ot">;</span></span>
<span id="cb62-3"><a href="#cb62-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb63"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb63-1"><a href="#cb63-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb63-2"><a href="#cb63-2" aria-hidden="true" tabindex="-1"></a>assertFieldByXPath(<span class="va">$xpath</span><span class="ot">,</span> <span class="va">$value</span><span class="ot">,</span> <span class="va">$message</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>) </span>
<span id="cb63-3"><a href="#cb63-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field exists in the current page by the given XPath.</td>
<td>draft, needs testing or better examples
<div class="sourceCode" id="cb64"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb64-1"><a href="#cb64-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb64-2"><a href="#cb64-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldByXPath(<span class="st">&#39;/input[@type=&quot;checkbox&quot; and position()=2]&#39;</span><span class="ot">,</span> <span class="kw">TRUE</span><span class="ot">,</span> <span class="st">&quot;The second checkbox is ticked&quot;</span>)<span class="ot">;</span> </span>
<span id="cb64-3"><a href="#cb64-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertFieldByXPath(<span class="st">&#39;/input[@name=&quot;info[]&quot; and @class=&quot;custom-class&quot;]&#39;</span><span class="ot">,</span> <span class="kw">TRUE</span><span class="ot">,</span> <span class="st">&quot;There is an input field called &#39;info&#39; with class &#39;custom-class&#39; &quot;</span>)<span class="ot">;</span> </span>
<span id="cb64-4"><a href="#cb64-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb65"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb65-1"><a href="#cb65-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb65-2"><a href="#cb65-2" aria-hidden="true" tabindex="-1"></a>assertNoFieldByXPath(<span class="va">$xpath</span><span class="ot">,</span> <span class="va">$value</span><span class="ot">,</span> <span class="va">$message</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>) </span>
<span id="cb65-3"><a href="#cb65-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that a field does NOT exist in the current page by the given XPath.</td>
<td>draft, needs testing or better examples
<div class="sourceCode" id="cb66"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb66-1"><a href="#cb66-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb66-2"><a href="#cb66-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldByXPath(<span class="st">&#39;/input[@type=&quot;checkbox&quot; and position()=2]&#39;</span><span class="ot">,</span> <span class="kw">TRUE</span><span class="ot">,</span> <span class="st">&quot;The second checkbox is not ticked&quot;</span>)<span class="ot">;</span> </span>
<span id="cb66-3"><a href="#cb66-3" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoFieldByXPath(<span class="st">&#39;/input[@name=&quot;info[]&quot; and @class=&quot;custom-class&quot;]&#39;</span><span class="ot">,</span> <span class="kw">TRUE</span><span class="ot">,</span> <span class="st">&quot;There is an input field called &#39;info&#39; with class &#39;custom-class&#39; &quot;</span>)<span class="ot">;</span> </span>
<span id="cb66-4"><a href="#cb66-4" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb67"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb67-1"><a href="#cb67-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb67-2"><a href="#cb67-2" aria-hidden="true" tabindex="-1"></a>assertNoDuplicateIds(<span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>) </span>
<span id="cb67-3"><a href="#cb67-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that each HTML ID on the page is used for just one element.</td>
<td><div class="sourceCode" id="cb68"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb68-1"><a href="#cb68-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb68-2"><a href="#cb68-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertNoDuplicateIds(<span class="st">&#39;There are no duplicate IDs&#39;</span>)<span class="ot">;</span> </span>
<span id="cb68-3"><a href="#cb68-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td colspan="3"><h3 id="misc">Miscellaneous</h3></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb69"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb69-1"><a href="#cb69-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb69-2"><a href="#cb69-2" aria-hidden="true" tabindex="-1"></a>pass(<span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb69-3"><a href="#cb69-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Make an assertion that is always positive.</td>
<td><div class="sourceCode" id="cb70"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb70-1"><a href="#cb70-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb70-2"><a href="#cb70-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;pass(<span class="st">&quot;This assertion will always pass&quot;</span>)<span class="ot">;</span></span>
<span id="cb70-3"><a href="#cb70-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb71"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb71-1"><a href="#cb71-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb71-2"><a href="#cb71-2" aria-hidden="true" tabindex="-1"></a>fail(<span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb71-3"><a href="#cb71-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Make an assertion that is always negative.</td>
<td><div class="sourceCode" id="cb72"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb72-1"><a href="#cb72-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb72-2"><a href="#cb72-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;fail(<span class="st">&quot;This assertion will always fail&quot;</span>)<span class="ot">;</span></span>
<span id="cb72-3"><a href="#cb72-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td><div class="sourceCode" id="cb73"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb73-1"><a href="#cb73-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb73-2"><a href="#cb73-2" aria-hidden="true" tabindex="-1"></a><span class="bu">error</span>(<span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$group</span> <span class="op">=</span> <span class="st">&#39;Other&#39;</span>)</span>
<span id="cb73-3"><a href="#cb73-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Make an assertion that always yields an error condition.</td>
<td><div class="sourceCode" id="cb74"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb74-1"><a href="#cb74-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb74-2"><a href="#cb74-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;<span class="bu">error</span>(<span class="st">&quot;This will generate an error.&quot;</span>)<span class="ot">;</span></span>
<span id="cb74-3"><a href="#cb74-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td><div class="sourceCode" id="cb75"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb75-1"><a href="#cb75-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb75-2"><a href="#cb75-2" aria-hidden="true" tabindex="-1"></a>assertMail(<span class="va">$name</span><span class="ot">,</span> <span class="va">$value</span> <span class="op">=</span> <span class="st">&#39;&#39;</span><span class="ot">,</span> <span class="va">$message</span> <span class="op">=</span> <span class="st">&#39;&#39;</span>)</span>
<span id="cb75-3"><a href="#cb75-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
<td>Assert that the most recently sent email message has a field $name (e.g. "subject", "body") with the given $value.</td>
<td><div class="sourceCode" id="cb76"><pre class="sourceCode php"><code class="sourceCode php"><span id="cb76-1"><a href="#cb76-1" aria-hidden="true" tabindex="-1"></a><span class="kw">&lt;?php</span></span>
<span id="cb76-2"><a href="#cb76-2" aria-hidden="true" tabindex="-1"></a><span class="va">$this</span>-&gt;assertMail(<span class="st">&quot;subject&quot;</span><span class="ot">,</span> <span class="st">&quot;My latest email&quot;</span><span class="ot">,</span> <span class="st">&#39;The last message subject was &quot;My latest email&quot;&#39;</span>)<span class="ot">;</span></span>
<span id="cb76-3"><a href="#cb76-3" aria-hidden="true" tabindex="-1"></a><span class="kw">?&gt;</span></span></code></pre></div></td>
</tr>
<tr class="even">
<td colspan="2">For Drupal 8 follow <a href="https://api.drupal.org/api/drupal/core!modules!simpletest!src!AssertContentTrait.php/trait/AssertContentTrait/8" title="trait AssertContentTrait">trait AssertContentTrait</a></td>
<td></td>
</tr>
</tbody>
</table>
