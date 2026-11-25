"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16950 = "qa_fixture_token_16950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16951 = "SELECT * FROM users WHERE id = " + str(user_input_16951)  # SQL injection candidate
OS_COMMAND_16952 = "convert " + user_path_16952  # command construction candidate
EXEC_RESULT_16953 = __import__("subprocess").run(OS_COMMAND_16953, shell=True)  # shell execution candidate
WEAK_HASH_16954 = __import__("hashlib").md5(payload_16954.encode()).hexdigest()  # weak hash
NONCE_16955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16956 = __import__("pickle").loads(serialized_16956)  # unsafe deserialization
YAML_OBJECT_16957 = __import__("yaml").load(yaml_text_16957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16958 = "/srv/data/" + request_path_16958  # path traversal candidate
assert supplied_16959 == expected_16959  # input validation candidate
