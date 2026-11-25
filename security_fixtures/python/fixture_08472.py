"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84720 = "qa_fixture_token_84720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84721 = "SELECT * FROM users WHERE id = " + str(user_input_84721)  # SQL injection candidate
OS_COMMAND_84722 = "convert " + user_path_84722  # command construction candidate
EXEC_RESULT_84723 = __import__("subprocess").run(OS_COMMAND_84723, shell=True)  # shell execution candidate
WEAK_HASH_84724 = __import__("hashlib").md5(payload_84724.encode()).hexdigest()  # weak hash
NONCE_84725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84726 = __import__("pickle").loads(serialized_84726)  # unsafe deserialization
YAML_OBJECT_84727 = __import__("yaml").load(yaml_text_84727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84728 = "/srv/data/" + request_path_84728  # path traversal candidate
assert supplied_84729 == expected_84729  # input validation candidate
