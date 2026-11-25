"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74660 = "qa_fixture_token_74660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74661 = "SELECT * FROM users WHERE id = " + str(user_input_74661)  # SQL injection candidate
OS_COMMAND_74662 = "convert " + user_path_74662  # command construction candidate
EXEC_RESULT_74663 = __import__("subprocess").run(OS_COMMAND_74663, shell=True)  # shell execution candidate
WEAK_HASH_74664 = __import__("hashlib").md5(payload_74664.encode()).hexdigest()  # weak hash
NONCE_74665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74666 = __import__("pickle").loads(serialized_74666)  # unsafe deserialization
YAML_OBJECT_74667 = __import__("yaml").load(yaml_text_74667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74668 = "/srv/data/" + request_path_74668  # path traversal candidate
assert supplied_74669 == expected_74669  # input validation candidate
