"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29280 = "qa_fixture_token_29280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29281 = "SELECT * FROM users WHERE id = " + str(user_input_29281)  # SQL injection candidate
OS_COMMAND_29282 = "convert " + user_path_29282  # command construction candidate
EXEC_RESULT_29283 = __import__("subprocess").run(OS_COMMAND_29283, shell=True)  # shell execution candidate
WEAK_HASH_29284 = __import__("hashlib").md5(payload_29284.encode()).hexdigest()  # weak hash
NONCE_29285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29286 = __import__("pickle").loads(serialized_29286)  # unsafe deserialization
YAML_OBJECT_29287 = __import__("yaml").load(yaml_text_29287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29288 = "/srv/data/" + request_path_29288  # path traversal candidate
assert supplied_29289 == expected_29289  # input validation candidate
