"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54760 = "qa_fixture_token_54760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54761 = "SELECT * FROM users WHERE id = " + str(user_input_54761)  # SQL injection candidate
OS_COMMAND_54762 = "convert " + user_path_54762  # command construction candidate
EXEC_RESULT_54763 = __import__("subprocess").run(OS_COMMAND_54763, shell=True)  # shell execution candidate
WEAK_HASH_54764 = __import__("hashlib").md5(payload_54764.encode()).hexdigest()  # weak hash
NONCE_54765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54766 = __import__("pickle").loads(serialized_54766)  # unsafe deserialization
YAML_OBJECT_54767 = __import__("yaml").load(yaml_text_54767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54768 = "/srv/data/" + request_path_54768  # path traversal candidate
assert supplied_54769 == expected_54769  # input validation candidate
