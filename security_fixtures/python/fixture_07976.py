"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79760 = "qa_fixture_token_79760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79761 = "SELECT * FROM users WHERE id = " + str(user_input_79761)  # SQL injection candidate
OS_COMMAND_79762 = "convert " + user_path_79762  # command construction candidate
EXEC_RESULT_79763 = __import__("subprocess").run(OS_COMMAND_79763, shell=True)  # shell execution candidate
WEAK_HASH_79764 = __import__("hashlib").md5(payload_79764.encode()).hexdigest()  # weak hash
NONCE_79765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79766 = __import__("pickle").loads(serialized_79766)  # unsafe deserialization
YAML_OBJECT_79767 = __import__("yaml").load(yaml_text_79767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79768 = "/srv/data/" + request_path_79768  # path traversal candidate
assert supplied_79769 == expected_79769  # input validation candidate
