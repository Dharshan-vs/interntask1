#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create instructor group
instructor_group, created = Group.objects.get_or_create(name='instructor')

if created:
    print("✅ Created 'instructor' group")
    
    # Get all permissions
    all_permissions = Permission.objects.all()
    
    # Add all permissions to instructor group
    instructor_group.permissions.set(all_permissions)
    
    print(f"✅ Added {all_permissions.count()} permissions to instructor group")
else:
    print("ℹ️ 'instructor' group already exists")

print("🎉 Setup complete! Instructor group is ready.")
