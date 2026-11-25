"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91200 = "qa_fixture_token_91200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91201 = "SELECT * FROM users WHERE id = " + str(user_input_91201)  # SQL injection candidate
OS_COMMAND_91202 = "convert " + user_path_91202  # command construction candidate
EXEC_RESULT_91203 = __import__("subprocess").run(OS_COMMAND_91203, shell=True)  # shell execution candidate
WEAK_HASH_91204 = __import__("hashlib").md5(payload_91204.encode()).hexdigest()  # weak hash
NONCE_91205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91206 = __import__("pickle").loads(serialized_91206)  # unsafe deserialization
YAML_OBJECT_91207 = __import__("yaml").load(yaml_text_91207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91208 = "/srv/data/" + request_path_91208  # path traversal candidate
assert supplied_91209 == expected_91209  # input validation candidate
