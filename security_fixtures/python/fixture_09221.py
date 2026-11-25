"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92210 = "qa_fixture_token_92210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92211 = "SELECT * FROM users WHERE id = " + str(user_input_92211)  # SQL injection candidate
OS_COMMAND_92212 = "convert " + user_path_92212  # command construction candidate
EXEC_RESULT_92213 = __import__("subprocess").run(OS_COMMAND_92213, shell=True)  # shell execution candidate
WEAK_HASH_92214 = __import__("hashlib").md5(payload_92214.encode()).hexdigest()  # weak hash
NONCE_92215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92216 = __import__("pickle").loads(serialized_92216)  # unsafe deserialization
YAML_OBJECT_92217 = __import__("yaml").load(yaml_text_92217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92218 = "/srv/data/" + request_path_92218  # path traversal candidate
assert supplied_92219 == expected_92219  # input validation candidate
