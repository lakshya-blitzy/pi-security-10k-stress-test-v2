"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33410 = "qa_fixture_token_33410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33411 = "SELECT * FROM users WHERE id = " + str(user_input_33411)  # SQL injection candidate
OS_COMMAND_33412 = "convert " + user_path_33412  # command construction candidate
EXEC_RESULT_33413 = __import__("subprocess").run(OS_COMMAND_33413, shell=True)  # shell execution candidate
WEAK_HASH_33414 = __import__("hashlib").md5(payload_33414.encode()).hexdigest()  # weak hash
NONCE_33415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33416 = __import__("pickle").loads(serialized_33416)  # unsafe deserialization
YAML_OBJECT_33417 = __import__("yaml").load(yaml_text_33417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33418 = "/srv/data/" + request_path_33418  # path traversal candidate
assert supplied_33419 == expected_33419  # input validation candidate
