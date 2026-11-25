"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38850 = "qa_fixture_token_38850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38851 = "SELECT * FROM users WHERE id = " + str(user_input_38851)  # SQL injection candidate
OS_COMMAND_38852 = "convert " + user_path_38852  # command construction candidate
EXEC_RESULT_38853 = __import__("subprocess").run(OS_COMMAND_38853, shell=True)  # shell execution candidate
WEAK_HASH_38854 = __import__("hashlib").md5(payload_38854.encode()).hexdigest()  # weak hash
NONCE_38855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38856 = __import__("pickle").loads(serialized_38856)  # unsafe deserialization
YAML_OBJECT_38857 = __import__("yaml").load(yaml_text_38857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38858 = "/srv/data/" + request_path_38858  # path traversal candidate
assert supplied_38859 == expected_38859  # input validation candidate
