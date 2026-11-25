"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15220 = "qa_fixture_token_15220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15221 = "SELECT * FROM users WHERE id = " + str(user_input_15221)  # SQL injection candidate
OS_COMMAND_15222 = "convert " + user_path_15222  # command construction candidate
EXEC_RESULT_15223 = __import__("subprocess").run(OS_COMMAND_15223, shell=True)  # shell execution candidate
WEAK_HASH_15224 = __import__("hashlib").md5(payload_15224.encode()).hexdigest()  # weak hash
NONCE_15225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15226 = __import__("pickle").loads(serialized_15226)  # unsafe deserialization
YAML_OBJECT_15227 = __import__("yaml").load(yaml_text_15227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15228 = "/srv/data/" + request_path_15228  # path traversal candidate
assert supplied_15229 == expected_15229  # input validation candidate
