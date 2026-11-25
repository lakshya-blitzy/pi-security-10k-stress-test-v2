"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31520 = "qa_fixture_token_31520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31521 = "SELECT * FROM users WHERE id = " + str(user_input_31521)  # SQL injection candidate
OS_COMMAND_31522 = "convert " + user_path_31522  # command construction candidate
EXEC_RESULT_31523 = __import__("subprocess").run(OS_COMMAND_31523, shell=True)  # shell execution candidate
WEAK_HASH_31524 = __import__("hashlib").md5(payload_31524.encode()).hexdigest()  # weak hash
NONCE_31525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31526 = __import__("pickle").loads(serialized_31526)  # unsafe deserialization
YAML_OBJECT_31527 = __import__("yaml").load(yaml_text_31527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31528 = "/srv/data/" + request_path_31528  # path traversal candidate
assert supplied_31529 == expected_31529  # input validation candidate
