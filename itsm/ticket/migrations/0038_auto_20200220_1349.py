# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2020-02-20 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0037_auto_20200212_1554'),
    ]

    operations = [
        migrations.RemoveField(model_name='signtask', name='is_active',),
        migrations.DeleteModel(name='TaskField',),
        migrations.CreateModel(
            name='TaskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(blank=True, max_length=64, null=True, verbose_name='创建人')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updated_by', models.CharField(blank=True, max_length=64, null=True, verbose_name='修改人')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='是否软删除')),
                ('is_builtin', models.BooleanField(default=False, verbose_name='是否是内置字段')),
                ('is_readonly', models.BooleanField(default=False, verbose_name='是否只读')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否生效')),
                ('display', models.BooleanField(default=False, verbose_name='是否显示在单据列表中')),
                (
                    'source_type',
                    models.CharField(
                        choices=[('CUSTOM', '自定义数据'), ('API', '接口数据'), ('DATADICT', '数据字典'), ('RPC', 'RPC数据')],
                        default='CUSTOM',
                        max_length=32,
                        verbose_name='数据来源类型',
                    ),
                ),
                (
                    'source_uri',
                    models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='接口uri'),
                ),
                ('api_instance_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='api实例主键')),
                ('kv_relation', jsonfield.fields.JSONCharField(default={}, max_length=64, verbose_name='源数据的kv关系配置')),
                (
                    'type',
                    models.CharField(
                        choices=[
                            ('STRING', '单行文本'),
                            ('TEXT', '多行文本'),
                            ('INT', '数字'),
                            ('DATE', '日期'),
                            ('DATETIME', '时间'),
                            ('DATETIMERANGE', '时间间隔'),
                            ('TABLE', '表格'),
                            ('SELECT', '单选下拉框'),
                            ('MULTISELECT', '多选下拉框'),
                            ('CHECKBOX', '复选框'),
                            ('RADIO', '单选框'),
                            ('MEMBER', '单选人员选择'),
                            ('MEMBERS', '多选人员选择'),
                            ('RICHTEXT', '富文本'),
                            ('FILE', '附件上传'),
                            ('CUSTOMTABLE', '自定义表格'),
                            ('TREESELECT', '树形选择'),
                            ('CASCADE', '级联'),
                        ],
                        default='STRING',
                        max_length=32,
                        verbose_name='字段类型',
                    ),
                ),
                ('key', models.CharField(max_length=255, verbose_name='字段标识')),
                ('name', models.CharField(max_length=64, verbose_name='字段名')),
                (
                    'layout',
                    models.CharField(
                        choices=[('COL_6', '半行'), ('COL_12', '整行')], default='COL_6', max_length=32, verbose_name='布局'
                    ),
                ),
                (
                    'validate_type',
                    models.CharField(
                        choices=[('OPTION', '可选'), ('REQUIRE', '必填')],
                        default='REQUIRE',
                        max_length=32,
                        verbose_name='校验规则',
                    ),
                ),
                (
                    'show_type',
                    models.IntegerField(choices=[(1, '直接显示'), (0, '根据条件判断')], default=1, verbose_name='显示条件类型'),
                ),
                ('show_conditions', jsonfield.fields.JSONField(default={}, verbose_name='字段的显示条件')),
                ('regex', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='正则校验规则关键字')),
                ('regex_config', jsonfield.fields.JSONCharField(default={}, max_length=255, verbose_name='正则校验规则配置')),
                (
                    'custom_regex',
                    models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='自定义正则规则'),
                ),
                ('desc', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='字段填写说明')),
                ('tips', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='字段展示说明')),
                ('is_tips', models.BooleanField(default=False, verbose_name='额外提示')),
                ('default', models.CharField(blank=True, default='', max_length=10000, null=True, verbose_name='默认值')),
                ('choice', jsonfield.fields.JSONField(default=[], verbose_name='选项')),
                ('related_fields', jsonfield.fields.JSONField(blank=True, default={}, null=True, verbose_name='级联字段')),
                ('meta', jsonfield.fields.JSONField(default={}, verbose_name='复杂描述信息')),
                (
                    'state_id',
                    models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='对应的状态id'),
                ),
                ('_value', models.TextField(blank=True, null=True, verbose_name='表单值')),
                (
                    'source',
                    models.CharField(
                        choices=[('CUSTOM', '自定义添加'), ('TABLE', '基础模型添加')],
                        default='CUSTOM',
                        max_length=32,
                        verbose_name='添加方式',
                    ),
                ),
                ('workflow_field_id', models.IntegerField(default=-1, verbose_name='流程版本字段ID')),
                ('task_id', models.IntegerField(default=-1, verbose_name='任务ID')),
            ],
            options={'verbose_name': '任务字段值', 'verbose_name_plural': '任务字段值',},
            managers=[('_objects', django.db.models.manager.Manager()),],
        ),
    ]