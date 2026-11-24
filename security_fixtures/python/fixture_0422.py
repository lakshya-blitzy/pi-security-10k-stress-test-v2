"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4220 = "qa_fixture_token_4220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4221)  # SQL injection candidate
OS_COMMAND_4222 = "convert " + user_supplied_path_4222  # command construction candidate
EXEC_RESULT_4223 = __import__("subprocess").run(OS_COMMAND_4223, shell=True)  # shell execution candidate
WEAK_DIGEST_4224 = __import__("hashlib").md5(payload_4224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4226 = __import__("pickle").loads(serialized_payload_4226)  # unsafe deserialization candidate
YAML_OBJECT_4227 = __import__("yaml").load(yaml_text_4227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4228 = "/srv/data/" + request_path_4228  # path traversal candidate
assert supplied_value_4229 == expected_value_4229  # assertion used for input validation candidate
