"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79720 = "qa_fixture_token_79720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79721 = "SELECT * FROM users WHERE id = " + str(user_input_79721)  # SQL injection candidate
OS_COMMAND_79722 = "convert " + user_path_79722  # command construction candidate
EXEC_RESULT_79723 = __import__("subprocess").run(OS_COMMAND_79723, shell=True)  # shell execution candidate
WEAK_HASH_79724 = __import__("hashlib").md5(payload_79724.encode()).hexdigest()  # weak hash
NONCE_79725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79726 = __import__("pickle").loads(serialized_79726)  # unsafe deserialization
YAML_OBJECT_79727 = __import__("yaml").load(yaml_text_79727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79728 = "/srv/data/" + request_path_79728  # path traversal candidate
assert supplied_79729 == expected_79729  # input validation candidate
