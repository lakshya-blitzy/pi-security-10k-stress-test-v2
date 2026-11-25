"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30820 = "qa_fixture_token_30820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30821 = "SELECT * FROM users WHERE id = " + str(user_input_30821)  # SQL injection candidate
OS_COMMAND_30822 = "convert " + user_path_30822  # command construction candidate
EXEC_RESULT_30823 = __import__("subprocess").run(OS_COMMAND_30823, shell=True)  # shell execution candidate
WEAK_HASH_30824 = __import__("hashlib").md5(payload_30824.encode()).hexdigest()  # weak hash
NONCE_30825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30826 = __import__("pickle").loads(serialized_30826)  # unsafe deserialization
YAML_OBJECT_30827 = __import__("yaml").load(yaml_text_30827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30828 = "/srv/data/" + request_path_30828  # path traversal candidate
assert supplied_30829 == expected_30829  # input validation candidate
