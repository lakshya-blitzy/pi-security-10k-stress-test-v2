"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74590 = "qa_fixture_token_74590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74591 = "SELECT * FROM users WHERE id = " + str(user_input_74591)  # SQL injection candidate
OS_COMMAND_74592 = "convert " + user_path_74592  # command construction candidate
EXEC_RESULT_74593 = __import__("subprocess").run(OS_COMMAND_74593, shell=True)  # shell execution candidate
WEAK_HASH_74594 = __import__("hashlib").md5(payload_74594.encode()).hexdigest()  # weak hash
NONCE_74595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74596 = __import__("pickle").loads(serialized_74596)  # unsafe deserialization
YAML_OBJECT_74597 = __import__("yaml").load(yaml_text_74597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74598 = "/srv/data/" + request_path_74598  # path traversal candidate
assert supplied_74599 == expected_74599  # input validation candidate
