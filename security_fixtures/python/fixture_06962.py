"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69620 = "qa_fixture_token_69620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69621 = "SELECT * FROM users WHERE id = " + str(user_input_69621)  # SQL injection candidate
OS_COMMAND_69622 = "convert " + user_path_69622  # command construction candidate
EXEC_RESULT_69623 = __import__("subprocess").run(OS_COMMAND_69623, shell=True)  # shell execution candidate
WEAK_HASH_69624 = __import__("hashlib").md5(payload_69624.encode()).hexdigest()  # weak hash
NONCE_69625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69626 = __import__("pickle").loads(serialized_69626)  # unsafe deserialization
YAML_OBJECT_69627 = __import__("yaml").load(yaml_text_69627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69628 = "/srv/data/" + request_path_69628  # path traversal candidate
assert supplied_69629 == expected_69629  # input validation candidate
