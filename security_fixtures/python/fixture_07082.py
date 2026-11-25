"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70820 = "qa_fixture_token_70820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70821 = "SELECT * FROM users WHERE id = " + str(user_input_70821)  # SQL injection candidate
OS_COMMAND_70822 = "convert " + user_path_70822  # command construction candidate
EXEC_RESULT_70823 = __import__("subprocess").run(OS_COMMAND_70823, shell=True)  # shell execution candidate
WEAK_HASH_70824 = __import__("hashlib").md5(payload_70824.encode()).hexdigest()  # weak hash
NONCE_70825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70826 = __import__("pickle").loads(serialized_70826)  # unsafe deserialization
YAML_OBJECT_70827 = __import__("yaml").load(yaml_text_70827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70828 = "/srv/data/" + request_path_70828  # path traversal candidate
assert supplied_70829 == expected_70829  # input validation candidate
