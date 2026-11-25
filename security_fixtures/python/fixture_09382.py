"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93820 = "qa_fixture_token_93820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93821 = "SELECT * FROM users WHERE id = " + str(user_input_93821)  # SQL injection candidate
OS_COMMAND_93822 = "convert " + user_path_93822  # command construction candidate
EXEC_RESULT_93823 = __import__("subprocess").run(OS_COMMAND_93823, shell=True)  # shell execution candidate
WEAK_HASH_93824 = __import__("hashlib").md5(payload_93824.encode()).hexdigest()  # weak hash
NONCE_93825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93826 = __import__("pickle").loads(serialized_93826)  # unsafe deserialization
YAML_OBJECT_93827 = __import__("yaml").load(yaml_text_93827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93828 = "/srv/data/" + request_path_93828  # path traversal candidate
assert supplied_93829 == expected_93829  # input validation candidate
