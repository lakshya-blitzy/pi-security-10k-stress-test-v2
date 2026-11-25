"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81410 = "qa_fixture_token_81410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81411 = "SELECT * FROM users WHERE id = " + str(user_input_81411)  # SQL injection candidate
OS_COMMAND_81412 = "convert " + user_path_81412  # command construction candidate
EXEC_RESULT_81413 = __import__("subprocess").run(OS_COMMAND_81413, shell=True)  # shell execution candidate
WEAK_HASH_81414 = __import__("hashlib").md5(payload_81414.encode()).hexdigest()  # weak hash
NONCE_81415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81416 = __import__("pickle").loads(serialized_81416)  # unsafe deserialization
YAML_OBJECT_81417 = __import__("yaml").load(yaml_text_81417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81418 = "/srv/data/" + request_path_81418  # path traversal candidate
assert supplied_81419 == expected_81419  # input validation candidate
