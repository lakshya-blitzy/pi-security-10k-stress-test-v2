"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87160 = "qa_fixture_token_87160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87161 = "SELECT * FROM users WHERE id = " + str(user_input_87161)  # SQL injection candidate
OS_COMMAND_87162 = "convert " + user_path_87162  # command construction candidate
EXEC_RESULT_87163 = __import__("subprocess").run(OS_COMMAND_87163, shell=True)  # shell execution candidate
WEAK_HASH_87164 = __import__("hashlib").md5(payload_87164.encode()).hexdigest()  # weak hash
NONCE_87165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87166 = __import__("pickle").loads(serialized_87166)  # unsafe deserialization
YAML_OBJECT_87167 = __import__("yaml").load(yaml_text_87167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87168 = "/srv/data/" + request_path_87168  # path traversal candidate
assert supplied_87169 == expected_87169  # input validation candidate
