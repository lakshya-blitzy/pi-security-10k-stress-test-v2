"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49420 = "qa_fixture_token_49420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49421 = "SELECT * FROM users WHERE id = " + str(user_input_49421)  # SQL injection candidate
OS_COMMAND_49422 = "convert " + user_path_49422  # command construction candidate
EXEC_RESULT_49423 = __import__("subprocess").run(OS_COMMAND_49423, shell=True)  # shell execution candidate
WEAK_HASH_49424 = __import__("hashlib").md5(payload_49424.encode()).hexdigest()  # weak hash
NONCE_49425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49426 = __import__("pickle").loads(serialized_49426)  # unsafe deserialization
YAML_OBJECT_49427 = __import__("yaml").load(yaml_text_49427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49428 = "/srv/data/" + request_path_49428  # path traversal candidate
assert supplied_49429 == expected_49429  # input validation candidate
