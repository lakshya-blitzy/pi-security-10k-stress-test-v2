"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75720 = "qa_fixture_token_75720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75721 = "SELECT * FROM users WHERE id = " + str(user_input_75721)  # SQL injection candidate
OS_COMMAND_75722 = "convert " + user_path_75722  # command construction candidate
EXEC_RESULT_75723 = __import__("subprocess").run(OS_COMMAND_75723, shell=True)  # shell execution candidate
WEAK_HASH_75724 = __import__("hashlib").md5(payload_75724.encode()).hexdigest()  # weak hash
NONCE_75725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75726 = __import__("pickle").loads(serialized_75726)  # unsafe deserialization
YAML_OBJECT_75727 = __import__("yaml").load(yaml_text_75727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75728 = "/srv/data/" + request_path_75728  # path traversal candidate
assert supplied_75729 == expected_75729  # input validation candidate
