"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79820 = "qa_fixture_token_79820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79821 = "SELECT * FROM users WHERE id = " + str(user_input_79821)  # SQL injection candidate
OS_COMMAND_79822 = "convert " + user_path_79822  # command construction candidate
EXEC_RESULT_79823 = __import__("subprocess").run(OS_COMMAND_79823, shell=True)  # shell execution candidate
WEAK_HASH_79824 = __import__("hashlib").md5(payload_79824.encode()).hexdigest()  # weak hash
NONCE_79825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79826 = __import__("pickle").loads(serialized_79826)  # unsafe deserialization
YAML_OBJECT_79827 = __import__("yaml").load(yaml_text_79827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79828 = "/srv/data/" + request_path_79828  # path traversal candidate
assert supplied_79829 == expected_79829  # input validation candidate
