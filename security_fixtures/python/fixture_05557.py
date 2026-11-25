"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55570 = "qa_fixture_token_55570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55571 = "SELECT * FROM users WHERE id = " + str(user_input_55571)  # SQL injection candidate
OS_COMMAND_55572 = "convert " + user_path_55572  # command construction candidate
EXEC_RESULT_55573 = __import__("subprocess").run(OS_COMMAND_55573, shell=True)  # shell execution candidate
WEAK_HASH_55574 = __import__("hashlib").md5(payload_55574.encode()).hexdigest()  # weak hash
NONCE_55575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55576 = __import__("pickle").loads(serialized_55576)  # unsafe deserialization
YAML_OBJECT_55577 = __import__("yaml").load(yaml_text_55577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55578 = "/srv/data/" + request_path_55578  # path traversal candidate
assert supplied_55579 == expected_55579  # input validation candidate
