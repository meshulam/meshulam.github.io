---
layout: post
title: Dotfile Makeover 2016
date: '2016-01-18 18:16:49'
---

For the past couple years, I've halfheartedly maintained a [dotfile repository](https://github.com/meshulam/dotfiles) where I keep config files for the Unix-style applications I use on a regular basis. Most of it was naïvely adopted from convincing-sounding commenters on Hacker News, who mandated using the hottest Z Shell frameworks, Vim plugin managers, and other configuration esoterica.

A lot about it was kind of magic to me, and I had a suspicion that some of the configuration was unnecessary for my own use, or was even resulting in poor performance. So I finally decided to give my configs a once-over.

### Objectives

I use a small number of computers and OSes on a regular basis: personal and work OS X laptops, personal Ubuntu server, plus the fleet of CentOS servers that I need to log into occasionally. While the specific breakdown will change over time, I wanted my personal configuration to reflect some aspects of how I use computers:

* **OS neutral** - My configs should be relatively portable across different Unix-like OSes.
* **As simple as possible, but no simpler** - Just like in real software development, every additional component has an intrinsic cost in complexity and future maintenance. Before adding a new tool or changing something, evaluate whether it's worth the cost.
* **Enrichment over redefinition** - There will always be times when I need to log onto a box that doesn't have my configs installed. This should ideally not be a miserable experience. Changing keybindings and stuff is fine, but my own environment shouldn't differ too dramatically from a "stock" setup. No need to reinvent the wheel, after all.

There were two main areas I wanted to focus on: my shell and Vim configs.

### Shell

Most people get on perfectly well with Bash, but I chose to stick with ZSH, which I've been using for a couple years. This was mainly because I've gotten used to the awesome tab-completion, but re-reading [this presentation](http://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692) reaffirmed my conviction.

I've been using [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) since I started using zsh, but have been thinking about dumping it for a while. It seems to make new terminal sessions start up slowly, and I wasn't sure I needed a whole plugin system to configure the few things I actually use from it.

I made a simple [.zshrc](https://github.com/meshulam/dotfiles/blob/master/.zshrc) that  sources all files in a given directory, letting me split up my config into separate files for aliases, prompt, etc:

    ZSH=~/cfg/zsh
    GLOB="${ZSH}/*"
    for sourcefile in $~GLOB
    do
        source "$sourcefile"
    done

This seems to be a good compromise between a framework like oh-my-zsh and a single monolithic .zshrc. I started with a totally blank slate and have been re-adding aliases and options that I've noticed not working the way I want or expect. 

Notable things I did:

- Replaced oh-my-zsh's git prompt with Git's provided [git-prompt.sh](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh)
- Learned how to configure [history sharing between shell sessions](https://github.com/meshulam/dotfiles/blob/a0bd77afdda1f2a3616da7fd490269762dfa4705/zsh/history.zsh) so I know why it sometimes doesn't behave how I expect it to

I really like that I've either written or explicitly added everything that gets sourced. I think I'll be much less likely to be surprised by behavior or performance problems in the future.

### Vim config

I wound up sticking with [Pathogen](https://github.com/tpope/vim-pathogen) as a Vim plugin manager and using Git submodules to pin to plugin versions. There are newer frameworks that help with stuff like auto-updating, but I don't add/update plugins too often so I wanted to stick with the simplest thing. I don't use submodules in Git too often, so I made a command cheatsheet for adding/updating them.

I still went through my existing plugins and vimrc and made some changes:

* Set spacebar as the leader key and started using it in custom keybindings. I never got too crazy with adding key mappings but I can see myself using it more now that I understand the leader is basically a user-owned "namespace" for shortcuts.
* Mapped 'jk' to exiting insert mode: `inoremap jk <esc>`. This one has been a life-changer. Hitting escape has been in my muscle memory for years, but after a day I was totally used to it and will never go back. It's so fast!
* Got rid of [MiniBufExpl](https://github.com/fholgado/minibufexpl.vim) as a way to display open buffers like tabs. I still get the urge to cycle through buffers, but I'm trying to break that habit and figure out a more vim-like workflow that works for me. For now, listing buffers and switching by number is working okay.

### Further changes

At some point I'll tackle my tmux config, since I'm sure I could be using more of its power day-to-day. I'd also like to write an install script to automatically symlink the config files from the repo to their expected locations. But for now I'm happy with where things are at, and being more familiar with my configs will make me more likely to dive in and change stuff if I feel the need to.