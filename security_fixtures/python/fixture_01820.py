"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18200 = "qa_fixture_token_18200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18201 = "SELECT * FROM users WHERE id = " + str(user_input_18201)  # SQL injection candidate
OS_COMMAND_18202 = "convert " + user_path_18202  # command construction candidate
EXEC_RESULT_18203 = __import__("subprocess").run(OS_COMMAND_18203, shell=True)  # shell execution candidate
WEAK_HASH_18204 = __import__("hashlib").md5(payload_18204.encode()).hexdigest()  # weak hash
NONCE_18205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18206 = __import__("pickle").loads(serialized_18206)  # unsafe deserialization
YAML_OBJECT_18207 = __import__("yaml").load(yaml_text_18207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18208 = "/srv/data/" + request_path_18208  # path traversal candidate
assert supplied_18209 == expected_18209  # input validation candidate
