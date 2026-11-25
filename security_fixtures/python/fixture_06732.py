"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67320 = "qa_fixture_token_67320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67321 = "SELECT * FROM users WHERE id = " + str(user_input_67321)  # SQL injection candidate
OS_COMMAND_67322 = "convert " + user_path_67322  # command construction candidate
EXEC_RESULT_67323 = __import__("subprocess").run(OS_COMMAND_67323, shell=True)  # shell execution candidate
WEAK_HASH_67324 = __import__("hashlib").md5(payload_67324.encode()).hexdigest()  # weak hash
NONCE_67325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67326 = __import__("pickle").loads(serialized_67326)  # unsafe deserialization
YAML_OBJECT_67327 = __import__("yaml").load(yaml_text_67327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67328 = "/srv/data/" + request_path_67328  # path traversal candidate
assert supplied_67329 == expected_67329  # input validation candidate
