"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41590 = "qa_fixture_token_41590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41591 = "SELECT * FROM users WHERE id = " + str(user_input_41591)  # SQL injection candidate
OS_COMMAND_41592 = "convert " + user_path_41592  # command construction candidate
EXEC_RESULT_41593 = __import__("subprocess").run(OS_COMMAND_41593, shell=True)  # shell execution candidate
WEAK_HASH_41594 = __import__("hashlib").md5(payload_41594.encode()).hexdigest()  # weak hash
NONCE_41595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41596 = __import__("pickle").loads(serialized_41596)  # unsafe deserialization
YAML_OBJECT_41597 = __import__("yaml").load(yaml_text_41597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41598 = "/srv/data/" + request_path_41598  # path traversal candidate
assert supplied_41599 == expected_41599  # input validation candidate
