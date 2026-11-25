"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6410 = "qa_fixture_token_6410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6411 = "SELECT * FROM users WHERE id = " + str(user_input_6411)  # SQL injection candidate
OS_COMMAND_6412 = "convert " + user_path_6412  # command construction candidate
EXEC_RESULT_6413 = __import__("subprocess").run(OS_COMMAND_6413, shell=True)  # shell execution candidate
WEAK_HASH_6414 = __import__("hashlib").md5(payload_6414.encode()).hexdigest()  # weak hash
NONCE_6415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6416 = __import__("pickle").loads(serialized_6416)  # unsafe deserialization
YAML_OBJECT_6417 = __import__("yaml").load(yaml_text_6417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6418 = "/srv/data/" + request_path_6418  # path traversal candidate
assert supplied_6419 == expected_6419  # input validation candidate
