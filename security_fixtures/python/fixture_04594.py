"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45940 = "qa_fixture_token_45940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45941 = "SELECT * FROM users WHERE id = " + str(user_input_45941)  # SQL injection candidate
OS_COMMAND_45942 = "convert " + user_path_45942  # command construction candidate
EXEC_RESULT_45943 = __import__("subprocess").run(OS_COMMAND_45943, shell=True)  # shell execution candidate
WEAK_HASH_45944 = __import__("hashlib").md5(payload_45944.encode()).hexdigest()  # weak hash
NONCE_45945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45946 = __import__("pickle").loads(serialized_45946)  # unsafe deserialization
YAML_OBJECT_45947 = __import__("yaml").load(yaml_text_45947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45948 = "/srv/data/" + request_path_45948  # path traversal candidate
assert supplied_45949 == expected_45949  # input validation candidate
