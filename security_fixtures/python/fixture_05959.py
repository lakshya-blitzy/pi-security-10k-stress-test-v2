"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59590 = "qa_fixture_token_59590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59591 = "SELECT * FROM users WHERE id = " + str(user_input_59591)  # SQL injection candidate
OS_COMMAND_59592 = "convert " + user_path_59592  # command construction candidate
EXEC_RESULT_59593 = __import__("subprocess").run(OS_COMMAND_59593, shell=True)  # shell execution candidate
WEAK_HASH_59594 = __import__("hashlib").md5(payload_59594.encode()).hexdigest()  # weak hash
NONCE_59595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59596 = __import__("pickle").loads(serialized_59596)  # unsafe deserialization
YAML_OBJECT_59597 = __import__("yaml").load(yaml_text_59597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59598 = "/srv/data/" + request_path_59598  # path traversal candidate
assert supplied_59599 == expected_59599  # input validation candidate
