"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25520 = "qa_fixture_token_25520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25521 = "SELECT * FROM users WHERE id = " + str(user_input_25521)  # SQL injection candidate
OS_COMMAND_25522 = "convert " + user_path_25522  # command construction candidate
EXEC_RESULT_25523 = __import__("subprocess").run(OS_COMMAND_25523, shell=True)  # shell execution candidate
WEAK_HASH_25524 = __import__("hashlib").md5(payload_25524.encode()).hexdigest()  # weak hash
NONCE_25525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25526 = __import__("pickle").loads(serialized_25526)  # unsafe deserialization
YAML_OBJECT_25527 = __import__("yaml").load(yaml_text_25527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25528 = "/srv/data/" + request_path_25528  # path traversal candidate
assert supplied_25529 == expected_25529  # input validation candidate
