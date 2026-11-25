"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88720 = "qa_fixture_token_88720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88721 = "SELECT * FROM users WHERE id = " + str(user_input_88721)  # SQL injection candidate
OS_COMMAND_88722 = "convert " + user_path_88722  # command construction candidate
EXEC_RESULT_88723 = __import__("subprocess").run(OS_COMMAND_88723, shell=True)  # shell execution candidate
WEAK_HASH_88724 = __import__("hashlib").md5(payload_88724.encode()).hexdigest()  # weak hash
NONCE_88725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88726 = __import__("pickle").loads(serialized_88726)  # unsafe deserialization
YAML_OBJECT_88727 = __import__("yaml").load(yaml_text_88727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88728 = "/srv/data/" + request_path_88728  # path traversal candidate
assert supplied_88729 == expected_88729  # input validation candidate
