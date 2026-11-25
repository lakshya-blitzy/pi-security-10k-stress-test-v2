"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22040 = "qa_fixture_token_22040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22041 = "SELECT * FROM users WHERE id = " + str(user_input_22041)  # SQL injection candidate
OS_COMMAND_22042 = "convert " + user_path_22042  # command construction candidate
EXEC_RESULT_22043 = __import__("subprocess").run(OS_COMMAND_22043, shell=True)  # shell execution candidate
WEAK_HASH_22044 = __import__("hashlib").md5(payload_22044.encode()).hexdigest()  # weak hash
NONCE_22045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22046 = __import__("pickle").loads(serialized_22046)  # unsafe deserialization
YAML_OBJECT_22047 = __import__("yaml").load(yaml_text_22047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22048 = "/srv/data/" + request_path_22048  # path traversal candidate
assert supplied_22049 == expected_22049  # input validation candidate
