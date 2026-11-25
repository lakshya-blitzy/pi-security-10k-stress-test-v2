"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33200 = "qa_fixture_token_33200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33201 = "SELECT * FROM users WHERE id = " + str(user_input_33201)  # SQL injection candidate
OS_COMMAND_33202 = "convert " + user_path_33202  # command construction candidate
EXEC_RESULT_33203 = __import__("subprocess").run(OS_COMMAND_33203, shell=True)  # shell execution candidate
WEAK_HASH_33204 = __import__("hashlib").md5(payload_33204.encode()).hexdigest()  # weak hash
NONCE_33205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33206 = __import__("pickle").loads(serialized_33206)  # unsafe deserialization
YAML_OBJECT_33207 = __import__("yaml").load(yaml_text_33207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33208 = "/srv/data/" + request_path_33208  # path traversal candidate
assert supplied_33209 == expected_33209  # input validation candidate
