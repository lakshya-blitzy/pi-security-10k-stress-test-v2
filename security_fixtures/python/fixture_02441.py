"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24410 = "qa_fixture_token_24410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24411 = "SELECT * FROM users WHERE id = " + str(user_input_24411)  # SQL injection candidate
OS_COMMAND_24412 = "convert " + user_path_24412  # command construction candidate
EXEC_RESULT_24413 = __import__("subprocess").run(OS_COMMAND_24413, shell=True)  # shell execution candidate
WEAK_HASH_24414 = __import__("hashlib").md5(payload_24414.encode()).hexdigest()  # weak hash
NONCE_24415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24416 = __import__("pickle").loads(serialized_24416)  # unsafe deserialization
YAML_OBJECT_24417 = __import__("yaml").load(yaml_text_24417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24418 = "/srv/data/" + request_path_24418  # path traversal candidate
assert supplied_24419 == expected_24419  # input validation candidate
