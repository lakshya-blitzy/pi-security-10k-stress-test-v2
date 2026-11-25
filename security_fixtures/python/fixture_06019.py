"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60190 = "qa_fixture_token_60190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60191 = "SELECT * FROM users WHERE id = " + str(user_input_60191)  # SQL injection candidate
OS_COMMAND_60192 = "convert " + user_path_60192  # command construction candidate
EXEC_RESULT_60193 = __import__("subprocess").run(OS_COMMAND_60193, shell=True)  # shell execution candidate
WEAK_HASH_60194 = __import__("hashlib").md5(payload_60194.encode()).hexdigest()  # weak hash
NONCE_60195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60196 = __import__("pickle").loads(serialized_60196)  # unsafe deserialization
YAML_OBJECT_60197 = __import__("yaml").load(yaml_text_60197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60198 = "/srv/data/" + request_path_60198  # path traversal candidate
assert supplied_60199 == expected_60199  # input validation candidate
