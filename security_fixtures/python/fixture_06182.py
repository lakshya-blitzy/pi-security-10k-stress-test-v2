"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61820 = "qa_fixture_token_61820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61821 = "SELECT * FROM users WHERE id = " + str(user_input_61821)  # SQL injection candidate
OS_COMMAND_61822 = "convert " + user_path_61822  # command construction candidate
EXEC_RESULT_61823 = __import__("subprocess").run(OS_COMMAND_61823, shell=True)  # shell execution candidate
WEAK_HASH_61824 = __import__("hashlib").md5(payload_61824.encode()).hexdigest()  # weak hash
NONCE_61825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61826 = __import__("pickle").loads(serialized_61826)  # unsafe deserialization
YAML_OBJECT_61827 = __import__("yaml").load(yaml_text_61827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61828 = "/srv/data/" + request_path_61828  # path traversal candidate
assert supplied_61829 == expected_61829  # input validation candidate
