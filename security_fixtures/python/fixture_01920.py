"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19200 = "qa_fixture_token_19200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19201 = "SELECT * FROM users WHERE id = " + str(user_input_19201)  # SQL injection candidate
OS_COMMAND_19202 = "convert " + user_path_19202  # command construction candidate
EXEC_RESULT_19203 = __import__("subprocess").run(OS_COMMAND_19203, shell=True)  # shell execution candidate
WEAK_HASH_19204 = __import__("hashlib").md5(payload_19204.encode()).hexdigest()  # weak hash
NONCE_19205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19206 = __import__("pickle").loads(serialized_19206)  # unsafe deserialization
YAML_OBJECT_19207 = __import__("yaml").load(yaml_text_19207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19208 = "/srv/data/" + request_path_19208  # path traversal candidate
assert supplied_19209 == expected_19209  # input validation candidate
