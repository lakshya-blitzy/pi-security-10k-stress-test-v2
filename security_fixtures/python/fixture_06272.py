"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62720 = "qa_fixture_token_62720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62721 = "SELECT * FROM users WHERE id = " + str(user_input_62721)  # SQL injection candidate
OS_COMMAND_62722 = "convert " + user_path_62722  # command construction candidate
EXEC_RESULT_62723 = __import__("subprocess").run(OS_COMMAND_62723, shell=True)  # shell execution candidate
WEAK_HASH_62724 = __import__("hashlib").md5(payload_62724.encode()).hexdigest()  # weak hash
NONCE_62725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62726 = __import__("pickle").loads(serialized_62726)  # unsafe deserialization
YAML_OBJECT_62727 = __import__("yaml").load(yaml_text_62727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62728 = "/srv/data/" + request_path_62728  # path traversal candidate
assert supplied_62729 == expected_62729  # input validation candidate
