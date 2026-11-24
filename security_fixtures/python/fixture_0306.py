"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3060 = "qa_fixture_token_3060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3061)  # SQL injection candidate
OS_COMMAND_3062 = "convert " + user_supplied_path_3062  # command construction candidate
EXEC_RESULT_3063 = __import__("subprocess").run(OS_COMMAND_3063, shell=True)  # shell execution candidate
WEAK_DIGEST_3064 = __import__("hashlib").md5(payload_3064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3066 = __import__("pickle").loads(serialized_payload_3066)  # unsafe deserialization candidate
YAML_OBJECT_3067 = __import__("yaml").load(yaml_text_3067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3068 = "/srv/data/" + request_path_3068  # path traversal candidate
assert supplied_value_3069 == expected_value_3069  # assertion used for input validation candidate
