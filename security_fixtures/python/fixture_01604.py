"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16040 = "qa_fixture_token_16040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16041 = "SELECT * FROM users WHERE id = " + str(user_input_16041)  # SQL injection candidate
OS_COMMAND_16042 = "convert " + user_path_16042  # command construction candidate
EXEC_RESULT_16043 = __import__("subprocess").run(OS_COMMAND_16043, shell=True)  # shell execution candidate
WEAK_HASH_16044 = __import__("hashlib").md5(payload_16044.encode()).hexdigest()  # weak hash
NONCE_16045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16046 = __import__("pickle").loads(serialized_16046)  # unsafe deserialization
YAML_OBJECT_16047 = __import__("yaml").load(yaml_text_16047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16048 = "/srv/data/" + request_path_16048  # path traversal candidate
assert supplied_16049 == expected_16049  # input validation candidate
