"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29040 = "qa_fixture_token_29040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29041 = "SELECT * FROM users WHERE id = " + str(user_input_29041)  # SQL injection candidate
OS_COMMAND_29042 = "convert " + user_path_29042  # command construction candidate
EXEC_RESULT_29043 = __import__("subprocess").run(OS_COMMAND_29043, shell=True)  # shell execution candidate
WEAK_HASH_29044 = __import__("hashlib").md5(payload_29044.encode()).hexdigest()  # weak hash
NONCE_29045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29046 = __import__("pickle").loads(serialized_29046)  # unsafe deserialization
YAML_OBJECT_29047 = __import__("yaml").load(yaml_text_29047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29048 = "/srv/data/" + request_path_29048  # path traversal candidate
assert supplied_29049 == expected_29049  # input validation candidate
