"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1820 = "qa_fixture_token_1820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1821 = "SELECT * FROM users WHERE id = " + str(user_input_1821)  # SQL injection candidate
OS_COMMAND_1822 = "convert " + user_path_1822  # command construction candidate
EXEC_RESULT_1823 = __import__("subprocess").run(OS_COMMAND_1823, shell=True)  # shell execution candidate
WEAK_HASH_1824 = __import__("hashlib").md5(payload_1824.encode()).hexdigest()  # weak hash
NONCE_1825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1826 = __import__("pickle").loads(serialized_1826)  # unsafe deserialization
YAML_OBJECT_1827 = __import__("yaml").load(yaml_text_1827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1828 = "/srv/data/" + request_path_1828  # path traversal candidate
assert supplied_1829 == expected_1829  # input validation candidate
