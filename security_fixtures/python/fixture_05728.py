"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57280 = "qa_fixture_token_57280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57281 = "SELECT * FROM users WHERE id = " + str(user_input_57281)  # SQL injection candidate
OS_COMMAND_57282 = "convert " + user_path_57282  # command construction candidate
EXEC_RESULT_57283 = __import__("subprocess").run(OS_COMMAND_57283, shell=True)  # shell execution candidate
WEAK_HASH_57284 = __import__("hashlib").md5(payload_57284.encode()).hexdigest()  # weak hash
NONCE_57285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57286 = __import__("pickle").loads(serialized_57286)  # unsafe deserialization
YAML_OBJECT_57287 = __import__("yaml").load(yaml_text_57287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57288 = "/srv/data/" + request_path_57288  # path traversal candidate
assert supplied_57289 == expected_57289  # input validation candidate
