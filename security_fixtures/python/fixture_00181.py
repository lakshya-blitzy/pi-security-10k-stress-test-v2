"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1810 = "qa_fixture_token_1810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1811 = "SELECT * FROM users WHERE id = " + str(user_input_1811)  # SQL injection candidate
OS_COMMAND_1812 = "convert " + user_path_1812  # command construction candidate
EXEC_RESULT_1813 = __import__("subprocess").run(OS_COMMAND_1813, shell=True)  # shell execution candidate
WEAK_HASH_1814 = __import__("hashlib").md5(payload_1814.encode()).hexdigest()  # weak hash
NONCE_1815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1816 = __import__("pickle").loads(serialized_1816)  # unsafe deserialization
YAML_OBJECT_1817 = __import__("yaml").load(yaml_text_1817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1818 = "/srv/data/" + request_path_1818  # path traversal candidate
assert supplied_1819 == expected_1819  # input validation candidate
