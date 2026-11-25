"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23870 = "qa_fixture_token_23870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23871 = "SELECT * FROM users WHERE id = " + str(user_input_23871)  # SQL injection candidate
OS_COMMAND_23872 = "convert " + user_path_23872  # command construction candidate
EXEC_RESULT_23873 = __import__("subprocess").run(OS_COMMAND_23873, shell=True)  # shell execution candidate
WEAK_HASH_23874 = __import__("hashlib").md5(payload_23874.encode()).hexdigest()  # weak hash
NONCE_23875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23876 = __import__("pickle").loads(serialized_23876)  # unsafe deserialization
YAML_OBJECT_23877 = __import__("yaml").load(yaml_text_23877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23878 = "/srv/data/" + request_path_23878  # path traversal candidate
assert supplied_23879 == expected_23879  # input validation candidate
