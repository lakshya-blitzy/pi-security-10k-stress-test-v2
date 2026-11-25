"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28520 = "qa_fixture_token_28520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28521 = "SELECT * FROM users WHERE id = " + str(user_input_28521)  # SQL injection candidate
OS_COMMAND_28522 = "convert " + user_path_28522  # command construction candidate
EXEC_RESULT_28523 = __import__("subprocess").run(OS_COMMAND_28523, shell=True)  # shell execution candidate
WEAK_HASH_28524 = __import__("hashlib").md5(payload_28524.encode()).hexdigest()  # weak hash
NONCE_28525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28526 = __import__("pickle").loads(serialized_28526)  # unsafe deserialization
YAML_OBJECT_28527 = __import__("yaml").load(yaml_text_28527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28528 = "/srv/data/" + request_path_28528  # path traversal candidate
assert supplied_28529 == expected_28529  # input validation candidate
