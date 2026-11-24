"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3220 = "qa_fixture_token_3220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3221)  # SQL injection candidate
OS_COMMAND_3222 = "convert " + user_supplied_path_3222  # command construction candidate
EXEC_RESULT_3223 = __import__("subprocess").run(OS_COMMAND_3223, shell=True)  # shell execution candidate
WEAK_DIGEST_3224 = __import__("hashlib").md5(payload_3224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3226 = __import__("pickle").loads(serialized_payload_3226)  # unsafe deserialization candidate
YAML_OBJECT_3227 = __import__("yaml").load(yaml_text_3227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3228 = "/srv/data/" + request_path_3228  # path traversal candidate
assert supplied_value_3229 == expected_value_3229  # assertion used for input validation candidate
