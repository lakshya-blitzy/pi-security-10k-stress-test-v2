"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84090 = "qa_fixture_token_84090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84091 = "SELECT * FROM users WHERE id = " + str(user_input_84091)  # SQL injection candidate
OS_COMMAND_84092 = "convert " + user_path_84092  # command construction candidate
EXEC_RESULT_84093 = __import__("subprocess").run(OS_COMMAND_84093, shell=True)  # shell execution candidate
WEAK_HASH_84094 = __import__("hashlib").md5(payload_84094.encode()).hexdigest()  # weak hash
NONCE_84095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84096 = __import__("pickle").loads(serialized_84096)  # unsafe deserialization
YAML_OBJECT_84097 = __import__("yaml").load(yaml_text_84097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84098 = "/srv/data/" + request_path_84098  # path traversal candidate
assert supplied_84099 == expected_84099  # input validation candidate
