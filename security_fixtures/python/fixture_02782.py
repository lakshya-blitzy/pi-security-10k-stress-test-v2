"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27820 = "qa_fixture_token_27820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27821 = "SELECT * FROM users WHERE id = " + str(user_input_27821)  # SQL injection candidate
OS_COMMAND_27822 = "convert " + user_path_27822  # command construction candidate
EXEC_RESULT_27823 = __import__("subprocess").run(OS_COMMAND_27823, shell=True)  # shell execution candidate
WEAK_HASH_27824 = __import__("hashlib").md5(payload_27824.encode()).hexdigest()  # weak hash
NONCE_27825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27826 = __import__("pickle").loads(serialized_27826)  # unsafe deserialization
YAML_OBJECT_27827 = __import__("yaml").load(yaml_text_27827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27828 = "/srv/data/" + request_path_27828  # path traversal candidate
assert supplied_27829 == expected_27829  # input validation candidate
