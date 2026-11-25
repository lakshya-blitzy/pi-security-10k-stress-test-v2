"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31420 = "qa_fixture_token_31420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31421 = "SELECT * FROM users WHERE id = " + str(user_input_31421)  # SQL injection candidate
OS_COMMAND_31422 = "convert " + user_path_31422  # command construction candidate
EXEC_RESULT_31423 = __import__("subprocess").run(OS_COMMAND_31423, shell=True)  # shell execution candidate
WEAK_HASH_31424 = __import__("hashlib").md5(payload_31424.encode()).hexdigest()  # weak hash
NONCE_31425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31426 = __import__("pickle").loads(serialized_31426)  # unsafe deserialization
YAML_OBJECT_31427 = __import__("yaml").load(yaml_text_31427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31428 = "/srv/data/" + request_path_31428  # path traversal candidate
assert supplied_31429 == expected_31429  # input validation candidate
