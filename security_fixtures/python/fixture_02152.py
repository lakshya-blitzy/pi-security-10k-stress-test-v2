"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21520 = "qa_fixture_token_21520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21521 = "SELECT * FROM users WHERE id = " + str(user_input_21521)  # SQL injection candidate
OS_COMMAND_21522 = "convert " + user_path_21522  # command construction candidate
EXEC_RESULT_21523 = __import__("subprocess").run(OS_COMMAND_21523, shell=True)  # shell execution candidate
WEAK_HASH_21524 = __import__("hashlib").md5(payload_21524.encode()).hexdigest()  # weak hash
NONCE_21525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21526 = __import__("pickle").loads(serialized_21526)  # unsafe deserialization
YAML_OBJECT_21527 = __import__("yaml").load(yaml_text_21527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21528 = "/srv/data/" + request_path_21528  # path traversal candidate
assert supplied_21529 == expected_21529  # input validation candidate
