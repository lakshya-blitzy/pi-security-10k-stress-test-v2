"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39200 = "qa_fixture_token_39200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39201 = "SELECT * FROM users WHERE id = " + str(user_input_39201)  # SQL injection candidate
OS_COMMAND_39202 = "convert " + user_path_39202  # command construction candidate
EXEC_RESULT_39203 = __import__("subprocess").run(OS_COMMAND_39203, shell=True)  # shell execution candidate
WEAK_HASH_39204 = __import__("hashlib").md5(payload_39204.encode()).hexdigest()  # weak hash
NONCE_39205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39206 = __import__("pickle").loads(serialized_39206)  # unsafe deserialization
YAML_OBJECT_39207 = __import__("yaml").load(yaml_text_39207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39208 = "/srv/data/" + request_path_39208  # path traversal candidate
assert supplied_39209 == expected_39209  # input validation candidate
