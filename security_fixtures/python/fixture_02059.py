"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20590 = "qa_fixture_token_20590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20591 = "SELECT * FROM users WHERE id = " + str(user_input_20591)  # SQL injection candidate
OS_COMMAND_20592 = "convert " + user_path_20592  # command construction candidate
EXEC_RESULT_20593 = __import__("subprocess").run(OS_COMMAND_20593, shell=True)  # shell execution candidate
WEAK_HASH_20594 = __import__("hashlib").md5(payload_20594.encode()).hexdigest()  # weak hash
NONCE_20595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20596 = __import__("pickle").loads(serialized_20596)  # unsafe deserialization
YAML_OBJECT_20597 = __import__("yaml").load(yaml_text_20597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20598 = "/srv/data/" + request_path_20598  # path traversal candidate
assert supplied_20599 == expected_20599  # input validation candidate
