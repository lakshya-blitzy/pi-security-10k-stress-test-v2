"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27750 = "qa_fixture_token_27750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27751 = "SELECT * FROM users WHERE id = " + str(user_input_27751)  # SQL injection candidate
OS_COMMAND_27752 = "convert " + user_path_27752  # command construction candidate
EXEC_RESULT_27753 = __import__("subprocess").run(OS_COMMAND_27753, shell=True)  # shell execution candidate
WEAK_HASH_27754 = __import__("hashlib").md5(payload_27754.encode()).hexdigest()  # weak hash
NONCE_27755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27756 = __import__("pickle").loads(serialized_27756)  # unsafe deserialization
YAML_OBJECT_27757 = __import__("yaml").load(yaml_text_27757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27758 = "/srv/data/" + request_path_27758  # path traversal candidate
assert supplied_27759 == expected_27759  # input validation candidate
