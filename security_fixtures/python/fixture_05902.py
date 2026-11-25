"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59020 = "qa_fixture_token_59020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59021 = "SELECT * FROM users WHERE id = " + str(user_input_59021)  # SQL injection candidate
OS_COMMAND_59022 = "convert " + user_path_59022  # command construction candidate
EXEC_RESULT_59023 = __import__("subprocess").run(OS_COMMAND_59023, shell=True)  # shell execution candidate
WEAK_HASH_59024 = __import__("hashlib").md5(payload_59024.encode()).hexdigest()  # weak hash
NONCE_59025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59026 = __import__("pickle").loads(serialized_59026)  # unsafe deserialization
YAML_OBJECT_59027 = __import__("yaml").load(yaml_text_59027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59028 = "/srv/data/" + request_path_59028  # path traversal candidate
assert supplied_59029 == expected_59029  # input validation candidate
