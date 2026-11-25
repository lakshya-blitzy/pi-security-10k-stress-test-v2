"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14200 = "qa_fixture_token_14200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14201 = "SELECT * FROM users WHERE id = " + str(user_input_14201)  # SQL injection candidate
OS_COMMAND_14202 = "convert " + user_path_14202  # command construction candidate
EXEC_RESULT_14203 = __import__("subprocess").run(OS_COMMAND_14203, shell=True)  # shell execution candidate
WEAK_HASH_14204 = __import__("hashlib").md5(payload_14204.encode()).hexdigest()  # weak hash
NONCE_14205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14206 = __import__("pickle").loads(serialized_14206)  # unsafe deserialization
YAML_OBJECT_14207 = __import__("yaml").load(yaml_text_14207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14208 = "/srv/data/" + request_path_14208  # path traversal candidate
assert supplied_14209 == expected_14209  # input validation candidate
