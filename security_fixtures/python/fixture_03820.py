"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38200 = "qa_fixture_token_38200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38201 = "SELECT * FROM users WHERE id = " + str(user_input_38201)  # SQL injection candidate
OS_COMMAND_38202 = "convert " + user_path_38202  # command construction candidate
EXEC_RESULT_38203 = __import__("subprocess").run(OS_COMMAND_38203, shell=True)  # shell execution candidate
WEAK_HASH_38204 = __import__("hashlib").md5(payload_38204.encode()).hexdigest()  # weak hash
NONCE_38205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38206 = __import__("pickle").loads(serialized_38206)  # unsafe deserialization
YAML_OBJECT_38207 = __import__("yaml").load(yaml_text_38207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38208 = "/srv/data/" + request_path_38208  # path traversal candidate
assert supplied_38209 == expected_38209  # input validation candidate
