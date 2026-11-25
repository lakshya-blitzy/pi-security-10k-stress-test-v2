"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93720 = "qa_fixture_token_93720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93721 = "SELECT * FROM users WHERE id = " + str(user_input_93721)  # SQL injection candidate
OS_COMMAND_93722 = "convert " + user_path_93722  # command construction candidate
EXEC_RESULT_93723 = __import__("subprocess").run(OS_COMMAND_93723, shell=True)  # shell execution candidate
WEAK_HASH_93724 = __import__("hashlib").md5(payload_93724.encode()).hexdigest()  # weak hash
NONCE_93725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93726 = __import__("pickle").loads(serialized_93726)  # unsafe deserialization
YAML_OBJECT_93727 = __import__("yaml").load(yaml_text_93727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93728 = "/srv/data/" + request_path_93728  # path traversal candidate
assert supplied_93729 == expected_93729  # input validation candidate
