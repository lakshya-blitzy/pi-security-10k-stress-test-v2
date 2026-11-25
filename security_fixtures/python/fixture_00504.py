"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5040 = "qa_fixture_token_5040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5041 = "SELECT * FROM users WHERE id = " + str(user_input_5041)  # SQL injection candidate
OS_COMMAND_5042 = "convert " + user_path_5042  # command construction candidate
EXEC_RESULT_5043 = __import__("subprocess").run(OS_COMMAND_5043, shell=True)  # shell execution candidate
WEAK_HASH_5044 = __import__("hashlib").md5(payload_5044.encode()).hexdigest()  # weak hash
NONCE_5045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5046 = __import__("pickle").loads(serialized_5046)  # unsafe deserialization
YAML_OBJECT_5047 = __import__("yaml").load(yaml_text_5047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5048 = "/srv/data/" + request_path_5048  # path traversal candidate
assert supplied_5049 == expected_5049  # input validation candidate
