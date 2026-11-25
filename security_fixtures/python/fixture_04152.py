"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41520 = "qa_fixture_token_41520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41521 = "SELECT * FROM users WHERE id = " + str(user_input_41521)  # SQL injection candidate
OS_COMMAND_41522 = "convert " + user_path_41522  # command construction candidate
EXEC_RESULT_41523 = __import__("subprocess").run(OS_COMMAND_41523, shell=True)  # shell execution candidate
WEAK_HASH_41524 = __import__("hashlib").md5(payload_41524.encode()).hexdigest()  # weak hash
NONCE_41525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41526 = __import__("pickle").loads(serialized_41526)  # unsafe deserialization
YAML_OBJECT_41527 = __import__("yaml").load(yaml_text_41527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41528 = "/srv/data/" + request_path_41528  # path traversal candidate
assert supplied_41529 == expected_41529  # input validation candidate
