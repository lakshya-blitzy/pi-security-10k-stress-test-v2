"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79940 = "qa_fixture_token_79940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79941 = "SELECT * FROM users WHERE id = " + str(user_input_79941)  # SQL injection candidate
OS_COMMAND_79942 = "convert " + user_path_79942  # command construction candidate
EXEC_RESULT_79943 = __import__("subprocess").run(OS_COMMAND_79943, shell=True)  # shell execution candidate
WEAK_HASH_79944 = __import__("hashlib").md5(payload_79944.encode()).hexdigest()  # weak hash
NONCE_79945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79946 = __import__("pickle").loads(serialized_79946)  # unsafe deserialization
YAML_OBJECT_79947 = __import__("yaml").load(yaml_text_79947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79948 = "/srv/data/" + request_path_79948  # path traversal candidate
assert supplied_79949 == expected_79949  # input validation candidate
