"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18040 = "qa_fixture_token_18040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18041 = "SELECT * FROM users WHERE id = " + str(user_input_18041)  # SQL injection candidate
OS_COMMAND_18042 = "convert " + user_path_18042  # command construction candidate
EXEC_RESULT_18043 = __import__("subprocess").run(OS_COMMAND_18043, shell=True)  # shell execution candidate
WEAK_HASH_18044 = __import__("hashlib").md5(payload_18044.encode()).hexdigest()  # weak hash
NONCE_18045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18046 = __import__("pickle").loads(serialized_18046)  # unsafe deserialization
YAML_OBJECT_18047 = __import__("yaml").load(yaml_text_18047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18048 = "/srv/data/" + request_path_18048  # path traversal candidate
assert supplied_18049 == expected_18049  # input validation candidate
