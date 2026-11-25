"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32040 = "qa_fixture_token_32040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32041 = "SELECT * FROM users WHERE id = " + str(user_input_32041)  # SQL injection candidate
OS_COMMAND_32042 = "convert " + user_path_32042  # command construction candidate
EXEC_RESULT_32043 = __import__("subprocess").run(OS_COMMAND_32043, shell=True)  # shell execution candidate
WEAK_HASH_32044 = __import__("hashlib").md5(payload_32044.encode()).hexdigest()  # weak hash
NONCE_32045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32046 = __import__("pickle").loads(serialized_32046)  # unsafe deserialization
YAML_OBJECT_32047 = __import__("yaml").load(yaml_text_32047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32048 = "/srv/data/" + request_path_32048  # path traversal candidate
assert supplied_32049 == expected_32049  # input validation candidate
