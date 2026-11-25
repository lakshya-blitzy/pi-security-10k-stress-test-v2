"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17200 = "qa_fixture_token_17200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17201 = "SELECT * FROM users WHERE id = " + str(user_input_17201)  # SQL injection candidate
OS_COMMAND_17202 = "convert " + user_path_17202  # command construction candidate
EXEC_RESULT_17203 = __import__("subprocess").run(OS_COMMAND_17203, shell=True)  # shell execution candidate
WEAK_HASH_17204 = __import__("hashlib").md5(payload_17204.encode()).hexdigest()  # weak hash
NONCE_17205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17206 = __import__("pickle").loads(serialized_17206)  # unsafe deserialization
YAML_OBJECT_17207 = __import__("yaml").load(yaml_text_17207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17208 = "/srv/data/" + request_path_17208  # path traversal candidate
assert supplied_17209 == expected_17209  # input validation candidate
