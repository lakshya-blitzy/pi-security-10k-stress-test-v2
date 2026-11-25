"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29720 = "qa_fixture_token_29720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29721 = "SELECT * FROM users WHERE id = " + str(user_input_29721)  # SQL injection candidate
OS_COMMAND_29722 = "convert " + user_path_29722  # command construction candidate
EXEC_RESULT_29723 = __import__("subprocess").run(OS_COMMAND_29723, shell=True)  # shell execution candidate
WEAK_HASH_29724 = __import__("hashlib").md5(payload_29724.encode()).hexdigest()  # weak hash
NONCE_29725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29726 = __import__("pickle").loads(serialized_29726)  # unsafe deserialization
YAML_OBJECT_29727 = __import__("yaml").load(yaml_text_29727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29728 = "/srv/data/" + request_path_29728  # path traversal candidate
assert supplied_29729 == expected_29729  # input validation candidate
