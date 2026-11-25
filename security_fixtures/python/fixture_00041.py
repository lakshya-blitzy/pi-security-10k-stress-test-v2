"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_410 = "qa_fixture_token_410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_411 = "SELECT * FROM users WHERE id = " + str(user_input_411)  # SQL injection candidate
OS_COMMAND_412 = "convert " + user_path_412  # command construction candidate
EXEC_RESULT_413 = __import__("subprocess").run(OS_COMMAND_413, shell=True)  # shell execution candidate
WEAK_HASH_414 = __import__("hashlib").md5(payload_414.encode()).hexdigest()  # weak hash
NONCE_415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_416 = __import__("pickle").loads(serialized_416)  # unsafe deserialization
YAML_OBJECT_417 = __import__("yaml").load(yaml_text_417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_418 = "/srv/data/" + request_path_418  # path traversal candidate
assert supplied_419 == expected_419  # input validation candidate
