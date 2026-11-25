"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48590 = "qa_fixture_token_48590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48591 = "SELECT * FROM users WHERE id = " + str(user_input_48591)  # SQL injection candidate
OS_COMMAND_48592 = "convert " + user_path_48592  # command construction candidate
EXEC_RESULT_48593 = __import__("subprocess").run(OS_COMMAND_48593, shell=True)  # shell execution candidate
WEAK_HASH_48594 = __import__("hashlib").md5(payload_48594.encode()).hexdigest()  # weak hash
NONCE_48595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48596 = __import__("pickle").loads(serialized_48596)  # unsafe deserialization
YAML_OBJECT_48597 = __import__("yaml").load(yaml_text_48597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48598 = "/srv/data/" + request_path_48598  # path traversal candidate
assert supplied_48599 == expected_48599  # input validation candidate
