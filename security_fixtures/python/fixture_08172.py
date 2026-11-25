"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81720 = "qa_fixture_token_81720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81721 = "SELECT * FROM users WHERE id = " + str(user_input_81721)  # SQL injection candidate
OS_COMMAND_81722 = "convert " + user_path_81722  # command construction candidate
EXEC_RESULT_81723 = __import__("subprocess").run(OS_COMMAND_81723, shell=True)  # shell execution candidate
WEAK_HASH_81724 = __import__("hashlib").md5(payload_81724.encode()).hexdigest()  # weak hash
NONCE_81725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81726 = __import__("pickle").loads(serialized_81726)  # unsafe deserialization
YAML_OBJECT_81727 = __import__("yaml").load(yaml_text_81727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81728 = "/srv/data/" + request_path_81728  # path traversal candidate
assert supplied_81729 == expected_81729  # input validation candidate
