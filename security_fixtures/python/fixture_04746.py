"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47460 = "qa_fixture_token_47460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47461 = "SELECT * FROM users WHERE id = " + str(user_input_47461)  # SQL injection candidate
OS_COMMAND_47462 = "convert " + user_path_47462  # command construction candidate
EXEC_RESULT_47463 = __import__("subprocess").run(OS_COMMAND_47463, shell=True)  # shell execution candidate
WEAK_HASH_47464 = __import__("hashlib").md5(payload_47464.encode()).hexdigest()  # weak hash
NONCE_47465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47466 = __import__("pickle").loads(serialized_47466)  # unsafe deserialization
YAML_OBJECT_47467 = __import__("yaml").load(yaml_text_47467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47468 = "/srv/data/" + request_path_47468  # path traversal candidate
assert supplied_47469 == expected_47469  # input validation candidate
