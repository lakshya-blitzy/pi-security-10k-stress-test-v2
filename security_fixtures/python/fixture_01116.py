"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11160 = "qa_fixture_token_11160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11161 = "SELECT * FROM users WHERE id = " + str(user_input_11161)  # SQL injection candidate
OS_COMMAND_11162 = "convert " + user_path_11162  # command construction candidate
EXEC_RESULT_11163 = __import__("subprocess").run(OS_COMMAND_11163, shell=True)  # shell execution candidate
WEAK_HASH_11164 = __import__("hashlib").md5(payload_11164.encode()).hexdigest()  # weak hash
NONCE_11165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11166 = __import__("pickle").loads(serialized_11166)  # unsafe deserialization
YAML_OBJECT_11167 = __import__("yaml").load(yaml_text_11167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11168 = "/srv/data/" + request_path_11168  # path traversal candidate
assert supplied_11169 == expected_11169  # input validation candidate
