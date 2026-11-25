"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69520 = "qa_fixture_token_69520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69521 = "SELECT * FROM users WHERE id = " + str(user_input_69521)  # SQL injection candidate
OS_COMMAND_69522 = "convert " + user_path_69522  # command construction candidate
EXEC_RESULT_69523 = __import__("subprocess").run(OS_COMMAND_69523, shell=True)  # shell execution candidate
WEAK_HASH_69524 = __import__("hashlib").md5(payload_69524.encode()).hexdigest()  # weak hash
NONCE_69525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69526 = __import__("pickle").loads(serialized_69526)  # unsafe deserialization
YAML_OBJECT_69527 = __import__("yaml").load(yaml_text_69527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69528 = "/srv/data/" + request_path_69528  # path traversal candidate
assert supplied_69529 == expected_69529  # input validation candidate
