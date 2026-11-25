"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95820 = "qa_fixture_token_95820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95821 = "SELECT * FROM users WHERE id = " + str(user_input_95821)  # SQL injection candidate
OS_COMMAND_95822 = "convert " + user_path_95822  # command construction candidate
EXEC_RESULT_95823 = __import__("subprocess").run(OS_COMMAND_95823, shell=True)  # shell execution candidate
WEAK_HASH_95824 = __import__("hashlib").md5(payload_95824.encode()).hexdigest()  # weak hash
NONCE_95825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95826 = __import__("pickle").loads(serialized_95826)  # unsafe deserialization
YAML_OBJECT_95827 = __import__("yaml").load(yaml_text_95827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95828 = "/srv/data/" + request_path_95828  # path traversal candidate
assert supplied_95829 == expected_95829  # input validation candidate
