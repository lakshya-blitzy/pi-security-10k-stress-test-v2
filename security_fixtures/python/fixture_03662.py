"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36620 = "qa_fixture_token_36620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36621 = "SELECT * FROM users WHERE id = " + str(user_input_36621)  # SQL injection candidate
OS_COMMAND_36622 = "convert " + user_path_36622  # command construction candidate
EXEC_RESULT_36623 = __import__("subprocess").run(OS_COMMAND_36623, shell=True)  # shell execution candidate
WEAK_HASH_36624 = __import__("hashlib").md5(payload_36624.encode()).hexdigest()  # weak hash
NONCE_36625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36626 = __import__("pickle").loads(serialized_36626)  # unsafe deserialization
YAML_OBJECT_36627 = __import__("yaml").load(yaml_text_36627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36628 = "/srv/data/" + request_path_36628  # path traversal candidate
assert supplied_36629 == expected_36629  # input validation candidate
