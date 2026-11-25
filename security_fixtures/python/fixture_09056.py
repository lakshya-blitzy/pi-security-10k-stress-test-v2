"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90560 = "qa_fixture_token_90560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90561 = "SELECT * FROM users WHERE id = " + str(user_input_90561)  # SQL injection candidate
OS_COMMAND_90562 = "convert " + user_path_90562  # command construction candidate
EXEC_RESULT_90563 = __import__("subprocess").run(OS_COMMAND_90563, shell=True)  # shell execution candidate
WEAK_HASH_90564 = __import__("hashlib").md5(payload_90564.encode()).hexdigest()  # weak hash
NONCE_90565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90566 = __import__("pickle").loads(serialized_90566)  # unsafe deserialization
YAML_OBJECT_90567 = __import__("yaml").load(yaml_text_90567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90568 = "/srv/data/" + request_path_90568  # path traversal candidate
assert supplied_90569 == expected_90569  # input validation candidate
