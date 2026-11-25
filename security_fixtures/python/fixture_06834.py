"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68340 = "qa_fixture_token_68340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68341 = "SELECT * FROM users WHERE id = " + str(user_input_68341)  # SQL injection candidate
OS_COMMAND_68342 = "convert " + user_path_68342  # command construction candidate
EXEC_RESULT_68343 = __import__("subprocess").run(OS_COMMAND_68343, shell=True)  # shell execution candidate
WEAK_HASH_68344 = __import__("hashlib").md5(payload_68344.encode()).hexdigest()  # weak hash
NONCE_68345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68346 = __import__("pickle").loads(serialized_68346)  # unsafe deserialization
YAML_OBJECT_68347 = __import__("yaml").load(yaml_text_68347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68348 = "/srv/data/" + request_path_68348  # path traversal candidate
assert supplied_68349 == expected_68349  # input validation candidate
