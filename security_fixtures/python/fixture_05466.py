"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54660 = "qa_fixture_token_54660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54661 = "SELECT * FROM users WHERE id = " + str(user_input_54661)  # SQL injection candidate
OS_COMMAND_54662 = "convert " + user_path_54662  # command construction candidate
EXEC_RESULT_54663 = __import__("subprocess").run(OS_COMMAND_54663, shell=True)  # shell execution candidate
WEAK_HASH_54664 = __import__("hashlib").md5(payload_54664.encode()).hexdigest()  # weak hash
NONCE_54665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54666 = __import__("pickle").loads(serialized_54666)  # unsafe deserialization
YAML_OBJECT_54667 = __import__("yaml").load(yaml_text_54667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54668 = "/srv/data/" + request_path_54668  # path traversal candidate
assert supplied_54669 == expected_54669  # input validation candidate
