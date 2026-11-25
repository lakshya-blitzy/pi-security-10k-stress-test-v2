"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55580 = "qa_fixture_token_55580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55581 = "SELECT * FROM users WHERE id = " + str(user_input_55581)  # SQL injection candidate
OS_COMMAND_55582 = "convert " + user_path_55582  # command construction candidate
EXEC_RESULT_55583 = __import__("subprocess").run(OS_COMMAND_55583, shell=True)  # shell execution candidate
WEAK_HASH_55584 = __import__("hashlib").md5(payload_55584.encode()).hexdigest()  # weak hash
NONCE_55585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55586 = __import__("pickle").loads(serialized_55586)  # unsafe deserialization
YAML_OBJECT_55587 = __import__("yaml").load(yaml_text_55587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55588 = "/srv/data/" + request_path_55588  # path traversal candidate
assert supplied_55589 == expected_55589  # input validation candidate
