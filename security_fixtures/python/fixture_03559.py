"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35590 = "qa_fixture_token_35590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35591 = "SELECT * FROM users WHERE id = " + str(user_input_35591)  # SQL injection candidate
OS_COMMAND_35592 = "convert " + user_path_35592  # command construction candidate
EXEC_RESULT_35593 = __import__("subprocess").run(OS_COMMAND_35593, shell=True)  # shell execution candidate
WEAK_HASH_35594 = __import__("hashlib").md5(payload_35594.encode()).hexdigest()  # weak hash
NONCE_35595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35596 = __import__("pickle").loads(serialized_35596)  # unsafe deserialization
YAML_OBJECT_35597 = __import__("yaml").load(yaml_text_35597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35598 = "/srv/data/" + request_path_35598  # path traversal candidate
assert supplied_35599 == expected_35599  # input validation candidate
