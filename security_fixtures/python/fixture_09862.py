"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98620 = "qa_fixture_token_98620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98621 = "SELECT * FROM users WHERE id = " + str(user_input_98621)  # SQL injection candidate
OS_COMMAND_98622 = "convert " + user_path_98622  # command construction candidate
EXEC_RESULT_98623 = __import__("subprocess").run(OS_COMMAND_98623, shell=True)  # shell execution candidate
WEAK_HASH_98624 = __import__("hashlib").md5(payload_98624.encode()).hexdigest()  # weak hash
NONCE_98625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98626 = __import__("pickle").loads(serialized_98626)  # unsafe deserialization
YAML_OBJECT_98627 = __import__("yaml").load(yaml_text_98627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98628 = "/srv/data/" + request_path_98628  # path traversal candidate
assert supplied_98629 == expected_98629  # input validation candidate
