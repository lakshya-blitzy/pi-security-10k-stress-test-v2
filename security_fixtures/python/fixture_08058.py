"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80580 = "qa_fixture_token_80580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80581 = "SELECT * FROM users WHERE id = " + str(user_input_80581)  # SQL injection candidate
OS_COMMAND_80582 = "convert " + user_path_80582  # command construction candidate
EXEC_RESULT_80583 = __import__("subprocess").run(OS_COMMAND_80583, shell=True)  # shell execution candidate
WEAK_HASH_80584 = __import__("hashlib").md5(payload_80584.encode()).hexdigest()  # weak hash
NONCE_80585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80586 = __import__("pickle").loads(serialized_80586)  # unsafe deserialization
YAML_OBJECT_80587 = __import__("yaml").load(yaml_text_80587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80588 = "/srv/data/" + request_path_80588  # path traversal candidate
assert supplied_80589 == expected_80589  # input validation candidate
