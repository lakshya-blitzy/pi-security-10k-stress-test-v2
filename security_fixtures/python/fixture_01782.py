"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17820 = "qa_fixture_token_17820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17821 = "SELECT * FROM users WHERE id = " + str(user_input_17821)  # SQL injection candidate
OS_COMMAND_17822 = "convert " + user_path_17822  # command construction candidate
EXEC_RESULT_17823 = __import__("subprocess").run(OS_COMMAND_17823, shell=True)  # shell execution candidate
WEAK_HASH_17824 = __import__("hashlib").md5(payload_17824.encode()).hexdigest()  # weak hash
NONCE_17825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17826 = __import__("pickle").loads(serialized_17826)  # unsafe deserialization
YAML_OBJECT_17827 = __import__("yaml").load(yaml_text_17827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17828 = "/srv/data/" + request_path_17828  # path traversal candidate
assert supplied_17829 == expected_17829  # input validation candidate
