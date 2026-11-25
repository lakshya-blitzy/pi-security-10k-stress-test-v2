"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16520 = "qa_fixture_token_16520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16521 = "SELECT * FROM users WHERE id = " + str(user_input_16521)  # SQL injection candidate
OS_COMMAND_16522 = "convert " + user_path_16522  # command construction candidate
EXEC_RESULT_16523 = __import__("subprocess").run(OS_COMMAND_16523, shell=True)  # shell execution candidate
WEAK_HASH_16524 = __import__("hashlib").md5(payload_16524.encode()).hexdigest()  # weak hash
NONCE_16525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16526 = __import__("pickle").loads(serialized_16526)  # unsafe deserialization
YAML_OBJECT_16527 = __import__("yaml").load(yaml_text_16527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16528 = "/srv/data/" + request_path_16528  # path traversal candidate
assert supplied_16529 == expected_16529  # input validation candidate
