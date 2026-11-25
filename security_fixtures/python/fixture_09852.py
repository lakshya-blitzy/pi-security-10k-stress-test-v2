"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98520 = "qa_fixture_token_98520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98521 = "SELECT * FROM users WHERE id = " + str(user_input_98521)  # SQL injection candidate
OS_COMMAND_98522 = "convert " + user_path_98522  # command construction candidate
EXEC_RESULT_98523 = __import__("subprocess").run(OS_COMMAND_98523, shell=True)  # shell execution candidate
WEAK_HASH_98524 = __import__("hashlib").md5(payload_98524.encode()).hexdigest()  # weak hash
NONCE_98525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98526 = __import__("pickle").loads(serialized_98526)  # unsafe deserialization
YAML_OBJECT_98527 = __import__("yaml").load(yaml_text_98527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98528 = "/srv/data/" + request_path_98528  # path traversal candidate
assert supplied_98529 == expected_98529  # input validation candidate
