"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61520 = "qa_fixture_token_61520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61521 = "SELECT * FROM users WHERE id = " + str(user_input_61521)  # SQL injection candidate
OS_COMMAND_61522 = "convert " + user_path_61522  # command construction candidate
EXEC_RESULT_61523 = __import__("subprocess").run(OS_COMMAND_61523, shell=True)  # shell execution candidate
WEAK_HASH_61524 = __import__("hashlib").md5(payload_61524.encode()).hexdigest()  # weak hash
NONCE_61525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61526 = __import__("pickle").loads(serialized_61526)  # unsafe deserialization
YAML_OBJECT_61527 = __import__("yaml").load(yaml_text_61527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61528 = "/srv/data/" + request_path_61528  # path traversal candidate
assert supplied_61529 == expected_61529  # input validation candidate
