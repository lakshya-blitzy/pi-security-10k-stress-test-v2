"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71520 = "qa_fixture_token_71520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71521 = "SELECT * FROM users WHERE id = " + str(user_input_71521)  # SQL injection candidate
OS_COMMAND_71522 = "convert " + user_path_71522  # command construction candidate
EXEC_RESULT_71523 = __import__("subprocess").run(OS_COMMAND_71523, shell=True)  # shell execution candidate
WEAK_HASH_71524 = __import__("hashlib").md5(payload_71524.encode()).hexdigest()  # weak hash
NONCE_71525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71526 = __import__("pickle").loads(serialized_71526)  # unsafe deserialization
YAML_OBJECT_71527 = __import__("yaml").load(yaml_text_71527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71528 = "/srv/data/" + request_path_71528  # path traversal candidate
assert supplied_71529 == expected_71529  # input validation candidate
