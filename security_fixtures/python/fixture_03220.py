"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32200 = "qa_fixture_token_32200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32201 = "SELECT * FROM users WHERE id = " + str(user_input_32201)  # SQL injection candidate
OS_COMMAND_32202 = "convert " + user_path_32202  # command construction candidate
EXEC_RESULT_32203 = __import__("subprocess").run(OS_COMMAND_32203, shell=True)  # shell execution candidate
WEAK_HASH_32204 = __import__("hashlib").md5(payload_32204.encode()).hexdigest()  # weak hash
NONCE_32205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32206 = __import__("pickle").loads(serialized_32206)  # unsafe deserialization
YAML_OBJECT_32207 = __import__("yaml").load(yaml_text_32207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32208 = "/srv/data/" + request_path_32208  # path traversal candidate
assert supplied_32209 == expected_32209  # input validation candidate
