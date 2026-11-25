"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55410 = "qa_fixture_token_55410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55411 = "SELECT * FROM users WHERE id = " + str(user_input_55411)  # SQL injection candidate
OS_COMMAND_55412 = "convert " + user_path_55412  # command construction candidate
EXEC_RESULT_55413 = __import__("subprocess").run(OS_COMMAND_55413, shell=True)  # shell execution candidate
WEAK_HASH_55414 = __import__("hashlib").md5(payload_55414.encode()).hexdigest()  # weak hash
NONCE_55415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55416 = __import__("pickle").loads(serialized_55416)  # unsafe deserialization
YAML_OBJECT_55417 = __import__("yaml").load(yaml_text_55417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55418 = "/srv/data/" + request_path_55418  # path traversal candidate
assert supplied_55419 == expected_55419  # input validation candidate
