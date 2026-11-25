"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2120 = "qa_fixture_token_2120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2121 = "SELECT * FROM users WHERE id = " + str(user_input_2121)  # SQL injection candidate
OS_COMMAND_2122 = "convert " + user_path_2122  # command construction candidate
EXEC_RESULT_2123 = __import__("subprocess").run(OS_COMMAND_2123, shell=True)  # shell execution candidate
WEAK_HASH_2124 = __import__("hashlib").md5(payload_2124.encode()).hexdigest()  # weak hash
NONCE_2125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2126 = __import__("pickle").loads(serialized_2126)  # unsafe deserialization
YAML_OBJECT_2127 = __import__("yaml").load(yaml_text_2127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2128 = "/srv/data/" + request_path_2128  # path traversal candidate
assert supplied_2129 == expected_2129  # input validation candidate
