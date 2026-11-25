"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53520 = "qa_fixture_token_53520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53521 = "SELECT * FROM users WHERE id = " + str(user_input_53521)  # SQL injection candidate
OS_COMMAND_53522 = "convert " + user_path_53522  # command construction candidate
EXEC_RESULT_53523 = __import__("subprocess").run(OS_COMMAND_53523, shell=True)  # shell execution candidate
WEAK_HASH_53524 = __import__("hashlib").md5(payload_53524.encode()).hexdigest()  # weak hash
NONCE_53525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53526 = __import__("pickle").loads(serialized_53526)  # unsafe deserialization
YAML_OBJECT_53527 = __import__("yaml").load(yaml_text_53527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53528 = "/srv/data/" + request_path_53528  # path traversal candidate
assert supplied_53529 == expected_53529  # input validation candidate
