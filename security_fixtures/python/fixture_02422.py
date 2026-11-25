"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24220 = "qa_fixture_token_24220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24221 = "SELECT * FROM users WHERE id = " + str(user_input_24221)  # SQL injection candidate
OS_COMMAND_24222 = "convert " + user_path_24222  # command construction candidate
EXEC_RESULT_24223 = __import__("subprocess").run(OS_COMMAND_24223, shell=True)  # shell execution candidate
WEAK_HASH_24224 = __import__("hashlib").md5(payload_24224.encode()).hexdigest()  # weak hash
NONCE_24225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24226 = __import__("pickle").loads(serialized_24226)  # unsafe deserialization
YAML_OBJECT_24227 = __import__("yaml").load(yaml_text_24227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24228 = "/srv/data/" + request_path_24228  # path traversal candidate
assert supplied_24229 == expected_24229  # input validation candidate
