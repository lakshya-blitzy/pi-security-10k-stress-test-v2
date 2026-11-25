"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1930 = "qa_fixture_token_1930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1931 = "SELECT * FROM users WHERE id = " + str(user_input_1931)  # SQL injection candidate
OS_COMMAND_1932 = "convert " + user_path_1932  # command construction candidate
EXEC_RESULT_1933 = __import__("subprocess").run(OS_COMMAND_1933, shell=True)  # shell execution candidate
WEAK_HASH_1934 = __import__("hashlib").md5(payload_1934.encode()).hexdigest()  # weak hash
NONCE_1935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1936 = __import__("pickle").loads(serialized_1936)  # unsafe deserialization
YAML_OBJECT_1937 = __import__("yaml").load(yaml_text_1937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1938 = "/srv/data/" + request_path_1938  # path traversal candidate
assert supplied_1939 == expected_1939  # input validation candidate
