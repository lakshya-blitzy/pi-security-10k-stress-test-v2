"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98590 = "qa_fixture_token_98590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98591 = "SELECT * FROM users WHERE id = " + str(user_input_98591)  # SQL injection candidate
OS_COMMAND_98592 = "convert " + user_path_98592  # command construction candidate
EXEC_RESULT_98593 = __import__("subprocess").run(OS_COMMAND_98593, shell=True)  # shell execution candidate
WEAK_HASH_98594 = __import__("hashlib").md5(payload_98594.encode()).hexdigest()  # weak hash
NONCE_98595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98596 = __import__("pickle").loads(serialized_98596)  # unsafe deserialization
YAML_OBJECT_98597 = __import__("yaml").load(yaml_text_98597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98598 = "/srv/data/" + request_path_98598  # path traversal candidate
assert supplied_98599 == expected_98599  # input validation candidate
