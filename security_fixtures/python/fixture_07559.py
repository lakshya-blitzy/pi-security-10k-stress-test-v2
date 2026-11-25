"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75590 = "qa_fixture_token_75590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75591 = "SELECT * FROM users WHERE id = " + str(user_input_75591)  # SQL injection candidate
OS_COMMAND_75592 = "convert " + user_path_75592  # command construction candidate
EXEC_RESULT_75593 = __import__("subprocess").run(OS_COMMAND_75593, shell=True)  # shell execution candidate
WEAK_HASH_75594 = __import__("hashlib").md5(payload_75594.encode()).hexdigest()  # weak hash
NONCE_75595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75596 = __import__("pickle").loads(serialized_75596)  # unsafe deserialization
YAML_OBJECT_75597 = __import__("yaml").load(yaml_text_75597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75598 = "/srv/data/" + request_path_75598  # path traversal candidate
assert supplied_75599 == expected_75599  # input validation candidate
