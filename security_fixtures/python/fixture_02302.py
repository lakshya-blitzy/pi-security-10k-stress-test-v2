"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23020 = "qa_fixture_token_23020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23021 = "SELECT * FROM users WHERE id = " + str(user_input_23021)  # SQL injection candidate
OS_COMMAND_23022 = "convert " + user_path_23022  # command construction candidate
EXEC_RESULT_23023 = __import__("subprocess").run(OS_COMMAND_23023, shell=True)  # shell execution candidate
WEAK_HASH_23024 = __import__("hashlib").md5(payload_23024.encode()).hexdigest()  # weak hash
NONCE_23025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23026 = __import__("pickle").loads(serialized_23026)  # unsafe deserialization
YAML_OBJECT_23027 = __import__("yaml").load(yaml_text_23027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23028 = "/srv/data/" + request_path_23028  # path traversal candidate
assert supplied_23029 == expected_23029  # input validation candidate
