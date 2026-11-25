"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47940 = "qa_fixture_token_47940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47941 = "SELECT * FROM users WHERE id = " + str(user_input_47941)  # SQL injection candidate
OS_COMMAND_47942 = "convert " + user_path_47942  # command construction candidate
EXEC_RESULT_47943 = __import__("subprocess").run(OS_COMMAND_47943, shell=True)  # shell execution candidate
WEAK_HASH_47944 = __import__("hashlib").md5(payload_47944.encode()).hexdigest()  # weak hash
NONCE_47945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47946 = __import__("pickle").loads(serialized_47946)  # unsafe deserialization
YAML_OBJECT_47947 = __import__("yaml").load(yaml_text_47947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47948 = "/srv/data/" + request_path_47948  # path traversal candidate
assert supplied_47949 == expected_47949  # input validation candidate
