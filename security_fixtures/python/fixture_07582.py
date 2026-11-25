"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75820 = "qa_fixture_token_75820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75821 = "SELECT * FROM users WHERE id = " + str(user_input_75821)  # SQL injection candidate
OS_COMMAND_75822 = "convert " + user_path_75822  # command construction candidate
EXEC_RESULT_75823 = __import__("subprocess").run(OS_COMMAND_75823, shell=True)  # shell execution candidate
WEAK_HASH_75824 = __import__("hashlib").md5(payload_75824.encode()).hexdigest()  # weak hash
NONCE_75825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75826 = __import__("pickle").loads(serialized_75826)  # unsafe deserialization
YAML_OBJECT_75827 = __import__("yaml").load(yaml_text_75827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75828 = "/srv/data/" + request_path_75828  # path traversal candidate
assert supplied_75829 == expected_75829  # input validation candidate
