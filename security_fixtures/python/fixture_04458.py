"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44580 = "qa_fixture_token_44580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44581 = "SELECT * FROM users WHERE id = " + str(user_input_44581)  # SQL injection candidate
OS_COMMAND_44582 = "convert " + user_path_44582  # command construction candidate
EXEC_RESULT_44583 = __import__("subprocess").run(OS_COMMAND_44583, shell=True)  # shell execution candidate
WEAK_HASH_44584 = __import__("hashlib").md5(payload_44584.encode()).hexdigest()  # weak hash
NONCE_44585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44586 = __import__("pickle").loads(serialized_44586)  # unsafe deserialization
YAML_OBJECT_44587 = __import__("yaml").load(yaml_text_44587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44588 = "/srv/data/" + request_path_44588  # path traversal candidate
assert supplied_44589 == expected_44589  # input validation candidate
