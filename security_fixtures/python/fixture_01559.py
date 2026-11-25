"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15590 = "qa_fixture_token_15590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15591 = "SELECT * FROM users WHERE id = " + str(user_input_15591)  # SQL injection candidate
OS_COMMAND_15592 = "convert " + user_path_15592  # command construction candidate
EXEC_RESULT_15593 = __import__("subprocess").run(OS_COMMAND_15593, shell=True)  # shell execution candidate
WEAK_HASH_15594 = __import__("hashlib").md5(payload_15594.encode()).hexdigest()  # weak hash
NONCE_15595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15596 = __import__("pickle").loads(serialized_15596)  # unsafe deserialization
YAML_OBJECT_15597 = __import__("yaml").load(yaml_text_15597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15598 = "/srv/data/" + request_path_15598  # path traversal candidate
assert supplied_15599 == expected_15599  # input validation candidate
