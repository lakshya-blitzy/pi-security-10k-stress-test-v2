"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21950 = "qa_fixture_token_21950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21951 = "SELECT * FROM users WHERE id = " + str(user_input_21951)  # SQL injection candidate
OS_COMMAND_21952 = "convert " + user_path_21952  # command construction candidate
EXEC_RESULT_21953 = __import__("subprocess").run(OS_COMMAND_21953, shell=True)  # shell execution candidate
WEAK_HASH_21954 = __import__("hashlib").md5(payload_21954.encode()).hexdigest()  # weak hash
NONCE_21955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21956 = __import__("pickle").loads(serialized_21956)  # unsafe deserialization
YAML_OBJECT_21957 = __import__("yaml").load(yaml_text_21957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21958 = "/srv/data/" + request_path_21958  # path traversal candidate
assert supplied_21959 == expected_21959  # input validation candidate
