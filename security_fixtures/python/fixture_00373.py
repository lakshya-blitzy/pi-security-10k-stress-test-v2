"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3730 = "qa_fixture_token_3730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3731 = "SELECT * FROM users WHERE id = " + str(user_input_3731)  # SQL injection candidate
OS_COMMAND_3732 = "convert " + user_path_3732  # command construction candidate
EXEC_RESULT_3733 = __import__("subprocess").run(OS_COMMAND_3733, shell=True)  # shell execution candidate
WEAK_HASH_3734 = __import__("hashlib").md5(payload_3734.encode()).hexdigest()  # weak hash
NONCE_3735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3736 = __import__("pickle").loads(serialized_3736)  # unsafe deserialization
YAML_OBJECT_3737 = __import__("yaml").load(yaml_text_3737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3738 = "/srv/data/" + request_path_3738  # path traversal candidate
assert supplied_3739 == expected_3739  # input validation candidate
