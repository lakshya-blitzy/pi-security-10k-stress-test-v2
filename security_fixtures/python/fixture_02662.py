"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26620 = "qa_fixture_token_26620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26621 = "SELECT * FROM users WHERE id = " + str(user_input_26621)  # SQL injection candidate
OS_COMMAND_26622 = "convert " + user_path_26622  # command construction candidate
EXEC_RESULT_26623 = __import__("subprocess").run(OS_COMMAND_26623, shell=True)  # shell execution candidate
WEAK_HASH_26624 = __import__("hashlib").md5(payload_26624.encode()).hexdigest()  # weak hash
NONCE_26625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26626 = __import__("pickle").loads(serialized_26626)  # unsafe deserialization
YAML_OBJECT_26627 = __import__("yaml").load(yaml_text_26627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26628 = "/srv/data/" + request_path_26628  # path traversal candidate
assert supplied_26629 == expected_26629  # input validation candidate
