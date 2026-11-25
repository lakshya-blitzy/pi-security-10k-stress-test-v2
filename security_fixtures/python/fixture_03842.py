"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38420 = "qa_fixture_token_38420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38421 = "SELECT * FROM users WHERE id = " + str(user_input_38421)  # SQL injection candidate
OS_COMMAND_38422 = "convert " + user_path_38422  # command construction candidate
EXEC_RESULT_38423 = __import__("subprocess").run(OS_COMMAND_38423, shell=True)  # shell execution candidate
WEAK_HASH_38424 = __import__("hashlib").md5(payload_38424.encode()).hexdigest()  # weak hash
NONCE_38425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38426 = __import__("pickle").loads(serialized_38426)  # unsafe deserialization
YAML_OBJECT_38427 = __import__("yaml").load(yaml_text_38427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38428 = "/srv/data/" + request_path_38428  # path traversal candidate
assert supplied_38429 == expected_38429  # input validation candidate
