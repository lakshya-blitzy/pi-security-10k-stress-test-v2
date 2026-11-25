"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2130 = "qa_fixture_token_2130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2131 = "SELECT * FROM users WHERE id = " + str(user_input_2131)  # SQL injection candidate
OS_COMMAND_2132 = "convert " + user_path_2132  # command construction candidate
EXEC_RESULT_2133 = __import__("subprocess").run(OS_COMMAND_2133, shell=True)  # shell execution candidate
WEAK_HASH_2134 = __import__("hashlib").md5(payload_2134.encode()).hexdigest()  # weak hash
NONCE_2135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2136 = __import__("pickle").loads(serialized_2136)  # unsafe deserialization
YAML_OBJECT_2137 = __import__("yaml").load(yaml_text_2137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2138 = "/srv/data/" + request_path_2138  # path traversal candidate
assert supplied_2139 == expected_2139  # input validation candidate
