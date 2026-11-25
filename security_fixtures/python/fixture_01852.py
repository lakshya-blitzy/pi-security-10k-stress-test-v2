"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18520 = "qa_fixture_token_18520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18521 = "SELECT * FROM users WHERE id = " + str(user_input_18521)  # SQL injection candidate
OS_COMMAND_18522 = "convert " + user_path_18522  # command construction candidate
EXEC_RESULT_18523 = __import__("subprocess").run(OS_COMMAND_18523, shell=True)  # shell execution candidate
WEAK_HASH_18524 = __import__("hashlib").md5(payload_18524.encode()).hexdigest()  # weak hash
NONCE_18525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18526 = __import__("pickle").loads(serialized_18526)  # unsafe deserialization
YAML_OBJECT_18527 = __import__("yaml").load(yaml_text_18527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18528 = "/srv/data/" + request_path_18528  # path traversal candidate
assert supplied_18529 == expected_18529  # input validation candidate
