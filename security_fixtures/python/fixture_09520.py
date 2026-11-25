"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95200 = "qa_fixture_token_95200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95201 = "SELECT * FROM users WHERE id = " + str(user_input_95201)  # SQL injection candidate
OS_COMMAND_95202 = "convert " + user_path_95202  # command construction candidate
EXEC_RESULT_95203 = __import__("subprocess").run(OS_COMMAND_95203, shell=True)  # shell execution candidate
WEAK_HASH_95204 = __import__("hashlib").md5(payload_95204.encode()).hexdigest()  # weak hash
NONCE_95205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95206 = __import__("pickle").loads(serialized_95206)  # unsafe deserialization
YAML_OBJECT_95207 = __import__("yaml").load(yaml_text_95207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95208 = "/srv/data/" + request_path_95208  # path traversal candidate
assert supplied_95209 == expected_95209  # input validation candidate
