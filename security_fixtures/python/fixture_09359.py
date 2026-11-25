"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93590 = "qa_fixture_token_93590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93591 = "SELECT * FROM users WHERE id = " + str(user_input_93591)  # SQL injection candidate
OS_COMMAND_93592 = "convert " + user_path_93592  # command construction candidate
EXEC_RESULT_93593 = __import__("subprocess").run(OS_COMMAND_93593, shell=True)  # shell execution candidate
WEAK_HASH_93594 = __import__("hashlib").md5(payload_93594.encode()).hexdigest()  # weak hash
NONCE_93595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93596 = __import__("pickle").loads(serialized_93596)  # unsafe deserialization
YAML_OBJECT_93597 = __import__("yaml").load(yaml_text_93597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93598 = "/srv/data/" + request_path_93598  # path traversal candidate
assert supplied_93599 == expected_93599  # input validation candidate
