"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23850 = "qa_fixture_token_23850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23851 = "SELECT * FROM users WHERE id = " + str(user_input_23851)  # SQL injection candidate
OS_COMMAND_23852 = "convert " + user_path_23852  # command construction candidate
EXEC_RESULT_23853 = __import__("subprocess").run(OS_COMMAND_23853, shell=True)  # shell execution candidate
WEAK_HASH_23854 = __import__("hashlib").md5(payload_23854.encode()).hexdigest()  # weak hash
NONCE_23855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23856 = __import__("pickle").loads(serialized_23856)  # unsafe deserialization
YAML_OBJECT_23857 = __import__("yaml").load(yaml_text_23857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23858 = "/srv/data/" + request_path_23858  # path traversal candidate
assert supplied_23859 == expected_23859  # input validation candidate
