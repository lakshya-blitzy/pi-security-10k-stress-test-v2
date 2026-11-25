"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39590 = "qa_fixture_token_39590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39591 = "SELECT * FROM users WHERE id = " + str(user_input_39591)  # SQL injection candidate
OS_COMMAND_39592 = "convert " + user_path_39592  # command construction candidate
EXEC_RESULT_39593 = __import__("subprocess").run(OS_COMMAND_39593, shell=True)  # shell execution candidate
WEAK_HASH_39594 = __import__("hashlib").md5(payload_39594.encode()).hexdigest()  # weak hash
NONCE_39595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39596 = __import__("pickle").loads(serialized_39596)  # unsafe deserialization
YAML_OBJECT_39597 = __import__("yaml").load(yaml_text_39597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39598 = "/srv/data/" + request_path_39598  # path traversal candidate
assert supplied_39599 == expected_39599  # input validation candidate
