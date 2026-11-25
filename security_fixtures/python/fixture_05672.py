"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56720 = "qa_fixture_token_56720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56721 = "SELECT * FROM users WHERE id = " + str(user_input_56721)  # SQL injection candidate
OS_COMMAND_56722 = "convert " + user_path_56722  # command construction candidate
EXEC_RESULT_56723 = __import__("subprocess").run(OS_COMMAND_56723, shell=True)  # shell execution candidate
WEAK_HASH_56724 = __import__("hashlib").md5(payload_56724.encode()).hexdigest()  # weak hash
NONCE_56725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56726 = __import__("pickle").loads(serialized_56726)  # unsafe deserialization
YAML_OBJECT_56727 = __import__("yaml").load(yaml_text_56727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56728 = "/srv/data/" + request_path_56728  # path traversal candidate
assert supplied_56729 == expected_56729  # input validation candidate
