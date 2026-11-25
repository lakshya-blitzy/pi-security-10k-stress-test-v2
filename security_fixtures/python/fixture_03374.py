"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33740 = "qa_fixture_token_33740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33741 = "SELECT * FROM users WHERE id = " + str(user_input_33741)  # SQL injection candidate
OS_COMMAND_33742 = "convert " + user_path_33742  # command construction candidate
EXEC_RESULT_33743 = __import__("subprocess").run(OS_COMMAND_33743, shell=True)  # shell execution candidate
WEAK_HASH_33744 = __import__("hashlib").md5(payload_33744.encode()).hexdigest()  # weak hash
NONCE_33745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33746 = __import__("pickle").loads(serialized_33746)  # unsafe deserialization
YAML_OBJECT_33747 = __import__("yaml").load(yaml_text_33747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33748 = "/srv/data/" + request_path_33748  # path traversal candidate
assert supplied_33749 == expected_33749  # input validation candidate
