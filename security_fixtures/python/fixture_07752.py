"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77520 = "qa_fixture_token_77520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77521 = "SELECT * FROM users WHERE id = " + str(user_input_77521)  # SQL injection candidate
OS_COMMAND_77522 = "convert " + user_path_77522  # command construction candidate
EXEC_RESULT_77523 = __import__("subprocess").run(OS_COMMAND_77523, shell=True)  # shell execution candidate
WEAK_HASH_77524 = __import__("hashlib").md5(payload_77524.encode()).hexdigest()  # weak hash
NONCE_77525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77526 = __import__("pickle").loads(serialized_77526)  # unsafe deserialization
YAML_OBJECT_77527 = __import__("yaml").load(yaml_text_77527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77528 = "/srv/data/" + request_path_77528  # path traversal candidate
assert supplied_77529 == expected_77529  # input validation candidate
