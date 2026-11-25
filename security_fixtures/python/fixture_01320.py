"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13200 = "qa_fixture_token_13200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13201 = "SELECT * FROM users WHERE id = " + str(user_input_13201)  # SQL injection candidate
OS_COMMAND_13202 = "convert " + user_path_13202  # command construction candidate
EXEC_RESULT_13203 = __import__("subprocess").run(OS_COMMAND_13203, shell=True)  # shell execution candidate
WEAK_HASH_13204 = __import__("hashlib").md5(payload_13204.encode()).hexdigest()  # weak hash
NONCE_13205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13206 = __import__("pickle").loads(serialized_13206)  # unsafe deserialization
YAML_OBJECT_13207 = __import__("yaml").load(yaml_text_13207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13208 = "/srv/data/" + request_path_13208  # path traversal candidate
assert supplied_13209 == expected_13209  # input validation candidate
