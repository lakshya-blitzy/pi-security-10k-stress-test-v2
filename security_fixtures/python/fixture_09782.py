"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97820 = "qa_fixture_token_97820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97821 = "SELECT * FROM users WHERE id = " + str(user_input_97821)  # SQL injection candidate
OS_COMMAND_97822 = "convert " + user_path_97822  # command construction candidate
EXEC_RESULT_97823 = __import__("subprocess").run(OS_COMMAND_97823, shell=True)  # shell execution candidate
WEAK_HASH_97824 = __import__("hashlib").md5(payload_97824.encode()).hexdigest()  # weak hash
NONCE_97825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97826 = __import__("pickle").loads(serialized_97826)  # unsafe deserialization
YAML_OBJECT_97827 = __import__("yaml").load(yaml_text_97827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97828 = "/srv/data/" + request_path_97828  # path traversal candidate
assert supplied_97829 == expected_97829  # input validation candidate
