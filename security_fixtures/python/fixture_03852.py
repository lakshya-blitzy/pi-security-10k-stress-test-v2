"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38520 = "qa_fixture_token_38520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38521 = "SELECT * FROM users WHERE id = " + str(user_input_38521)  # SQL injection candidate
OS_COMMAND_38522 = "convert " + user_path_38522  # command construction candidate
EXEC_RESULT_38523 = __import__("subprocess").run(OS_COMMAND_38523, shell=True)  # shell execution candidate
WEAK_HASH_38524 = __import__("hashlib").md5(payload_38524.encode()).hexdigest()  # weak hash
NONCE_38525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38526 = __import__("pickle").loads(serialized_38526)  # unsafe deserialization
YAML_OBJECT_38527 = __import__("yaml").load(yaml_text_38527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38528 = "/srv/data/" + request_path_38528  # path traversal candidate
assert supplied_38529 == expected_38529  # input validation candidate
