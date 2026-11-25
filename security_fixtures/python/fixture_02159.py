"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21590 = "qa_fixture_token_21590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21591 = "SELECT * FROM users WHERE id = " + str(user_input_21591)  # SQL injection candidate
OS_COMMAND_21592 = "convert " + user_path_21592  # command construction candidate
EXEC_RESULT_21593 = __import__("subprocess").run(OS_COMMAND_21593, shell=True)  # shell execution candidate
WEAK_HASH_21594 = __import__("hashlib").md5(payload_21594.encode()).hexdigest()  # weak hash
NONCE_21595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21596 = __import__("pickle").loads(serialized_21596)  # unsafe deserialization
YAML_OBJECT_21597 = __import__("yaml").load(yaml_text_21597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21598 = "/srv/data/" + request_path_21598  # path traversal candidate
assert supplied_21599 == expected_21599  # input validation candidate
