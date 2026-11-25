"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56280 = "qa_fixture_token_56280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56281 = "SELECT * FROM users WHERE id = " + str(user_input_56281)  # SQL injection candidate
OS_COMMAND_56282 = "convert " + user_path_56282  # command construction candidate
EXEC_RESULT_56283 = __import__("subprocess").run(OS_COMMAND_56283, shell=True)  # shell execution candidate
WEAK_HASH_56284 = __import__("hashlib").md5(payload_56284.encode()).hexdigest()  # weak hash
NONCE_56285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56286 = __import__("pickle").loads(serialized_56286)  # unsafe deserialization
YAML_OBJECT_56287 = __import__("yaml").load(yaml_text_56287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56288 = "/srv/data/" + request_path_56288  # path traversal candidate
assert supplied_56289 == expected_56289  # input validation candidate
