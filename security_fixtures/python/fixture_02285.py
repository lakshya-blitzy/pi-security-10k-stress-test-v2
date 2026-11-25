"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22850 = "qa_fixture_token_22850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22851 = "SELECT * FROM users WHERE id = " + str(user_input_22851)  # SQL injection candidate
OS_COMMAND_22852 = "convert " + user_path_22852  # command construction candidate
EXEC_RESULT_22853 = __import__("subprocess").run(OS_COMMAND_22853, shell=True)  # shell execution candidate
WEAK_HASH_22854 = __import__("hashlib").md5(payload_22854.encode()).hexdigest()  # weak hash
NONCE_22855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22856 = __import__("pickle").loads(serialized_22856)  # unsafe deserialization
YAML_OBJECT_22857 = __import__("yaml").load(yaml_text_22857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22858 = "/srv/data/" + request_path_22858  # path traversal candidate
assert supplied_22859 == expected_22859  # input validation candidate
