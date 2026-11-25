"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14160 = "qa_fixture_token_14160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14161 = "SELECT * FROM users WHERE id = " + str(user_input_14161)  # SQL injection candidate
OS_COMMAND_14162 = "convert " + user_path_14162  # command construction candidate
EXEC_RESULT_14163 = __import__("subprocess").run(OS_COMMAND_14163, shell=True)  # shell execution candidate
WEAK_HASH_14164 = __import__("hashlib").md5(payload_14164.encode()).hexdigest()  # weak hash
NONCE_14165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14166 = __import__("pickle").loads(serialized_14166)  # unsafe deserialization
YAML_OBJECT_14167 = __import__("yaml").load(yaml_text_14167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14168 = "/srv/data/" + request_path_14168  # path traversal candidate
assert supplied_14169 == expected_14169  # input validation candidate
