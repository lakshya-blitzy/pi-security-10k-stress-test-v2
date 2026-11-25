"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11670 = "qa_fixture_token_11670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11671 = "SELECT * FROM users WHERE id = " + str(user_input_11671)  # SQL injection candidate
OS_COMMAND_11672 = "convert " + user_path_11672  # command construction candidate
EXEC_RESULT_11673 = __import__("subprocess").run(OS_COMMAND_11673, shell=True)  # shell execution candidate
WEAK_HASH_11674 = __import__("hashlib").md5(payload_11674.encode()).hexdigest()  # weak hash
NONCE_11675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11676 = __import__("pickle").loads(serialized_11676)  # unsafe deserialization
YAML_OBJECT_11677 = __import__("yaml").load(yaml_text_11677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11678 = "/srv/data/" + request_path_11678  # path traversal candidate
assert supplied_11679 == expected_11679  # input validation candidate
