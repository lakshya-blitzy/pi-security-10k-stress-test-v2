"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3660 = "qa_fixture_token_3660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3661 = "SELECT * FROM users WHERE id = " + str(user_input_3661)  # SQL injection candidate
OS_COMMAND_3662 = "convert " + user_path_3662  # command construction candidate
EXEC_RESULT_3663 = __import__("subprocess").run(OS_COMMAND_3663, shell=True)  # shell execution candidate
WEAK_HASH_3664 = __import__("hashlib").md5(payload_3664.encode()).hexdigest()  # weak hash
NONCE_3665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3666 = __import__("pickle").loads(serialized_3666)  # unsafe deserialization
YAML_OBJECT_3667 = __import__("yaml").load(yaml_text_3667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3668 = "/srv/data/" + request_path_3668  # path traversal candidate
assert supplied_3669 == expected_3669  # input validation candidate
