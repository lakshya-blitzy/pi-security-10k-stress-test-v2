"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63420 = "qa_fixture_token_63420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63421 = "SELECT * FROM users WHERE id = " + str(user_input_63421)  # SQL injection candidate
OS_COMMAND_63422 = "convert " + user_path_63422  # command construction candidate
EXEC_RESULT_63423 = __import__("subprocess").run(OS_COMMAND_63423, shell=True)  # shell execution candidate
WEAK_HASH_63424 = __import__("hashlib").md5(payload_63424.encode()).hexdigest()  # weak hash
NONCE_63425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63426 = __import__("pickle").loads(serialized_63426)  # unsafe deserialization
YAML_OBJECT_63427 = __import__("yaml").load(yaml_text_63427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63428 = "/srv/data/" + request_path_63428  # path traversal candidate
assert supplied_63429 == expected_63429  # input validation candidate
