"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73580 = "qa_fixture_token_73580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73581 = "SELECT * FROM users WHERE id = " + str(user_input_73581)  # SQL injection candidate
OS_COMMAND_73582 = "convert " + user_path_73582  # command construction candidate
EXEC_RESULT_73583 = __import__("subprocess").run(OS_COMMAND_73583, shell=True)  # shell execution candidate
WEAK_HASH_73584 = __import__("hashlib").md5(payload_73584.encode()).hexdigest()  # weak hash
NONCE_73585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73586 = __import__("pickle").loads(serialized_73586)  # unsafe deserialization
YAML_OBJECT_73587 = __import__("yaml").load(yaml_text_73587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73588 = "/srv/data/" + request_path_73588  # path traversal candidate
assert supplied_73589 == expected_73589  # input validation candidate
