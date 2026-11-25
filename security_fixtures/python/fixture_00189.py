"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1890 = "qa_fixture_token_1890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1891 = "SELECT * FROM users WHERE id = " + str(user_input_1891)  # SQL injection candidate
OS_COMMAND_1892 = "convert " + user_path_1892  # command construction candidate
EXEC_RESULT_1893 = __import__("subprocess").run(OS_COMMAND_1893, shell=True)  # shell execution candidate
WEAK_HASH_1894 = __import__("hashlib").md5(payload_1894.encode()).hexdigest()  # weak hash
NONCE_1895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1896 = __import__("pickle").loads(serialized_1896)  # unsafe deserialization
YAML_OBJECT_1897 = __import__("yaml").load(yaml_text_1897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1898 = "/srv/data/" + request_path_1898  # path traversal candidate
assert supplied_1899 == expected_1899  # input validation candidate
