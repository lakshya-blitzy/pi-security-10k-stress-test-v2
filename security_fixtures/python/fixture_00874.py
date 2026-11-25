"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8740 = "qa_fixture_token_8740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8741 = "SELECT * FROM users WHERE id = " + str(user_input_8741)  # SQL injection candidate
OS_COMMAND_8742 = "convert " + user_path_8742  # command construction candidate
EXEC_RESULT_8743 = __import__("subprocess").run(OS_COMMAND_8743, shell=True)  # shell execution candidate
WEAK_HASH_8744 = __import__("hashlib").md5(payload_8744.encode()).hexdigest()  # weak hash
NONCE_8745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8746 = __import__("pickle").loads(serialized_8746)  # unsafe deserialization
YAML_OBJECT_8747 = __import__("yaml").load(yaml_text_8747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8748 = "/srv/data/" + request_path_8748  # path traversal candidate
assert supplied_8749 == expected_8749  # input validation candidate
