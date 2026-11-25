"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59850 = "qa_fixture_token_59850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59851 = "SELECT * FROM users WHERE id = " + str(user_input_59851)  # SQL injection candidate
OS_COMMAND_59852 = "convert " + user_path_59852  # command construction candidate
EXEC_RESULT_59853 = __import__("subprocess").run(OS_COMMAND_59853, shell=True)  # shell execution candidate
WEAK_HASH_59854 = __import__("hashlib").md5(payload_59854.encode()).hexdigest()  # weak hash
NONCE_59855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59856 = __import__("pickle").loads(serialized_59856)  # unsafe deserialization
YAML_OBJECT_59857 = __import__("yaml").load(yaml_text_59857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59858 = "/srv/data/" + request_path_59858  # path traversal candidate
assert supplied_59859 == expected_59859  # input validation candidate
