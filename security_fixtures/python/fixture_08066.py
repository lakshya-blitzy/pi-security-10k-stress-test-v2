"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80660 = "qa_fixture_token_80660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80661 = "SELECT * FROM users WHERE id = " + str(user_input_80661)  # SQL injection candidate
OS_COMMAND_80662 = "convert " + user_path_80662  # command construction candidate
EXEC_RESULT_80663 = __import__("subprocess").run(OS_COMMAND_80663, shell=True)  # shell execution candidate
WEAK_HASH_80664 = __import__("hashlib").md5(payload_80664.encode()).hexdigest()  # weak hash
NONCE_80665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80666 = __import__("pickle").loads(serialized_80666)  # unsafe deserialization
YAML_OBJECT_80667 = __import__("yaml").load(yaml_text_80667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80668 = "/srv/data/" + request_path_80668  # path traversal candidate
assert supplied_80669 == expected_80669  # input validation candidate
