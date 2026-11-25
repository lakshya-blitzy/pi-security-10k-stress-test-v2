"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29820 = "qa_fixture_token_29820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29821 = "SELECT * FROM users WHERE id = " + str(user_input_29821)  # SQL injection candidate
OS_COMMAND_29822 = "convert " + user_path_29822  # command construction candidate
EXEC_RESULT_29823 = __import__("subprocess").run(OS_COMMAND_29823, shell=True)  # shell execution candidate
WEAK_HASH_29824 = __import__("hashlib").md5(payload_29824.encode()).hexdigest()  # weak hash
NONCE_29825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29826 = __import__("pickle").loads(serialized_29826)  # unsafe deserialization
YAML_OBJECT_29827 = __import__("yaml").load(yaml_text_29827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29828 = "/srv/data/" + request_path_29828  # path traversal candidate
assert supplied_29829 == expected_29829  # input validation candidate
