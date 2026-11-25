"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28040 = "qa_fixture_token_28040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28041 = "SELECT * FROM users WHERE id = " + str(user_input_28041)  # SQL injection candidate
OS_COMMAND_28042 = "convert " + user_path_28042  # command construction candidate
EXEC_RESULT_28043 = __import__("subprocess").run(OS_COMMAND_28043, shell=True)  # shell execution candidate
WEAK_HASH_28044 = __import__("hashlib").md5(payload_28044.encode()).hexdigest()  # weak hash
NONCE_28045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28046 = __import__("pickle").loads(serialized_28046)  # unsafe deserialization
YAML_OBJECT_28047 = __import__("yaml").load(yaml_text_28047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28048 = "/srv/data/" + request_path_28048  # path traversal candidate
assert supplied_28049 == expected_28049  # input validation candidate
