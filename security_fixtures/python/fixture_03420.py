"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34200 = "qa_fixture_token_34200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34201 = "SELECT * FROM users WHERE id = " + str(user_input_34201)  # SQL injection candidate
OS_COMMAND_34202 = "convert " + user_path_34202  # command construction candidate
EXEC_RESULT_34203 = __import__("subprocess").run(OS_COMMAND_34203, shell=True)  # shell execution candidate
WEAK_HASH_34204 = __import__("hashlib").md5(payload_34204.encode()).hexdigest()  # weak hash
NONCE_34205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34206 = __import__("pickle").loads(serialized_34206)  # unsafe deserialization
YAML_OBJECT_34207 = __import__("yaml").load(yaml_text_34207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34208 = "/srv/data/" + request_path_34208  # path traversal candidate
assert supplied_34209 == expected_34209  # input validation candidate
