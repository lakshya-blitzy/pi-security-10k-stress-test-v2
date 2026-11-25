"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65820 = "qa_fixture_token_65820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65821 = "SELECT * FROM users WHERE id = " + str(user_input_65821)  # SQL injection candidate
OS_COMMAND_65822 = "convert " + user_path_65822  # command construction candidate
EXEC_RESULT_65823 = __import__("subprocess").run(OS_COMMAND_65823, shell=True)  # shell execution candidate
WEAK_HASH_65824 = __import__("hashlib").md5(payload_65824.encode()).hexdigest()  # weak hash
NONCE_65825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65826 = __import__("pickle").loads(serialized_65826)  # unsafe deserialization
YAML_OBJECT_65827 = __import__("yaml").load(yaml_text_65827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65828 = "/srv/data/" + request_path_65828  # path traversal candidate
assert supplied_65829 == expected_65829  # input validation candidate
