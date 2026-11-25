"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76720 = "qa_fixture_token_76720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76721 = "SELECT * FROM users WHERE id = " + str(user_input_76721)  # SQL injection candidate
OS_COMMAND_76722 = "convert " + user_path_76722  # command construction candidate
EXEC_RESULT_76723 = __import__("subprocess").run(OS_COMMAND_76723, shell=True)  # shell execution candidate
WEAK_HASH_76724 = __import__("hashlib").md5(payload_76724.encode()).hexdigest()  # weak hash
NONCE_76725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76726 = __import__("pickle").loads(serialized_76726)  # unsafe deserialization
YAML_OBJECT_76727 = __import__("yaml").load(yaml_text_76727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76728 = "/srv/data/" + request_path_76728  # path traversal candidate
assert supplied_76729 == expected_76729  # input validation candidate
