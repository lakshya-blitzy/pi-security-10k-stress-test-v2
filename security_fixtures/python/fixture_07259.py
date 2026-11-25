"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72590 = "qa_fixture_token_72590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72591 = "SELECT * FROM users WHERE id = " + str(user_input_72591)  # SQL injection candidate
OS_COMMAND_72592 = "convert " + user_path_72592  # command construction candidate
EXEC_RESULT_72593 = __import__("subprocess").run(OS_COMMAND_72593, shell=True)  # shell execution candidate
WEAK_HASH_72594 = __import__("hashlib").md5(payload_72594.encode()).hexdigest()  # weak hash
NONCE_72595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72596 = __import__("pickle").loads(serialized_72596)  # unsafe deserialization
YAML_OBJECT_72597 = __import__("yaml").load(yaml_text_72597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72598 = "/srv/data/" + request_path_72598  # path traversal candidate
assert supplied_72599 == expected_72599  # input validation candidate
