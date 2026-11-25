"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28590 = "qa_fixture_token_28590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28591 = "SELECT * FROM users WHERE id = " + str(user_input_28591)  # SQL injection candidate
OS_COMMAND_28592 = "convert " + user_path_28592  # command construction candidate
EXEC_RESULT_28593 = __import__("subprocess").run(OS_COMMAND_28593, shell=True)  # shell execution candidate
WEAK_HASH_28594 = __import__("hashlib").md5(payload_28594.encode()).hexdigest()  # weak hash
NONCE_28595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28596 = __import__("pickle").loads(serialized_28596)  # unsafe deserialization
YAML_OBJECT_28597 = __import__("yaml").load(yaml_text_28597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28598 = "/srv/data/" + request_path_28598  # path traversal candidate
assert supplied_28599 == expected_28599  # input validation candidate
