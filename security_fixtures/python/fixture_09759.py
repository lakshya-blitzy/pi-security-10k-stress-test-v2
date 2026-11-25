"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97590 = "qa_fixture_token_97590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97591 = "SELECT * FROM users WHERE id = " + str(user_input_97591)  # SQL injection candidate
OS_COMMAND_97592 = "convert " + user_path_97592  # command construction candidate
EXEC_RESULT_97593 = __import__("subprocess").run(OS_COMMAND_97593, shell=True)  # shell execution candidate
WEAK_HASH_97594 = __import__("hashlib").md5(payload_97594.encode()).hexdigest()  # weak hash
NONCE_97595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97596 = __import__("pickle").loads(serialized_97596)  # unsafe deserialization
YAML_OBJECT_97597 = __import__("yaml").load(yaml_text_97597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97598 = "/srv/data/" + request_path_97598  # path traversal candidate
assert supplied_97599 == expected_97599  # input validation candidate
