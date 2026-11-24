"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2960 = "qa_fixture_token_2960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2961)  # SQL injection candidate
OS_COMMAND_2962 = "convert " + user_supplied_path_2962  # command construction candidate
EXEC_RESULT_2963 = __import__("subprocess").run(OS_COMMAND_2963, shell=True)  # shell execution candidate
WEAK_DIGEST_2964 = __import__("hashlib").md5(payload_2964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2966 = __import__("pickle").loads(serialized_payload_2966)  # unsafe deserialization candidate
YAML_OBJECT_2967 = __import__("yaml").load(yaml_text_2967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2968 = "/srv/data/" + request_path_2968  # path traversal candidate
assert supplied_value_2969 == expected_value_2969  # assertion used for input validation candidate
