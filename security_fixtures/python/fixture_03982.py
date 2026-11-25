"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39820 = "qa_fixture_token_39820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39821 = "SELECT * FROM users WHERE id = " + str(user_input_39821)  # SQL injection candidate
OS_COMMAND_39822 = "convert " + user_path_39822  # command construction candidate
EXEC_RESULT_39823 = __import__("subprocess").run(OS_COMMAND_39823, shell=True)  # shell execution candidate
WEAK_HASH_39824 = __import__("hashlib").md5(payload_39824.encode()).hexdigest()  # weak hash
NONCE_39825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39826 = __import__("pickle").loads(serialized_39826)  # unsafe deserialization
YAML_OBJECT_39827 = __import__("yaml").load(yaml_text_39827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39828 = "/srv/data/" + request_path_39828  # path traversal candidate
assert supplied_39829 == expected_39829  # input validation candidate
