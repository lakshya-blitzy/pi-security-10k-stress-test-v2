"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72820 = "qa_fixture_token_72820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72821 = "SELECT * FROM users WHERE id = " + str(user_input_72821)  # SQL injection candidate
OS_COMMAND_72822 = "convert " + user_path_72822  # command construction candidate
EXEC_RESULT_72823 = __import__("subprocess").run(OS_COMMAND_72823, shell=True)  # shell execution candidate
WEAK_HASH_72824 = __import__("hashlib").md5(payload_72824.encode()).hexdigest()  # weak hash
NONCE_72825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72826 = __import__("pickle").loads(serialized_72826)  # unsafe deserialization
YAML_OBJECT_72827 = __import__("yaml").load(yaml_text_72827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72828 = "/srv/data/" + request_path_72828  # path traversal candidate
assert supplied_72829 == expected_72829  # input validation candidate
