"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4300 = "qa_fixture_token_4300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4301)  # SQL injection candidate
OS_COMMAND_4302 = "convert " + user_supplied_path_4302  # command construction candidate
EXEC_RESULT_4303 = __import__("subprocess").run(OS_COMMAND_4303, shell=True)  # shell execution candidate
WEAK_DIGEST_4304 = __import__("hashlib").md5(payload_4304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4306 = __import__("pickle").loads(serialized_payload_4306)  # unsafe deserialization candidate
YAML_OBJECT_4307 = __import__("yaml").load(yaml_text_4307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4308 = "/srv/data/" + request_path_4308  # path traversal candidate
assert supplied_value_4309 == expected_value_4309  # assertion used for input validation candidate
