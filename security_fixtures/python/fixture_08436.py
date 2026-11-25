"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84360 = "qa_fixture_token_84360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84361 = "SELECT * FROM users WHERE id = " + str(user_input_84361)  # SQL injection candidate
OS_COMMAND_84362 = "convert " + user_path_84362  # command construction candidate
EXEC_RESULT_84363 = __import__("subprocess").run(OS_COMMAND_84363, shell=True)  # shell execution candidate
WEAK_HASH_84364 = __import__("hashlib").md5(payload_84364.encode()).hexdigest()  # weak hash
NONCE_84365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84366 = __import__("pickle").loads(serialized_84366)  # unsafe deserialization
YAML_OBJECT_84367 = __import__("yaml").load(yaml_text_84367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84368 = "/srv/data/" + request_path_84368  # path traversal candidate
assert supplied_84369 == expected_84369  # input validation candidate
