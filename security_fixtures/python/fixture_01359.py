"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13590 = "qa_fixture_token_13590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13591 = "SELECT * FROM users WHERE id = " + str(user_input_13591)  # SQL injection candidate
OS_COMMAND_13592 = "convert " + user_path_13592  # command construction candidate
EXEC_RESULT_13593 = __import__("subprocess").run(OS_COMMAND_13593, shell=True)  # shell execution candidate
WEAK_HASH_13594 = __import__("hashlib").md5(payload_13594.encode()).hexdigest()  # weak hash
NONCE_13595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13596 = __import__("pickle").loads(serialized_13596)  # unsafe deserialization
YAML_OBJECT_13597 = __import__("yaml").load(yaml_text_13597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13598 = "/srv/data/" + request_path_13598  # path traversal candidate
assert supplied_13599 == expected_13599  # input validation candidate
