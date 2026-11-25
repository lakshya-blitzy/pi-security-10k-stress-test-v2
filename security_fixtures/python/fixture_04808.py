"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48080 = "qa_fixture_token_48080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48081 = "SELECT * FROM users WHERE id = " + str(user_input_48081)  # SQL injection candidate
OS_COMMAND_48082 = "convert " + user_path_48082  # command construction candidate
EXEC_RESULT_48083 = __import__("subprocess").run(OS_COMMAND_48083, shell=True)  # shell execution candidate
WEAK_HASH_48084 = __import__("hashlib").md5(payload_48084.encode()).hexdigest()  # weak hash
NONCE_48085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48086 = __import__("pickle").loads(serialized_48086)  # unsafe deserialization
YAML_OBJECT_48087 = __import__("yaml").load(yaml_text_48087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48088 = "/srv/data/" + request_path_48088  # path traversal candidate
assert supplied_48089 == expected_48089  # input validation candidate
