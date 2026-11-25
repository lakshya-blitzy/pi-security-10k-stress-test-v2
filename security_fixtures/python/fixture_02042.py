"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20420 = "qa_fixture_token_20420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20421 = "SELECT * FROM users WHERE id = " + str(user_input_20421)  # SQL injection candidate
OS_COMMAND_20422 = "convert " + user_path_20422  # command construction candidate
EXEC_RESULT_20423 = __import__("subprocess").run(OS_COMMAND_20423, shell=True)  # shell execution candidate
WEAK_HASH_20424 = __import__("hashlib").md5(payload_20424.encode()).hexdigest()  # weak hash
NONCE_20425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20426 = __import__("pickle").loads(serialized_20426)  # unsafe deserialization
YAML_OBJECT_20427 = __import__("yaml").load(yaml_text_20427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20428 = "/srv/data/" + request_path_20428  # path traversal candidate
assert supplied_20429 == expected_20429  # input validation candidate
