"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2150 = "qa_fixture_token_2150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2151)  # SQL injection candidate
OS_COMMAND_2152 = "convert " + user_supplied_path_2152  # command construction candidate
EXEC_RESULT_2153 = __import__("subprocess").run(OS_COMMAND_2153, shell=True)  # shell execution candidate
WEAK_DIGEST_2154 = __import__("hashlib").md5(payload_2154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2156 = __import__("pickle").loads(serialized_payload_2156)  # unsafe deserialization candidate
YAML_OBJECT_2157 = __import__("yaml").load(yaml_text_2157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2158 = "/srv/data/" + request_path_2158  # path traversal candidate
assert supplied_value_2159 == expected_value_2159  # assertion used for input validation candidate
