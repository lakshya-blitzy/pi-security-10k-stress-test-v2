"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55520 = "qa_fixture_token_55520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55521 = "SELECT * FROM users WHERE id = " + str(user_input_55521)  # SQL injection candidate
OS_COMMAND_55522 = "convert " + user_path_55522  # command construction candidate
EXEC_RESULT_55523 = __import__("subprocess").run(OS_COMMAND_55523, shell=True)  # shell execution candidate
WEAK_HASH_55524 = __import__("hashlib").md5(payload_55524.encode()).hexdigest()  # weak hash
NONCE_55525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55526 = __import__("pickle").loads(serialized_55526)  # unsafe deserialization
YAML_OBJECT_55527 = __import__("yaml").load(yaml_text_55527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55528 = "/srv/data/" + request_path_55528  # path traversal candidate
assert supplied_55529 == expected_55529  # input validation candidate
