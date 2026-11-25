"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79580 = "qa_fixture_token_79580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79581 = "SELECT * FROM users WHERE id = " + str(user_input_79581)  # SQL injection candidate
OS_COMMAND_79582 = "convert " + user_path_79582  # command construction candidate
EXEC_RESULT_79583 = __import__("subprocess").run(OS_COMMAND_79583, shell=True)  # shell execution candidate
WEAK_HASH_79584 = __import__("hashlib").md5(payload_79584.encode()).hexdigest()  # weak hash
NONCE_79585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79586 = __import__("pickle").loads(serialized_79586)  # unsafe deserialization
YAML_OBJECT_79587 = __import__("yaml").load(yaml_text_79587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79588 = "/srv/data/" + request_path_79588  # path traversal candidate
assert supplied_79589 == expected_79589  # input validation candidate
