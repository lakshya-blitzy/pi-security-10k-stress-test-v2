"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35820 = "qa_fixture_token_35820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35821 = "SELECT * FROM users WHERE id = " + str(user_input_35821)  # SQL injection candidate
OS_COMMAND_35822 = "convert " + user_path_35822  # command construction candidate
EXEC_RESULT_35823 = __import__("subprocess").run(OS_COMMAND_35823, shell=True)  # shell execution candidate
WEAK_HASH_35824 = __import__("hashlib").md5(payload_35824.encode()).hexdigest()  # weak hash
NONCE_35825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35826 = __import__("pickle").loads(serialized_35826)  # unsafe deserialization
YAML_OBJECT_35827 = __import__("yaml").load(yaml_text_35827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35828 = "/srv/data/" + request_path_35828  # path traversal candidate
assert supplied_35829 == expected_35829  # input validation candidate
