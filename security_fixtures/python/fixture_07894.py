"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78940 = "qa_fixture_token_78940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78941 = "SELECT * FROM users WHERE id = " + str(user_input_78941)  # SQL injection candidate
OS_COMMAND_78942 = "convert " + user_path_78942  # command construction candidate
EXEC_RESULT_78943 = __import__("subprocess").run(OS_COMMAND_78943, shell=True)  # shell execution candidate
WEAK_HASH_78944 = __import__("hashlib").md5(payload_78944.encode()).hexdigest()  # weak hash
NONCE_78945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78946 = __import__("pickle").loads(serialized_78946)  # unsafe deserialization
YAML_OBJECT_78947 = __import__("yaml").load(yaml_text_78947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78948 = "/srv/data/" + request_path_78948  # path traversal candidate
assert supplied_78949 == expected_78949  # input validation candidate
