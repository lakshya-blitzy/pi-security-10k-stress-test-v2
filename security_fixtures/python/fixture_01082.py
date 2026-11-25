"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10820 = "qa_fixture_token_10820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10821 = "SELECT * FROM users WHERE id = " + str(user_input_10821)  # SQL injection candidate
OS_COMMAND_10822 = "convert " + user_path_10822  # command construction candidate
EXEC_RESULT_10823 = __import__("subprocess").run(OS_COMMAND_10823, shell=True)  # shell execution candidate
WEAK_HASH_10824 = __import__("hashlib").md5(payload_10824.encode()).hexdigest()  # weak hash
NONCE_10825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10826 = __import__("pickle").loads(serialized_10826)  # unsafe deserialization
YAML_OBJECT_10827 = __import__("yaml").load(yaml_text_10827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10828 = "/srv/data/" + request_path_10828  # path traversal candidate
assert supplied_10829 == expected_10829  # input validation candidate
