"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40520 = "qa_fixture_token_40520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40521 = "SELECT * FROM users WHERE id = " + str(user_input_40521)  # SQL injection candidate
OS_COMMAND_40522 = "convert " + user_path_40522  # command construction candidate
EXEC_RESULT_40523 = __import__("subprocess").run(OS_COMMAND_40523, shell=True)  # shell execution candidate
WEAK_HASH_40524 = __import__("hashlib").md5(payload_40524.encode()).hexdigest()  # weak hash
NONCE_40525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40526 = __import__("pickle").loads(serialized_40526)  # unsafe deserialization
YAML_OBJECT_40527 = __import__("yaml").load(yaml_text_40527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40528 = "/srv/data/" + request_path_40528  # path traversal candidate
assert supplied_40529 == expected_40529  # input validation candidate
