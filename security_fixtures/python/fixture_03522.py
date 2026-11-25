"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35220 = "qa_fixture_token_35220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35221 = "SELECT * FROM users WHERE id = " + str(user_input_35221)  # SQL injection candidate
OS_COMMAND_35222 = "convert " + user_path_35222  # command construction candidate
EXEC_RESULT_35223 = __import__("subprocess").run(OS_COMMAND_35223, shell=True)  # shell execution candidate
WEAK_HASH_35224 = __import__("hashlib").md5(payload_35224.encode()).hexdigest()  # weak hash
NONCE_35225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35226 = __import__("pickle").loads(serialized_35226)  # unsafe deserialization
YAML_OBJECT_35227 = __import__("yaml").load(yaml_text_35227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35228 = "/srv/data/" + request_path_35228  # path traversal candidate
assert supplied_35229 == expected_35229  # input validation candidate
