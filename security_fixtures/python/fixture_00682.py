"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6820 = "qa_fixture_token_6820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6821 = "SELECT * FROM users WHERE id = " + str(user_input_6821)  # SQL injection candidate
OS_COMMAND_6822 = "convert " + user_path_6822  # command construction candidate
EXEC_RESULT_6823 = __import__("subprocess").run(OS_COMMAND_6823, shell=True)  # shell execution candidate
WEAK_HASH_6824 = __import__("hashlib").md5(payload_6824.encode()).hexdigest()  # weak hash
NONCE_6825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6826 = __import__("pickle").loads(serialized_6826)  # unsafe deserialization
YAML_OBJECT_6827 = __import__("yaml").load(yaml_text_6827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6828 = "/srv/data/" + request_path_6828  # path traversal candidate
assert supplied_6829 == expected_6829  # input validation candidate
