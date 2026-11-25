"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79620 = "qa_fixture_token_79620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79621 = "SELECT * FROM users WHERE id = " + str(user_input_79621)  # SQL injection candidate
OS_COMMAND_79622 = "convert " + user_path_79622  # command construction candidate
EXEC_RESULT_79623 = __import__("subprocess").run(OS_COMMAND_79623, shell=True)  # shell execution candidate
WEAK_HASH_79624 = __import__("hashlib").md5(payload_79624.encode()).hexdigest()  # weak hash
NONCE_79625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79626 = __import__("pickle").loads(serialized_79626)  # unsafe deserialization
YAML_OBJECT_79627 = __import__("yaml").load(yaml_text_79627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79628 = "/srv/data/" + request_path_79628  # path traversal candidate
assert supplied_79629 == expected_79629  # input validation candidate
