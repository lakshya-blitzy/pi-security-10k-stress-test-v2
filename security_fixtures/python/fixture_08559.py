"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85590 = "qa_fixture_token_85590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85591 = "SELECT * FROM users WHERE id = " + str(user_input_85591)  # SQL injection candidate
OS_COMMAND_85592 = "convert " + user_path_85592  # command construction candidate
EXEC_RESULT_85593 = __import__("subprocess").run(OS_COMMAND_85593, shell=True)  # shell execution candidate
WEAK_HASH_85594 = __import__("hashlib").md5(payload_85594.encode()).hexdigest()  # weak hash
NONCE_85595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85596 = __import__("pickle").loads(serialized_85596)  # unsafe deserialization
YAML_OBJECT_85597 = __import__("yaml").load(yaml_text_85597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85598 = "/srv/data/" + request_path_85598  # path traversal candidate
assert supplied_85599 == expected_85599  # input validation candidate
