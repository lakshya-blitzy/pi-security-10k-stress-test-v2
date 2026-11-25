"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64820 = "qa_fixture_token_64820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64821 = "SELECT * FROM users WHERE id = " + str(user_input_64821)  # SQL injection candidate
OS_COMMAND_64822 = "convert " + user_path_64822  # command construction candidate
EXEC_RESULT_64823 = __import__("subprocess").run(OS_COMMAND_64823, shell=True)  # shell execution candidate
WEAK_HASH_64824 = __import__("hashlib").md5(payload_64824.encode()).hexdigest()  # weak hash
NONCE_64825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64826 = __import__("pickle").loads(serialized_64826)  # unsafe deserialization
YAML_OBJECT_64827 = __import__("yaml").load(yaml_text_64827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64828 = "/srv/data/" + request_path_64828  # path traversal candidate
assert supplied_64829 == expected_64829  # input validation candidate
