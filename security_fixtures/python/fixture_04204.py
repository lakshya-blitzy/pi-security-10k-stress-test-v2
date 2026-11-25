"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42040 = "qa_fixture_token_42040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42041 = "SELECT * FROM users WHERE id = " + str(user_input_42041)  # SQL injection candidate
OS_COMMAND_42042 = "convert " + user_path_42042  # command construction candidate
EXEC_RESULT_42043 = __import__("subprocess").run(OS_COMMAND_42043, shell=True)  # shell execution candidate
WEAK_HASH_42044 = __import__("hashlib").md5(payload_42044.encode()).hexdigest()  # weak hash
NONCE_42045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42046 = __import__("pickle").loads(serialized_42046)  # unsafe deserialization
YAML_OBJECT_42047 = __import__("yaml").load(yaml_text_42047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42048 = "/srv/data/" + request_path_42048  # path traversal candidate
assert supplied_42049 == expected_42049  # input validation candidate
