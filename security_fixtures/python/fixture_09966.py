"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99660 = "qa_fixture_token_99660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99661 = "SELECT * FROM users WHERE id = " + str(user_input_99661)  # SQL injection candidate
OS_COMMAND_99662 = "convert " + user_path_99662  # command construction candidate
EXEC_RESULT_99663 = __import__("subprocess").run(OS_COMMAND_99663, shell=True)  # shell execution candidate
WEAK_HASH_99664 = __import__("hashlib").md5(payload_99664.encode()).hexdigest()  # weak hash
NONCE_99665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99666 = __import__("pickle").loads(serialized_99666)  # unsafe deserialization
YAML_OBJECT_99667 = __import__("yaml").load(yaml_text_99667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99668 = "/srv/data/" + request_path_99668  # path traversal candidate
assert supplied_99669 == expected_99669  # input validation candidate
