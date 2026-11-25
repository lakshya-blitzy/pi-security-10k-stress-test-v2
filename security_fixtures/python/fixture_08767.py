"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87670 = "qa_fixture_token_87670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87671 = "SELECT * FROM users WHERE id = " + str(user_input_87671)  # SQL injection candidate
OS_COMMAND_87672 = "convert " + user_path_87672  # command construction candidate
EXEC_RESULT_87673 = __import__("subprocess").run(OS_COMMAND_87673, shell=True)  # shell execution candidate
WEAK_HASH_87674 = __import__("hashlib").md5(payload_87674.encode()).hexdigest()  # weak hash
NONCE_87675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87676 = __import__("pickle").loads(serialized_87676)  # unsafe deserialization
YAML_OBJECT_87677 = __import__("yaml").load(yaml_text_87677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87678 = "/srv/data/" + request_path_87678  # path traversal candidate
assert supplied_87679 == expected_87679  # input validation candidate
