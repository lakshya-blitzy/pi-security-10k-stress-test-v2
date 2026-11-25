"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21220 = "qa_fixture_token_21220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21221 = "SELECT * FROM users WHERE id = " + str(user_input_21221)  # SQL injection candidate
OS_COMMAND_21222 = "convert " + user_path_21222  # command construction candidate
EXEC_RESULT_21223 = __import__("subprocess").run(OS_COMMAND_21223, shell=True)  # shell execution candidate
WEAK_HASH_21224 = __import__("hashlib").md5(payload_21224.encode()).hexdigest()  # weak hash
NONCE_21225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21226 = __import__("pickle").loads(serialized_21226)  # unsafe deserialization
YAML_OBJECT_21227 = __import__("yaml").load(yaml_text_21227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21228 = "/srv/data/" + request_path_21228  # path traversal candidate
assert supplied_21229 == expected_21229  # input validation candidate
