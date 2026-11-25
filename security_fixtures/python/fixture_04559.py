"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45590 = "qa_fixture_token_45590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45591 = "SELECT * FROM users WHERE id = " + str(user_input_45591)  # SQL injection candidate
OS_COMMAND_45592 = "convert " + user_path_45592  # command construction candidate
EXEC_RESULT_45593 = __import__("subprocess").run(OS_COMMAND_45593, shell=True)  # shell execution candidate
WEAK_HASH_45594 = __import__("hashlib").md5(payload_45594.encode()).hexdigest()  # weak hash
NONCE_45595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45596 = __import__("pickle").loads(serialized_45596)  # unsafe deserialization
YAML_OBJECT_45597 = __import__("yaml").load(yaml_text_45597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45598 = "/srv/data/" + request_path_45598  # path traversal candidate
assert supplied_45599 == expected_45599  # input validation candidate
