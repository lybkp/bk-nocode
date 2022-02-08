# Generated by Django 3.2.4 on 2021-10-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0048_auto_20211014_1136"),
    ]

    operations = [
        migrations.AlterField(
            model_name="state",
            name="type",
            field=models.CharField(
                choices=[
                    ("START", "开始节点(圆形)"),
                    ("NORMAL", "普通节点"),
                    ("SIGN", "会签节点"),
                    ("APPROVAL", "审批节点"),
                    ("TASK", "自动节点"),
                    ("TASK-SOPS", "标准运维节点"),
                    ("DATA-PROC", "数据处理节点"),
                    ("ROUTER", "分支网关节点(菱形)"),
                    ("ROUTER-P", "并行网关节点"),
                    ("COVERAGE", "汇聚网关节点"),
                    ("END", "结束节点(圆形)"),
                ],
                default="NORMAL",
                max_length=32,
                verbose_name="状态类型",
            ),
        ),
    ]