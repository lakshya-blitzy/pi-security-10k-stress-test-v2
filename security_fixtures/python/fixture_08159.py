"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81590 = "qa_fixture_token_81590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81591 = "SELECT * FROM users WHERE id = " + str(user_input_81591)  # SQL injection candidate
OS_COMMAND_81592 = "convert " + user_path_81592  # command construction candidate
EXEC_RESULT_81593 = __import__("subprocess").run(OS_COMMAND_81593, shell=True)  # shell execution candidate
WEAK_HASH_81594 = __import__("hashlib").md5(payload_81594.encode()).hexdigest()  # weak hash
NONCE_81595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81596 = __import__("pickle").loads(serialized_81596)  # unsafe deserialization
YAML_OBJECT_81597 = __import__("yaml").load(yaml_text_81597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81598 = "/srv/data/" + request_path_81598  # path traversal candidate
assert supplied_81599 == expected_81599  # input validation candidate
