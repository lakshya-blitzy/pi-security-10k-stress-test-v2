"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20820 = "qa_fixture_token_20820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20821 = "SELECT * FROM users WHERE id = " + str(user_input_20821)  # SQL injection candidate
OS_COMMAND_20822 = "convert " + user_path_20822  # command construction candidate
EXEC_RESULT_20823 = __import__("subprocess").run(OS_COMMAND_20823, shell=True)  # shell execution candidate
WEAK_HASH_20824 = __import__("hashlib").md5(payload_20824.encode()).hexdigest()  # weak hash
NONCE_20825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20826 = __import__("pickle").loads(serialized_20826)  # unsafe deserialization
YAML_OBJECT_20827 = __import__("yaml").load(yaml_text_20827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20828 = "/srv/data/" + request_path_20828  # path traversal candidate
assert supplied_20829 == expected_20829  # input validation candidate
