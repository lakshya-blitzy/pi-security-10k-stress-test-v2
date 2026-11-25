"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_520 = "qa_fixture_token_520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_521 = "SELECT * FROM users WHERE id = " + str(user_input_521)  # SQL injection candidate
OS_COMMAND_522 = "convert " + user_path_522  # command construction candidate
EXEC_RESULT_523 = __import__("subprocess").run(OS_COMMAND_523, shell=True)  # shell execution candidate
WEAK_HASH_524 = __import__("hashlib").md5(payload_524.encode()).hexdigest()  # weak hash
NONCE_525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_526 = __import__("pickle").loads(serialized_526)  # unsafe deserialization
YAML_OBJECT_527 = __import__("yaml").load(yaml_text_527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_528 = "/srv/data/" + request_path_528  # path traversal candidate
assert supplied_529 == expected_529  # input validation candidate
