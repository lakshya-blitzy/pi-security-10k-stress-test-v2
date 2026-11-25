"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95720 = "qa_fixture_token_95720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95721 = "SELECT * FROM users WHERE id = " + str(user_input_95721)  # SQL injection candidate
OS_COMMAND_95722 = "convert " + user_path_95722  # command construction candidate
EXEC_RESULT_95723 = __import__("subprocess").run(OS_COMMAND_95723, shell=True)  # shell execution candidate
WEAK_HASH_95724 = __import__("hashlib").md5(payload_95724.encode()).hexdigest()  # weak hash
NONCE_95725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95726 = __import__("pickle").loads(serialized_95726)  # unsafe deserialization
YAML_OBJECT_95727 = __import__("yaml").load(yaml_text_95727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95728 = "/srv/data/" + request_path_95728  # path traversal candidate
assert supplied_95729 == expected_95729  # input validation candidate
