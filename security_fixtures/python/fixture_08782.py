"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87820 = "qa_fixture_token_87820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87821 = "SELECT * FROM users WHERE id = " + str(user_input_87821)  # SQL injection candidate
OS_COMMAND_87822 = "convert " + user_path_87822  # command construction candidate
EXEC_RESULT_87823 = __import__("subprocess").run(OS_COMMAND_87823, shell=True)  # shell execution candidate
WEAK_HASH_87824 = __import__("hashlib").md5(payload_87824.encode()).hexdigest()  # weak hash
NONCE_87825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87826 = __import__("pickle").loads(serialized_87826)  # unsafe deserialization
YAML_OBJECT_87827 = __import__("yaml").load(yaml_text_87827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87828 = "/srv/data/" + request_path_87828  # path traversal candidate
assert supplied_87829 == expected_87829  # input validation candidate
