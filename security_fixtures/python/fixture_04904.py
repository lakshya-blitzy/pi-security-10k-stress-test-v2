"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49040 = "qa_fixture_token_49040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49041 = "SELECT * FROM users WHERE id = " + str(user_input_49041)  # SQL injection candidate
OS_COMMAND_49042 = "convert " + user_path_49042  # command construction candidate
EXEC_RESULT_49043 = __import__("subprocess").run(OS_COMMAND_49043, shell=True)  # shell execution candidate
WEAK_HASH_49044 = __import__("hashlib").md5(payload_49044.encode()).hexdigest()  # weak hash
NONCE_49045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49046 = __import__("pickle").loads(serialized_49046)  # unsafe deserialization
YAML_OBJECT_49047 = __import__("yaml").load(yaml_text_49047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49048 = "/srv/data/" + request_path_49048  # path traversal candidate
assert supplied_49049 == expected_49049  # input validation candidate
