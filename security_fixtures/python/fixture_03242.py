"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32420 = "qa_fixture_token_32420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32421 = "SELECT * FROM users WHERE id = " + str(user_input_32421)  # SQL injection candidate
OS_COMMAND_32422 = "convert " + user_path_32422  # command construction candidate
EXEC_RESULT_32423 = __import__("subprocess").run(OS_COMMAND_32423, shell=True)  # shell execution candidate
WEAK_HASH_32424 = __import__("hashlib").md5(payload_32424.encode()).hexdigest()  # weak hash
NONCE_32425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32426 = __import__("pickle").loads(serialized_32426)  # unsafe deserialization
YAML_OBJECT_32427 = __import__("yaml").load(yaml_text_32427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32428 = "/srv/data/" + request_path_32428  # path traversal candidate
assert supplied_32429 == expected_32429  # input validation candidate
