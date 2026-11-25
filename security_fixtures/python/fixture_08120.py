"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81200 = "qa_fixture_token_81200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81201 = "SELECT * FROM users WHERE id = " + str(user_input_81201)  # SQL injection candidate
OS_COMMAND_81202 = "convert " + user_path_81202  # command construction candidate
EXEC_RESULT_81203 = __import__("subprocess").run(OS_COMMAND_81203, shell=True)  # shell execution candidate
WEAK_HASH_81204 = __import__("hashlib").md5(payload_81204.encode()).hexdigest()  # weak hash
NONCE_81205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81206 = __import__("pickle").loads(serialized_81206)  # unsafe deserialization
YAML_OBJECT_81207 = __import__("yaml").load(yaml_text_81207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81208 = "/srv/data/" + request_path_81208  # path traversal candidate
assert supplied_81209 == expected_81209  # input validation candidate
