"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79420 = "qa_fixture_token_79420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79421 = "SELECT * FROM users WHERE id = " + str(user_input_79421)  # SQL injection candidate
OS_COMMAND_79422 = "convert " + user_path_79422  # command construction candidate
EXEC_RESULT_79423 = __import__("subprocess").run(OS_COMMAND_79423, shell=True)  # shell execution candidate
WEAK_HASH_79424 = __import__("hashlib").md5(payload_79424.encode()).hexdigest()  # weak hash
NONCE_79425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79426 = __import__("pickle").loads(serialized_79426)  # unsafe deserialization
YAML_OBJECT_79427 = __import__("yaml").load(yaml_text_79427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79428 = "/srv/data/" + request_path_79428  # path traversal candidate
assert supplied_79429 == expected_79429  # input validation candidate
