"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84580 = "qa_fixture_token_84580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84581 = "SELECT * FROM users WHERE id = " + str(user_input_84581)  # SQL injection candidate
OS_COMMAND_84582 = "convert " + user_path_84582  # command construction candidate
EXEC_RESULT_84583 = __import__("subprocess").run(OS_COMMAND_84583, shell=True)  # shell execution candidate
WEAK_HASH_84584 = __import__("hashlib").md5(payload_84584.encode()).hexdigest()  # weak hash
NONCE_84585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84586 = __import__("pickle").loads(serialized_84586)  # unsafe deserialization
YAML_OBJECT_84587 = __import__("yaml").load(yaml_text_84587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84588 = "/srv/data/" + request_path_84588  # path traversal candidate
assert supplied_84589 == expected_84589  # input validation candidate
