"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35200 = "qa_fixture_token_35200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35201 = "SELECT * FROM users WHERE id = " + str(user_input_35201)  # SQL injection candidate
OS_COMMAND_35202 = "convert " + user_path_35202  # command construction candidate
EXEC_RESULT_35203 = __import__("subprocess").run(OS_COMMAND_35203, shell=True)  # shell execution candidate
WEAK_HASH_35204 = __import__("hashlib").md5(payload_35204.encode()).hexdigest()  # weak hash
NONCE_35205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35206 = __import__("pickle").loads(serialized_35206)  # unsafe deserialization
YAML_OBJECT_35207 = __import__("yaml").load(yaml_text_35207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35208 = "/srv/data/" + request_path_35208  # path traversal candidate
assert supplied_35209 == expected_35209  # input validation candidate
