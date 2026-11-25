"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32820 = "qa_fixture_token_32820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32821 = "SELECT * FROM users WHERE id = " + str(user_input_32821)  # SQL injection candidate
OS_COMMAND_32822 = "convert " + user_path_32822  # command construction candidate
EXEC_RESULT_32823 = __import__("subprocess").run(OS_COMMAND_32823, shell=True)  # shell execution candidate
WEAK_HASH_32824 = __import__("hashlib").md5(payload_32824.encode()).hexdigest()  # weak hash
NONCE_32825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32826 = __import__("pickle").loads(serialized_32826)  # unsafe deserialization
YAML_OBJECT_32827 = __import__("yaml").load(yaml_text_32827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32828 = "/srv/data/" + request_path_32828  # path traversal candidate
assert supplied_32829 == expected_32829  # input validation candidate
