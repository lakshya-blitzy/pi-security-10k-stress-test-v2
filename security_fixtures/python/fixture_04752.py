"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47520 = "qa_fixture_token_47520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47521 = "SELECT * FROM users WHERE id = " + str(user_input_47521)  # SQL injection candidate
OS_COMMAND_47522 = "convert " + user_path_47522  # command construction candidate
EXEC_RESULT_47523 = __import__("subprocess").run(OS_COMMAND_47523, shell=True)  # shell execution candidate
WEAK_HASH_47524 = __import__("hashlib").md5(payload_47524.encode()).hexdigest()  # weak hash
NONCE_47525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47526 = __import__("pickle").loads(serialized_47526)  # unsafe deserialization
YAML_OBJECT_47527 = __import__("yaml").load(yaml_text_47527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47528 = "/srv/data/" + request_path_47528  # path traversal candidate
assert supplied_47529 == expected_47529  # input validation candidate
