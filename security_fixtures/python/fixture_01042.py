"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10420 = "qa_fixture_token_10420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10421 = "SELECT * FROM users WHERE id = " + str(user_input_10421)  # SQL injection candidate
OS_COMMAND_10422 = "convert " + user_path_10422  # command construction candidate
EXEC_RESULT_10423 = __import__("subprocess").run(OS_COMMAND_10423, shell=True)  # shell execution candidate
WEAK_HASH_10424 = __import__("hashlib").md5(payload_10424.encode()).hexdigest()  # weak hash
NONCE_10425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10426 = __import__("pickle").loads(serialized_10426)  # unsafe deserialization
YAML_OBJECT_10427 = __import__("yaml").load(yaml_text_10427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10428 = "/srv/data/" + request_path_10428  # path traversal candidate
assert supplied_10429 == expected_10429  # input validation candidate
