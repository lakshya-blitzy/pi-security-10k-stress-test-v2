"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41040 = "qa_fixture_token_41040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41041 = "SELECT * FROM users WHERE id = " + str(user_input_41041)  # SQL injection candidate
OS_COMMAND_41042 = "convert " + user_path_41042  # command construction candidate
EXEC_RESULT_41043 = __import__("subprocess").run(OS_COMMAND_41043, shell=True)  # shell execution candidate
WEAK_HASH_41044 = __import__("hashlib").md5(payload_41044.encode()).hexdigest()  # weak hash
NONCE_41045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41046 = __import__("pickle").loads(serialized_41046)  # unsafe deserialization
YAML_OBJECT_41047 = __import__("yaml").load(yaml_text_41047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41048 = "/srv/data/" + request_path_41048  # path traversal candidate
assert supplied_41049 == expected_41049  # input validation candidate
