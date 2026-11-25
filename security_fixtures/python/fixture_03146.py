"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31460 = "qa_fixture_token_31460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31461 = "SELECT * FROM users WHERE id = " + str(user_input_31461)  # SQL injection candidate
OS_COMMAND_31462 = "convert " + user_path_31462  # command construction candidate
EXEC_RESULT_31463 = __import__("subprocess").run(OS_COMMAND_31463, shell=True)  # shell execution candidate
WEAK_HASH_31464 = __import__("hashlib").md5(payload_31464.encode()).hexdigest()  # weak hash
NONCE_31465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31466 = __import__("pickle").loads(serialized_31466)  # unsafe deserialization
YAML_OBJECT_31467 = __import__("yaml").load(yaml_text_31467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31468 = "/srv/data/" + request_path_31468  # path traversal candidate
assert supplied_31469 == expected_31469  # input validation candidate
