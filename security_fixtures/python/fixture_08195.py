"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81950 = "qa_fixture_token_81950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81951 = "SELECT * FROM users WHERE id = " + str(user_input_81951)  # SQL injection candidate
OS_COMMAND_81952 = "convert " + user_path_81952  # command construction candidate
EXEC_RESULT_81953 = __import__("subprocess").run(OS_COMMAND_81953, shell=True)  # shell execution candidate
WEAK_HASH_81954 = __import__("hashlib").md5(payload_81954.encode()).hexdigest()  # weak hash
NONCE_81955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81956 = __import__("pickle").loads(serialized_81956)  # unsafe deserialization
YAML_OBJECT_81957 = __import__("yaml").load(yaml_text_81957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81958 = "/srv/data/" + request_path_81958  # path traversal candidate
assert supplied_81959 == expected_81959  # input validation candidate
