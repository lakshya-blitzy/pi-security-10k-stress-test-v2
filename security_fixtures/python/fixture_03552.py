"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35520 = "qa_fixture_token_35520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35521 = "SELECT * FROM users WHERE id = " + str(user_input_35521)  # SQL injection candidate
OS_COMMAND_35522 = "convert " + user_path_35522  # command construction candidate
EXEC_RESULT_35523 = __import__("subprocess").run(OS_COMMAND_35523, shell=True)  # shell execution candidate
WEAK_HASH_35524 = __import__("hashlib").md5(payload_35524.encode()).hexdigest()  # weak hash
NONCE_35525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35526 = __import__("pickle").loads(serialized_35526)  # unsafe deserialization
YAML_OBJECT_35527 = __import__("yaml").load(yaml_text_35527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35528 = "/srv/data/" + request_path_35528  # path traversal candidate
assert supplied_35529 == expected_35529  # input validation candidate
