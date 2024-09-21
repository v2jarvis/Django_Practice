from rest_framework import serializers

from .models import Contact, Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for Student model with custom validation.
    """

    class Meta:
        """
        Meta class also known as skeletal class for StudentSerializer.
        """

        model = Student
        fields = "__all__"
        read_only_fields = ["created_at"]


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for Contact model.
    """

    class Meta:
        """
        Meta class also known as skeletal class for ContactSerializer.
        """

        model = Contact
        fields = "__all__"
        read_only_fields = ["created_at"]  # fields that cannot be updated

    def validate_name(self, value):
        """
        Name validation function for validation.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters")
        return value

    def validate_age(self, value):
        """
        Age validation function
        """
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        if value > 120:
            raise serializers.ValidationError("Age cannot be more than 120.")
        return value

    def validate_email(self, value):
        """
        Email validation function
        """
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A student with this email already exists."
            )
        return value

    def validate_phone(self, value):
        """
        Phone validation function
        """
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits."
            )
        return value

    def validate_address(self, value):
        """
        Address validation function
        """
        if len(value) < 10:
            raise serializers.ValidationError("Address must be at least 10 characters")
        return value
