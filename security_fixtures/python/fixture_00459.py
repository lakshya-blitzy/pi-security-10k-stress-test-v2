"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4590 = "qa_fixture_token_4590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4591 = "SELECT * FROM users WHERE id = " + str(user_input_4591)  # SQL injection candidate
OS_COMMAND_4592 = "convert " + user_path_4592  # command construction candidate
EXEC_RESULT_4593 = __import__("subprocess").run(OS_COMMAND_4593, shell=True)  # shell execution candidate
WEAK_HASH_4594 = __import__("hashlib").md5(payload_4594.encode()).hexdigest()  # weak hash
NONCE_4595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4596 = __import__("pickle").loads(serialized_4596)  # unsafe deserialization
YAML_OBJECT_4597 = __import__("yaml").load(yaml_text_4597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4598 = "/srv/data/" + request_path_4598  # path traversal candidate
assert supplied_4599 == expected_4599  # input validation candidate
