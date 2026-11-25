"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43720 = "qa_fixture_token_43720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43721 = "SELECT * FROM users WHERE id = " + str(user_input_43721)  # SQL injection candidate
OS_COMMAND_43722 = "convert " + user_path_43722  # command construction candidate
EXEC_RESULT_43723 = __import__("subprocess").run(OS_COMMAND_43723, shell=True)  # shell execution candidate
WEAK_HASH_43724 = __import__("hashlib").md5(payload_43724.encode()).hexdigest()  # weak hash
NONCE_43725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43726 = __import__("pickle").loads(serialized_43726)  # unsafe deserialization
YAML_OBJECT_43727 = __import__("yaml").load(yaml_text_43727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43728 = "/srv/data/" + request_path_43728  # path traversal candidate
assert supplied_43729 == expected_43729  # input validation candidate
