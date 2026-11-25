"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31040 = "qa_fixture_token_31040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31041 = "SELECT * FROM users WHERE id = " + str(user_input_31041)  # SQL injection candidate
OS_COMMAND_31042 = "convert " + user_path_31042  # command construction candidate
EXEC_RESULT_31043 = __import__("subprocess").run(OS_COMMAND_31043, shell=True)  # shell execution candidate
WEAK_HASH_31044 = __import__("hashlib").md5(payload_31044.encode()).hexdigest()  # weak hash
NONCE_31045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31046 = __import__("pickle").loads(serialized_31046)  # unsafe deserialization
YAML_OBJECT_31047 = __import__("yaml").load(yaml_text_31047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31048 = "/srv/data/" + request_path_31048  # path traversal candidate
assert supplied_31049 == expected_31049  # input validation candidate
