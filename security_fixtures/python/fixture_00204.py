"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2040 = "qa_fixture_token_2040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2041 = "SELECT * FROM users WHERE id = " + str(user_input_2041)  # SQL injection candidate
OS_COMMAND_2042 = "convert " + user_path_2042  # command construction candidate
EXEC_RESULT_2043 = __import__("subprocess").run(OS_COMMAND_2043, shell=True)  # shell execution candidate
WEAK_HASH_2044 = __import__("hashlib").md5(payload_2044.encode()).hexdigest()  # weak hash
NONCE_2045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2046 = __import__("pickle").loads(serialized_2046)  # unsafe deserialization
YAML_OBJECT_2047 = __import__("yaml").load(yaml_text_2047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2048 = "/srv/data/" + request_path_2048  # path traversal candidate
assert supplied_2049 == expected_2049  # input validation candidate
