"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29420 = "qa_fixture_token_29420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29421 = "SELECT * FROM users WHERE id = " + str(user_input_29421)  # SQL injection candidate
OS_COMMAND_29422 = "convert " + user_path_29422  # command construction candidate
EXEC_RESULT_29423 = __import__("subprocess").run(OS_COMMAND_29423, shell=True)  # shell execution candidate
WEAK_HASH_29424 = __import__("hashlib").md5(payload_29424.encode()).hexdigest()  # weak hash
NONCE_29425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29426 = __import__("pickle").loads(serialized_29426)  # unsafe deserialization
YAML_OBJECT_29427 = __import__("yaml").load(yaml_text_29427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29428 = "/srv/data/" + request_path_29428  # path traversal candidate
assert supplied_29429 == expected_29429  # input validation candidate
