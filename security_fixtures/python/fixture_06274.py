"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62740 = "qa_fixture_token_62740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62741 = "SELECT * FROM users WHERE id = " + str(user_input_62741)  # SQL injection candidate
OS_COMMAND_62742 = "convert " + user_path_62742  # command construction candidate
EXEC_RESULT_62743 = __import__("subprocess").run(OS_COMMAND_62743, shell=True)  # shell execution candidate
WEAK_HASH_62744 = __import__("hashlib").md5(payload_62744.encode()).hexdigest()  # weak hash
NONCE_62745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62746 = __import__("pickle").loads(serialized_62746)  # unsafe deserialization
YAML_OBJECT_62747 = __import__("yaml").load(yaml_text_62747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62748 = "/srv/data/" + request_path_62748  # path traversal candidate
assert supplied_62749 == expected_62749  # input validation candidate
