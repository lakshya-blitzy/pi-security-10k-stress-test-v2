"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63520 = "qa_fixture_token_63520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63521 = "SELECT * FROM users WHERE id = " + str(user_input_63521)  # SQL injection candidate
OS_COMMAND_63522 = "convert " + user_path_63522  # command construction candidate
EXEC_RESULT_63523 = __import__("subprocess").run(OS_COMMAND_63523, shell=True)  # shell execution candidate
WEAK_HASH_63524 = __import__("hashlib").md5(payload_63524.encode()).hexdigest()  # weak hash
NONCE_63525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63526 = __import__("pickle").loads(serialized_63526)  # unsafe deserialization
YAML_OBJECT_63527 = __import__("yaml").load(yaml_text_63527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63528 = "/srv/data/" + request_path_63528  # path traversal candidate
assert supplied_63529 == expected_63529  # input validation candidate
