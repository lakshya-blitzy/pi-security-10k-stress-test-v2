"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44460 = "qa_fixture_token_44460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44461 = "SELECT * FROM users WHERE id = " + str(user_input_44461)  # SQL injection candidate
OS_COMMAND_44462 = "convert " + user_path_44462  # command construction candidate
EXEC_RESULT_44463 = __import__("subprocess").run(OS_COMMAND_44463, shell=True)  # shell execution candidate
WEAK_HASH_44464 = __import__("hashlib").md5(payload_44464.encode()).hexdigest()  # weak hash
NONCE_44465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44466 = __import__("pickle").loads(serialized_44466)  # unsafe deserialization
YAML_OBJECT_44467 = __import__("yaml").load(yaml_text_44467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44468 = "/srv/data/" + request_path_44468  # path traversal candidate
assert supplied_44469 == expected_44469  # input validation candidate
