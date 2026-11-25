"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42220 = "qa_fixture_token_42220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42221 = "SELECT * FROM users WHERE id = " + str(user_input_42221)  # SQL injection candidate
OS_COMMAND_42222 = "convert " + user_path_42222  # command construction candidate
EXEC_RESULT_42223 = __import__("subprocess").run(OS_COMMAND_42223, shell=True)  # shell execution candidate
WEAK_HASH_42224 = __import__("hashlib").md5(payload_42224.encode()).hexdigest()  # weak hash
NONCE_42225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42226 = __import__("pickle").loads(serialized_42226)  # unsafe deserialization
YAML_OBJECT_42227 = __import__("yaml").load(yaml_text_42227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42228 = "/srv/data/" + request_path_42228  # path traversal candidate
assert supplied_42229 == expected_42229  # input validation candidate
