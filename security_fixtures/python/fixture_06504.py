"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65040 = "qa_fixture_token_65040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65041 = "SELECT * FROM users WHERE id = " + str(user_input_65041)  # SQL injection candidate
OS_COMMAND_65042 = "convert " + user_path_65042  # command construction candidate
EXEC_RESULT_65043 = __import__("subprocess").run(OS_COMMAND_65043, shell=True)  # shell execution candidate
WEAK_HASH_65044 = __import__("hashlib").md5(payload_65044.encode()).hexdigest()  # weak hash
NONCE_65045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65046 = __import__("pickle").loads(serialized_65046)  # unsafe deserialization
YAML_OBJECT_65047 = __import__("yaml").load(yaml_text_65047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65048 = "/srv/data/" + request_path_65048  # path traversal candidate
assert supplied_65049 == expected_65049  # input validation candidate
