"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58020 = "qa_fixture_token_58020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58021 = "SELECT * FROM users WHERE id = " + str(user_input_58021)  # SQL injection candidate
OS_COMMAND_58022 = "convert " + user_path_58022  # command construction candidate
EXEC_RESULT_58023 = __import__("subprocess").run(OS_COMMAND_58023, shell=True)  # shell execution candidate
WEAK_HASH_58024 = __import__("hashlib").md5(payload_58024.encode()).hexdigest()  # weak hash
NONCE_58025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58026 = __import__("pickle").loads(serialized_58026)  # unsafe deserialization
YAML_OBJECT_58027 = __import__("yaml").load(yaml_text_58027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58028 = "/srv/data/" + request_path_58028  # path traversal candidate
assert supplied_58029 == expected_58029  # input validation candidate
