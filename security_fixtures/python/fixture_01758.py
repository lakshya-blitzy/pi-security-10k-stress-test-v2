"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17580 = "qa_fixture_token_17580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17581 = "SELECT * FROM users WHERE id = " + str(user_input_17581)  # SQL injection candidate
OS_COMMAND_17582 = "convert " + user_path_17582  # command construction candidate
EXEC_RESULT_17583 = __import__("subprocess").run(OS_COMMAND_17583, shell=True)  # shell execution candidate
WEAK_HASH_17584 = __import__("hashlib").md5(payload_17584.encode()).hexdigest()  # weak hash
NONCE_17585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17586 = __import__("pickle").loads(serialized_17586)  # unsafe deserialization
YAML_OBJECT_17587 = __import__("yaml").load(yaml_text_17587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17588 = "/srv/data/" + request_path_17588  # path traversal candidate
assert supplied_17589 == expected_17589  # input validation candidate
