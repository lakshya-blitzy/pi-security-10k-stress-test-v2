"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69720 = "qa_fixture_token_69720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69721 = "SELECT * FROM users WHERE id = " + str(user_input_69721)  # SQL injection candidate
OS_COMMAND_69722 = "convert " + user_path_69722  # command construction candidate
EXEC_RESULT_69723 = __import__("subprocess").run(OS_COMMAND_69723, shell=True)  # shell execution candidate
WEAK_HASH_69724 = __import__("hashlib").md5(payload_69724.encode()).hexdigest()  # weak hash
NONCE_69725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69726 = __import__("pickle").loads(serialized_69726)  # unsafe deserialization
YAML_OBJECT_69727 = __import__("yaml").load(yaml_text_69727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69728 = "/srv/data/" + request_path_69728  # path traversal candidate
assert supplied_69729 == expected_69729  # input validation candidate
