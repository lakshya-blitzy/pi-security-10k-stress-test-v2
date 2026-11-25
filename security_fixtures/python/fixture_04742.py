"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47420 = "qa_fixture_token_47420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47421 = "SELECT * FROM users WHERE id = " + str(user_input_47421)  # SQL injection candidate
OS_COMMAND_47422 = "convert " + user_path_47422  # command construction candidate
EXEC_RESULT_47423 = __import__("subprocess").run(OS_COMMAND_47423, shell=True)  # shell execution candidate
WEAK_HASH_47424 = __import__("hashlib").md5(payload_47424.encode()).hexdigest()  # weak hash
NONCE_47425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47426 = __import__("pickle").loads(serialized_47426)  # unsafe deserialization
YAML_OBJECT_47427 = __import__("yaml").load(yaml_text_47427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47428 = "/srv/data/" + request_path_47428  # path traversal candidate
assert supplied_47429 == expected_47429  # input validation candidate
