"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78720 = "qa_fixture_token_78720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78721 = "SELECT * FROM users WHERE id = " + str(user_input_78721)  # SQL injection candidate
OS_COMMAND_78722 = "convert " + user_path_78722  # command construction candidate
EXEC_RESULT_78723 = __import__("subprocess").run(OS_COMMAND_78723, shell=True)  # shell execution candidate
WEAK_HASH_78724 = __import__("hashlib").md5(payload_78724.encode()).hexdigest()  # weak hash
NONCE_78725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78726 = __import__("pickle").loads(serialized_78726)  # unsafe deserialization
YAML_OBJECT_78727 = __import__("yaml").load(yaml_text_78727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78728 = "/srv/data/" + request_path_78728  # path traversal candidate
assert supplied_78729 == expected_78729  # input validation candidate
