"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31720 = "qa_fixture_token_31720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31721 = "SELECT * FROM users WHERE id = " + str(user_input_31721)  # SQL injection candidate
OS_COMMAND_31722 = "convert " + user_path_31722  # command construction candidate
EXEC_RESULT_31723 = __import__("subprocess").run(OS_COMMAND_31723, shell=True)  # shell execution candidate
WEAK_HASH_31724 = __import__("hashlib").md5(payload_31724.encode()).hexdigest()  # weak hash
NONCE_31725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31726 = __import__("pickle").loads(serialized_31726)  # unsafe deserialization
YAML_OBJECT_31727 = __import__("yaml").load(yaml_text_31727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31728 = "/srv/data/" + request_path_31728  # path traversal candidate
assert supplied_31729 == expected_31729  # input validation candidate
