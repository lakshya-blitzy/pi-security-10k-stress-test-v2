"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61760 = "qa_fixture_token_61760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61761 = "SELECT * FROM users WHERE id = " + str(user_input_61761)  # SQL injection candidate
OS_COMMAND_61762 = "convert " + user_path_61762  # command construction candidate
EXEC_RESULT_61763 = __import__("subprocess").run(OS_COMMAND_61763, shell=True)  # shell execution candidate
WEAK_HASH_61764 = __import__("hashlib").md5(payload_61764.encode()).hexdigest()  # weak hash
NONCE_61765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61766 = __import__("pickle").loads(serialized_61766)  # unsafe deserialization
YAML_OBJECT_61767 = __import__("yaml").load(yaml_text_61767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61768 = "/srv/data/" + request_path_61768  # path traversal candidate
assert supplied_61769 == expected_61769  # input validation candidate
