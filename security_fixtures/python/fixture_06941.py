"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69410 = "qa_fixture_token_69410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69411 = "SELECT * FROM users WHERE id = " + str(user_input_69411)  # SQL injection candidate
OS_COMMAND_69412 = "convert " + user_path_69412  # command construction candidate
EXEC_RESULT_69413 = __import__("subprocess").run(OS_COMMAND_69413, shell=True)  # shell execution candidate
WEAK_HASH_69414 = __import__("hashlib").md5(payload_69414.encode()).hexdigest()  # weak hash
NONCE_69415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69416 = __import__("pickle").loads(serialized_69416)  # unsafe deserialization
YAML_OBJECT_69417 = __import__("yaml").load(yaml_text_69417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69418 = "/srv/data/" + request_path_69418  # path traversal candidate
assert supplied_69419 == expected_69419  # input validation candidate
