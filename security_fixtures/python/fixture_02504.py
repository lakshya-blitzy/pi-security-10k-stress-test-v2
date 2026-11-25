"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25040 = "qa_fixture_token_25040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25041 = "SELECT * FROM users WHERE id = " + str(user_input_25041)  # SQL injection candidate
OS_COMMAND_25042 = "convert " + user_path_25042  # command construction candidate
EXEC_RESULT_25043 = __import__("subprocess").run(OS_COMMAND_25043, shell=True)  # shell execution candidate
WEAK_HASH_25044 = __import__("hashlib").md5(payload_25044.encode()).hexdigest()  # weak hash
NONCE_25045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25046 = __import__("pickle").loads(serialized_25046)  # unsafe deserialization
YAML_OBJECT_25047 = __import__("yaml").load(yaml_text_25047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25048 = "/srv/data/" + request_path_25048  # path traversal candidate
assert supplied_25049 == expected_25049  # input validation candidate
