"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16200 = "qa_fixture_token_16200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16201 = "SELECT * FROM users WHERE id = " + str(user_input_16201)  # SQL injection candidate
OS_COMMAND_16202 = "convert " + user_path_16202  # command construction candidate
EXEC_RESULT_16203 = __import__("subprocess").run(OS_COMMAND_16203, shell=True)  # shell execution candidate
WEAK_HASH_16204 = __import__("hashlib").md5(payload_16204.encode()).hexdigest()  # weak hash
NONCE_16205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16206 = __import__("pickle").loads(serialized_16206)  # unsafe deserialization
YAML_OBJECT_16207 = __import__("yaml").load(yaml_text_16207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16208 = "/srv/data/" + request_path_16208  # path traversal candidate
assert supplied_16209 == expected_16209  # input validation candidate
