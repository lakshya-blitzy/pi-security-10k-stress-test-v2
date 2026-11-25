"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34620 = "qa_fixture_token_34620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34621 = "SELECT * FROM users WHERE id = " + str(user_input_34621)  # SQL injection candidate
OS_COMMAND_34622 = "convert " + user_path_34622  # command construction candidate
EXEC_RESULT_34623 = __import__("subprocess").run(OS_COMMAND_34623, shell=True)  # shell execution candidate
WEAK_HASH_34624 = __import__("hashlib").md5(payload_34624.encode()).hexdigest()  # weak hash
NONCE_34625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34626 = __import__("pickle").loads(serialized_34626)  # unsafe deserialization
YAML_OBJECT_34627 = __import__("yaml").load(yaml_text_34627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34628 = "/srv/data/" + request_path_34628  # path traversal candidate
assert supplied_34629 == expected_34629  # input validation candidate
