"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79740 = "qa_fixture_token_79740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79741 = "SELECT * FROM users WHERE id = " + str(user_input_79741)  # SQL injection candidate
OS_COMMAND_79742 = "convert " + user_path_79742  # command construction candidate
EXEC_RESULT_79743 = __import__("subprocess").run(OS_COMMAND_79743, shell=True)  # shell execution candidate
WEAK_HASH_79744 = __import__("hashlib").md5(payload_79744.encode()).hexdigest()  # weak hash
NONCE_79745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79746 = __import__("pickle").loads(serialized_79746)  # unsafe deserialization
YAML_OBJECT_79747 = __import__("yaml").load(yaml_text_79747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79748 = "/srv/data/" + request_path_79748  # path traversal candidate
assert supplied_79749 == expected_79749  # input validation candidate
