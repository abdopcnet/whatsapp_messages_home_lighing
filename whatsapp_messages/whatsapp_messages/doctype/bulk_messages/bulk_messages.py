# Copyright (c) 2025, abdopcnet@gmail.com and contributors
# For license information, please see license.txt

import frappe
import os
from frappe.model.document import Document
from frappe.utils import get_files_path, get_hook_method
from frappe import _


class bulk_messages(Document):
	def validate(self):
		# Validate whatsapp_image field
		if self.whatsapp_image:
			self._validate_file_field('whatsapp_image', allowed_extensions=['jpg', 'jpeg', 'png'])
		
		# Validate whatsapp_attach_video field
		if self.whatsapp_attach_video:
			self._validate_file_field('whatsapp_attach_video', allowed_extensions=['mp4'])
	
	def _validate_file_field(self, fieldname, allowed_extensions):
		"""Validate file field: no spaces, correct extension, and public"""
		file_path = getattr(self, fieldname, None)
		if not file_path:
			return
		
		# Extract filename from path
		filename = os.path.basename(file_path.split('?')[0])
		
		# Check for spaces in filename
		if ' ' in filename:
			frappe.throw(
				_("اسم الملف لا يمكن أن يحتوي على مسافات. يرجى إعادة تسمية الملف: {0}").format(filename),
				title=_("اسم ملف غير صحيح")
			)
		
		# Check file extension
		file_extension = os.path.splitext(filename)[1].lstrip('.').lower()
		if file_extension not in allowed_extensions:
			# Translate extension names to Arabic
			ext_names_ar = {
				'jpg': 'jpg',
				'jpeg': 'jpeg',
				'png': 'png',
				'mp4': 'mp4'
			}
			allowed_ar = ', '.join([ext_names_ar.get(ext, ext) for ext in allowed_extensions])
			frappe.throw(
				_("امتداد الملف يجب أن يكون واحداً من: {0}. تم العثور على: {1}").format(
					allowed_ar, 
					file_extension or 'لا يوجد'
				),
				title=_("امتداد ملف غير صحيح")
			)
		
		# Check if file is public
		file_docs = frappe.get_all(
			"File",
			filters={"file_url": file_path.split('?')[0]},
			fields=["name", "is_private"],
			limit=1
		)
		
		if file_docs:
			file_doc = frappe.get_doc("File", file_docs[0].name)
			if file_doc.is_private:
				frappe.throw(
					_("الملف يجب أن يكون عام (ليس خاص). الملف: {0}").format(filename),
					title=_("الملف يجب أن يكون عام")
				)
