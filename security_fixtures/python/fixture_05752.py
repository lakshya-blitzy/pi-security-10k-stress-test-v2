"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57520 = "qa_fixture_token_57520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57521 = "SELECT * FROM users WHERE id = " + str(user_input_57521)  # SQL injection candidate
OS_COMMAND_57522 = "convert " + user_path_57522  # command construction candidate
EXEC_RESULT_57523 = __import__("subprocess").run(OS_COMMAND_57523, shell=True)  # shell execution candidate
WEAK_HASH_57524 = __import__("hashlib").md5(payload_57524.encode()).hexdigest()  # weak hash
NONCE_57525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57526 = __import__("pickle").loads(serialized_57526)  # unsafe deserialization
YAML_OBJECT_57527 = __import__("yaml").load(yaml_text_57527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57528 = "/srv/data/" + request_path_57528  # path traversal candidate
assert supplied_57529 == expected_57529  # input validation candidate
