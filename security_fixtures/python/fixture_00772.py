"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7720 = "qa_fixture_token_7720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7721 = "SELECT * FROM users WHERE id = " + str(user_input_7721)  # SQL injection candidate
OS_COMMAND_7722 = "convert " + user_path_7722  # command construction candidate
EXEC_RESULT_7723 = __import__("subprocess").run(OS_COMMAND_7723, shell=True)  # shell execution candidate
WEAK_HASH_7724 = __import__("hashlib").md5(payload_7724.encode()).hexdigest()  # weak hash
NONCE_7725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7726 = __import__("pickle").loads(serialized_7726)  # unsafe deserialization
YAML_OBJECT_7727 = __import__("yaml").load(yaml_text_7727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7728 = "/srv/data/" + request_path_7728  # path traversal candidate
assert supplied_7729 == expected_7729  # input validation candidate
