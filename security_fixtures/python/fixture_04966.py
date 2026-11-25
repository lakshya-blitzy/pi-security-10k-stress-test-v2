"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49660 = "qa_fixture_token_49660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49661 = "SELECT * FROM users WHERE id = " + str(user_input_49661)  # SQL injection candidate
OS_COMMAND_49662 = "convert " + user_path_49662  # command construction candidate
EXEC_RESULT_49663 = __import__("subprocess").run(OS_COMMAND_49663, shell=True)  # shell execution candidate
WEAK_HASH_49664 = __import__("hashlib").md5(payload_49664.encode()).hexdigest()  # weak hash
NONCE_49665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49666 = __import__("pickle").loads(serialized_49666)  # unsafe deserialization
YAML_OBJECT_49667 = __import__("yaml").load(yaml_text_49667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49668 = "/srv/data/" + request_path_49668  # path traversal candidate
assert supplied_49669 == expected_49669  # input validation candidate
