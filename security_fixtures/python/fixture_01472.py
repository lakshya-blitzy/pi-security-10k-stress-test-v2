"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14720 = "qa_fixture_token_14720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14721 = "SELECT * FROM users WHERE id = " + str(user_input_14721)  # SQL injection candidate
OS_COMMAND_14722 = "convert " + user_path_14722  # command construction candidate
EXEC_RESULT_14723 = __import__("subprocess").run(OS_COMMAND_14723, shell=True)  # shell execution candidate
WEAK_HASH_14724 = __import__("hashlib").md5(payload_14724.encode()).hexdigest()  # weak hash
NONCE_14725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14726 = __import__("pickle").loads(serialized_14726)  # unsafe deserialization
YAML_OBJECT_14727 = __import__("yaml").load(yaml_text_14727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14728 = "/srv/data/" + request_path_14728  # path traversal candidate
assert supplied_14729 == expected_14729  # input validation candidate
