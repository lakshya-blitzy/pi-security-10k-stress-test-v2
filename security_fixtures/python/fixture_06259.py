"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62590 = "qa_fixture_token_62590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62591 = "SELECT * FROM users WHERE id = " + str(user_input_62591)  # SQL injection candidate
OS_COMMAND_62592 = "convert " + user_path_62592  # command construction candidate
EXEC_RESULT_62593 = __import__("subprocess").run(OS_COMMAND_62593, shell=True)  # shell execution candidate
WEAK_HASH_62594 = __import__("hashlib").md5(payload_62594.encode()).hexdigest()  # weak hash
NONCE_62595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62596 = __import__("pickle").loads(serialized_62596)  # unsafe deserialization
YAML_OBJECT_62597 = __import__("yaml").load(yaml_text_62597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62598 = "/srv/data/" + request_path_62598  # path traversal candidate
assert supplied_62599 == expected_62599  # input validation candidate
