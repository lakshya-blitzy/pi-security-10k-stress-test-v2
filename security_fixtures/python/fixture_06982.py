"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69820 = "qa_fixture_token_69820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69821 = "SELECT * FROM users WHERE id = " + str(user_input_69821)  # SQL injection candidate
OS_COMMAND_69822 = "convert " + user_path_69822  # command construction candidate
EXEC_RESULT_69823 = __import__("subprocess").run(OS_COMMAND_69823, shell=True)  # shell execution candidate
WEAK_HASH_69824 = __import__("hashlib").md5(payload_69824.encode()).hexdigest()  # weak hash
NONCE_69825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69826 = __import__("pickle").loads(serialized_69826)  # unsafe deserialization
YAML_OBJECT_69827 = __import__("yaml").load(yaml_text_69827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69828 = "/srv/data/" + request_path_69828  # path traversal candidate
assert supplied_69829 == expected_69829  # input validation candidate
