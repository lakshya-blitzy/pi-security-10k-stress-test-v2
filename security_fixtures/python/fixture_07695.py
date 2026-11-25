"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76950 = "qa_fixture_token_76950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76951 = "SELECT * FROM users WHERE id = " + str(user_input_76951)  # SQL injection candidate
OS_COMMAND_76952 = "convert " + user_path_76952  # command construction candidate
EXEC_RESULT_76953 = __import__("subprocess").run(OS_COMMAND_76953, shell=True)  # shell execution candidate
WEAK_HASH_76954 = __import__("hashlib").md5(payload_76954.encode()).hexdigest()  # weak hash
NONCE_76955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76956 = __import__("pickle").loads(serialized_76956)  # unsafe deserialization
YAML_OBJECT_76957 = __import__("yaml").load(yaml_text_76957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76958 = "/srv/data/" + request_path_76958  # path traversal candidate
assert supplied_76959 == expected_76959  # input validation candidate
