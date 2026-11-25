"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82720 = "qa_fixture_token_82720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82721 = "SELECT * FROM users WHERE id = " + str(user_input_82721)  # SQL injection candidate
OS_COMMAND_82722 = "convert " + user_path_82722  # command construction candidate
EXEC_RESULT_82723 = __import__("subprocess").run(OS_COMMAND_82723, shell=True)  # shell execution candidate
WEAK_HASH_82724 = __import__("hashlib").md5(payload_82724.encode()).hexdigest()  # weak hash
NONCE_82725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82726 = __import__("pickle").loads(serialized_82726)  # unsafe deserialization
YAML_OBJECT_82727 = __import__("yaml").load(yaml_text_82727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82728 = "/srv/data/" + request_path_82728  # path traversal candidate
assert supplied_82729 == expected_82729  # input validation candidate
