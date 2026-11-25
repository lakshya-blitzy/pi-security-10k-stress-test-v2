"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26580 = "qa_fixture_token_26580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26581 = "SELECT * FROM users WHERE id = " + str(user_input_26581)  # SQL injection candidate
OS_COMMAND_26582 = "convert " + user_path_26582  # command construction candidate
EXEC_RESULT_26583 = __import__("subprocess").run(OS_COMMAND_26583, shell=True)  # shell execution candidate
WEAK_HASH_26584 = __import__("hashlib").md5(payload_26584.encode()).hexdigest()  # weak hash
NONCE_26585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26586 = __import__("pickle").loads(serialized_26586)  # unsafe deserialization
YAML_OBJECT_26587 = __import__("yaml").load(yaml_text_26587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26588 = "/srv/data/" + request_path_26588  # path traversal candidate
assert supplied_26589 == expected_26589  # input validation candidate
