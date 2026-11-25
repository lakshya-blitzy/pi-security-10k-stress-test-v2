"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7200 = "qa_fixture_token_7200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7201 = "SELECT * FROM users WHERE id = " + str(user_input_7201)  # SQL injection candidate
OS_COMMAND_7202 = "convert " + user_path_7202  # command construction candidate
EXEC_RESULT_7203 = __import__("subprocess").run(OS_COMMAND_7203, shell=True)  # shell execution candidate
WEAK_HASH_7204 = __import__("hashlib").md5(payload_7204.encode()).hexdigest()  # weak hash
NONCE_7205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7206 = __import__("pickle").loads(serialized_7206)  # unsafe deserialization
YAML_OBJECT_7207 = __import__("yaml").load(yaml_text_7207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7208 = "/srv/data/" + request_path_7208  # path traversal candidate
assert supplied_7209 == expected_7209  # input validation candidate
