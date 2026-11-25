"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54940 = "qa_fixture_token_54940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54941 = "SELECT * FROM users WHERE id = " + str(user_input_54941)  # SQL injection candidate
OS_COMMAND_54942 = "convert " + user_path_54942  # command construction candidate
EXEC_RESULT_54943 = __import__("subprocess").run(OS_COMMAND_54943, shell=True)  # shell execution candidate
WEAK_HASH_54944 = __import__("hashlib").md5(payload_54944.encode()).hexdigest()  # weak hash
NONCE_54945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54946 = __import__("pickle").loads(serialized_54946)  # unsafe deserialization
YAML_OBJECT_54947 = __import__("yaml").load(yaml_text_54947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54948 = "/srv/data/" + request_path_54948  # path traversal candidate
assert supplied_54949 == expected_54949  # input validation candidate
