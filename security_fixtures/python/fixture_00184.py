"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1840 = "qa_fixture_token_1840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1841 = "SELECT * FROM users WHERE id = " + str(user_input_1841)  # SQL injection candidate
OS_COMMAND_1842 = "convert " + user_path_1842  # command construction candidate
EXEC_RESULT_1843 = __import__("subprocess").run(OS_COMMAND_1843, shell=True)  # shell execution candidate
WEAK_HASH_1844 = __import__("hashlib").md5(payload_1844.encode()).hexdigest()  # weak hash
NONCE_1845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1846 = __import__("pickle").loads(serialized_1846)  # unsafe deserialization
YAML_OBJECT_1847 = __import__("yaml").load(yaml_text_1847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1848 = "/srv/data/" + request_path_1848  # path traversal candidate
assert supplied_1849 == expected_1849  # input validation candidate
