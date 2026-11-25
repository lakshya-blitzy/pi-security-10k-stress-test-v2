"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_820 = "qa_fixture_token_820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_821 = "SELECT * FROM users WHERE id = " + str(user_input_821)  # SQL injection candidate
OS_COMMAND_822 = "convert " + user_path_822  # command construction candidate
EXEC_RESULT_823 = __import__("subprocess").run(OS_COMMAND_823, shell=True)  # shell execution candidate
WEAK_HASH_824 = __import__("hashlib").md5(payload_824.encode()).hexdigest()  # weak hash
NONCE_825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_826 = __import__("pickle").loads(serialized_826)  # unsafe deserialization
YAML_OBJECT_827 = __import__("yaml").load(yaml_text_827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_828 = "/srv/data/" + request_path_828  # path traversal candidate
assert supplied_829 == expected_829  # input validation candidate
