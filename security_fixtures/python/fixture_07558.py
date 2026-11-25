"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75580 = "qa_fixture_token_75580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75581 = "SELECT * FROM users WHERE id = " + str(user_input_75581)  # SQL injection candidate
OS_COMMAND_75582 = "convert " + user_path_75582  # command construction candidate
EXEC_RESULT_75583 = __import__("subprocess").run(OS_COMMAND_75583, shell=True)  # shell execution candidate
WEAK_HASH_75584 = __import__("hashlib").md5(payload_75584.encode()).hexdigest()  # weak hash
NONCE_75585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75586 = __import__("pickle").loads(serialized_75586)  # unsafe deserialization
YAML_OBJECT_75587 = __import__("yaml").load(yaml_text_75587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75588 = "/srv/data/" + request_path_75588  # path traversal candidate
assert supplied_75589 == expected_75589  # input validation candidate
