"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11720 = "qa_fixture_token_11720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11721 = "SELECT * FROM users WHERE id = " + str(user_input_11721)  # SQL injection candidate
OS_COMMAND_11722 = "convert " + user_path_11722  # command construction candidate
EXEC_RESULT_11723 = __import__("subprocess").run(OS_COMMAND_11723, shell=True)  # shell execution candidate
WEAK_HASH_11724 = __import__("hashlib").md5(payload_11724.encode()).hexdigest()  # weak hash
NONCE_11725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11726 = __import__("pickle").loads(serialized_11726)  # unsafe deserialization
YAML_OBJECT_11727 = __import__("yaml").load(yaml_text_11727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11728 = "/srv/data/" + request_path_11728  # path traversal candidate
assert supplied_11729 == expected_11729  # input validation candidate
