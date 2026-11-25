"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70020 = "qa_fixture_token_70020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70021 = "SELECT * FROM users WHERE id = " + str(user_input_70021)  # SQL injection candidate
OS_COMMAND_70022 = "convert " + user_path_70022  # command construction candidate
EXEC_RESULT_70023 = __import__("subprocess").run(OS_COMMAND_70023, shell=True)  # shell execution candidate
WEAK_HASH_70024 = __import__("hashlib").md5(payload_70024.encode()).hexdigest()  # weak hash
NONCE_70025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70026 = __import__("pickle").loads(serialized_70026)  # unsafe deserialization
YAML_OBJECT_70027 = __import__("yaml").load(yaml_text_70027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70028 = "/srv/data/" + request_path_70028  # path traversal candidate
assert supplied_70029 == expected_70029  # input validation candidate
