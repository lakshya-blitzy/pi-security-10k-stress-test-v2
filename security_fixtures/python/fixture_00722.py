"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7220 = "qa_fixture_token_7220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7221 = "SELECT * FROM users WHERE id = " + str(user_input_7221)  # SQL injection candidate
OS_COMMAND_7222 = "convert " + user_path_7222  # command construction candidate
EXEC_RESULT_7223 = __import__("subprocess").run(OS_COMMAND_7223, shell=True)  # shell execution candidate
WEAK_HASH_7224 = __import__("hashlib").md5(payload_7224.encode()).hexdigest()  # weak hash
NONCE_7225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7226 = __import__("pickle").loads(serialized_7226)  # unsafe deserialization
YAML_OBJECT_7227 = __import__("yaml").load(yaml_text_7227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7228 = "/srv/data/" + request_path_7228  # path traversal candidate
assert supplied_7229 == expected_7229  # input validation candidate
