#!/usr/bin/env ruby

# usage: `ruby process-images.rb <sourcedir>`
#
require "fileutils"

source_dir = "../../web-images"
dest_dir = "../images"
max_size_bytes = 180 * 1000
force_overwrite = false     # If true, will overwrite dest files even if their
                            # mtime is after the source mtime

Dir.glob("#{source_dir}/**/*.{jpg,jpeg,tif,tiff}") do |filename|
  outfile = "#{dest_dir}/#{File.basename(filename, ".*")}.jpg"

  if !force_overwrite &&
      File.exist?(outfile) &&
      File.mtime(outfile) > File.mtime(filename)
    puts "skipping newer destination file #{outfile}"
    next
  end

  if File.size(filename) < max_size_bytes && File.extname(filename) == ".jpg"
    puts "copying #{filename}"
    FileUtils.cp(filename, outfile)
  else
    puts "converting #{filename}"
    v = %x[ convert "#{filename}" -resize "1024x1024" -unsharp 2x0.5+0.5+0 -quality 90 "#{outfile}" ]
  end
end
