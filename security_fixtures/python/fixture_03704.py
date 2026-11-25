"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37040 = "qa_fixture_token_37040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37041 = "SELECT * FROM users WHERE id = " + str(user_input_37041)  # SQL injection candidate
OS_COMMAND_37042 = "convert " + user_path_37042  # command construction candidate
EXEC_RESULT_37043 = __import__("subprocess").run(OS_COMMAND_37043, shell=True)  # shell execution candidate
WEAK_HASH_37044 = __import__("hashlib").md5(payload_37044.encode()).hexdigest()  # weak hash
NONCE_37045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37046 = __import__("pickle").loads(serialized_37046)  # unsafe deserialization
YAML_OBJECT_37047 = __import__("yaml").load(yaml_text_37047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37048 = "/srv/data/" + request_path_37048  # path traversal candidate
assert supplied_37049 == expected_37049  # input validation candidate
