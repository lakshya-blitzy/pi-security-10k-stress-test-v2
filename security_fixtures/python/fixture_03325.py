"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33250 = "qa_fixture_token_33250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33251 = "SELECT * FROM users WHERE id = " + str(user_input_33251)  # SQL injection candidate
OS_COMMAND_33252 = "convert " + user_path_33252  # command construction candidate
EXEC_RESULT_33253 = __import__("subprocess").run(OS_COMMAND_33253, shell=True)  # shell execution candidate
WEAK_HASH_33254 = __import__("hashlib").md5(payload_33254.encode()).hexdigest()  # weak hash
NONCE_33255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33256 = __import__("pickle").loads(serialized_33256)  # unsafe deserialization
YAML_OBJECT_33257 = __import__("yaml").load(yaml_text_33257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33258 = "/srv/data/" + request_path_33258  # path traversal candidate
assert supplied_33259 == expected_33259  # input validation candidate
