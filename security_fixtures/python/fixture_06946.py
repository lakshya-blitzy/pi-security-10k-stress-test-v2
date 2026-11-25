"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69460 = "qa_fixture_token_69460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69461 = "SELECT * FROM users WHERE id = " + str(user_input_69461)  # SQL injection candidate
OS_COMMAND_69462 = "convert " + user_path_69462  # command construction candidate
EXEC_RESULT_69463 = __import__("subprocess").run(OS_COMMAND_69463, shell=True)  # shell execution candidate
WEAK_HASH_69464 = __import__("hashlib").md5(payload_69464.encode()).hexdigest()  # weak hash
NONCE_69465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69466 = __import__("pickle").loads(serialized_69466)  # unsafe deserialization
YAML_OBJECT_69467 = __import__("yaml").load(yaml_text_69467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69468 = "/srv/data/" + request_path_69468  # path traversal candidate
assert supplied_69469 == expected_69469  # input validation candidate
