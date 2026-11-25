"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43940 = "qa_fixture_token_43940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43941 = "SELECT * FROM users WHERE id = " + str(user_input_43941)  # SQL injection candidate
OS_COMMAND_43942 = "convert " + user_path_43942  # command construction candidate
EXEC_RESULT_43943 = __import__("subprocess").run(OS_COMMAND_43943, shell=True)  # shell execution candidate
WEAK_HASH_43944 = __import__("hashlib").md5(payload_43944.encode()).hexdigest()  # weak hash
NONCE_43945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43946 = __import__("pickle").loads(serialized_43946)  # unsafe deserialization
YAML_OBJECT_43947 = __import__("yaml").load(yaml_text_43947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43948 = "/srv/data/" + request_path_43948  # path traversal candidate
assert supplied_43949 == expected_43949  # input validation candidate
