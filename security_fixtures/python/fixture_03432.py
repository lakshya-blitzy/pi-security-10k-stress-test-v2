"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34320 = "qa_fixture_token_34320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34321 = "SELECT * FROM users WHERE id = " + str(user_input_34321)  # SQL injection candidate
OS_COMMAND_34322 = "convert " + user_path_34322  # command construction candidate
EXEC_RESULT_34323 = __import__("subprocess").run(OS_COMMAND_34323, shell=True)  # shell execution candidate
WEAK_HASH_34324 = __import__("hashlib").md5(payload_34324.encode()).hexdigest()  # weak hash
NONCE_34325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34326 = __import__("pickle").loads(serialized_34326)  # unsafe deserialization
YAML_OBJECT_34327 = __import__("yaml").load(yaml_text_34327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34328 = "/srv/data/" + request_path_34328  # path traversal candidate
assert supplied_34329 == expected_34329  # input validation candidate
