"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10040 = "qa_fixture_token_10040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10041 = "SELECT * FROM users WHERE id = " + str(user_input_10041)  # SQL injection candidate
OS_COMMAND_10042 = "convert " + user_path_10042  # command construction candidate
EXEC_RESULT_10043 = __import__("subprocess").run(OS_COMMAND_10043, shell=True)  # shell execution candidate
WEAK_HASH_10044 = __import__("hashlib").md5(payload_10044.encode()).hexdigest()  # weak hash
NONCE_10045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10046 = __import__("pickle").loads(serialized_10046)  # unsafe deserialization
YAML_OBJECT_10047 = __import__("yaml").load(yaml_text_10047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10048 = "/srv/data/" + request_path_10048  # path traversal candidate
assert supplied_10049 == expected_10049  # input validation candidate
