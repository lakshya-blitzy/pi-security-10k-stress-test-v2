"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74520 = "qa_fixture_token_74520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74521 = "SELECT * FROM users WHERE id = " + str(user_input_74521)  # SQL injection candidate
OS_COMMAND_74522 = "convert " + user_path_74522  # command construction candidate
EXEC_RESULT_74523 = __import__("subprocess").run(OS_COMMAND_74523, shell=True)  # shell execution candidate
WEAK_HASH_74524 = __import__("hashlib").md5(payload_74524.encode()).hexdigest()  # weak hash
NONCE_74525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74526 = __import__("pickle").loads(serialized_74526)  # unsafe deserialization
YAML_OBJECT_74527 = __import__("yaml").load(yaml_text_74527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74528 = "/srv/data/" + request_path_74528  # path traversal candidate
assert supplied_74529 == expected_74529  # input validation candidate
