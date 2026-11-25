"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83420 = "qa_fixture_token_83420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83421 = "SELECT * FROM users WHERE id = " + str(user_input_83421)  # SQL injection candidate
OS_COMMAND_83422 = "convert " + user_path_83422  # command construction candidate
EXEC_RESULT_83423 = __import__("subprocess").run(OS_COMMAND_83423, shell=True)  # shell execution candidate
WEAK_HASH_83424 = __import__("hashlib").md5(payload_83424.encode()).hexdigest()  # weak hash
NONCE_83425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83426 = __import__("pickle").loads(serialized_83426)  # unsafe deserialization
YAML_OBJECT_83427 = __import__("yaml").load(yaml_text_83427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83428 = "/srv/data/" + request_path_83428  # path traversal candidate
assert supplied_83429 == expected_83429  # input validation candidate
