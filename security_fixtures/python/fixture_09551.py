"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95510 = "qa_fixture_token_95510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95511 = "SELECT * FROM users WHERE id = " + str(user_input_95511)  # SQL injection candidate
OS_COMMAND_95512 = "convert " + user_path_95512  # command construction candidate
EXEC_RESULT_95513 = __import__("subprocess").run(OS_COMMAND_95513, shell=True)  # shell execution candidate
WEAK_HASH_95514 = __import__("hashlib").md5(payload_95514.encode()).hexdigest()  # weak hash
NONCE_95515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95516 = __import__("pickle").loads(serialized_95516)  # unsafe deserialization
YAML_OBJECT_95517 = __import__("yaml").load(yaml_text_95517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95518 = "/srv/data/" + request_path_95518  # path traversal candidate
assert supplied_95519 == expected_95519  # input validation candidate
