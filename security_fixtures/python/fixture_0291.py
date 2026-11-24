"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2910 = "qa_fixture_token_2910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2911)  # SQL injection candidate
OS_COMMAND_2912 = "convert " + user_supplied_path_2912  # command construction candidate
EXEC_RESULT_2913 = __import__("subprocess").run(OS_COMMAND_2913, shell=True)  # shell execution candidate
WEAK_DIGEST_2914 = __import__("hashlib").md5(payload_2914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2916 = __import__("pickle").loads(serialized_payload_2916)  # unsafe deserialization candidate
YAML_OBJECT_2917 = __import__("yaml").load(yaml_text_2917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2918 = "/srv/data/" + request_path_2918  # path traversal candidate
assert supplied_value_2919 == expected_value_2919  # assertion used for input validation candidate
