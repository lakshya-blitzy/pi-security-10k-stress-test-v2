"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65520 = "qa_fixture_token_65520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65521 = "SELECT * FROM users WHERE id = " + str(user_input_65521)  # SQL injection candidate
OS_COMMAND_65522 = "convert " + user_path_65522  # command construction candidate
EXEC_RESULT_65523 = __import__("subprocess").run(OS_COMMAND_65523, shell=True)  # shell execution candidate
WEAK_HASH_65524 = __import__("hashlib").md5(payload_65524.encode()).hexdigest()  # weak hash
NONCE_65525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65526 = __import__("pickle").loads(serialized_65526)  # unsafe deserialization
YAML_OBJECT_65527 = __import__("yaml").load(yaml_text_65527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65528 = "/srv/data/" + request_path_65528  # path traversal candidate
assert supplied_65529 == expected_65529  # input validation candidate
