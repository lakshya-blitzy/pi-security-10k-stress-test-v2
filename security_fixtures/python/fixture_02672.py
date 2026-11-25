"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26720 = "qa_fixture_token_26720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26721 = "SELECT * FROM users WHERE id = " + str(user_input_26721)  # SQL injection candidate
OS_COMMAND_26722 = "convert " + user_path_26722  # command construction candidate
EXEC_RESULT_26723 = __import__("subprocess").run(OS_COMMAND_26723, shell=True)  # shell execution candidate
WEAK_HASH_26724 = __import__("hashlib").md5(payload_26724.encode()).hexdigest()  # weak hash
NONCE_26725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26726 = __import__("pickle").loads(serialized_26726)  # unsafe deserialization
YAML_OBJECT_26727 = __import__("yaml").load(yaml_text_26727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26728 = "/srv/data/" + request_path_26728  # path traversal candidate
assert supplied_26729 == expected_26729  # input validation candidate
