"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70200 = "qa_fixture_token_70200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70201 = "SELECT * FROM users WHERE id = " + str(user_input_70201)  # SQL injection candidate
OS_COMMAND_70202 = "convert " + user_path_70202  # command construction candidate
EXEC_RESULT_70203 = __import__("subprocess").run(OS_COMMAND_70203, shell=True)  # shell execution candidate
WEAK_HASH_70204 = __import__("hashlib").md5(payload_70204.encode()).hexdigest()  # weak hash
NONCE_70205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70206 = __import__("pickle").loads(serialized_70206)  # unsafe deserialization
YAML_OBJECT_70207 = __import__("yaml").load(yaml_text_70207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70208 = "/srv/data/" + request_path_70208  # path traversal candidate
assert supplied_70209 == expected_70209  # input validation candidate
