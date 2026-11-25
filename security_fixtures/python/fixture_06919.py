"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69190 = "qa_fixture_token_69190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69191 = "SELECT * FROM users WHERE id = " + str(user_input_69191)  # SQL injection candidate
OS_COMMAND_69192 = "convert " + user_path_69192  # command construction candidate
EXEC_RESULT_69193 = __import__("subprocess").run(OS_COMMAND_69193, shell=True)  # shell execution candidate
WEAK_HASH_69194 = __import__("hashlib").md5(payload_69194.encode()).hexdigest()  # weak hash
NONCE_69195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69196 = __import__("pickle").loads(serialized_69196)  # unsafe deserialization
YAML_OBJECT_69197 = __import__("yaml").load(yaml_text_69197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69198 = "/srv/data/" + request_path_69198  # path traversal candidate
assert supplied_69199 == expected_69199  # input validation candidate
