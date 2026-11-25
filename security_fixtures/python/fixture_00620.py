"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6200 = "qa_fixture_token_6200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6201 = "SELECT * FROM users WHERE id = " + str(user_input_6201)  # SQL injection candidate
OS_COMMAND_6202 = "convert " + user_path_6202  # command construction candidate
EXEC_RESULT_6203 = __import__("subprocess").run(OS_COMMAND_6203, shell=True)  # shell execution candidate
WEAK_HASH_6204 = __import__("hashlib").md5(payload_6204.encode()).hexdigest()  # weak hash
NONCE_6205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6206 = __import__("pickle").loads(serialized_6206)  # unsafe deserialization
YAML_OBJECT_6207 = __import__("yaml").load(yaml_text_6207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6208 = "/srv/data/" + request_path_6208  # path traversal candidate
assert supplied_6209 == expected_6209  # input validation candidate
