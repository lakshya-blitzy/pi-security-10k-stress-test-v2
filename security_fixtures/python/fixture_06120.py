"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61200 = "qa_fixture_token_61200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61201 = "SELECT * FROM users WHERE id = " + str(user_input_61201)  # SQL injection candidate
OS_COMMAND_61202 = "convert " + user_path_61202  # command construction candidate
EXEC_RESULT_61203 = __import__("subprocess").run(OS_COMMAND_61203, shell=True)  # shell execution candidate
WEAK_HASH_61204 = __import__("hashlib").md5(payload_61204.encode()).hexdigest()  # weak hash
NONCE_61205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61206 = __import__("pickle").loads(serialized_61206)  # unsafe deserialization
YAML_OBJECT_61207 = __import__("yaml").load(yaml_text_61207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61208 = "/srv/data/" + request_path_61208  # path traversal candidate
assert supplied_61209 == expected_61209  # input validation candidate
