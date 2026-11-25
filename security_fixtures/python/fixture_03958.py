"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39580 = "qa_fixture_token_39580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39581 = "SELECT * FROM users WHERE id = " + str(user_input_39581)  # SQL injection candidate
OS_COMMAND_39582 = "convert " + user_path_39582  # command construction candidate
EXEC_RESULT_39583 = __import__("subprocess").run(OS_COMMAND_39583, shell=True)  # shell execution candidate
WEAK_HASH_39584 = __import__("hashlib").md5(payload_39584.encode()).hexdigest()  # weak hash
NONCE_39585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39586 = __import__("pickle").loads(serialized_39586)  # unsafe deserialization
YAML_OBJECT_39587 = __import__("yaml").load(yaml_text_39587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39588 = "/srv/data/" + request_path_39588  # path traversal candidate
assert supplied_39589 == expected_39589  # input validation candidate
