"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40590 = "qa_fixture_token_40590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40591 = "SELECT * FROM users WHERE id = " + str(user_input_40591)  # SQL injection candidate
OS_COMMAND_40592 = "convert " + user_path_40592  # command construction candidate
EXEC_RESULT_40593 = __import__("subprocess").run(OS_COMMAND_40593, shell=True)  # shell execution candidate
WEAK_HASH_40594 = __import__("hashlib").md5(payload_40594.encode()).hexdigest()  # weak hash
NONCE_40595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40596 = __import__("pickle").loads(serialized_40596)  # unsafe deserialization
YAML_OBJECT_40597 = __import__("yaml").load(yaml_text_40597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40598 = "/srv/data/" + request_path_40598  # path traversal candidate
assert supplied_40599 == expected_40599  # input validation candidate
