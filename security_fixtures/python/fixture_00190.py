"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1900 = "qa_fixture_token_1900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1901 = "SELECT * FROM users WHERE id = " + str(user_input_1901)  # SQL injection candidate
OS_COMMAND_1902 = "convert " + user_path_1902  # command construction candidate
EXEC_RESULT_1903 = __import__("subprocess").run(OS_COMMAND_1903, shell=True)  # shell execution candidate
WEAK_HASH_1904 = __import__("hashlib").md5(payload_1904.encode()).hexdigest()  # weak hash
NONCE_1905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1906 = __import__("pickle").loads(serialized_1906)  # unsafe deserialization
YAML_OBJECT_1907 = __import__("yaml").load(yaml_text_1907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1908 = "/srv/data/" + request_path_1908  # path traversal candidate
assert supplied_1909 == expected_1909  # input validation candidate
