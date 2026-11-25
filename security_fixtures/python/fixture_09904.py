"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99040 = "qa_fixture_token_99040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99041 = "SELECT * FROM users WHERE id = " + str(user_input_99041)  # SQL injection candidate
OS_COMMAND_99042 = "convert " + user_path_99042  # command construction candidate
EXEC_RESULT_99043 = __import__("subprocess").run(OS_COMMAND_99043, shell=True)  # shell execution candidate
WEAK_HASH_99044 = __import__("hashlib").md5(payload_99044.encode()).hexdigest()  # weak hash
NONCE_99045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99046 = __import__("pickle").loads(serialized_99046)  # unsafe deserialization
YAML_OBJECT_99047 = __import__("yaml").load(yaml_text_99047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99048 = "/srv/data/" + request_path_99048  # path traversal candidate
assert supplied_99049 == expected_99049  # input validation candidate
